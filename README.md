# ytable-mirror
Allows you to duplicate your google tables to yandex disk

## Setup
### 1. Install necessary packages
   ```pip install -r requirements.txt```

### 2. Prepare your files
1) At `config.py` find `Y_CLIENT_ID` and go to https://oauth.yandex.ru/authorize?response_type=token&client_id=`<Y_CLIENT_ID>` <br> to give access to your files and receive your personal oauth token. Write it in `config.py`
2) Create your Google app, save json credentials and past is into `config.py` <br> (see guide: https://www.datalytics.ru/all/rabotaem-s-api-google-drive-s-pomoschyu-python/)
3) Check your Google files permission, it should be possible to get files by url, or you can share it with application email

### 3. Create special data file
Create a text file. Each line of what should have this format: `table_id yandex/path/file.xslx`<br> 
Table id can be taken from its url in `/d/---/` `https://docs.google.com/spreadsheets/d/Copy_this_code/`<br>
Yandex path is the path where the file will be written, start any path with `/` symbol

## Run program
`python main.py example.txt`
