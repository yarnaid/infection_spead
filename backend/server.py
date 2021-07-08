import os

from gRPC import spec_pb2_grpc, spec_pb2
from dataStructure.gRPC import Map, UpdateResponse, Metadata, statusCode, HumanState, BaseUnit, BuildingType, HumanType, \
    Building
from concurrent import futures
from pure_protobuf.types import int32
import logging
import grpc
import uuid


class ModelingSerializer:
    @staticmethod
    def create_update_response(human, status):  # create pb2 object from backed human
        return UpdateResponse(meta=status,
                              state=HumanState(
                                  base=BaseUnit(id=int32(human.id), coord_x=float(human.x), coord_y=float(human.y)),
                                  type=HumanType(human.type),
                              ))

    @staticmethod
    def create_grpc_building(building, status, map_w, map_h):  # create pb2 object from backend building
        return Map(meta=status, map_size_w=map_w, map_size_h=map_h,
                   building=Building(
                       base=BaseUnit(id=int32(building.id), coord_x=float(building.x), coord_y=float(building.y)),
                       type=BuildingType(building.type),
                       width=int32(building.width),
                       length=int32(building.length),
                       angle=int32(building.angle)
                   ))

    @staticmethod
    def create_success_meta_response(request):
        return Metadata(status=statusCode.SUCCESS,
                        request_id=int32(request.meta.request_id))


class ModelingServicer(spec_pb2_grpc.ModelingServicer):

    def __init__(self, map_obj, model_objects, serializer):  # Remember our Backend output exists
        self.map = map_obj
        self.model_objects = model_objects
        self.serializer = serializer

    def GetUpdate(self, request, context):  # Generator of people on modeling
        logger.info("Get update request")
        status = self.serializer.create_success_meta_response(request)

        for elem in self.model_objects:
            status.UUID = str(uuid.uuid1())
            grpc_state = self.serializer.create_update_response(elem, status)
            yield grpc_state

    def GetMap(self, request, context):  # Generator of map objects
        logger.info("Get map request")
        status = self.serializer.create_success_meta_response(request)
        map_w, map_h = self.map.size()  # method to get size of map
        for building in self.map:
            status.UUID = str(uuid.uuid1())
            grpc_building = self.serializer.create_grpc_building(building, status, map_w, map_h)
            yield grpc_building


def serve():  # Responsible for the operation of the server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=os.cpu_count()))
    spec_pb2_grpc.add_ModelingServicer_to_server(
        ModelingServicer(None, None, ModelingSerializer), server)  # NEED BACKEND OUTPUT INSTEAD OF NONE
    logger.info("Set Modeling Servicer")
    server.add_insecure_port('[::]:50051')
    server.start()
    logger.info("Start server")
    server.wait_for_termination()


logging.basicConfig(format='%(relativeCreated)5d %(name)-15s %(levelname)-8s %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
if __name__ == '__main__':
    serve()
