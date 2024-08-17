"""Granny file extended data parse test"""

from ctypes import POINTER, Structure, c_char_p, c_float, c_uint8, cast
from granny_dll_funcs import granny_begin_file_data_tree_writing, granny_get_file_info, granny_get_mesh_vertices, granny_read_entire_file, granny_write_data_tree_to_file
from granny_dll_vars import GrannyFileInfoType, GrannyGRNFileMV_ThisPlatform
from granny_formats import GrannyFileInfo

#You find this information inside of granny viewer if you view the meshes in detail. Materials::ExtendedData
#This example uses the material extended data that the mod tools for halo reach and up use.
class HaloMatExtendedData(Structure):
    """ Halo material extended data, ditto """
    _pack_ = 1
    _fields_ = [
                ('bungie_shader_path',c_char_p),
                ('bungie_shader_type',c_char_p)]

def parse_extended_data(file_info : GrannyFileInfo):
    
    for material_index in range(file_info.contents.material_count):
        material = file_info.contents.materials[material_index]


def parse_extended_data_test(file_path : str) -> bool:
    """This will load a gr2 file, modify its vertices and save it as a different file."""
    file = granny_read_entire_file(file_path)
    if file:
        file_info = granny_get_file_info(file)
        
        if file_info.contents is None:
            print("Could not get file info..")
            return False

        parse_extended_data(file_info)
        return True
    else:
        print(f"\nCould not open {file_path}")
        return False