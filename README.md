# SmartLabServer
The server side applications for SCC300 Smart Lab project based on Django in Python. The server is runned with AliCloud VPS machine in Singapore. It parses and stores data Particle Photon devices located in SCC 330 Labs of Lancaster University in UK. 
Client side implementations on Photon devices can be found in this repo:
https://github.com/Nomad519/NetworkedStudio

SCC330 Networked Studio Contributors: Viktor Kolev, Eduard Schlotter, James Thomas-Woodhouse, Cyrus Gao

## Data Transmitting
The data is sent via webhook applications triggered by Particle console. Webhook applications package the data (currently temperature, humidity and ambient light level) into JSON format, and send it to the server with a POST request. 

## Data Storing
The data collected are planned to be saved in a database or database-like system. Currently I am using Gogle Sheet because it comes with convinient Google Sheet apis. I also used a package called gspread availible in pip which handles spreadsheet method on google sheet without manually implement the POST or GET request to Google Sheet Server.

## Data Presenting
Data stored is displayed with line charts powered by Google Charts in JS. Since I am currently using Google Sheet, it comes with apis which can present data into charts. I embbed these charts into HTMLs for presentation.

## Misc
I used Bootstrap libraries for CSS in my HTMLs.
## APIs For the Door Sensors

The aim of the these two APIs is to receive a string containing the coming or leaving info from the door of lab and a time string. The server uses this to generate a history of people activities in lab and present current number of people in lab.

- **/senddoor**

  *requires method: POST*

  post data and date string to this path from photon

  String body:

  ```c
  num + ',' + Time.timeStr()
    //num == 1 || -1
  ```

  To reset number of people to 0, set the string body to:

  ```c
  "-reset"
  ```

  And if this is done successfully, you would see success message from response of this request

- **/getdoor**

  *requires method: GET*

  To get current number of people in the lab (always >= 0).

  The result would be returned as HTTP response.


