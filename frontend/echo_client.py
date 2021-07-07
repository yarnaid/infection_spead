from __future__ import print_function
from gRPC import spec_pb2_grpc, spec_pb2
from dataStructure.gRPC import statusCode, UpdateRequest, Metadata
from pure_protobuf.types import int32
from itertools import count
import logging
import uuid
import grpc


def update_request(stub):  # Request to update the states of modeling objects
    req = UpdateRequest(meta=Metadata(status=statusCode.SUCCESS,
                                      request_id=int32(next(counter)),
                                      UUID=str(uuid.uuid1()))
                        )
    object_generator = stub.GetUpdate(req)  # We get a generator of people in the simulation from the server
    return object_generator


def get_map(stub):  # Request for getting map objects
    req = spec_pb2.Empty()
    map_generator = stub.GetMap(req)  # We received a generator of objects on the map from the server
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
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.debug('black betty')
    counter = count(1)
    # run_get_map()
    # run_update()
