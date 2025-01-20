import whisper
import torch
import os

Dir_Path = "audio"

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
    with open("script.txt", 'w') as file:
        file.writelines(result["text"])

