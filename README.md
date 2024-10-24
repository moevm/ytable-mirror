# ytable-mirror
Allows you to duplicate your google tables to yandex disk

## Setup
### 1. Install necessary packages
   ```pip install -r requirements.txt```

### 2. Yandex preparation
1) At `config.py` find `Y_CLIENT_ID` and go to https://oauth.yandex.ru/authorize?response_type=token&client_id=`<Y_CLIENT_ID>` <br> to give access to your files and receive your personal oauth token. Write it in `config.py`
### 3. Google app preparation
1) Go to Google Cloud Console, create application by pressing a button at the left upper corner
2) Chose your project, click *APIs & services* and enable google drive api
3) Move to *Credentials*, click *Create Credentials* chose *Service account* type. Then chose your service account -> keys -> add key -> create new key -> chose json 
4) Then edit `config.py`, specify `G_SERVICE_ACCOUNT_FILE` by entering the path to your json key
5) (Optional) You can share your table to a service account (email is displayed in json or at Google Cloud Console). <br>
   (It's not important because service account can reach files that accessible by url)

### 4. Create special data file
Create a text file. Each line of what should have this format: `table_id yandex/path/file.xslx`<br> 
Table id can be taken from its url in `/d/---/` `https://docs.google.com/spreadsheets/d/Copy_this_code/`<br>
Yandex path is the path where the file will be written, start any path with `/` symbol

## Run program
`python main.py example.txt`
