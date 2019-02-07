# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import apikey_pb2 as apikey__pb2


class ApiKeyerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GenerateNewApiKey = channel.unary_unary(
        '/apikey.ApiKeyer/GenerateNewApiKey',
        request_serializer=apikey__pb2.KeyRequest.SerializeToString,
        response_deserializer=apikey__pb2.ApiKey.FromString,
        )
    self.RevokeApiKey = channel.unary_unary(
        '/apikey.ApiKeyer/RevokeApiKey',
        request_serializer=apikey__pb2.ApiKey.SerializeToString,
        response_deserializer=apikey__pb2.Empty.FromString,
        )
    self.ListApiKeys = channel.unary_unary(
        '/apikey.ApiKeyer/ListApiKeys',
        request_serializer=apikey__pb2.KeyListRequest.SerializeToString,
        response_deserializer=apikey__pb2.ApiKeyList.FromString,
        )


class ApiKeyerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GenerateNewApiKey(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RevokeApiKey(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListApiKeys(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ApiKeyerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GenerateNewApiKey': grpc.unary_unary_rpc_method_handler(
          servicer.GenerateNewApiKey,
          request_deserializer=apikey__pb2.KeyRequest.FromString,
          response_serializer=apikey__pb2.ApiKey.SerializeToString,
      ),
      'RevokeApiKey': grpc.unary_unary_rpc_method_handler(
          servicer.RevokeApiKey,
          request_deserializer=apikey__pb2.ApiKey.FromString,
          response_serializer=apikey__pb2.Empty.SerializeToString,
      ),
      'ListApiKeys': grpc.unary_unary_rpc_method_handler(
          servicer.ListApiKeys,
          request_deserializer=apikey__pb2.KeyListRequest.FromString,
          response_serializer=apikey__pb2.ApiKeyList.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'apikey.ApiKeyer', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
