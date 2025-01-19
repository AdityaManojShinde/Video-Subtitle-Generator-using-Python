import ffmpeg
import os
import shutil
from tkinter import filedialog , Tk


# Folder Paths
AUDIO_DIR = "./audio"
VIDEO_DIR = "./video"

def copy_video(video_path: str):
    os.makedirs(VIDEO_DIR,exist_ok=True)
    if video_path:
        file_name = os.path.basename(video_path)
        folder_path = os.path.join(VIDEO_DIR,file_name)
        shutil.copy(video_path, folder_path)
        return folder_path
    return None

def get_video_path() -> str:
    root = Tk() # <- create tkinter instance
    root.withdraw() # <- hide tkinter running window
    # pick video path with file picker of given filetypes
    video_path = filedialog.askopenfilename(title="Select a Video", filetypes=[("Video Files", "*.mp4 *.mkv *.avi *.mov")])
    return video_path

def extract_audio(input_file: str, output_file: str):
    os.makedirs(AUDIO_DIR,exist_ok=True)
    audio = ffmpeg.input(input_file)
    audio.output(output_file).run()
    
def replace_extension(filename : str) -> str:
    converted_file = filename.rsplit('.', 1)[0] + ".mp3"
    return converted_file

# main execution function
def get_audio():
    video_path: str = get_video_path()
    input_file_path = copy_video(video_path=video_path)
    filename = replace_extension(os.path.basename(input_file_path))
    output_path = os.path.join(AUDIO_DIR,filename)
    extract_audio(input_file=input_file_path,output_file=output_path)


