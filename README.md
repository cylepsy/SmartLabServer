# SmartLabServer
The server side applications for SCC330 Smart Lab project based on Django in Python. The server is runned with Linux VM in Lancaster University. It parses and stores data Particle Photon devices located in SCC 330 Labs of Lancaster University in UK. 
Client side implementations on Photon devices can be found in this repo:
https://github.com/Nomad519/NetworkedStudio

SCC330 Networked Studio Contributors: Viktor Kolev, Eduard Schlotter, James Thomas-Woodhouse, Cyrus Gao

## How to run the server

1. ### Use ssh to connect to the VM

   If you are working off campus, please connect to the University VPN first. If you don't know how, have a look at [here](https://lancasteranswers.lancs.ac.uk/portal/app/portlets/results/viewsolution.jsp?solutionid=111025142706591).

   Once you are connecting the Uni VPN, you now need to use SSH to connect to the VM.

   - #### For Linux, Mac user:

     Use the command below to connect the Linux VM in our Uni:

     ```bash
     ssh -p6767 uniusername@sccug-330-03.lancs.ac.uk
     ```

     Replace "uniusername" to your Uni studnet account name. You should be asked to enter your password to login.


   - #### For Windows user:

     You can use some software like  [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) to build an SSH connection. However, I recommand to use some console emulator software like [cmder](http://cmder.net) which supports all sets of Linux bash commands including SSH we need.

2. ### Get the latest server file

   Once you are logged into the VM, you will be directed into your personal directory named by your names. There are three ways to get the latest server files:

   - #### Use the files in my directory

     1. Go to the outer directory of your current position:

        ```bash
        cd ..
        ```

     2. Go to my personal folder

        ```bash
        cd gaot
        ```

     3. Enter the Server folder

        ```bash
        cd SmartLabServer
        ```

   - #### Copy the files from my folder to your own folder

     Do this if you are planing on **implement** the server project. Once you get into my personal folder, use **cp** command to copy the files to your working directory:

     ``` bash
     cp SmartLabServer yourfolder
     ```

   - #### Use GIT command line to clone this repository 

3. ### Run the Django project

   Once you get into SmartLabServer folder, enter the project folder(forgive my name):

   ```bash
   cd untitled
   ```

   Run the server:

   ```bash
   sudo python3 manage.py runserver 0.0.0.0:80
   ```

   Your server should  be running now! Check [Django Documents](https://docs.djangoproject.com/en/1.11/) for more help.

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


