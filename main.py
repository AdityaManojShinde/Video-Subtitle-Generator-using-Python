import whisper
import torch

# Test Whisper model
def test_whisper():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = whisper.load_model("base", device=device)
    result = model.transcribe("audio.mp3")
    with open("script.txt", 'w') as file:
        file.writelines(result["text"])

# Start Project execution
def main() -> None:
    # add all the processes
    # test basic working of the wisper base model
    test_whisper()
    

if __name__ == "__main__":
    main()