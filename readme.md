# Ffmpeg batch download script

## Instructions
- Create `./out` directory.
- Create `./out/log_file.txt` file.
- Download an ffmpeg binary and place it next to the script (`./ffmpeg`/`ffmpeg.exe`).
- Create `./list.csv` containing the url to download in the first column and the name (names are used for identification, so they must be unique!).

The script saves an empty file with the name of a download once the download has been finished. This stops the same file from being downloaded multiple times, meaning that you can choose to only append to the list file instead of deleting already downloaded videos. 