#!/bin/bash
# This script makes a request to 0.0.0.0:5000/catch_me and causes the server to respond with "You got me!" in the body of the response
curl -s -X PUT -L 0.0.0.0:5000/catch_me -d "user_id=98"