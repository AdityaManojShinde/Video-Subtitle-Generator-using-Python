import os
    
# make change file extension to .mp3
def replace_extension(filename : str) -> str:
    converted_file = filename.rsplit('.', 1)[0] + ".mp3"
    return converted_file

#delete all files from video folder
def delete_videos(dir_path):
    # check if video folder exits
    if os.path.exists(dir_path):
        for file in os.listdir(dir_path): # <- returns list of file names in given folder
            file_path = os.path.join(dir_path,file) # <- create path to delete file
            os.remove(file_path) # <- delete file
    else:
        print(f"The folder {dir_path} does not exist.")