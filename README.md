# SmartLabServer
The server side applications for SCC300 Smart Lab project based on Django in Python. The server is runned with AliCloud VPS machine in Singapore. It parses and stores data Particle Photon devices located in SCC 300 Labs of Lancaster University in UK. 
Client side codes flashed in Photon devices can be found in this repo:
https://github.com/Nomad519/NetworkedStudio

## Data Transmitting
The data is sent via webhook applications triggered by Particle console. Webhook applications package the data (currently temperature, humidity and ambient light level) into JSON format, and send it to the server with a POST request. 

## Data Storing
The data collected are planned to be saved in a database or database-like system. Currently I am using Gogle Sheet because it comes with convinient Google Sheet apis. I also used a package called gspread availible in pip which handles spreadsheet method on google sheet without manually implement the POST or GET request to Google Sheet Server.

## Data Presenting
Data stored is displayed with line charts powered by Google Charts in JS. Since I am currently using Google Sheet, it comes with apis which can present data into charts. I embbed these charts into HTMLs for presentation.

## Misc
I used Bootstrap libraries for CSS in my HTMLs.
