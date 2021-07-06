# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from gRPC import spec_pb2 as spec__pb2


class ModelingStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetUpdate = channel.unary_stream(
            '/Modeling/GetUpdate',
            request_serializer=spec__pb2.UpdateRequest.SerializeToString,
            response_deserializer=spec__pb2.UpdateResponse.FromString,
        )
        self.GetMap = channel.unary_stream(
            '/Modeling/GetMap',
            request_serializer=spec__pb2.Empty.SerializeToString,
            response_deserializer=spec__pb2.Map.FromString,
        )


class ModelingServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMap(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ModelingServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetUpdate': grpc.unary_stream_rpc_method_handler(
            servicer.GetUpdate,
            request_deserializer=spec__pb2.UpdateRequest.FromString,
            response_serializer=spec__pb2.UpdateResponse.SerializeToString,
        ),
        'GetMap': grpc.unary_stream_rpc_method_handler(
            servicer.GetMap,
            request_deserializer=spec__pb2.Empty.FromString,
            response_serializer=spec__pb2.Map.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'Modeling', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Modeling(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetUpdate(request,
                  target,
                  options=(),
                  channel_credentials=None,
                  call_credentials=None,
                  insecure=False,
                  compression=None,
                  wait_for_ready=None,
                  timeout=None,
                  metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Modeling/GetUpdate',
                                              spec__pb2.UpdateRequest.SerializeToString,
                                              spec__pb2.UpdateResponse.FromString,
                                              options, channel_credentials,
                                              insecure, call_credentials, compression, wait_for_ready, timeout,
                                              metadata)

    @staticmethod
    def GetMap(request,
               target,
               options=(),
               channel_credentials=None,
               call_credentials=None,
               insecure=False,
               compression=None,
               wait_for_ready=None,
               timeout=None,
               metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Modeling/GetMap',
                                              spec__pb2.Empty.SerializeToString,
                                              spec__pb2.Map.FromString,
                                              options, channel_credentials,
                                              insecure, call_credentials, compression, wait_for_ready, timeout,
                                              metadata)
