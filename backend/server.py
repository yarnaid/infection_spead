import logging
import os
import typing  # noqa
import uuid
from concurrent import futures
from pathlib import Path

import grpc
from dataStructure.gRPC import (
    Building,
    BuildingType,
    Empty,
    HealthStatus,
    HumanState,
    MapMessage,
    Metadata,
    StatusCode,
    UpdateRequest,
    UpdateResponse,
)
from grpc_lib import spec_pb2_grpc, spec_pb2
from pure_protobuf.types import int32

from backend.map_generation import ResearchMap

CONFIG_FILE_NAME = "backend_config.txt"
BASE_PATH = Path(__file__).absolute().parent


class ModelingSerializer:
    @staticmethod
    def create_update_response(request: UpdateRequest, humans) -> UpdateResponse:  # create pb2 object
        # from backed human
        status = ModelingSerializer.create_success_meta_response(request)
        return UpdateResponse(meta=status, state=[ModelingSerializer.create_human(human) for human in humans])

    @staticmethod
    def create_get_map_response(request: Empty, src_map: ResearchMap) -> spec_pb2.Map:  # create pb2 object from backend building
        return spec_pb2.Map(meta=spec_pb2.Metadata(status=1))
        status = ModelingSerializer.create_success_meta_response(request)
        return MapMessage(
            meta=status,
            map_size_w=float(src_map.config_data.map_width),
            map_size_h=float(src_map.config_data.map_length),
            building=[ModelingSerializer.create_building(building) for building in src_map.iter_buildings()],
        )

    @staticmethod
    def create_success_meta_response(request) -> Metadata:
        return Metadata(status=StatusCode.SUCCESS, request_id=int32(request.meta.request_id), UUID=str(uuid.uuid4()))

    @staticmethod
    def create_human(human) -> HumanState:
        return HumanState(
            id=int32(human.id), coord_x=float(human.x), coord_y=float(human.y), health_status=HealthStatus(human.type)
        )

    @staticmethod
    def create_building(building) -> Building:
        return Building(
            id=int32(building.id),
            coord_x=float(building.coord_x),
            coord_y=float(building.coord_y),
            type=BuildingType(building.type),
            width=int32(building.width),
            length=int32(building.length),
            angle=int32(building.angle),
        )


class ModelingServicer(spec_pb2_grpc.ModelingServicer):

    map: ResearchMap
    human_generator: None
    serializer: ModelingSerializer

    def __init__(self, src_map, human_generator, serializer: ModelingSerializer) -> None:
        """
         Remember our Backend output exits
        :param map_generator: generator: generator from which we can read map objects
        :param human_generator: generator : generator from which we can read humans object
        :param serializer: class : serializer so that you can bring the modeling objects to the proto form
        """
        self.map = src_map
        self.human_objects = human_generator
        self.serializer = serializer

    def GetUpdate(self, request, context) -> UpdateResponse:  # Generator of people on modeling
        del context
        logger.info("Get update request")
        return self.serializer.create_update_response(request, self.human_objects)

    def GetMap(self, request, context) -> spec_pb2.Map:  # Generator of map objects
        del context
        logger.info("Get map request")
        resp = self.serializer.create_get_map_response(request, self.map)
        print("HERE")
        return resp


def serve():  # Responsible for the operation of the server
    res_map = ResearchMap(str(BASE_PATH / CONFIG_FILE_NAME))
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=os.cpu_count()))
    spec_pb2_grpc.add_ModelingServicer_to_server(ModelingServicer(res_map, None, ModelingSerializer), server)
    logger.info("Set Modeling Servicer")
    server.add_insecure_port("[::]:50051")
    server.start()
    logger.info("Start server")
    server.wait_for_termination()


logging.basicConfig(format="%(relativeCreated)5d %(name)-15s %(levelname)-8s %(message)s")
logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)
if __name__ == "__main__":
    serve()
