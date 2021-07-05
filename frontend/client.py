from __future__ import print_function
from gRPC import spec_pb2_grpc, spec_pb2
from dataStructure.gRPC import gRPC_status_creator, RequestCounter
import logging

import grpc


def update_request(stub):  # Request to update the states of modeling objects
    req = spec_pb2.UpdateRequest(meta=spec_pb2.Metadata(status=gRPC_status_creator["SUCCESS"],
                                                        request_id=RequestCounter.give_id()))
    object_generator = stub.GetUpdate(req)  # We get a generator of people in the simulation from the server
    return object_generator


def get_map(stub):  # Request for getting map objects
    req = spec_pb2.Empty()
    map_generator = stub.Map(req)  # We received a generator of objects on the map from the server
    return map_generator


def run_update():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = spec_pb2_grpc.ModelingStub(channel)
        update_request(stub)


def run_get_map():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = spec_pb2_grpc.ModelingStub(channel)
        get_map(stub)


if __name__ == '__main__':
    logging.basicConfig()
    run_update()
    run_get_map()
