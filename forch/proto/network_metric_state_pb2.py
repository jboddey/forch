# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: forch/proto/network_metric_state.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from forch.proto import shared_constants_pb2 as forch_dot_proto_dot_shared__constants__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='forch/proto/network_metric_state.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n&forch/proto/network_metric_state.proto\x1a\"forch/proto/shared_constants.proto\"t\n\x08\x41\x63lState\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\"\n\x05rules\x18\x02 \x03(\x0b\x32\x13.AclState.RuleState\x1a\x36\n\tRuleState\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x14\n\x0cpacket_count\x18\x03 \x01(\x05\"P\n\x0cVlanAclState\x12\x17\n\x04\x61\x63ls\x18\x01 \x03(\x0b\x32\t.AclState\x12\'\n\x11packet_rate_state\x18\x02 \x01(\x0e\x32\x0c.State.State\"2\n\tVlanState\x12\x0f\n\x07vlan_id\x18\x01 \x01(\x05\x12\x14\n\x0cpacket_count\x18\x02 \x01(\x05\x62\x06proto3')
  ,
  dependencies=[forch_dot_proto_dot_shared__constants__pb2.DESCRIPTOR,])




_ACLSTATE_RULESTATE = _descriptor.Descriptor(
  name='RuleState',
  full_name='AclState.RuleState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='description', full_name='AclState.RuleState.description', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packet_count', full_name='AclState.RuleState.packet_count', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=140,
  serialized_end=194,
)

_ACLSTATE = _descriptor.Descriptor(
  name='AclState',
  full_name='AclState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='AclState.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rules', full_name='AclState.rules', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ACLSTATE_RULESTATE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=78,
  serialized_end=194,
)


_VLANACLSTATE = _descriptor.Descriptor(
  name='VlanAclState',
  full_name='VlanAclState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='acls', full_name='VlanAclState.acls', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packet_rate_state', full_name='VlanAclState.packet_rate_state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=196,
  serialized_end=276,
)


_VLANSTATE = _descriptor.Descriptor(
  name='VlanState',
  full_name='VlanState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vlan_id', full_name='VlanState.vlan_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packet_count', full_name='VlanState.packet_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=278,
  serialized_end=328,
)

_ACLSTATE_RULESTATE.containing_type = _ACLSTATE
_ACLSTATE.fields_by_name['rules'].message_type = _ACLSTATE_RULESTATE
_VLANACLSTATE.fields_by_name['acls'].message_type = _ACLSTATE
_VLANACLSTATE.fields_by_name['packet_rate_state'].enum_type = forch_dot_proto_dot_shared__constants__pb2._STATE_STATE
DESCRIPTOR.message_types_by_name['AclState'] = _ACLSTATE
DESCRIPTOR.message_types_by_name['VlanAclState'] = _VLANACLSTATE
DESCRIPTOR.message_types_by_name['VlanState'] = _VLANSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AclState = _reflection.GeneratedProtocolMessageType('AclState', (_message.Message,), dict(

  RuleState = _reflection.GeneratedProtocolMessageType('RuleState', (_message.Message,), dict(
    DESCRIPTOR = _ACLSTATE_RULESTATE,
    __module__ = 'forch.proto.network_metric_state_pb2'
    # @@protoc_insertion_point(class_scope:AclState.RuleState)
    ))
  ,
  DESCRIPTOR = _ACLSTATE,
  __module__ = 'forch.proto.network_metric_state_pb2'
  # @@protoc_insertion_point(class_scope:AclState)
  ))
_sym_db.RegisterMessage(AclState)
_sym_db.RegisterMessage(AclState.RuleState)

VlanAclState = _reflection.GeneratedProtocolMessageType('VlanAclState', (_message.Message,), dict(
  DESCRIPTOR = _VLANACLSTATE,
  __module__ = 'forch.proto.network_metric_state_pb2'
  # @@protoc_insertion_point(class_scope:VlanAclState)
  ))
_sym_db.RegisterMessage(VlanAclState)

VlanState = _reflection.GeneratedProtocolMessageType('VlanState', (_message.Message,), dict(
  DESCRIPTOR = _VLANSTATE,
  __module__ = 'forch.proto.network_metric_state_pb2'
  # @@protoc_insertion_point(class_scope:VlanState)
  ))
_sym_db.RegisterMessage(VlanState)


# @@protoc_insertion_point(module_scope)
