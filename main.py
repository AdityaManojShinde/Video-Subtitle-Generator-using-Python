import whisper

# Start Project execution
def main() -> None:
    # add all the processes
    # basic working of the wisper base model
    model = whisper.load_model("base")
    result = model.transcribe("audio.mp3")
    with open("script.txt", 'w') as file:
        file.writelines(result["text"])

if __name__ == "__main__":
    main()