# ytable-mirror
Allows you to duplicate your google tables to yandex disk

## Setup
### 1. Install necessary packages
   ```pip install -r requirements.txt```

### 2. Prepare your files
1) At `config.py` find `Y_CLIENT_ID` and go to https://oauth.yandex.ru/authorize?response_type=token&client_id=`<Y_CLIENT_ID>` <br> to give access to your files and receive your personal oauth token. Write it in `config.py`
2) Check your google files permission, it should be possible to get files by url

### 3. Create special data file
Create a text file. Each line of what should have this format: `table_id yandex/path/file.xslx`<br> 
Table id can be taken from its url in `/d/---/` `https://docs.google.com/spreadsheets/d/Copy_this_code/`<br>
Yandex path is the path where the file will be written, start any path with `/` symbol

## Run program
`python main.py file.txt`