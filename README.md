# ytable-mirror
Allows you to duplicate your google tables to yandex disk

## Setup
Most of the preparations would be done during running the program for the first time. The only thing You have to do is
to prepare you google application and create files for further work.
### 1. Google app preparation
1) Go to Google Cloud Console, create application by pressing a button at the left upper corner
2) Chose your project, click *APIs & services* and enable google drive api
3) Move to *Credentials*, click *Create Credentials* chose *Service account* type. Then chose your service account -> keys -> add key -> create new key -> chose json
4) (Optional) You can share your table to a service account (email is displayed in json or at Google Cloud Console). <br>
   (It's not important because service account can reach files that accessible by url)

### 2. Create special data file
Create a text file. Each line of what should have this format: `table_id yandex/path/file.xslx`<br> 
Table id can be taken from its url in `/d/---/` `https://docs.google.com/spreadsheets/d/Copy_this_code/`<br>
Yandex path is the path where the file will be written, start any path with `/` symbol

## Run program
Run via bash script<br>
Set permission firstly:<br>
`chmod a+x ./run`<br>
Then run script (it's available to enter multiple files):<br>
`./run file_1.txt file_2.txt`
