# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from fleetspeak.src.common.proto.fleetspeak import common_pb2 as fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2
from fleetspeak.src.server.proto.fleetspeak_server import admin_pb2 as fleetspeak_dot_src_dot_server_dot_proto_dot_fleetspeak__server_dot_admin__pb2


class AdminStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateBroadcast = channel.unary_unary(
        '/fleetspeak.server.Admin/CreateBroadcast',
        request_serializer=fleetspeak_dot_src_dot_server_dot_proto_dot_fleetspeak__server_dot_admin__pb2.CreateBroadcastRequest.SerializeToString,
        response_deserializer=fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.EmptyMessage.FromString,
        )
    self.ListActiveBroadcasts = channel.unary_unary(
        '/fleetspeak.server.Admin/ListActiveBroadcasts',
        request_serializer=fleetspeak_dot_src_dot_server_dot_proto_dot_fleetspeak__server_dot_admin__pb2.ListActiveBroadcastsRequest.SerializeToString,
        response_deserializer=fleetspeak_dot_src_dot_server_dot_proto_dot_fleetspeak__server_dot_admin__pb2.ListActiveBroadcastsResponse.FromString,
        )
    self.ListClients = channel.unary_unary(
        '/fleetspeak.server.Admin/ListClients',
        request_serializer=fleetspeak_dot_src_dot_server_dot_proto_dot_fleetspeak__server_dot_admin__pb2.ListClientsRequest.SerializeToString,
        response_deserializer=fleetspeak_dot_src_dot_server_dot_proto_dot_fleetspeak__server_dot_admin__pb2.ListClientsResponse.FromString,
        )
    self.ListClientContacts = channel.unary_unary(
        '/fleetspeak.server.Admin/ListClientContacts',
        request_serializer=fleetspeak_dot_src_dot_server_dot_proto_dot_fleetspeak__server_dot_admin__pb2.ListClientContactsRequest.SerializeToString,
        response_deserializer=fleetspeak_dot_src_dot_server_dot_proto_dot_fleetspeak__server_dot_admin__pb2.ListClientContactsResponse.FromString,
        )
    self.GetMessageStatus = channel.unary_unary(
        '/fleetspeak.server.Admin/GetMessageStatus',
        request_serializer=fleetspeak_dot_src_dot_server_dot_proto_dot_fleetspeak__server_dot_admin__pb2.GetMessageStatusRequest.SerializeToString,
        response_deserializer=fleetspeak_dot_src_dot_server_dot_proto_dot_fleetspeak__server_dot_admin__pb2.GetMessageStatusResponse.FromString,
        )
    self.InsertMessage = channel.unary_unary(
        '/fleetspeak.server.Admin/InsertMessage',
        request_serializer=fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.Message.SerializeToString,
        response_deserializer=fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.EmptyMessage.FromString,
        )
    self.StoreFile = channel.unary_unary(
        '/fleetspeak.server.Admin/StoreFile',
        request_serializer=fleetspeak_dot_src_dot_server_dot_proto_dot_fleetspeak__server_dot_admin__pb2.StoreFileRequest.SerializeToString,
        response_deserializer=fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.EmptyMessage.FromString,
        )
    self.KeepAlive = channel.unary_unary(
        '/fleetspeak.server.Admin/KeepAlive',
        request_serializer=fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.EmptyMessage.SerializeToString,
        response_deserializer=fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.EmptyMessage.FromString,
        )


class AdminServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def CreateBroadcast(self, request, context):
    """CreateBroadcast creates a FS broadcast, potentially sending a message to
    many machines in the fleet.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListActiveBroadcasts(self, request, context):
    """ListActiveBroadcasts lists the currently active FS broadcasts.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListClients(self, request, context):
    """ListClients lists the currently active FS clients.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListClientContacts(self, request, context):
    """ListClientContacts lists the contact history for a client.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetMessageStatus(self, request, context):
    """GetMessageStatus retrieves the current status of a message.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InsertMessage(self, request, context):
    """InsertMessage inserts a message into the Fleetspeak system to be processed
    by the server or delivered to a client.
    TODO: Have this method return the message that is written to the
    datastore (or at least the id).
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StoreFile(self, request, context):
    """StoreFile inserts a file into the Fleetspeak system.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def KeepAlive(self, request, context):
    """KeepAlive does as little as possible.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AdminServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateBroadcast': grpc.unary_unary_rpc_method_handler(
          servicer.CreateBroadcast,
          request_deserializer=fleetspeak_dot_src_dot_server_dot_proto_dot_fleetspeak__server_dot_admin__pb2.CreateBroadcastRequest.FromString,
          response_serializer=fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.EmptyMessage.SerializeToString,
      ),
      'ListActiveBroadcasts': grpc.unary_unary_rpc_method_handler(
          servicer.ListActiveBroadcasts,
          request_deserializer=fleetspeak_dot_src_dot_server_dot_proto_dot_fleetspeak__server_dot_admin__pb2.ListActiveBroadcastsRequest.FromString,
          response_serializer=fleetspeak_dot_src_dot_server_dot_proto_dot_fleetspeak__server_dot_admin__pb2.ListActiveBroadcastsResponse.SerializeToString,
      ),
      'ListClients': grpc.unary_unary_rpc_method_handler(
          servicer.ListClients,
          request_deserializer=fleetspeak_dot_src_dot_server_dot_proto_dot_fleetspeak__server_dot_admin__pb2.ListClientsRequest.FromString,
          response_serializer=fleetspeak_dot_src_dot_server_dot_proto_dot_fleetspeak__server_dot_admin__pb2.ListClientsResponse.SerializeToString,
      ),
      'ListClientContacts': grpc.unary_unary_rpc_method_handler(
          servicer.ListClientContacts,
          request_deserializer=fleetspeak_dot_src_dot_server_dot_proto_dot_fleetspeak__server_dot_admin__pb2.ListClientContactsRequest.FromString,
          response_serializer=fleetspeak_dot_src_dot_server_dot_proto_dot_fleetspeak__server_dot_admin__pb2.ListClientContactsResponse.SerializeToString,
      ),
      'GetMessageStatus': grpc.unary_unary_rpc_method_handler(
          servicer.GetMessageStatus,
          request_deserializer=fleetspeak_dot_src_dot_server_dot_proto_dot_fleetspeak__server_dot_admin__pb2.GetMessageStatusRequest.FromString,
          response_serializer=fleetspeak_dot_src_dot_server_dot_proto_dot_fleetspeak__server_dot_admin__pb2.GetMessageStatusResponse.SerializeToString,
      ),
      'InsertMessage': grpc.unary_unary_rpc_method_handler(
          servicer.InsertMessage,
          request_deserializer=fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.Message.FromString,
          response_serializer=fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.EmptyMessage.SerializeToString,
      ),
      'StoreFile': grpc.unary_unary_rpc_method_handler(
          servicer.StoreFile,
          request_deserializer=fleetspeak_dot_src_dot_server_dot_proto_dot_fleetspeak__server_dot_admin__pb2.StoreFileRequest.FromString,
          response_serializer=fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.EmptyMessage.SerializeToString,
      ),
      'KeepAlive': grpc.unary_unary_rpc_method_handler(
          servicer.KeepAlive,
          request_deserializer=fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.EmptyMessage.FromString,
          response_serializer=fleetspeak_dot_src_dot_common_dot_proto_dot_fleetspeak_dot_common__pb2.EmptyMessage.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'fleetspeak.server.Admin', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
