import whisper
import torch
import os
import tkinter as tk
from tkinter import filedialog


Dir_Path = "audio"

def get_audio_file():
    file_path = ""
    if os.path.exists(Dir_Path):
        for file in os.listdir(Dir_Path):
            file_path = os.path.join(Dir_Path, file)
        return file_path
    return Dir_Path

def transcriptor():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = whisper.load_model("small", device=device)
    file_path = get_audio_file()
    
    if file_path:
        result = model.transcribe(file_path, word_timestamps=True)  # Get transcribed text with timestamps
        
        # Create a GUI for file save dialog
        root = tk.Tk()
        root.withdraw()
        save_path = filedialog.asksaveasfilename(defaultextension=".srt", filetypes=[("Subtitle Files", "*.srt"), ("All Files", "*.*")])
        
        if save_path:
            with open(save_path, 'w', encoding="utf-8") as file:
                file.writelines(result["text"])
            print(f"Subtitle file saved at: {save_path}")
        else:
            print("No save location selected.")
    else:
        print("No audio file found in the directory.")