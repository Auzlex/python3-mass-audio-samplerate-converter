#!/usr/bin/env python3
import os
import sys

# librosa 0.8.1
# soundfile 0.9.0
import librosa
import soundfile as sf

"""
    Config
"""
target_samplerate = 22050       # the target sample rate we wish to convert the audio files to, 
                                # for those interested in automation maybe a python cli input would be better
target_fname = "target"         # name of the target folder :: files we want to convert :: in same directory as script
conversion_fname = "converted"  # name of the folder :: converted files will be dumped here :: in same directory as script

"""
    Directory functions
"""

def root_dir():
    """returns the root directory of this file location"""

    return os.path.dirname(os.path.realpath(__file__))

def target_folder():
    """returns the directory of the target folder to extract from"""

    global target_fname
    return os.path.join( root_dir(), target_fname )

def conversion_folder():
    """returns the directory of the target folder to extract from"""

    global conversion_fname
    return os.path.join( root_dir(), conversion_fname )

def validate_dirs():
    """validates directory existence"""
    
    if not os.path.exists(target_folder()): # validate folder exists
        print(f"Target folder was not found creating new dir in: {target_folder()}")
        os.mkdir(target_folder())

    if not os.path.exists(conversion_folder()): # validate folder exists
        print(f"Conversion folder was not found creating new dir in: {conversion_folder()}")
        os.mkdir(conversion_folder())

"""
    Conversion
"""
def begin_conversion():
    """invoked on execution of the script to begin conversion of files in target folder"""

    # get files in the target directory
    files = os.listdir( target_folder() )
    filecount = len(files)

    if filecount > 0: # if the file count is greater than 0
        print(f"{filecount} Found, processing...")

        for file in files: # for every file in files list

            # make sure they are wav files
            if file.lower().split(".")[1] == "wav":
                print(f"reading -> {file} from target")
                try:
                    # attempt to read file in with librosa
                    x, sr = librosa.load(os.path.join( target_folder(), file ))
                except Exception as err:
                    print(f"Error occurred when opening file {file}\n{err}")
                    continue
                
                # librosa resample x data with that files sample rate to target_samplerate
                y = librosa.resample(x, sr, target_samplerate)

                #soundfile sf write
                print(f"writing -> {file} to converted")
                sf.write(os.path.join( conversion_folder(), file ), y, target_samplerate, subtype='PCM_24')
                print(f"done!")
    else:
        print( "\nTarget folder is empty, please place files you want to convert in this folder. Note nested folders will not work." )

"""
    Execution
"""

# if this is the entry point then lets initialize the core script
if __name__ == "__main__":

    validate_dirs() # validates directories
    begin_conversion() # begin conversion
