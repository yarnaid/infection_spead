from gRPC import spec_pb2_grpc, spec_pb2
from concurrent import futures

import logging
import grpc
from dataStructure.gRPC import gRPC_status_creator


class ModelingServicer(spec_pb2_grpc.ModelingServicer):

    def GetUpdate(self, request, context):
        upd = spec_pb2.UpdateResponse(meta=spec_pb2.Metadata(status=gRPC_status_creator("SUCCESS"),
                                                             request_id=request.meta.request_id))
        return upd

    def GetMap(self, request, context):
        current_map = []  # One of output of our server
        for building in current_map:
            grpc_building = self.create_grpc_building(building, request)
            yield grpc_building

    @staticmethod
    def create_grpc_building(building, request):
        return spec_pb2.Map(meta=spec_pb2.Metadata(status=gRPC_status_creator("SUCCESS"),
                                                   request_id=request.meta.request_id),
                            building=spec_pb2.Metadata.Building(
                                id=building.id,
                                type=building.type,
                                coord_x=building.x,
                                coord_y=building.y,
                                width=building.width,
                                length=building.length,
                                angle=building.angle
                            ))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    spec_pb2_grpc.add_ModelingServicer_to_server(
        ModelingServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
