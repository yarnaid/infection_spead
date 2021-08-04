from __future__ import print_function
from gRPC import spec_pb2_grpc, spec_pb2
from dataStructure.gRPC import StatusCode, UpdateRequest, Metadata
from pure_protobuf.types import int32
from itertools import count
import logging
import uuid
import grpc


def update_request(stub):
    """
    Request to update the states of modeling objects
    :param stub: a stub that we can use to use the functions described in spec. proto
    :return: spec.proto Request Response obj : containing list of all Human and their par in modeling
    """
    req = UpdateRequest(meta=Metadata(status=StatusCode.SUCCESS,
                                      request_id=int32(next(counter)),
                                      UUID=str(uuid.uuid4()))
                        )
    human_list = stub.GetUpdate(req)  # We get a list of people in the simulation from the server
    logger.info("Receive update response")
    return human_list


def get_map(stub):
    """
    Request for getting map objects
    :param stub: a stub that we can use to use the functions described in spec. proto
    :return: spec.proto Map obj : containing Map data and list of all building and their par in modeling
    """
    req = spec_pb2.Empty()
    src_map = stub.GetMap(req)  # We received a generator of objects on the map from the server
    logger.info("Receive map from server ")
    return src_map


def run_update():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        logger.info("Set channel to server")
        stub = spec_pb2_grpc.ModelingStub(channel)
        update_request(stub)


def run_get_map():
    with grpc.insecure_channel('localhost:50051') as channel:
        logger.info("Set channel to server")
        stub = spec_pb2_grpc.ModelingStub(channel)
        src_map = get_map(stub)
    return src_map


logging.basicConfig(format='%(relativeCreated)5d %(name)-15s %(levelname)-8s %(message)s')
logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)
counter = count(1)     # set counter for requests
