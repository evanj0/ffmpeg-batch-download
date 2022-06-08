import csv
from datetime import datetime
import os


out_dir = os.path.join(os.curdir, 'out')
list_path = os.path.join(os.curdir, 'list.csv')
ffmpeg_path = os.path.join(os.curdir, 'ffmpeg')


def read_download_list(path: str) -> list[tuple[str, str]]:
    """Reads the download list and returns a list of `(url, name)` pairs."""
    downloads = []
    with open(path) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            url = row[0].strip()
            name = row[1].strip()
            downloads.append((url, name))
    return downloads


def ffmpeg_download(url, name, dest):
    output_path = os.path.join(dest, f'{name}.mp4')
    exec_path = ffmpeg_path
    write_log(f'Started ffmpeg process (url={url} exec_path={exec_path} output_path={output_path}).')
    os.system(f'{exec_path} -v quiet -stats -i "{url}" -c copy "{output_path}"')


def write_log(msg: str):
    text = f'[{datetime.now()}] {msg}'
    with open(os.path.join(out_dir, 'log_file.txt'), mode='a') as log_file:
        log_file.write(f'{text}\n')
    print(text)


def save_completion_file(out_dir: str, name: str):
    f = open(os.path.join(out_dir, name), mode='x')
    f.close()


def check_completion_file(out_dir: str, name: str):
    return os.path.exists(os.path.join(out_dir, name))


if __name__ == '__main__':
    downloads = read_download_list(list_path)
    for (url, name) in downloads:
        if check_completion_file(out_dir, name):
            write_log(f'Already downloaded "{name}".')
        else:
            write_log(f'Downloading "{name}" (url={url}).')
            ffmpeg_download(url, name, out_dir)
            write_log(f'Downloaded "{name}".')
            save_completion_file(out_dir, name)