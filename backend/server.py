import os

from gRPC import spec_pb2_grpc, spec_pb2
from dataStructure.gRPC import Map, UpdateResponse, Metadata, statusCode, HumanState, BaseUnit, BuildingType, HumanType, \
    Building
from concurrent import futures
from pure_protobuf.types import int32
import logging
import grpc
import uuid


class ModelingServicer(spec_pb2_grpc.ModelingServicer):

    def __init__(self, map_obj, model_objects):  # Remember our Backend output exists
        self.map = map_obj
        self.model_objects = model_objects

    def GetUpdate(self, request, context):  # Generator of people on modeling
        status = Metadata(status=statusCode.SUCCESS,
                          request_id=int32(request.meta.request_id))

        for elem in self.model_objects:
            status.UUID = str(uuid.uuid1())
            grpc_state = ModelingServicer.create_update_response(elem, status)
            yield grpc_state

    @staticmethod
    def create_update_response(human, status):  # create pb2 object from backed human
        return UpdateResponse(meta=status,
                              state=HumanState(
                                  base=BaseUnit(id=int32(human.id), coord_x=int32(human.x), coord_y=int32(human.y)),
                                  type=HumanType(human.type),
                              ))

    def GetMap(self, request, context):  # Generator of map objects
        status = Metadata(status=statusCode.SUCCESS,
                          request_id=int32(request.meta.request_id))
        for building in self.map:
            status.UUID = str(uuid.uuid1())
            grpc_building = self.create_grpc_building(building, status)
            yield grpc_building

    @staticmethod
    def create_grpc_building(building, status):  # create pb2 object from backend building
        return Map(meta=status,
                   building=Building(
                       base=BaseUnit(id=int32(building.id), coord_x=int32(building.x), coord_y=int32(building.y)),
                       type=BuildingType(building.type),
                       width=int32(building.width),
                       length=int32(building.length),
                       angle=int32(building.angle)
                   ))


def serve():  # Responsible for the operation of the server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=os.cpu_count()))
    spec_pb2_grpc.add_ModelingServicer_to_server(
        ModelingServicer(None, None), server)  # NEED BACKEND OUTPUT INSTEAD OF NONE
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
