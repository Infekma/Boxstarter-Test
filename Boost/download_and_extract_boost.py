import download_from_web
import zipfile
import os
import tempfile

# the code currently assumes we're always downloading a zip
boost_download_url = r"https://dl.bintray.com/boostorg/release/1.74.0/source/boost_1_74_0.zip"
boost_output_dir = r"C:\boost_build"

# create temporary directory to work at
with tempfile.TemporaryDirectory() as temp_download_dir:
    print(f'created temporary directory at {temp_download_dir}')

    file_output_dir = f"{temp_download_dir}/boost.zip"
    # download the boost zip file
    download_file(boost_download_url, file_output_dir)

    # TODO: add progress bar for zip progress?
    # extract the downloaded file
    with zipfile.ZipFile(file_output_dir, 'r') as zip_ref:
        zip_ref.extractall(temp_download_dir)

        # boost stores everything inside a directory, namely: boost_x_x_x..
        # this step renames the folder and relocates it to "boost_output_dir"
        output_folder = zip_ref.namelist()[0]
        os.rename(f"{temp_download_dir}/{output_folder}", boost_output_dir)