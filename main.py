from config import ConfigSingleton
from google_class import GServiceDownloader
from yandex_func import upload_file
import argparse
import logging
import os
import re


logging.basicConfig(level=logging.INFO, format="[%(asctime)s][%(levelname)s]: %(message)s")
config = ConfigSingleton()
config.extend_from_confing_file()

parser = argparse.ArgumentParser(prog='YMirror')
parser.add_argument('files', nargs='+')
args = parser.parse_args()
files = args.files
line_pattern = "^\S{44} \/?(?:\w+\/)+\w+.xlsx$"

def main_loop():
    for file in files:
        logging.info(f'Current data file: {file}')
        if os.path.exists(file):
            logging.info('Set up google service')
            g_service = GServiceDownloader(config.G_SERVICE_ACCOUNT_FILE, config.G_SCOPES)

            with open(file, 'r') as f:
                for i, line in enumerate(f.readlines()):
                    line = line.replace('\n', '')
                    # skip empty line
                    if line == '':
                        logging.warning("Line is empty! Skip")
                        continue

                    logging.info(f"Current line is {i + 1}: {line} ")
                    # check line's format
                    if re.search(line_pattern, line) is None:
                        logging.warning("Line format is incorrect! Skip")
                        continue

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
            logging.warning('Unable to find file, skip')

if __name__ == '__main__':
    main_loop()
