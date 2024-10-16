"""Contains all functions to be called from the Granny DLL"""
# Import Ctypes so we can call functions from dlls.
from ctypes import c_bool, c_float, c_int, c_int32, c_uint, c_uint32, c_void_p, cdll, c_char_p, POINTER
from granny_formats import GrannyDataTypeDefinition, GrannyFile, GrannyFileDataTreeWriter, GrannyFileHeader, GrannyFileInfo, GrannyFileMagic, GrannyGRNSection, GrannyLogCallback, GrannyMemoryArena, GrannyMesh, GrannyModel, GrannyModelInstance, GrannyStringTable, GrannyTransform, GrannyVariantBuilder
from gr2lib_settings import granny_dll_path
GrannyDLL = cdll.LoadLibrary(granny_dll_path)


def granny_get_version_string() -> c_char_p:
    """Function returning the granny dll version as a string."""
    GrannyDLL.GrannyGetVersionString.restype=c_char_p
    version = GrannyDLL.GrannyGetVersionString().decode('UTF-8')
    return version

def granny_get_version(major_version: c_int32, minor_version: c_int32, build_number: c_int32, customization: c_int32):
    """Function returning granny dll version as pointers."""
    GrannyDLL.GrannyGetVersion.argtypes=[POINTER(c_int32),POINTER(c_int32),POINTER(c_int32),POINTER(c_int32)]
    GrannyDLL.GrannyGetVersion()

def granny_versions_match(major_version: c_int32, minor_version: c_int32, build_number: c_int32, customization: c_int32) -> c_bool:
    """Check if version matches the dlls."""
    GrannyDLL.GrannyVersionsMatch_.argtypes=[c_int32,c_int32,c_int32,c_int32]
    GrannyDLL.GrannyReadEntireFile.restype=c_bool
    result = GrannyDLL.GrannyVersionsMatch_()
    return result

def granny_read_entire_file(file_path : str) -> GrannyFile:
    """Reads the entire granny file and returns it to a GrannyFile class."""
    file_path_bytes = file_path.encode()
    GrannyDLL.GrannyReadEntireFile.argtypes=[c_char_p]
    GrannyDLL.GrannyReadEntireFile.restype=POINTER(GrannyFile)
    file = GrannyDLL.GrannyReadEntireFile(file_path_bytes)
    return file

def granny_free_file(file : GrannyFile, section_index : c_int32):
    """Frees a section of data inside a granny file."""
    GrannyDLL.GrannyFreeFile.argtypes=[POINTER(GrannyTransform)]
    GrannyDLL.GrannyFreeFile(file,section_index)

def granny_get_grn_section_array(header : GrannyFileHeader) -> GrannyGRNSection:
    """Returns the section array inside of the granny file header."""
    GrannyDLL.GrannyGetGRNSectionArray.argtypes=[POINTER(GrannyFileHeader)]
    GrannyDLL.GrannyGetGRNSectionArray.restype=POINTER(GrannyGRNSection)
    result = GrannyDLL.GrannyGetGRNSectionArray(header)
    return result

def granny_get_file_info(file : GrannyFile) -> GrannyFileInfo:
    """Gets the file info block of the granny file. The meat of it all."""
    GrannyDLL.GrannyGetFileInfo.argtypes=[POINTER(GrannyFile)]
    GrannyDLL.GrannyGetFileInfo.restype=POINTER(GrannyFileInfo)
    result = GrannyDLL.GrannyGetFileInfo(file)
    return result

def granny_make_identity(result : GrannyTransform):
    """Some transform identity stuff, idk how it works"""
    GrannyDLL.GrannyMakeIdentity.argtypes=[POINTER(GrannyTransform)]
    GrannyDLL.GrannyMakeIdentity(result)

def granny_multiply(result : GrannyTransform, a : GrannyTransform,b : GrannyTransform):
    """Multiplies transforms and returns the result to the first arg."""
    GrannyDLL.GrannyMultiply.argtypes=[POINTER(GrannyTransform),POINTER(GrannyTransform),POINTER(GrannyTransform)]
    GrannyDLL.GrannyMultiply(result,a,b)

def granny_build_inverse(result : GrannyTransform, source : GrannyTransform):
    """Idk what this is used for, sorry i no good at math."""
    GrannyDLL.GrannyBuildInverse.argtypes=[POINTER(GrannyTransform),POINTER(GrannyTransform)]
    GrannyDLL.GrannyBuildInverse(result,source)

def granny_build_composite_transform_4x4(transform : GrannyTransform, composite_4x4 : c_float):
    """Idk what this is used for, sorry i no good at math."""
    GrannyDLL.GrannyBuildCompositeTransform4x4.argtypes=[POINTER(GrannyTransform),POINTER(c_float)]
    GrannyDLL.GrannyBuildCompositeTransform4x4(transform,composite_4x4)

def granny_compute_basis_conversion(file_info : GrannyFileInfo, desired_units_per_meter : c_float, desired_origin_3 : c_float, desired_right_3 : c_float, desired_up_3 : c_float, desired_back_3 : c_float, result_affine_3 : c_float, result_linear_3x3 : c_float, result_inverse_linear_3x3 : c_float) -> c_bool:
    """Conversion stuff"""
    GrannyDLL.GrannyComputeBasisConversion.argtypes=[POINTER(GrannyFileInfo),c_float,POINTER(c_float),POINTER(c_float),POINTER(c_float),POINTER(c_float),POINTER(c_float),POINTER(c_float),POINTER(c_float)]
    GrannyDLL.GrannyComputeBasisConversion.restype=c_bool
    result = GrannyDLL.GrannyComputeBasisConversion(file_info,desired_units_per_meter,desired_origin_3,desired_right_3,desired_up_3,desired_back_3,result_affine_3,result_linear_3x3,result_inverse_linear_3x3)
    return result

def granny_transform_file(file_info : GrannyFileInfo, affine_3 : c_float, linear_3x3 : c_float, inverse_linear_3x3 : c_float, affine_tolerance : c_float, linear_tolerance : c_float, flags : c_uint):
    """Transforms entire file"""
    GrannyDLL.GrannyTransformFile.argtypes=[POINTER(GrannyFileInfo),POINTER(c_float),POINTER(c_float),POINTER(c_float),c_float,c_float,c_uint]
    GrannyDLL.GrannyTransformFile(file_info,affine_3,linear_3x3,inverse_linear_3x3,affine_tolerance,linear_tolerance,flags)

def granny_get_member_unit_size(member_type : GrannyDataTypeDefinition) -> c_int32:
    """Gets the size of a member unit, what else?"""
    GrannyDLL.GrannyGetMemberUnitSize.argtypes=[POINTER(GrannyDataTypeDefinition)]
    GrannyDLL.GrannyGetMemberUnitSize.restype=c_int32
    result = GrannyDLL.GrannyGetMemberUnitSize(member_type)
    return result

def granny_get_member_type_size(member_type : GrannyDataTypeDefinition) -> c_int32:
    """Gets the size of a member type, what else?"""
    GrannyDLL.GrannyGetMemberTypeSize.argtypes=[POINTER(GrannyDataTypeDefinition)]
    GrannyDLL.GrannyGetMemberTypeSize.restype=c_int32
    result = GrannyDLL.GrannyGetMemberTypeSize(member_type)
    return result

def granny_get_total_object_size(type_def : GrannyDataTypeDefinition) -> c_int32:
    """Gets the total size of an object, what else?"""
    GrannyDLL.GrannyGetTotalObjectSize.argtypes=[POINTER(GrannyDataTypeDefinition)]
    GrannyDLL.GrannyGetTotalObjectSize.restype=c_int32
    result = GrannyDLL.GrannyGetTotalObjectSize(type_def)
    return result

def granny_get_total_type_size(type_def : GrannyDataTypeDefinition) -> c_int32:
    """Gets the total size of a type, what else?"""
    GrannyDLL.GrannyGetTotalTypeSize.argtypes=[POINTER(GrannyDataTypeDefinition)]
    GrannyDLL.GrannyGetTotalTypeSize.restype=c_int32
    result = GrannyDLL.GrannyGetTotalTypeSize(type_def)
    return result

def granny_instantiate_model(type_def : GrannyModel) -> GrannyModelInstance:
    """Instantiates a model"""
    GrannyDLL.GrannyInstantiateModel.argtypes=[POINTER(GrannyModel)]
    GrannyDLL.GrannyInstantiateModel.restype=POINTER(GrannyModelInstance)
    result = GrannyDLL.GrannyInstantiateModel(type_def)
    return result

def granny_free_model_instance(model_instance : GrannyModelInstance):
    """Frees a model instance"""
    GrannyDLL.GrannyFreeModelInstance.argtypes=[POINTER(GrannyModelInstance)]
    GrannyDLL.GrannyFreeModelInstance(model_instance)

def granny_begin_file_data_tree_writing(root_object_type_def : GrannyDataTypeDefinition, root_object : c_void_p, default_type_section_index : c_int32, default_object_section_index : c_int32) -> c_void_p:
    """Used for writing gr2 files."""
    GrannyDLL.GrannyBeginFileDataTreeWriting.argtypes=[POINTER(GrannyDataTypeDefinition), c_void_p, c_int32, c_int32]
    GrannyDLL.GrannyBeginFileDataTreeWriting.restype=POINTER(GrannyFileDataTreeWriter)
    result = GrannyDLL.GrannyBeginFileDataTreeWriting(root_object_type_def, root_object, default_type_section_index, default_object_section_index)
    return result

def granny_write_data_tree_to_file(writer: c_void_p, file_type_tag: c_uint32, platform_magic_value : GrannyFileMagic, file_name: str, file_section_count: c_int32) -> c_bool:
    """Used for writing gr2 files."""
    file_name_bytes = file_name.encode()
    GrannyDLL.GrannyWriteDataTreeToFile.argtypes=[c_void_p, c_uint32, POINTER(GrannyFileMagic), c_char_p, c_int32]
    GrannyDLL.GrannyWriteDataTreeToFile.restype=c_bool
    result = GrannyDLL.GrannyWriteDataTreeToFile(writer, file_type_tag, platform_magic_value, file_name_bytes, file_section_count)
    return result

def granny_end_file_data_tree_writing(writer: c_void_p):
    """Used for writing gr2 files."""
    GrannyDLL.GrannyEndFileDataTreeWriting.argtypes=[c_void_p]
    GrannyDLL.GrannyEndFileDataTreeWriting(writer)

def granny_get_mesh_vertex_type(mesh : GrannyMesh) -> GrannyDataTypeDefinition:
    """Gets the vertex type used in the mesh"""
    GrannyDLL.GrannyGetMeshVertexType.argtypes=[POINTER(GrannyMesh)]
    GrannyDLL.GrannyGetMeshVertexType.restype=GrannyDataTypeDefinition
    result = GrannyDLL.GrannyGetMeshVertexType(mesh)
    return result

def granny_get_mesh_vertices(mesh : GrannyMesh) -> c_void_p:
    """Gets the vertices used in the mesh"""
    GrannyDLL.GrannyGetMeshVertices.argtypes=[POINTER(GrannyMesh)]
    GrannyDLL.GrannyGetMeshVertices.restype=c_void_p
    result = GrannyDLL.GrannyGetMeshVertices(mesh)
    return result

def granny_set_log_file_name(file_name : str, clear : c_bool) -> c_bool:
    """Sets a file for the granny dll to log to.
    granny_set_log_file_name("c:/blargh.txt", true);
    to turn off: granny_set_log_file_name(0, false);
    """
    file_name_bytes = file_name.encode()
    GrannyDLL.GrannySetLogFileName.argtypes=[c_char_p, c_bool]
    GrannyDLL.GrannySetLogFileName.restype=c_bool
    result = GrannyDLL.GrannySetLogFileName(file_name_bytes)
    return result

def granny_get_log_callback(result : GrannyLogCallback):
    """Granny logging function"""
    GrannyDLL.GrannyGetLogCallback.argtypes=[POINTER(GrannyLogCallback)]
    GrannyDLL.GrannyGetLogCallback(result)

def granny_set_log_callback(result : GrannyLogCallback):
    """Granny logging function"""
    GrannyDLL.GrannySetLogCallback.argtypes=[POINTER(GrannyLogCallback)]
    GrannyDLL.GrannySetLogCallback(result)

def granny_get_log_message_type_string(message_type: c_int) -> c_char_p:
    """Granny logging function"""
    GrannyDLL.GrannyGetLogMessageTypeString.argtypes=[c_int]
    GrannyDLL.GrannyGetLogMessageTypeString.restype=c_char_p
    result = GrannyDLL.GrannyGetLogMessageTypeString(message_type)
    return result

def granny_get_log_message_origin_string(origin: c_int) -> c_char_p:
    """Granny logging function"""
    GrannyDLL.GrannyGetLogMessageOriginString.argtypes=[c_int]
    GrannyDLL.GrannyGetLogMessageOriginString.restype=c_char_p
    result = GrannyDLL.GrannyGetLogMessageOriginString(origin)
    return result

def granny_logging() -> c_bool:
    """Granny logging function"""
    GrannyDLL.GrannyLogging.restype=c_bool
    result = GrannyDLL.GrannyLogging()
    return result

def granny_filter_message(origin: c_int, enabled : c_bool):
    """Granny logging function"""
    GrannyDLL.GrannyFilterMessage.argtypes=[c_int, c_bool]
    GrannyDLL.GrannyFilterMessage(origin, enabled)

def granny_filter_all_messages(enabled: c_bool):
    """Granny logging function"""
    GrannyDLL.GrannyFilterAllMessages.argtypes=[c_bool]
    GrannyDLL.GrannyFilterAllMessages(enabled)

def granny_set_vertex_color(vertex_layout: GrannyDataTypeDefinition, vertex_pointer : c_void_p, colour_index: c_int32, color: c_float):
    GrannyDLL.GrannySetVertexColor.argtypes=[POINTER(GrannyDataTypeDefinition),c_void_p,c_int32,POINTER(c_float)]
    GrannyDLL.GrannySetVertexColor(vertex_layout,vertex_pointer,colour_index,color)

def granny_get_mesh_is_rigid(mesh: GrannyMesh) -> c_bool:
    """Checks if the mesh is rigid."""
    GrannyDLL.GrannyMeshIsRigid.argtypes=[POINTER(GrannyMesh)]
    GrannyDLL.GrannyMeshIsRigid.restype=c_bool
    result = GrannyDLL.GrannyMeshIsRigid(mesh)
    return result

def granny_new_memory_arena() -> GrannyMemoryArena:
    GrannyDLL.GrannyNewMemoryArena.restype=POINTER(GrannyMemoryArena)
    result = GrannyDLL.GrannyNewMemoryArena()
    return result

def granny_new_string_table() -> GrannyStringTable:
    GrannyDLL.GrannyNewStringTable.restype=POINTER(GrannyStringTable)
    result = GrannyDLL.GrannyNewStringTable()
    return result

def granny_new_arena_string_table(memory_arena: GrannyMemoryArena) -> GrannyStringTable:
    GrannyDLL.GrannyNewArenaStringTable.argtypes=[POINTER(GrannyMemoryArena)]
    GrannyDLL.GrannyNewArenaStringTable.restype=POINTER(GrannyStringTable)
    result = GrannyDLL.GrannyNewArenaStringTable(memory_arena)
    return result

def granny_set_transform_with_identity_check(result: GrannyTransform, position_3: c_float, orientation4: c_float, scale_shear_3x3: c_float):
    GrannyDLL.GrannySetTransformWithIdentityCheck.argtypes=[POINTER(GrannyTransform),POINTER(c_float),POINTER(c_float),POINTER(c_float)]
    GrannyDLL.GrannySetTransformWithIdentityCheck(result,position_3,orientation4,scale_shear_3x3)

def granny_set_transform(result: GrannyTransform, position_3: c_float, orientation4: c_float, scale_shear_3x3: c_float):
    GrannyDLL.GrannySetTransform.argtypes=[POINTER(GrannyTransform),POINTER(c_float),POINTER(c_float),POINTER(c_float)]
    GrannyDLL.GrannySetTransform(result,position_3,orientation4,scale_shear_3x3)

def granny_begin_variant(string_table_builder: GrannyStringTable) -> GrannyVariantBuilder:
    GrannyDLL.GrannyBeginVariant.argtypes=[POINTER(GrannyStringTable)]
    GrannyDLL.GrannyBeginVariant.restype=POINTER(GrannyVariantBuilder)
    result = GrannyDLL.GrannyBeginVariant(string_table_builder)
    return result

def granny_end_variant(builder: GrannyVariantBuilder, type: GrannyDataTypeDefinition, object: c_void_p) -> c_void_p:
    GrannyDLL.GrannyEndVariant.argtypes=[POINTER(GrannyVariantBuilder),POINTER(POINTER(GrannyDataTypeDefinition)),POINTER(c_void_p)]
    GrannyDLL.GrannyEndVariant.restype=c_void_p
    result = GrannyDLL.GrannyEndVariant(builder,type,object)
    return result

def granny_abort_variant(granny_variant_builder: GrannyVariantBuilder):
    GrannyDLL.GrannyAbortVariant.argtypes=[POINTER(GrannyVariantBuilder)]
    GrannyDLL.GrannyAbortVariant(granny_variant_builder)

def granny_get_resulting_variant_type_size(builder: GrannyVariantBuilder) -> c_int32:
    GrannyDLL.GrannyGetResultingVariantTypeSize.argtypes=[POINTER(GrannyVariantBuilder)]
    GrannyDLL.GrannyGetResultingVariantTypeSize.restype=c_int32
    result = GrannyDLL.GrannyGetResultingVariantTypeSize(builder)
    return result

def granny_get_resulting_variant_object_size(builder: GrannyVariantBuilder) -> c_int32:
    GrannyDLL.GrannyGetResultingVariantObjectSize.argtypes=[POINTER(GrannyVariantBuilder)]
    GrannyDLL.GrannyGetResultingVariantObjectSize.restype=c_int32
    result = GrannyDLL.GrannyGetResultingVariantObjectSize(builder)
    return result

def granny_end_variant_in_place(builder: GrannyVariantBuilder,type_memory: c_void_p, type: GrannyDataTypeDefinition,object_memory: c_void_p, object: c_void_p) -> c_bool:
    GrannyDLL.GrannyEndVariantInPlace.argtypes=[POINTER(GrannyVariantBuilder),c_void_p,POINTER(POINTER(GrannyDataTypeDefinition)),c_void_p,POINTER(c_void_p)]
    GrannyDLL.GrannyEndVariantInPlace.restype=c_bool
    result = GrannyDLL.GrannyEndVariantInPlace(builder,type_memory,type,object_memory,object)
    return result

def granny_add_bool_member(granny_variant_builder: GrannyVariantBuilder, name: c_char_p, value:c_int):
    GrannyDLL.GrannyAddBoolMember.argtypes=[POINTER(GrannyVariantBuilder),c_char_p,c_int]
    GrannyDLL.GrannyAddBoolMember(granny_variant_builder,name,value)

def granny_add_bool_array_member(granny_variant_builder: GrannyVariantBuilder, name: c_char_p, width: c_int32, value:c_int):
    GrannyDLL.GrannyAddBoolArrayMember.argtypes=[POINTER(GrannyVariantBuilder),c_char_p,c_int32,POINTER(c_int)]
    GrannyDLL.GrannyAddBoolArrayMember(granny_variant_builder,name,width,value)

def granny_add_integer_member(granny_variant_builder: GrannyVariantBuilder, name: c_char_p, value: c_int32):
    GrannyDLL.GrannyAddIntegerMember.argtypes=[POINTER(GrannyVariantBuilder),c_char_p,c_int32]
    GrannyDLL.GrannyAddIntegerMember(granny_variant_builder,name,value)

def granny_add_integer_array_member(granny_variant_builder: GrannyVariantBuilder, name: c_char_p, width: c_int32, value:c_int32):
    GrannyDLL.GrannyAddIntegerArrayMember.argtypes=[POINTER(GrannyVariantBuilder),c_char_p,c_int32,POINTER(c_int32)]
    GrannyDLL.GrannyAddIntegerArrayMember(granny_variant_builder,name,width,value)

def granny_add_unsigned_integer_member(granny_variant_builder: GrannyVariantBuilder, name: c_char_p, value: c_uint32):
    GrannyDLL.GrannyAddUnsignedIntegerMember.argtypes=[POINTER(GrannyVariantBuilder),c_char_p,c_uint32]
    GrannyDLL.GrannyAddUnsignedIntegerMember(granny_variant_builder,name,value)

def granny_add_scalar_member(granny_variant_builder: GrannyVariantBuilder, name: c_char_p, value: c_float):
    GrannyDLL.GrannyAddScalarMember.argtypes=[POINTER(GrannyVariantBuilder),c_char_p,c_float]
    GrannyDLL.GrannyAddScalarMember(granny_variant_builder,name,value)

def granny_add_scalar_array_member(granny_variant_builder: GrannyVariantBuilder, name: c_char_p, width: c_int32, value:c_float):
    GrannyDLL.GrannyAddScalarArrayMember.argtypes=[POINTER(GrannyVariantBuilder),c_char_p,c_int32,POINTER(c_float)]
    GrannyDLL.GrannyAddScalarArrayMember(granny_variant_builder,name,width,value)

def granny_add_string_member(granny_variant_builder: GrannyVariantBuilder, name: str, value: str):
    GrannyDLL.GrannyAddStringMember.argtypes=[POINTER(GrannyVariantBuilder),c_char_p,c_char_p]
    GrannyDLL.GrannyAddStringMember(granny_variant_builder,name.encode(),value.encode())

def granny_add_reference_member(granny_variant_builder: GrannyVariantBuilder, name: c_char_p, type: GrannyDataTypeDefinition,value: c_void_p):
    GrannyDLL.GrannyAddReferenceMember.argtypes=[POINTER(GrannyVariantBuilder),c_char_p,POINTER(GrannyDataTypeDefinition),c_void_p]
    GrannyDLL.GrannyAddReferenceMember(granny_variant_builder,name,type,value)

def granny_add_dynamic_array_member(builder: GrannyVariantBuilder, name: str, count: c_int32, entry_type: GrannyDataTypeDefinition, array_entries: c_void_p):
    GrannyDLL.GrannyAddDynamicArrayMember.argtypes=[POINTER(GrannyVariantBuilder),c_char_p,c_int32,POINTER(GrannyDataTypeDefinition),c_void_p]
    GrannyDLL.GrannyAddDynamicArrayMember(builder,name.encode(),count,entry_type,array_entries)