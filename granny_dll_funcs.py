"""Contains all functions to be called from the Granny DLL"""
# Import Ctypes so we can call functions from dlls.
from ctypes import c_bool, c_float, c_int32, c_uint, cdll, c_char_p, POINTER
from granny_formats import GrannyDataTypeDefinition, GrannyFile, GrannyFileHeader, GrannyFileInfo, GrannyGRNSection, GrannyModel, GrannyModelInstance, GrannyTransform
from gr2lib_settings import granny_dll_path
GrannyDLL = cdll.LoadLibrary(granny_dll_path)


def granny_get_version_string():
    """Function returning the granny dll version as a string."""
    GrannyDLL.GrannyGetVersionString.restype=c_char_p
    version = GrannyDLL.GrannyGetVersionString().decode('UTF-8')
    return version

def granny_get_version(major_version: c_int32, minor_version: c_int32, build_number: c_int32, customization: c_int32):
    """Function returning granny dll version as pointers."""
    GrannyDLL.GrannyGetVersion.argtypes=[POINTER(c_int32),POINTER(c_int32),POINTER(c_int32),POINTER(c_int32)]
    GrannyDLL.GrannyGetVersion()

def granny_versions_match(major_version: c_int32, minor_version: c_int32, build_number: c_int32, customization: c_int32):
    """Check if version matches the dlls."""
    GrannyDLL.GrannyVersionsMatch_.argtypes=[c_int32,c_int32,c_int32,c_int32]
    GrannyDLL.GrannyReadEntireFile.restype=c_bool
    GrannyDLL.GrannyVersionsMatch_()

def granny_read_entire_file(file_path : str):
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

def granny_get_grn_section_array(header : GrannyFileHeader):
    """Returns the section array inside of the granny file header."""
    GrannyDLL.GrannyGetGRNSectionArray.argtypes=[POINTER(GrannyFileHeader)]
    GrannyDLL.GrannyGetGRNSectionArray.restype=POINTER(GrannyGRNSection)
    result = GrannyDLL.GrannyGetGRNSectionArray(header)
    return result

def granny_get_file_info(file : GrannyFile):
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

def granny_compute_basis_conversion(file_info : GrannyFileInfo, desired_units_per_meter : c_float, desired_origin_3 : c_float, desired_right_3 : c_float, desired_up_3 : c_float, desired_back_3 : c_float, result_affine_3 : c_float, result_linear_3x3 : c_float, result_inverse_linear_3x3 : c_float):
    """Conversion stuff"""
    GrannyDLL.GrannyComputeBasisConversion.argtypes=[POINTER(GrannyFileInfo),c_float,POINTER(c_float),POINTER(c_float),POINTER(c_float),POINTER(c_float),POINTER(c_float),POINTER(c_float),POINTER(c_float)]
    GrannyDLL.GrannyComputeBasisConversion.restype=c_bool
    result = GrannyDLL.GrannyComputeBasisConversion(file_info,desired_units_per_meter,desired_origin_3,desired_right_3,desired_up_3,desired_back_3,result_affine_3,result_linear_3x3,result_inverse_linear_3x3)
    return result

def granny_transform_file(file_info : GrannyFileInfo, affine_3 : c_float, linear_3x3 : c_float, inverse_linear_3x3 : c_float, affine_tolerance : c_float, linear_tolerance : c_float, flags : c_uint):
    """Transforms entire file"""
    GrannyDLL.GrannyTransformFile.argtypes=[POINTER(GrannyFileInfo),POINTER(c_float),POINTER(c_float),POINTER(c_float),c_float,c_float,c_uint]
    GrannyDLL.GrannyTransformFile(file_info,affine_3,linear_3x3,inverse_linear_3x3,affine_tolerance,linear_tolerance,flags)

def granny_get_member_unit_size(member_type : GrannyDataTypeDefinition):
    """Gets the size of a member unit, what else?"""
    GrannyDLL.GrannyGetMemberUnitSize.argtypes=[POINTER(GrannyDataTypeDefinition)]
    GrannyDLL.GrannyGetMemberUnitSize.restype=c_int32
    result = GrannyDLL.GrannyGetMemberUnitSize(member_type)
    return result

def granny_get_member_type_size(member_type : GrannyDataTypeDefinition):
    """Gets the size of a member type, what else?"""
    GrannyDLL.GrannyGetMemberTypeSize.argtypes=[POINTER(GrannyDataTypeDefinition)]
    GrannyDLL.GrannyGetMemberTypeSize.restype=c_int32
    result = GrannyDLL.GrannyGetMemberTypeSize(member_type)
    return result

def granny_get_total_object_size(type_def : GrannyDataTypeDefinition):
    """Gets the total size of an object, what else?"""
    GrannyDLL.GrannyGetTotalObjectSize.argtypes=[POINTER(GrannyDataTypeDefinition)]
    GrannyDLL.GrannyGetTotalObjectSize.restype=c_int32
    result = GrannyDLL.GrannyGetTotalObjectSize(type_def)
    return result

def granny_get_total_type_size(type_def : GrannyDataTypeDefinition):
    """Gets the total size of a type, what else?"""
    GrannyDLL.GrannyGetTotalTypeSize.argtypes=[POINTER(GrannyDataTypeDefinition)]
    GrannyDLL.GrannyGetTotalTypeSize.restype=c_int32
    result = GrannyDLL.GrannyGetTotalTypeSize(type_def)
    return result

def granny_instantiate_model(type_def : GrannyModel):
    """Instantiates a model"""
    GrannyDLL.GrannyInstantiateModel.argtypes=[POINTER(GrannyModel)]
    GrannyDLL.GrannyInstantiateModel.restype=GrannyModelInstance
    result = GrannyDLL.GrannyInstantiateModel(type_def)
    return result