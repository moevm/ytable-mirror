import logging
from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.discovery import build
import io


class GServiceDownloader:
    mimeType = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

    def __init__(self, file, scopes):
        credentials = service_account.Credentials.from_service_account_file(file, scopes=scopes)
        self.service = build('drive', 'v3', credentials=credentials)

    def explore_available_content(self):
        results = self.service.files().list(fields="nextPageToken, files(id, name, mimeType)").execute()
        return results

    def download_table(self, file_id, filename):
        logging.info(f"Downloading {filename} from id {file_id}")
        request = self.service.files().export_media(fileId=file_id,
                                               mimeType=self.mimeType)
        fh = io.FileIO(filename, 'wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()
