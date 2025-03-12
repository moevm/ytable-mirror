#!/bin/bash

echo "Start building"
if ! [[ -e google_path.txt || -e y_oauth.txt ]]; then
  # enter filename
  echo "Creating config"
  while ! [[ -e $path ]]; do
    read -r -p "Enter google service json filename: " path
    if ! [[ -e $path ]]; then
      echo -n "Incorrect filename was entered"
    fi
  done
  echo "$path" > google_path.txt
  # get oath
  echo -n "Visit https://oauth.yandex.ru/authorize?response_type=token&client_id=3542ffc72e2c4e9f8a1ff379081ed5a5"$'\n'
  read -r -p "Enter yandex oauth: " oauth
  echo "$oauth" > y_oauth.txt
else
  path="./$(cat google_path.txt)"
fi

docker build . -t converter
docker run -v "$path":/app/google.json -v ./y_oauth.txt:/app/y_oauth.txt --rm converter $@
