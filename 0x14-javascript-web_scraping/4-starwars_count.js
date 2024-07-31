#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const character = JSON.parse(body);
    const films = character.films;
    console.log(films.length);
  }
});
