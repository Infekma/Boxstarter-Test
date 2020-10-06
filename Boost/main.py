from urllib.request import urlopen
import tempfile
import ntpath
import os

# file dependencies, these are other python scripts that need to be downloaded from the github
file_dependencies = [
    r"https://raw.githubusercontent.com/Infekma/Boxstarter-Test/main/Boost/download_and_extract_boost.py",
    r"https://raw.githubusercontent.com/Infekma/Boxstarter-Test/main/Boost/download_from_web.py",
    r"https://raw.githubusercontent.com/Infekma/Boxstarter-Test/main/Boost/main_setup_boost.py",
    ]

def download_python_file(url, output_dir):
    print(f"downloading python script from {url}")
    file_name = ntpath.basename(url)
    text_file = open(f"{output_dir}/{file_name}", "w",encoding='utf-8')
    text_file.write(urlopen(url).read().decode('utf-8'))
    text_file.close()

with tempfile.TemporaryDirectory() as temp_dir:
    print(f"downloading python scripts to temp dir: {temp_dir}")

    # iterate through each script and download
    for pyscript_url in file_dependencies:
        download_python_file(pyscript_url, temp_dir)
    
    print("Finished downloading all python scripts")
    print("Start executing scripts to setup boost")

    # now that all the scripts are downloaded, execute the files
    # 1. downloads boost and installs to C:/boost_build
    # 2. sets up boost by running bootstrap and b2 and installs C:/boost
    with cd(temp_dir): # change python working directory to temp dir
        exec(open(f"{temp_dir}/download_and_extract_boost.py").read())
        exec(open(f"{temp_dir}/main_setup_boost.py".read()))

    print("Finished executing scripts")