import os
from setuptools import setup, Extension
from sys import platform


from Cython.Build import cythonize

# Link the correct libraries
cg_include_dirs=["pyDSCSRenderer/Renderer/Cg"]
if platform == "linux" or platform == "linux2":
    cg_library_dirs = ["pyDSCSRenderer/Renderer/Cg/linux64"]
    cg_libraries=['Cg', 'CgGL']
elif platform == "darwin":
    cg_library_dirs = ["pyDSCSRenderer/Renderer/Cg/mac"]
    cg_libraries=['Cg']
elif platform == "win32":
    cg_library_dirs = ["pyDSCSRenderer/Renderer/Cg/windows"]
    cg_libraries=['cg', 'cgGL', 'glut32']
else:
    raise Exception("Unsupported platform: ", platform)

# Set the correct compiler flags
compiler = "msvc" # <- need to be able to detect this!!!
if compiler.startswith("msvc"):
    cpp_version = '/std:c++20'
elif compiler.startswith("clang"):
    cpp_version = "-std=c++20"
elif compiler.startswith("g++"):
    cpp_version = "-std=c++20"
elif compiler.startswith("gcc"):
    cpp_version = "-std=c++20"
else:
    raise Exception("Unrecognised compiler: ", compiler)

# Now compile
setup(ext_modules = cythonize(
    Extension(
       "pyDSCSRenderer",
       sources=[
           "pyDSCSRenderer/pyDSCSRenderer.pyx",
           "pyDSCSRenderer/Renderer/DSCS/Renderer.cpp",
           "pyDSCSRenderer/Renderer/DSCS/DataObjects/AnimationSampler.cpp",
           "pyDSCSRenderer/Renderer/DSCS/DataObjects/OpenGLDSCSMaterial.cpp",
           "pyDSCSRenderer/Renderer/DSCS/DataObjects/OpenGLDSCSMesh.cpp",
           "pyDSCSRenderer/Renderer/DSCS/DataObjects/OpenGLDSCSTexture.cpp",
           "pyDSCSRenderer/Renderer/DSCS/DataObjects/SkeletonDataBlocks.cpp",
           "pyDSCSRenderer/Renderer/DSCS/RenderObjects/Camera.cpp",
           "pyDSCSRenderer/Renderer/DSCS/ShaderSystem/cgGL/cgGLShaderBackend.cpp",
           "pyDSCSRenderer/Renderer/DSCS/ShaderSystem/cgGL/cgGLShaderObject.cpp",
           "pyDSCSRenderer/Renderer/DSCS/ShaderSystem/cgGL/Utils.cpp",
           "pyDSCSRenderer/Renderer/DSCS/ShaderSystem/cgGL/OpenGLSettings/OpenGLSettings.cpp",
           "pyDSCSRenderer/Renderer/FileFormats/DSCS/DSCStoOpenGL.cpp",
           "pyDSCSRenderer/Renderer/FileFormats/DSCS/AnimFile/AnimReadWrite.cpp",
           "pyDSCSRenderer/Renderer/FileFormats/DSCS/GeomFile/GeomReadWrite.cpp",
           "pyDSCSRenderer/Renderer/FileFormats/DSCS/GeomFile/MaterialReadWrite.cpp",
           "pyDSCSRenderer/Renderer/FileFormats/DSCS/GeomFile/MeshReadWrite.cpp",
           "pyDSCSRenderer/Renderer/FileFormats/DSCS/NameFile/NameReadWrite.cpp",
           "pyDSCSRenderer/Renderer/FileFormats/DSCS/SkelFile/SkelReadWrite.cpp",
           "pyDSCSRenderer/Renderer/FileFormats/Textures/DDS.cpp",
           "pyDSCSRenderer/Renderer/glad/src/glad.c",
           "pyDSCSRenderer/Renderer/serialisation/Exceptions.cpp",
           "pyDSCSRenderer/Renderer/serialisation/ReadWriter.cpp",
           "pyDSCSRenderer/Renderer/Utils/BitManip.cpp",
           "pyDSCSRenderer/Renderer/Utils/Float16.cpp",
           "pyDSCSRenderer/Renderer/Utils/Hashing.cpp",
           "pyDSCSRenderer/Renderer/Utils/Matrix.cpp",
           "pyDSCSRenderer/Renderer/Utils/OpenGL.cpp",
           "pyDSCSRenderer/Renderer/Utils/Vector.cpp"
       ],
       language="c++",
       extra_compile_args=[cpp_version],
       include_dirs=[*cg_include_dirs],
       library_dirs =[*cg_library_dirs],
       libraries=[*cg_libraries]
       
   )
))
