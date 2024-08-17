"""Granny file extended data parse test"""

#You find this information inside of granny viewer if you view the meshes in detail. Materials::ExtendedData
#This example uses the material extended data that the mod tools for halo reach and up use.
from ctypes import POINTER, Structure, byref, c_char_p, cast

from granny_dll_funcs import granny_get_file_info, granny_read_entire_file
from granny_formats import GrannyFileInfo


class HaloMatExtendedData(Structure):
    """ Halo material extended data, ditto """
    _pack_ = 1
    _fields_ = [
                ('bungie_shader_path',c_char_p),
                ('bungie_shader_type',c_char_p)]

def parse_extended_data(file_info : GrannyFileInfo):
    
    for material_index in range(file_info.contents.material_count):
        material = file_info.contents.materials[material_index]
        if material.contents.extended_data.type:
            extended_data = cast(material.contents.extended_data.object,POINTER(HaloMatExtendedData))
            print(f"Material Index: {material_index}")
            print(f"Shader Path: {extended_data.contents.bungie_shader_path}")
            print(f"Shader Type: {extended_data.contents.bungie_shader_type}")


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