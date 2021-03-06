import subprocess
import sys

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        
install_package("requests") # install request module dependency
        
# dependency: pip install requests
import requests



# Source & Credit: https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def download_file(download_url, output_dir):

    print(f"downloading file from {download_url}")
    file_stream = requests.get(download_url, stream=True)
    with open(output_dir, 'wb') as local_file:
        total_length = file_stream.headers.get('content-length')
        count = 0
        byte_per_chunk = 1024 * 1024 # 1 mb
        for data in file_stream.iter_content(byte_per_chunk):
            count += byte_per_chunk
            printProgressBar(count, int(total_length), prefix = "Progress:", suffix = "Complete", length = 50)
            local_file.write(data)
 