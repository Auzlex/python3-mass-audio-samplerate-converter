# python3-mass-audio-samplerate-converter
A simple python script that utilizes librosa and soundfile to mass convert a folder of wav files to a desired sample rate.

## How to use:

1. Clone the project to a specified directory with:

    `git clone https://github.com/Auzlex/python3-mass-audio-samplerate-converter`

2. It is recommended to use a virtual environment to run this script.

    This script will use:
    - librosa 0.8.1 
    - soundfile 0.10.3

    which may conflict with certain other projects that utilize the mentioned libraries. A requirements.txt has been provided.
    
3. Running the script:

    At the moment you will need to edit the "mass_audio_samplerate_converter.py" and change a variable named "target_samplerate = 22050" to a specified sample rate value you want to convert to.

    Firstly run the script
    ```
        python3 mass_audio_samplerate_converter.py
    ```
    On the first run 2 folders in the same directory as the script will be created:
    - "target" place your files you wish to convert in this folder.
    - "converted" files successfully converted will appear in this folder.

    <br>
    Once the folders exist a re-run of the script will begin the process of converting all the contents inside the target folder.
