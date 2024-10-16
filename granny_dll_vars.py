"""Contains all variables to be used from the granny dll."""

from ctypes import POINTER, cdll
from granny_formats import GrannyDataTypeDefinition, GrannyFileMagic
from gr2lib_settings import granny_dll_path
GrannyDLL = cdll.LoadLibrary(granny_dll_path)

GrannyFileInfoType = POINTER(GrannyDataTypeDefinition).in_dll(GrannyDLL, "GrannyFileInfoType")
GrannyStringType = POINTER(GrannyDataTypeDefinition).in_dll(GrannyDLL, "GrannyStringType")

GrannyGRNFileMV_ThisPlatform = POINTER(GrannyFileMagic).in_dll(GrannyDLL, "GrannyGRNFileMV_ThisPlatform")