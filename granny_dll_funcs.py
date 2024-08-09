"""Contains all functions to be called from the Granny DLL"""
# Import Ctypes so we can call functions from dlls.
from ctypes import cdll, c_char_p, POINTER
from granny_formats import GrannyFile, GrannyFileHeader, GrannyFileInfo, GrannyGRNSection
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
    GrannyDLL.GrannyGetGRNSectionArray.argtypes=[POINTER(GrannyFileHeader)]
    GrannyDLL.GrannyGetGRNSectionArray.restype=POINTER(GrannyGRNSection)
    result = GrannyDLL.GrannyGetGRNSectionArray(header)
    return result

def granny_get_file_info(file : GrannyFile):
    GrannyDLL.GrannyGetFileInfo.argtypes=[POINTER(GrannyFile)]
    GrannyDLL.GrannyGetFileInfo.restype=POINTER(GrannyFileInfo)
    result = GrannyDLL.GrannyGetFileInfo(file)
    return result