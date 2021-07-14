import os

from gRPC import spec_pb2_grpc, spec_pb2
from dataStructure.gRPC import Map, UpdateResponse, Metadata, statusCode, HumanState, BaseUnit, BuildingType, HumanType, \
    Building
from concurrent import futures
from pure_protobuf.types import int32
import logging
import grpc
import uuid
import typing


class ModelingSerializer:
    @staticmethod
    def create_update_response(request, humans) -> UpdateResponse:  # create pb2 object
        # from backed human
        status = ModelingSerializer.create_success_meta_response(request)
        return UpdateResponse(meta=status,
                              state=[ModelingSerializer.create_human(human) for human in humans]
                              )

    @staticmethod
    def create_get_map_response(request, buildings) -> Map:  # create pb2 object from backend building
        status = ModelingSerializer.create_success_meta_response(request)
        return Map(meta=status, map_size_w=buildings.width, map_size_h=buildings.length,
                   building=[ModelingSerializer.create_building(building) for building in buildings]
                   )

    @staticmethod
    def create_success_meta_response(request) -> Metadata:
        return Metadata(status=statusCode.SUCCESS,
                        request_id=int32(request.meta.request_id), UUID=str(uuid.uuid4()))

    @staticmethod
    def create_human(human) -> HumanState:
        return HumanState(
            base=BaseUnit(id=int32(human.id), coord_x=float(human.x), coord_y=float(human.y)),
            type=HumanType(human.type),
        )

    @staticmethod
    def create_building(building) -> Building:
        return Building(
            base=BaseUnit(id=int32(building.id), coord_x=float(building.x), coord_y=float(building.y)),
            type=BuildingType(building.type),
            width=int32(building.width),
            length=int32(building.length),
            angle=int32(building.angle)
        )


class ModelingServicer(spec_pb2_grpc.ModelingServicer):

    def __init__(self, map_generator, human_generator, serializer) -> None:
        """
         Remember our Backend output exits
        :param map_generator: generator: generator from which we can read map objects
        :param human_generator: generator : generator from which we can read humans object
        :param serializer: class : serializer so that you can bring the modeling objects to the proto form
        """
        self.map = map_generator
        self.human_objects = human_generator
        self.serializer = serializer

    def GetUpdate(self, request, context) -> UpdateResponse:  # Generator of people on modeling
        logger.info("Get update request")
        return self.serializer.create_update_response(request, self.human_objects)

    def GetMap(self, request, context) -> Map:  # Generator of map objects
        logger.info("Get map request")
        return self.serializer.create_get_map_response(request, self.map)


def serve():  # Responsible for the operation of the server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=os.cpu_count()))
    spec_pb2_grpc.add_ModelingServicer_to_server(
        ModelingServicer(None, None, ModelingSerializer), server)
    logger.info("Set Modeling Servicer")
    server.add_insecure_port('[::]:50051')
    server.start()
    logger.info("Start server")
    server.wait_for_termination()


logging.basicConfig(format='%(relativeCreated)5d %(name)-15s %(levelname)-8s %(message)s')
logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)
if __name__ == '__main__':
    serve()
