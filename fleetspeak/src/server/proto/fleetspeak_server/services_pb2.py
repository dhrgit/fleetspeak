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

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fleetspeak/src/server/proto/fleetspeak_server/services.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fleetspeak/src/server/proto/fleetspeak_server/services.proto',
  package='fleetspeak.server',
  syntax='proto3',
  serialized_pb=_b('\n<fleetspeak/src/server/proto/fleetspeak_server/services.proto\x12\x11\x66leetspeak.server\x1a\x19google/protobuf/any.proto\"m\n\rServiceConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x66\x61\x63tory\x18\x02 \x01(\t\x12\x17\n\x0fmax_parallelism\x18\x03 \x01(\r\x12$\n\x06\x63onfig\x18\x04 \x01(\x0b\x32\x14.google.protobuf.Anyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])




_SERVICECONFIG = _descriptor.Descriptor(
  name='ServiceConfig',
  full_name='fleetspeak.server.ServiceConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='fleetspeak.server.ServiceConfig.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='factory', full_name='fleetspeak.server.ServiceConfig.factory', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_parallelism', full_name='fleetspeak.server.ServiceConfig.max_parallelism', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='config', full_name='fleetspeak.server.ServiceConfig.config', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=110,
  serialized_end=219,
)

_SERVICECONFIG.fields_by_name['config'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['ServiceConfig'] = _SERVICECONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServiceConfig = _reflection.GeneratedProtocolMessageType('ServiceConfig', (_message.Message,), dict(
  DESCRIPTOR = _SERVICECONFIG,
  __module__ = 'fleetspeak.src.server.proto.fleetspeak_server.services_pb2'
  # @@protoc_insertion_point(class_scope:fleetspeak.server.ServiceConfig)
  ))
_sym_db.RegisterMessage(ServiceConfig)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
