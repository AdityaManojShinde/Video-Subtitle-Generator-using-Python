# Video Subtitle Generator Using Python

This project is a Python-based tool designed to extract audio from video files, transcribe the audio into text, and generate subtitles with precise synchronization. By leveraging **[Whisper](https://openai.com/research/whisper)**, an advanced speech-to-text model by OpenAI, and **FFmpeg** for audio extraction, this tool ensures high accuracy in transcription and supports multiple video formats. The **Tkinter** library provides a graphical interface to easily select videos for processing.

## Features

- **Audio Extraction**: Utilize **FFmpeg** to seamlessly extract audio from video files in formats like MP4, MKV, AVI, etc., ensuring compatibility and efficiency.
- **Speech-to-Text Transcription**: Convert spoken words into text with high accuracy using OpenAI's **[Whisper](https://openai.com/research/whisper)** model.
- **Accurate Subtitle Generation**: Produce properly synchronized subtitles in SRT format for use with any video player.
- **Multi-Language Support**: Generate subtitles in various languages supported by Whisper.
- **Graphical Interface for Video Selection**: Use **Tkinter** to browse and select video files easily, eliminating the need for command-line input.
- **Modular Code Structure**:
  - `main.py`: The entry point of the application.
  - `audio_ex.py`: Contains all logic related to audio extraction and processing.
  - `multi.py`: Multi-purpose utility functions to support the project.

## Installation Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/AdityaManojShinde/Video-Subtitle-Generator-using-Python.git
   cd Video-Subtitle-Generator-using-Python
   ```

2. **Install Required Libraries**:
   Install all dependencies listed in the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

3. **Install FFmpeg**:
   FFmpeg is required for audio extraction. Follow the instructions below to install FFmpeg on your system:

   - **Windows**:

     - Install FFmpeg using winget:
       ```bash
       winget install ffmpeg
       ```
     - Add FFmpeg to your system's PATH if not already added.

   - **MacOS**:

     - Install FFmpeg using Homebrew:
       ```bash
       brew install ffmpeg
       ```

   - **Linux**:
     - Install FFmpeg using your package manager. For example, on Ubuntu:
       ```bash
       sudo apt update
       sudo apt install ffmpeg
       ```

4. **Run the Application**:
   ```bash
   python main.py
   ```

## How It Works

1. **Select Video File**: Run the application and use the Tkinter dialog box to choose the video file you want to process.
2. **Extract Audio**: The `audio_ex.py` module uses FFmpeg to extract the audio from the selected video file.
3. **Transcription**: The extracted audio is transcribed into text using **[Whisper](https://openai.com/research/whisper)**.
4. **Subtitle Generation**: Synchronized subtitles are generated in SRT format, ready to be used with the original video.

## Future Enhancements

- Support for additional subtitle formats (e.g., VTT).
- Real-time transcription and subtitle generation.
- Improved GUI for a more intuitive user experience.
- Batch processing of multiple video files.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Developers

- [Aditya Shinde](https://github.com/AdityaManojShinde)
- [Pushkar Kumar](https://github.com/Pushkar0997)
