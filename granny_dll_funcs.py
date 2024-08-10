"""Contains all functions to be called from the Granny DLL"""
# Import Ctypes so we can call functions from dlls.
from ctypes import c_bool, c_float, c_uint, cdll, c_char_p, POINTER
from granny_formats import GrannyFile, GrannyFileHeader, GrannyFileInfo, GrannyGRNSection, GrannyTransform
from gr2lib_settings import granny_dll_path
GrannyDLL = cdll.LoadLibrary(granny_dll_path)


def granny_get_version_string():
    """Function printing granny dll version."""
    GrannyDLL.GrannyGetVersionString.restype=c_char_p
    version = GrannyDLL.GrannyGetVersionString().decode('UTF-8')
    return version

def granny_read_entire_file(file_path : str):
    """Reads the entire granny file and returns it to a GrannyFile class."""
    file_path_bytes = file_path.encode()
    GrannyDLL.GrannyReadEntireFile.argtypes=[c_char_p]
    GrannyDLL.GrannyReadEntireFile.restype=POINTER(GrannyFile)
    file = GrannyDLL.GrannyReadEntireFile(file_path_bytes)
    return file

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
    GrannyDLL.GrannyComputeBasisConversion.argtypes=[POINTER(GrannyFileInfo),POINTER(c_float),POINTER(c_float),POINTER(c_float),c_float,c_float,c_uint]
    GrannyDLL.GrannyComputeBasisConversion(file_info,affine_3,linear_3x3,inverse_linear_3x3,affine_tolerance,linear_tolerance,flags)