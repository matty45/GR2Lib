"""Granny file vertex modification test"""

from ctypes import POINTER, Structure, c_float, c_uint8, cast
from granny_dll_funcs import granny_begin_file_data_tree_writing, granny_get_file_info, granny_get_mesh_vertices, granny_read_entire_file, granny_write_data_tree_to_file
from granny_dll_vars import GrannyFileInfoType, GrannyGRNFileMV_ThisPlatform
from granny_formats import GrannyFileInfo

#You find this information inside of granny viewer if you view the meshes in detail. mesh::PrimaryVetexData::Vertices
#This example uses the vertex data type that the mod tools for halo reach and up use.
class HaloVertexType(Structure):
    """ Halo vertex type, ditto """
    _pack_ = 1
    _fields_ = [('position', c_float * 3),
                ('bone_weights',c_uint8 * 4),
                ('bone_indices',c_uint8 * 4),
                ('normal',c_float * 3),
                ('texture_coordinates_0',c_float * 3),
                ('texture_coordinates_1',c_float * 3),
                ('texture_coordinates_2',c_float * 3),
                ('texture_coordinates_3',c_float * 3),
                ('texture_coordinates_lighting',c_float * 3),
                ('color_set_1',c_float * 3),
                ('color_set_2',c_float * 3),
                ('blend_shape',c_float * 3),
                ('texture_coordinates_vertex_id',c_float * 2)]

def modify_some_stuff(file_info : GrannyFileInfo):
    
    for mesh_index in range(file_info.contents.mesh_count):
        mesh = file_info.contents.meshes[mesh_index]

        mesh_vertex_data = mesh.contents.primary_vertex_data.contents
        raw_vertices = granny_get_mesh_vertices(mesh)
        halo_vertices = cast(raw_vertices,POINTER(HaloVertexType))

        for vertex_index in range(mesh_vertex_data.vertex_count):
            halo_vertex = halo_vertices[vertex_index]
            halo_vertex.texture_coordinates_lighting[0] = 69
            halo_vertex.color_set_1[0] = 69
            halo_vertex.color_set_1[1] = 69
            halo_vertex.color_set_1[2] = 69
            halo_vertex.color_set_2[0] = 255
            halo_vertex.color_set_2[1] = 255
            halo_vertex.color_set_2[2] = 255

    data_tree_writer = granny_begin_file_data_tree_writing(GrannyFileInfoType,file_info,0,0)

    if data_tree_writer:
        test_file_name = "vertex_modify_test_result.gr2"
        file_write_success = granny_write_data_tree_to_file(data_tree_writer,0x80000037,GrannyGRNFileMV_ThisPlatform,test_file_name,1)
        if file_write_success:
            print(f"Managed to edit and write a file to {test_file_name}!")

def vertex_modify_test(file_path : str) -> bool:
    """This will load a gr2 file, modify its vertices and save it as a different file."""
    file = granny_read_entire_file(file_path)
    if file:
        file_info = granny_get_file_info(file)
        
        if file_info.contents is None:
            print("Could not get file info..")
            return False

        modify_some_stuff(file_info)
        return True
    else:
        print(f"\nCould not open {file_path}")
        return False