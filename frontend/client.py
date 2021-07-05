from __future__ import print_function
from gRPC import spec_pb2_grpc, spec_pb2
from dataStructure.gRPC import gRPC_status_creator,RequestCounter
import random
import logging

import grpc


def update_request(stub):
    req = spec_pb2.UpdateRequest(meta=spec_pb2.Metadata(status=gRPC_status_creator("SUCCESS"),
                                                        request_id=RequestCounter.give_id()))
    feature = stub.GetUpdate(req)


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = spec_pb2_grpc.ModelingStub(channel)
        update_request(stub)


if __name__ == '__main__':
    logging.basicConfig()
    run()
