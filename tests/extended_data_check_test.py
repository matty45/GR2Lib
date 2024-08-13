"""This loads a granny file and checks and prints out what parts of it that have extended data."""
from granny_dll_funcs import granny_get_file_info, granny_read_entire_file
from granny_formats import GrannyFileInfo

def print_extended_data(file_info : GrannyFileInfo):
    
    if file_info.contents.extended_data.type:
        print("File info contains extended data.")
    
    if file_info.contents.art_tool_info.contents.extended_data.type:
        print("File art tool info contains extended data.")

    if file_info.contents.exporter_info.contents.extended_data.type:
        print("File exporter info contains extended data.")

    print("\nIterating through textures:")

    for texture_index in range(file_info.contents.texture_count):
        texture = file_info.contents.textures[texture_index]
        if texture.contents.extended_data.type:
            print(f"Texture Index:{texture_index} {texture.contents.name.decode("UTF-8")} has extended data.")

    print("\nIterating through materials:")

    for material_index in range(file_info.contents.material_count):
        material = file_info.contents.materials[material_index]
        if material.contents.extended_data.type:
            print(f"Material Index:{material_index} {material.contents.name.decode("UTF-8")} has extended data.")

    print("\nIterating through skeletons:")

    for skeleton_index in range(file_info.contents.skeleton_count):
        skeleton = file_info.contents.skeletons[skeleton_index]
        if skeleton.contents.extended_data.type:
            print(f"Skeleton Index:{skeleton_index} {skeleton.contents.name.decode("UTF-8")} has extended data.")
        
        print(f"\nIterating bones inside of skeleton Index:{skeleton_index} {skeleton.contents.name.decode("UTF-8")}")
        for bone_index in range(skeleton.contents.bone_count):
            bone = skeleton.contents.bones[bone_index]
            if bone.extended_data.type:
                print(f"Bone Index:{bone_index} {bone.name.decode("UTF-8")} has extended data.")  

    print("\nIterating through meshes:")

    for mesh_index in range(file_info.contents.mesh_count):
        mesh = file_info.contents.meshes[mesh_index]
        if mesh.contents.extended_data.type:
            print(f"Mesh Index:{mesh_index} {mesh.contents.name.decode("UTF-8")} has extended data.")

    print("\nIterating through models:")

    for model_index in range(file_info.contents.model_count):
        model = file_info.contents.models[model_index]
        if model.contents.extended_data.type:
            print(f"Model Index:{model_index} {model.contents.name.decode("UTF-8")} has extended data.")
    
    print("\nIterating through track groups:")

    for track_group_index in range(file_info.contents.track_group_count):
        track_group = file_info.contents.track_groups[track_group_index]
        if track_group.contents.extended_data.type:
            print(f"Track Group Index:{track_group_index} {track_group.contents.name.decode("UTF-8")} has extended data.")
    
    print("\nIterating through animations:")

    for animation_index in range(file_info.contents.animation_count):
        animation = file_info.contents.animations[animation_index]
        if animation.contents.extended_data.type:
            print(f"Track Group Index:{animation_index} {animation.contents.name.decode("UTF-8")} has extended data.")

        


def extended_data_check_test(file_path : str) -> bool:

    file = granny_read_entire_file(file_path)
    if file:
        file_info = granny_get_file_info(file)
        
        if file_info.contents is None:
            print("Could not get file info..")
            return False

        print("\nPrinting out what parts of the granny file have custom extended data:")
        print_extended_data(file_info)
        return True
    else:
        print(f"\nCould not open {file_path}")
        return False



