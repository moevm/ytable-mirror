from config import ConfigSingleton
from functions import *
import logging


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


config = ConfigSingleton()
# insert google sheet id
table_id = '1zG21U9ERxID2AK_pcaCvyqp13PDzJHIkfAM5ejd8WBw'
filename = 'test.xlsx'
# path to yandex folder
y_path = '/Tables'

# init google service
g_service = create_google_service(config.G_SERVICE_ACCOUNT_FILE, config.G_SCOPES)

# download table
download_table(g_service, table_id, filename)
# upload file
code = upload_file(config.Y_OAuth, filename, y_path)
logging.info(f'uploading finished with web code {code}')
