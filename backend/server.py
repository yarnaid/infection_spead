from gRPC import spec_pb2_grpc, spec_pb2
from concurrent import futures

import logging
import grpc
from dataStructure.gRPC import gRPC_status_creator


class ModelingServicer(spec_pb2_grpc.ModelingServicer):

    def __init__(self, map_obj, model_objects):  # Remember our Backend output exists
        self.map = map_obj
        self.model_objects = model_objects

    def GetUpdate(self, request, context):  # Generator of people on modeling
        status = spec_pb2.Metadata(status=gRPC_status_creator["SUCCESS"],
                                   request_id=request.meta.request_id)
        for elem in self.model_objects:
            grpc_state = ModelingServicer.create_update_response(elem, status)
            yield grpc_state

    @staticmethod
    def create_update_response(human, status):  # create pb2 object from backed human
        return spec_pb2.UpdateResponse(meta=status,
                                       state=spec_pb2.State(
                                           id=human.id,
                                           type=human.type,
                                           coord_x=human.x,
                                           coord_y=human.y
                                       ))

    def GetMap(self, request, context):  # Generator of map objects
        status = spec_pb2.Metadata(status=gRPC_status_creator["SUCCESS"],
                                   request_id=request.meta.request_id)
        for building in self.map:
            grpc_building = self.create_grpc_building(building, status)
            yield grpc_building

    @staticmethod
    def create_grpc_building(building, status):  # create pb2 object from backend building
        return spec_pb2.Map(meta=status,
                            building=spec_pb2.Map.Building(
                                id=building.id,
                                type=building.type,
                                coord_x=building.x,
                                coord_y=building.y,
                                width=building.width,
                                length=building.length,
                                angle=building.angle
                            ))


def serve():  # Responsible for the operation of the server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    spec_pb2_grpc.add_ModelingServicer_to_server(
        ModelingServicer(None, None), server)  # NEED BACKEND OUTPUT INSTEAD OF NONE
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
