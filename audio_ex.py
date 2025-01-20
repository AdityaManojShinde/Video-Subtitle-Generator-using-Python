import ffmpeg
import os
import shutil
from tkinter import filedialog , Tk

from multi import replace_extension, delete_files


# Folder Paths
AUDIO_DIR = "./audio"
VIDEO_DIR = "./video"

def copy_video(video_path: str):
    os.makedirs(VIDEO_DIR,exist_ok=True)
    if video_path:
        file_name = os.path.basename(video_path)
        folder_path = os.path.join(VIDEO_DIR,file_name)
        shutil.copy(video_path, folder_path) # <- copy video folder_path
        return folder_path
    return None

def get_video_path() -> str:
    root = Tk() # <- create tkinter instance
    root.withdraw() # <- hide tkinter running window
    # pick video path with file picker of given filetypes
    video_path = filedialog.askopenfilename(title="Select a Video", filetypes=[("Video Files", "*.mp4 *.mkv *.avi *.mov")])
    return video_path

# extract audio from video
def extract_audio(input_file: str, output_file: str):
    os.makedirs(AUDIO_DIR,exist_ok=True)
    audio = ffmpeg.input(input_file)
    audio.output(output_file).run()
    

# main execution function
def get_audio():
    delete_files(AUDIO_DIR) # <- empty audio folder
    video_path: str = get_video_path()
    input_file_path = copy_video(video_path=video_path) # <- copy videos to video folder and return their path 
    filename = replace_extension(os.path.basename(input_file_path))
    output_path = os.path.join(AUDIO_DIR,filename)
    extract_audio(input_file=input_file_path,output_file=output_path)
    delete_files(VIDEO_DIR) # <- empty video folder