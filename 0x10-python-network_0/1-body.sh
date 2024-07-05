#!/bin/bash
# This script takes in a URL, sends a GET request to the URL, and displays the body of the response only if the status code is 200
response=$(curl -s -w "%{http_code}" "$1")
body=${response::-3}
status_code=${response: -3}
if [ "$status_code" -eq 200 ]; then
  echo "$body"
fi
