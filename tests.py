import whisper
import torch

# Test Whisper model
def test_whisper():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = whisper.load_model("base", device=device)
    result = model.transcribe("audio.mp3")
    print(result)
