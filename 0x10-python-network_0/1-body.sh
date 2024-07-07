#!/bin/bash
# This script sends a GET request to the URL and displays the body of the response only if the status code is 200
curl -sL -X GET "$1"
