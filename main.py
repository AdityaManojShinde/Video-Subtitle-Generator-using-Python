import whisper
import torch

# Start Project execution
def main() -> None:
    # add all the processes
    # basic working of the wisper base model
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = whisper.load_model("base", device=device)
    result = model.transcribe("audio.mp3")
    with open("script.txt", 'w') as file:
        file.writelines(result["text"])

if __name__ == "__main__":
    main()