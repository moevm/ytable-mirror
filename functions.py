import logging
# Google
from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.discovery import build
import io
# Yandex
import os
import requests


# Google
def create_google_service(file, scopes):
    logging.info('Creating google service')
    credentials = service_account.Credentials.from_service_account_file(file, scopes=scopes)
    service = build('drive', 'v3', credentials=credentials)
    return service


def explore_available_content(service):
    results = service.files().list(fields="nextPageToken, files(id, name, mimeType)").execute()
    return results


def download_table(service, file_id, filename):
    logging.info(f"Downloading {filename} from id {file_id}")
    request = service.files().export_media(fileId=file_id,
                                           mimeType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    fh = io.FileIO(filename, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))


# Yandex
def generate_header(o_auth):
    return {"Authorization": f"OAuth {o_auth}"}


def upload_file(o_auth, filepath, yandex_path):
    logging.info('Uploading to yandex')
    # Step 1: generate a link to download at
    logging.info('Generating a link to download at')
    filename = os.path.basename(filepath)
    link = f'https://cloud-api.yandex.net/v1/disk/resources/upload/?path={yandex_path}/{filename}&overwrite=true'
    req = requests.get(link, headers=generate_header(o_auth))
    if req.status_code == 200:
        href = req.json()['href']
    else:
        logging.error('')
        return req.status_code
    # Step 2: put data at the link
    logging.info('Sending to yandex')
    r = requests.put(href, data=open(filepath, 'rb'), headers=generate_header(o_auth))
    return r.status_code
