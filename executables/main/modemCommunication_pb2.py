# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: modemCommunication.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'modemCommunication.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18modemCommunication.proto\x12\x12modemCommunication\"D\n\x19ModemCommunicationRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x16\n\x0e\x63ontact_number\x18\x02 \x01(\x05\"*\n\x17ModemCommunicationReply\x12\x0f\n\x07message\x18\x01 \x01(\t2\x8d\x01\n\x19ModemCommunicationService\x12p\n\x12ModemCommunication\x12-.modemCommunication.ModemCommunicationRequest\x1a+.modemCommunication.ModemCommunicationReplyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'modemCommunication_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MODEMCOMMUNICATIONREQUEST']._serialized_start=48
  _globals['_MODEMCOMMUNICATIONREQUEST']._serialized_end=116
  _globals['_MODEMCOMMUNICATIONREPLY']._serialized_start=118
  _globals['_MODEMCOMMUNICATIONREPLY']._serialized_end=160
  _globals['_MODEMCOMMUNICATIONSERVICE']._serialized_start=163
  _globals['_MODEMCOMMUNICATIONSERVICE']._serialized_end=304
# @@protoc_insertion_point(module_scope)
