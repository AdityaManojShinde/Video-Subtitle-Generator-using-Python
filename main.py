from tests import test_whisper


# Start Project execution
def main() -> None:
    # add all the processes
    # test basic working of the whisper base model
    test_whisper()
    

if __name__ == "__main__":
    main()