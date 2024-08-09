"""This prints out the sizes of all granny related structs"""
from ctypes import sizeof
from gr2_format import*

def check_granny_struct_sizes():
    """Checks sizes of granny related structs"""
    assert sizeof(GrannyFile) == int(0x38), 'GrannyFile struct size is wrong.'
    assert sizeof(GrannyFileInfo) == int(0x94), 'GrannyFileInfo struct size is wrong.'
    assert sizeof(GrannyFileArtToolInfo) == int(0x58), 'GrannyFileArtToolInfo struct size is wrong.'
    assert sizeof(GrannyFileExporterInfo) == int(0x28), 'GrannyFileExporterInfo struct size is wrong.'
    assert sizeof(GrannyAnimation) == int(0x38), 'GrannyAnimation struct size is wrong.'
    assert sizeof(GrannyPeriodicLoop) == int(0x30), 'GrannyPeriodicLoop struct size is wrong.'
    assert sizeof(GrannyTextTrackEntry) == int(0xc), 'GrannyTextTrackEntry struct size is wrong.'
    assert sizeof(GrannyTextTrack) == int(0x14), 'GrannyTextTrack struct size is wrong.'
    assert sizeof(GrannyCurve2) == int(0x10), 'GrannyCurve2 struct size is wrong.'
    assert sizeof(GrannyTransformTrack) == int(0x3c), 'GrannyVectorTrack struct size is wrong.'
    assert sizeof(GrannyVectorTrack) == int(0x20), 'GrannyVectorTrack struct size is wrong.'
    assert sizeof(GrannyTrackGroup) == int(0xa4), 'GrannyTrackGroup struct size is wrong.'
    assert sizeof(GrannyModelMeshBinding) == int(0x8), 'GrannyModelMeshBinding struct size is wrong.'
    assert sizeof(GrannyModel) == int(0x70), 'GrannyModel struct size is wrong.'
    assert sizeof(GrannyMesh) == int(0x4c), 'GrannyMesh struct size is wrong.'
    assert sizeof(GrannyBoneBinding) == int(0x2c), 'GrannyBoneBinding struct size is wrong.'
    assert sizeof(GrannyMaterialBinding) == int(0x8), 'GrannyMaterialBinding struct size is wrong.'
    assert sizeof(GrannyMorphTarget) == int(0x14), 'GrannyMorphTarget struct size is wrong.'
    assert sizeof(GrannyTriTopology) == int(0x6c), 'GrannyTriTopology struct size is wrong.'
    assert sizeof(GrannyTriMaterialGroup) == int(0xc), 'GrannyTriMaterialGroup struct size is wrong.'
    assert sizeof(GrannyTriAnnotationSet) == int(0x2c), 'GrannyTriAnnotationSet struct size is wrong.'
    assert sizeof(GrannyVertexAnnotationSet) == int(0x2c), 'GrannyVertexAnnotationSet struct size is wrong.'
    assert sizeof(GrannyVertexData) == int(0x2c), 'GrannyVertexData struct size is wrong.'
    assert sizeof(GrannySkeleton) == int(0x28), 'GrannySkeleton struct size is wrong.'
    assert sizeof(GrannyBone) == int(0xa4), 'GrannyBone struct size is wrong.'
    assert sizeof(GrannyTransform) == int(0x44), 'GrannyTransform struct size is wrong.'
    assert sizeof(GrannyFileExporterInfo) == int(0x28), 'GrannyFileExporterInfo struct size is wrong.'
    assert sizeof(GrannyMaterial) == int(0x2c), 'GrannyMaterial struct size is wrong.'
    assert sizeof(GrannyMaterialMap) == int(0x10), 'GrannyMaterialMap struct size is wrong.'
    assert sizeof(GrannyTexture) == int(0x5c), 'GrannyTexture struct size is wrong.'
    assert sizeof(GrannyPixelLayout) == int(0x24), 'GrannyPixelLayout struct size is wrong.'
    assert sizeof(GrannyTextureImage) == int(0xc), 'GrannyTextureImage struct size is wrong.'
    assert sizeof(GrannyTextureMipLevel) == int(0x10), 'GrannyTextureMipLevel struct size is wrong.'
    assert sizeof(GrannyVariant) == int(0x10), 'GrannyVariant struct size is wrong.'
    assert sizeof(GrannyDataTypeDefinition) == int(0x2c), 'GrannyDataTypeDefinition struct size is wrong.'
    assert sizeof(GrannyRef) == int(0x8), 'GrannyRef struct size is wrong.'
    assert sizeof(GrannyFileHeader) == int(0x48), 'GrannyFileHeader struct size is wrong.'
    assert sizeof(GrannyFileMagic) == int(0x20), 'GrannyFileMagic struct size is wrong.'
    assert sizeof(GrannyGRNSection) == int(0x2c), 'GrannySection struct size is wrong.' 
    
    print("\nYour good to go! All struct sizes specified in check_granny_struct_sizes() are correct.")

