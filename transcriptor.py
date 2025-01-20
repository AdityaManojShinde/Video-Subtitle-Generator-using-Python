import whisper
import torch
import os

"""
Convert hindi speech to text
result = model.transcribe(file_path, verbose=True,
        language="hi")
    with open("script.txt", 'w',encoding="utf-8") as file:
        file.writelines(result["text"])
"""

Dir_Path = "audio"

#TODO: create a function to generate a subtitle file
#TODO: create another to burn subtitle file in  the video and regenerate it

def get_audio_file():
    file_path = ""
    if os.path.exists(Dir_Path):
        for file in os.listdir(Dir_Path):
            file_path = os.path.join(Dir_Path,file)
        return file_path
    return Dir_Path


def transcriptor():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = whisper.load_model("small", device=device)
    file_path = get_audio_file()
    result = model.transcribe(file_path)
    with open("script.txt", 'w',encoding="utf-8") as file:
        file.writelines(result["text"])

