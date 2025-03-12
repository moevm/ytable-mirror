import logging
import requests
from pprint import pprint


def generate_header(o_auth):
    return {"Authorization": f"OAuth {o_auth}"}


def upload_file(o_auth, filepath, yandex_path):
    logging.info('Uploading to yandex')
    logging.info('#1: Creating upload link')
    # Step 1: generate a link to download at
    link = f'https://cloud-api.yandex.net/v1/disk/resources/upload/?path={yandex_path}&overwrite=true'
    req = requests.get(link, headers=generate_header(o_auth))
    if req.status_code == 200:
        # Step 2: put data at the link
        href = req.json()['href']
        logging.info('#2: Sending to yandex')
        req = requests.put(href, data=open(filepath, 'rb'), headers=generate_header(o_auth))
        if req.status_code == 201:
            logging.info('Uploading went successful!')
        else:
            logging.warning(f'Uploading went unsuccessful, see details:')
            pprint(req.content.decode("utf-8"))
    else:
        logging.error(f'Ops, download link creation went unwell. See details in request:')
        pprint(req.content.decode("utf-8"))
