
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = 'oK@\xb8\xe7b!\xcb\x16\xcf\xabZcK\x9c\x0b'
    
_lr_action_items = {'DOMAIN':([20,40,46,47,51,60,61,63,67,70,71,73,74,76,85,89,94,101,103,112,113,115,117,120,124,],[39,53,39,39,62,39,39,39,39,39,-43,-48,39,39,39,-44,-49,-45,39,39,39,-52,39,-51,-50,]),'CONST':([19,21,22,24,25,27,31,32,36,43,50,54,55,56,93,96,97,102,105,],[20,-13,-15,-16,-17,20,-20,-18,-19,-14,-12,-28,-27,-11,-47,-21,-29,-42,-46,]),'NUMBER':([63,85,],[81,99,]),'MACRO_ENDIF':([5,8,9,10,11,12,14,15,17,18,50,56,],[-2,-3,-6,-9,16,-4,-8,-10,-5,-7,-12,-11,]),')':([103,110,111,114,119,121,122,],[109,-53,116,-55,123,-54,-56,]),'(':([91,104,],[103,113,]),',':([40,51,58,66,98,99,110,111,114,119,121,122,],[-37,-38,67,86,106,107,-53,117,-55,117,-54,-56,]),'ID':([2,4,6,20,23,26,28,33,34,37,38,39,40,46,47,51,53,57,60,61,62,63,64,65,67,68,69,70,71,72,73,74,76,83,85,86,89,92,94,100,101,103,106,107,108,112,113,115,117,118,120,124,],[3,5,13,40,41,42,45,48,49,51,52,-39,-37,40,40,-38,-40,66,40,40,-41,40,66,-30,40,-35,88,40,-43,91,-48,40,40,-31,40,-32,-44,104,-49,-36,-45,40,-34,-33,114,40,40,-52,40,122,-51,-50,]),'=':([52,66,],[63,85,]),'<':([29,30,],[46,47,]),'>':([40,51,59,87,],[-37,-38,68,100,]),'ICE_FILE':([7,],[14,]),'END':([35,40,41,42,44,51,75,77,78,79,80,81,82,84,88,90,95,109,116,123,],[50,-37,54,55,56,-38,93,-25,-26,96,-24,-22,-23,97,101,102,105,115,120,124,]),'STRING':([63,],[77,]),'DICTIONARY':([19,21,22,24,25,27,31,32,36,43,50,54,55,56,93,96,97,102,105,],[29,-13,-15,-16,-17,29,-20,-18,-19,-14,-12,-28,-27,-11,-47,-21,-29,-42,-46,]),'SEQUENCE':([19,21,22,24,25,27,31,32,36,43,50,54,55,56,93,96,97,102,105,],[30,-13,-15,-16,-17,30,-20,-18,-19,-14,-12,-28,-27,-11,-47,-21,-29,-42,-46,]),'ENUM':([19,21,22,24,25,27,31,32,36,43,50,54,55,56,93,96,97,102,105,],[28,-13,-15,-16,-17,28,-20,-18,-19,-14,-12,-28,-27,-11,-47,-21,-29,-42,-46,]),'MODULE':([5,8,9,10,12,14,15,17,18,19,21,22,24,25,27,31,32,36,43,50,54,55,56,93,96,97,102,105,],[6,6,-6,-9,6,-8,-10,6,-7,6,-13,-15,-16,-17,6,-20,-18,-19,-14,-12,-28,-27,-11,-47,-21,-29,-42,-46,]),'MACRO_INCLUDE':([5,9,12,14,18,],[7,-6,7,-8,-7,]),'MACRO_IFNDEF':([0,],[2,]),'STRUCT':([19,21,22,24,25,27,31,32,36,43,50,54,55,56,93,96,97,102,105,],[33,-13,-15,-16,-17,33,-20,-18,-19,-14,-12,-28,-27,-11,-47,-21,-29,-42,-46,]),'INTERFACE_TYPE':([61,73,76,94,115,120,124,],[74,-48,74,-49,-52,-51,-50,]),'FLOAT':([63,],[80,]),'OUT':([103,113,117,],[112,112,112,]),'BOOL':([63,],[82,]),'INTERFACE':([19,21,22,24,25,27,31,32,36,43,50,54,55,56,93,96,97,102,105,],[34,-13,-15,-16,-17,34,-20,-18,-19,-14,-12,-28,-27,-11,-47,-21,-29,-42,-46,]),'{':([13,45,48,49,],[19,57,60,61,]),'$end':([1,16,],[0,-1,]),'}':([19,21,22,24,25,27,31,32,36,43,50,54,55,56,61,64,65,70,71,73,76,83,86,89,93,94,96,97,101,102,105,106,107,115,120,124,],[35,-13,-15,-16,-17,44,-20,-18,-19,-14,-12,-28,-27,-11,75,84,-30,90,-43,-48,95,-31,-32,-44,-47,-49,-21,-29,-45,-42,-46,-34,-33,-52,-51,-50,]),'MACRO_DEFINE':([3,],[4,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'domain':([20,46,47,60,61,63,67,70,74,76,85,103,112,113,117,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'var_type':([20,46,47,60,61,63,67,70,74,76,85,103,112,113,117,],[38,58,59,69,72,78,87,69,92,72,98,108,118,108,108,]),'modules':([5,12,],[8,17,]),'module_member':([19,27,],[21,43,]),'module':([5,8,12,17,19,27,],[10,15,10,15,22,22,]),'sequence_type':([19,27,],[26,26,]),'dictionary_type':([19,27,],[23,23,]),'type_define':([19,27,],[24,24,]),'ice_file':([0,],[1,]),'struct':([19,27,],[25,25,]),'data':([63,],[79,]),'param':([103,113,117,],[110,110,121,]),'enum_members':([57,],[64,]),'params':([103,113,],[111,119,]),'member_funcs':([61,],[76,]),'module_members':([19,],[27,]),'enum':([19,27,],[31,31,]),'include_module':([5,12,],[9,18,]),'interface':([19,27,],[32,32,]),'member_func':([61,76,],[73,94,]),'file_statement':([5,],[11,]),'data_members':([60,],[70,]),'include_modules':([5,],[12,]),'data_member':([60,70,],[71,89,]),'enum_member':([57,64,],[65,83,]),'const_data':([19,27,],[36,36,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> ice_file","S'",1,None,None,None),
  ('ice_file -> MACRO_IFNDEF ID MACRO_DEFINE ID file_statement MACRO_ENDIF','ice_file',6,'p_ice_file','../icestream/iceyacc.py',23),
  ('file_statement -> <empty>','file_statement',0,'p_file_statement','../icestream/iceyacc.py',32),
  ('file_statement -> modules','file_statement',1,'p_file_statement','../icestream/iceyacc.py',33),
  ('file_statement -> include_modules','file_statement',1,'p_file_statement','../icestream/iceyacc.py',34),
  ('file_statement -> include_modules modules','file_statement',2,'p_file_statement','../icestream/iceyacc.py',35),
  ('include_modules -> include_module','include_modules',1,'p_include_modules','../icestream/iceyacc.py',46),
  ('include_modules -> include_modules include_module','include_modules',2,'p_include_modules','../icestream/iceyacc.py',47),
  ('include_module -> MACRO_INCLUDE ICE_FILE','include_module',2,'p_include_module','../icestream/iceyacc.py',55),
  ('modules -> module','modules',1,'p_modules','../icestream/iceyacc.py',60),
  ('modules -> modules module','modules',2,'p_modules','../icestream/iceyacc.py',61),
  ('module -> MODULE ID { module_members } END','module',6,'p_module','../icestream/iceyacc.py',66),
  ('module -> MODULE ID { } END','module',5,'p_module','../icestream/iceyacc.py',67),
  ('module_members -> module_member','module_members',1,'p_module_members','../icestream/iceyacc.py',77),
  ('module_members -> module_members module_member','module_members',2,'p_module_members','../icestream/iceyacc.py',78),
  ('module_member -> module','module_member',1,'p_module_member','../icestream/iceyacc.py',83),
  ('module_member -> type_define','module_member',1,'p_module_member','../icestream/iceyacc.py',84),
  ('module_member -> struct','module_member',1,'p_module_member','../icestream/iceyacc.py',85),
  ('module_member -> interface','module_member',1,'p_module_member','../icestream/iceyacc.py',86),
  ('module_member -> const_data','module_member',1,'p_module_member','../icestream/iceyacc.py',87),
  ('module_member -> enum','module_member',1,'p_module_member','../icestream/iceyacc.py',88),
  ('const_data -> CONST var_type ID = data END','const_data',6,'p_const_data','../icestream/iceyacc.py',93),
  ('data -> NUMBER','data',1,'p_data','../icestream/iceyacc.py',98),
  ('data -> BOOL','data',1,'p_data','../icestream/iceyacc.py',99),
  ('data -> FLOAT','data',1,'p_data','../icestream/iceyacc.py',100),
  ('data -> STRING','data',1,'p_data','../icestream/iceyacc.py',101),
  ('data -> var_type','data',1,'p_data_var','../icestream/iceyacc.py',106),
  ('type_define -> sequence_type ID END','type_define',3,'p_type_define','../icestream/iceyacc.py',111),
  ('type_define -> dictionary_type ID END','type_define',3,'p_type_define','../icestream/iceyacc.py',112),
  ('enum -> ENUM ID { enum_members } END','enum',6,'p_enum','../icestream/iceyacc.py',117),
  ('enum_members -> enum_member','enum_members',1,'p_enum_members','../icestream/iceyacc.py',122),
  ('enum_members -> enum_members enum_member','enum_members',2,'p_enum_members','../icestream/iceyacc.py',123),
  ('enum_member -> ID ,','enum_member',2,'p_enum_member','../icestream/iceyacc.py',128),
  ('enum_member -> ID = NUMBER ,','enum_member',4,'p_enum_member','../icestream/iceyacc.py',129),
  ('enum_member -> ID = var_type ,','enum_member',4,'p_enum_member','../icestream/iceyacc.py',130),
  ('sequence_type -> SEQUENCE < var_type >','sequence_type',4,'p_sequence_type','../icestream/iceyacc.py',138),
  ('dictionary_type -> DICTIONARY < var_type , var_type >','dictionary_type',6,'p_dictionary_type','../icestream/iceyacc.py',143),
  ('var_type -> ID','var_type',1,'p_var_type','../icestream/iceyacc.py',148),
  ('var_type -> domain ID','var_type',2,'p_var_type','../icestream/iceyacc.py',149),
  ('domain -> DOMAIN','domain',1,'p_domain','../icestream/iceyacc.py',157),
  ('domain -> ID DOMAIN','domain',2,'p_domain','../icestream/iceyacc.py',158),
  ('domain -> domain ID DOMAIN','domain',3,'p_domain','../icestream/iceyacc.py',159),
  ('struct -> STRUCT ID { data_members } END','struct',6,'p_struct','../icestream/iceyacc.py',170),
  ('data_members -> data_member','data_members',1,'p_data_members','../icestream/iceyacc.py',175),
  ('data_members -> data_members data_member','data_members',2,'p_data_members','../icestream/iceyacc.py',176),
  ('data_member -> var_type ID END','data_member',3,'p_data_member','../icestream/iceyacc.py',181),
  ('interface -> INTERFACE ID { member_funcs } END','interface',6,'p_interface','../icestream/iceyacc.py',186),
  ('interface -> INTERFACE ID { } END','interface',5,'p_interface','../icestream/iceyacc.py',187),
  ('member_funcs -> member_func','member_funcs',1,'p_member_funcs','../icestream/iceyacc.py',192),
  ('member_funcs -> member_funcs member_func','member_funcs',2,'p_member_funcs','../icestream/iceyacc.py',193),
  ('member_func -> INTERFACE_TYPE var_type ID ( params ) END','member_func',7,'p_member_func','../icestream/iceyacc.py',198),
  ('member_func -> var_type ID ( params ) END','member_func',6,'p_member_func','../icestream/iceyacc.py',199),
  ('member_func -> var_type ID ( ) END','member_func',5,'p_member_func','../icestream/iceyacc.py',200),
  ('params -> param','params',1,'p_params','../icestream/iceyacc.py',210),
  ('params -> params , param','params',3,'p_params','../icestream/iceyacc.py',211),
  ('param -> var_type ID','param',2,'p_param','../icestream/iceyacc.py',216),
  ('param -> OUT var_type ID','param',3,'p_param','../icestream/iceyacc.py',217),
]