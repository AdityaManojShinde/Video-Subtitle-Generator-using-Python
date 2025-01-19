#from tests import test_whisper
from audio_ex import get_audio


# Start Project execution
def main() -> None:
    # add all the processes
    get_audio()

    # test basic working of the wisper base model
    #test_whisper()


if __name__ == "__main__":
    main()