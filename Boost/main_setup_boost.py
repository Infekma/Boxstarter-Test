import os
from urllib.request import urlopen

# config
msvc_toolset = 14.1

# download the base config from the github repository and store the contents to a string
base_config_url = "https://raw.githubusercontent.com/Infekma/Boxstarter-Test/main/Boost/base-config.jam"
base_config = urlopen(base_config_url).read().decode('utf-8')

# TODO - something must've gone wrong if empty ?

# returns the b2 args for building boost
# b2 Example: "b2 --build-dir=C:\boost_build --prefix=C:\boost --libdir=C:\boost\lib64 --layout=tagged address-model=64 -j16 toolset=msvc-14.1 install"
def get_b2_args(build_dir : str, output_dir : str, architecture : int):
  return str(
    "b2"
    f" --build-dir={build_dir}"
    f" --prefix={output_dir}"
    f" --libdir={output_dir}\lib{str(architecture)}"
    " --layout=tagged" 
    f" address-model={str(architecture)}" 
    " -j16"
    f" toolset=msvc-{str(msvc_toolset)}"
    " install")
  
# build boost for the given python version by copying the base_config and adding the required python usage to the file
def build_boost(boost_build_dir : str, boost_output_dir : str, python_version : int, python_install_dir : str, architecture : int): 
  # write the project config settings required to build boost with this python version
  project_config = base_config
  project_config += f"\nusing python : {str(python_version)} : {python_install_dir} : {python_install_dir}/include : {python_install_dir}/libs ;"
  file = open(f"{boost_build_dir}\project-config.jam", "w")
  file.write(project_config)
  file.close
  
  # run b2 with the requirement args for this boost python build
  b2_args = get_b2_args(boost_build_dir, boost_output_dir, architecture)
  os.system(b2_args)
  
# script actions:
# 1. run bootstrap.bat - builds b2.exe
# 2. run b2.exe to build boost
# 3. set environmental variable for "BOOST_ROOT_DIR" to point to the boost_output_dir

# TODO: customizable input/output ?
build_dir = r"C:\boost_build"
output_dir = r"C:\boost"

# how to run bat from python: https://stackoverflow.com/questions/1818774/executing-a-subprocess-fails
# run the bootstrap.bat to build the b2 executable
os.system(f"{build_dir}\bootstrap.bat")

# TODO: this can be improved probably
build_boost(build_dir, output_dir, 3.7, "C:/Python/37-64", 64)
build_boost(build_dir, output_dir, 3.7, "C:/Python/37-32", 32)
build_boost(build_dir, output_dir, 2.7, "C:/Python/27-64", 64)
build_boost(build_dir, output_dir, 2.7, "C:/Python/27-32", 32)

# add "BOOST_ROOT_DIR" environmental variable and point to our boots output directory
os.environ['BOOST_ROOT_DIR'] = output_dir
