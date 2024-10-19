from config import ConfigSingleton
from google_class import GServiceDownloader
from yandex_func import upload_file
import argparse
import logging
import os


logging.basicConfig(level=logging.INFO, format="[%(asctime)s][%(levelname)s]: %(message)s")
config = ConfigSingleton()

parser = argparse.ArgumentParser(prog='YMirror')
parser.add_argument('filename')
args = parser.parse_args()
filename = args.filename

def main_loop():
    if os.path.exists(filename):
        logging.info('Set up google service')
        g_service = GServiceDownloader(config.G_SERVICE_ACCOUNT_FILE, config.G_SCOPES)

        with open(filename, 'r') as file:
            for i, line in enumerate(file.readlines()):
                line = line.replace('\n', '')
                logging.info(f"Current line is {i + 1}: {line} ")

                # parse data
                g_sheet_id = line.split()[0]
                y_path = line.split()[1]
                # define the name of a file, that would be downloaded and uploaded
                download_filename = os.path.basename(y_path)
                download_path = './' + download_filename

                # process
                g_service.download_table(g_sheet_id, download_path)
                upload_file(config.Y_OAuth, download_path, y_path)

                # remove temporary files
                logging.info('Removing temporary files ')
                os.remove(download_path)
    else:
        logging.warning('Unable to find necessary file, finishing the program')


if __name__ == '__main__':
    main_loop()
