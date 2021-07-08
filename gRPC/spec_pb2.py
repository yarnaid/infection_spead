# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spec.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='spec.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nspec.proto\"\x87\x01\n\x08Metadata\x12$\n\x06status\x18\x01 \x01(\x0e\x32\x14.Metadata.statusCode\x12\x12\n\nrequest_id\x18\x02 \x01(\x05\x12\x0c\n\x04UUID\x18\x03 \x01(\t\"3\n\nstatusCode\x12\r\n\tUNDEFINED\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\t\n\x05\x45RROR\x10\x02\"(\n\rUpdateRequest\x12\x17\n\x04meta\x18\x01 \x01(\x0b\x32\t.Metadata\"E\n\x0eUpdateResponse\x12\x17\n\x04meta\x18\x01 \x01(\x0b\x32\t.Metadata\x12\x1a\n\x05state\x18\x02 \x01(\x0b\x32\x0b.HumanState\"\x8a\x02\n\x03Map\x12\x17\n\x04meta\x18\x01 \x01(\x0b\x32\t.Metadata\x12\x12\n\nmap_size_w\x18\x02 \x01(\x02\x12\x12\n\nmap_size_h\x18\x03 \x01(\x02\x12\x1f\n\x08\x62uilding\x18\x04 \x01(\x0b\x32\r.Map.Building\x1a\xa0\x01\n\x08\x42uilding\x12\x17\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\t.BaseUnit\x12(\n\x04type\x18\x02 \x01(\x0e\x32\x1a.Map.Building.BuildingType\x12\r\n\x05width\x18\x03 \x01(\x05\x12\x0e\n\x06length\x18\x04 \x01(\x05\x12\r\n\x05\x61ngle\x18\x05 \x01(\x05\"#\n\x0c\x42uildingType\x12\t\n\x05HOUSE\x10\x00\x12\x08\n\x04ROAD\x10\x01\"\x85\x01\n\nHumanState\x12\x17\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\t.BaseUnit\x12#\n\x04type\x18\x02 \x01(\x0e\x32\x15.HumanState.HumanType\"9\n\tHumanType\x12\n\n\x06NORMAL\x10\x00\x12\x07\n\x03ILL\x10\x01\x12\r\n\tRECOVERED\x10\x02\x12\x08\n\x04\x44\x45\x41\x44\x10\x03\"\x07\n\x05\x45mpty\"8\n\x08\x42\x61seUnit\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07\x63oord_x\x18\x02 \x01(\x02\x12\x0f\n\x07\x63oord_y\x18\x03 \x01(\x02\x32X\n\x08Modeling\x12\x30\n\tGetUpdate\x12\x0e.UpdateRequest\x1a\x0f.UpdateResponse\"\x00\x30\x01\x12\x1a\n\x06GetMap\x12\x06.Empty\x1a\x04.Map\"\x00\x30\x01\x62\x06proto3'
)



_METADATA_STATUSCODE = _descriptor.EnumDescriptor(
  name='statusCode',
  full_name='Metadata.statusCode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=99,
  serialized_end=150,
)
_sym_db.RegisterEnumDescriptor(_METADATA_STATUSCODE)

_MAP_BUILDING_BUILDINGTYPE = _descriptor.EnumDescriptor(
  name='BuildingType',
  full_name='Map.Building.BuildingType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HOUSE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ROAD', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=497,
  serialized_end=532,
)
_sym_db.RegisterEnumDescriptor(_MAP_BUILDING_BUILDINGTYPE)

_HUMANSTATE_HUMANTYPE = _descriptor.EnumDescriptor(
  name='HumanType',
  full_name='HumanState.HumanType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NORMAL', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ILL', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RECOVERED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEAD', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=611,
  serialized_end=668,
)
_sym_db.RegisterEnumDescriptor(_HUMANSTATE_HUMANTYPE)


_METADATA = _descriptor.Descriptor(
  name='Metadata',
  full_name='Metadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='Metadata.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='request_id', full_name='Metadata.request_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='UUID', full_name='Metadata.UUID', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _METADATA_STATUSCODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15,
  serialized_end=150,
)


_UPDATEREQUEST = _descriptor.Descriptor(
  name='UpdateRequest',
  full_name='UpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='UpdateRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=152,
  serialized_end=192,
)


_UPDATERESPONSE = _descriptor.Descriptor(
  name='UpdateResponse',
  full_name='UpdateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='UpdateResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='UpdateResponse.state', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=194,
  serialized_end=263,
)


_MAP_BUILDING = _descriptor.Descriptor(
  name='Building',
  full_name='Map.Building',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='base', full_name='Map.Building.base', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='Map.Building.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='width', full_name='Map.Building.width', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='length', full_name='Map.Building.length', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='angle', full_name='Map.Building.angle', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MAP_BUILDING_BUILDINGTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=372,
  serialized_end=532,
)

_MAP = _descriptor.Descriptor(
  name='Map',
  full_name='Map',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='Map.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='map_size_w', full_name='Map.map_size_w', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='map_size_h', full_name='Map.map_size_h', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='building', full_name='Map.building', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_MAP_BUILDING, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=266,
  serialized_end=532,
)


_HUMANSTATE = _descriptor.Descriptor(
  name='HumanState',
  full_name='HumanState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='base', full_name='HumanState.base', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='HumanState.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _HUMANSTATE_HUMANTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=535,
  serialized_end=668,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=670,
  serialized_end=677,
)


_BASEUNIT = _descriptor.Descriptor(
  name='BaseUnit',
  full_name='BaseUnit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='BaseUnit.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='coord_x', full_name='BaseUnit.coord_x', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='coord_y', full_name='BaseUnit.coord_y', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=679,
  serialized_end=735,
)

_METADATA.fields_by_name['status'].enum_type = _METADATA_STATUSCODE
_METADATA_STATUSCODE.containing_type = _METADATA
_UPDATEREQUEST.fields_by_name['meta'].message_type = _METADATA
_UPDATERESPONSE.fields_by_name['meta'].message_type = _METADATA
_UPDATERESPONSE.fields_by_name['state'].message_type = _HUMANSTATE
_MAP_BUILDING.fields_by_name['base'].message_type = _BASEUNIT
_MAP_BUILDING.fields_by_name['type'].enum_type = _MAP_BUILDING_BUILDINGTYPE
_MAP_BUILDING.containing_type = _MAP
_MAP_BUILDING_BUILDINGTYPE.containing_type = _MAP_BUILDING
_MAP.fields_by_name['meta'].message_type = _METADATA
_MAP.fields_by_name['building'].message_type = _MAP_BUILDING
_HUMANSTATE.fields_by_name['base'].message_type = _BASEUNIT
_HUMANSTATE.fields_by_name['type'].enum_type = _HUMANSTATE_HUMANTYPE
_HUMANSTATE_HUMANTYPE.containing_type = _HUMANSTATE
DESCRIPTOR.message_types_by_name['Metadata'] = _METADATA
DESCRIPTOR.message_types_by_name['UpdateRequest'] = _UPDATEREQUEST
DESCRIPTOR.message_types_by_name['UpdateResponse'] = _UPDATERESPONSE
DESCRIPTOR.message_types_by_name['Map'] = _MAP
DESCRIPTOR.message_types_by_name['HumanState'] = _HUMANSTATE
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['BaseUnit'] = _BASEUNIT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Metadata = _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), {
  'DESCRIPTOR' : _METADATA,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:Metadata)
  })
_sym_db.RegisterMessage(Metadata)

UpdateRequest = _reflection.GeneratedProtocolMessageType('UpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEREQUEST,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:UpdateRequest)
  })
_sym_db.RegisterMessage(UpdateRequest)

UpdateResponse = _reflection.GeneratedProtocolMessageType('UpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATERESPONSE,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:UpdateResponse)
  })
_sym_db.RegisterMessage(UpdateResponse)

Map = _reflection.GeneratedProtocolMessageType('Map', (_message.Message,), {

  'Building' : _reflection.GeneratedProtocolMessageType('Building', (_message.Message,), {
    'DESCRIPTOR' : _MAP_BUILDING,
    '__module__' : 'spec_pb2'
    # @@protoc_insertion_point(class_scope:Map.Building)
    })
  ,
  'DESCRIPTOR' : _MAP,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:Map)
  })
_sym_db.RegisterMessage(Map)
_sym_db.RegisterMessage(Map.Building)

HumanState = _reflection.GeneratedProtocolMessageType('HumanState', (_message.Message,), {
  'DESCRIPTOR' : _HUMANSTATE,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:HumanState)
  })
_sym_db.RegisterMessage(HumanState)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)

BaseUnit = _reflection.GeneratedProtocolMessageType('BaseUnit', (_message.Message,), {
  'DESCRIPTOR' : _BASEUNIT,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:BaseUnit)
  })
_sym_db.RegisterMessage(BaseUnit)



_MODELING = _descriptor.ServiceDescriptor(
  name='Modeling',
  full_name='Modeling',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=737,
  serialized_end=825,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetUpdate',
    full_name='Modeling.GetUpdate',
    index=0,
    containing_service=None,
    input_type=_UPDATEREQUEST,
    output_type=_UPDATERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetMap',
    full_name='Modeling.GetMap',
    index=1,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_MAP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MODELING)

DESCRIPTOR.services_by_name['Modeling'] = _MODELING

# @@protoc_insertion_point(module_scope)
