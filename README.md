<img src="img src=https://i.imgur.com/MPUnZUm.jpg" width="160" height=auto />
![BuddySystemImg](https://i.imgur.com/MPUnZUm.jpg)

# BuddySystem: Walk safe & make a buddy along the way!

Mission: To increase the safety of the average to occasional commuter through the “safety in numbers” approach & hopefully make friends in the process.

## Description

BuddySystem is an application geared towards occasional to regular commuters to post requests to other users to accompany them on walks, providing routes, locations and arrival times. Users will be able to see times and locations of requested walks in their areas through their own profiles and private message other users to determine whether they would be the right walking Buddy for them.


## Environment

* __OS:__ Mac OS X 10.13.6
* __language:__ Python 3.4.3
* __database:__ mysql Ver 14.14 Distrib 5.7.18
* __documentation:__ Swagger (flasgger==0.6.6)
* __framework:__ Flask Ver 1.1.1
* __style:__
  * __python:__ PEP 8 (v. 1.7.0)


<img src="https://github.com/jarehec/AirBnB_clone_v3/blob/master/dev/hbnb_step5.png" />

## Installation Guide

Use the package manager pip to install all needed packages for BuddySystem. Install if not currently installed

```bash
sudo python -m pip install –upgrade pip
sudo pip3 install update
sudo pip3 install flask
sudo pip3 install flask-bootstrap
sudo pip3 install flask-moment
sudo pip3 install flask-wtf
sudo pip3 install flask-sqlalchemy
sudo pip3 install flask-migrate
sudo pip3 install flask-mail
```


---

### Web Server Gateway Interface (WSGI)
The python code for the WSGI is listed in the `/wsgi/` directory.  These python files run the designated Flask Application.

## SQLAlchemy DB Setup
Packages needed for installation already installed. Current Structure of Database
Role -> User -> UserInfo
- Create SQLAlchemy DB in flask shell
- Commit session at initial creation
- Migrate when new catagory is added added and upgrade

## How to Run
Ensure that port 5000 is free on machine and run the following commands:

```bash
export FLASKAPP=buddysystem.py
export FLASK_DEBUG=1
flask run
```
This starts the Flask application web server with the file that contains the application instance. We also want to execute in debug mode when testing

## Testing

### `unittest`

This project uses python library, `unittest` to run tests on all python files.
All unittests are in the `./tests` directory with the command:


## Authors

* Brittney Rene Goertzen, [@FibonacciRene](https://github.com/renefibonacci660)

## Additional Info
* For demonstration of functional application please click [here](https://www.youtube.com/watch?time_continue=5&v=_ymOdU2qMn0)
* For a blogpost detailing the creation of this MVP please click [here](https://www.linkedin.com/pulse/foundation-buddysystem-brittney-rene-goertzen)

## Next Iteration Plans for BuddySystem
This is the MVP of BuddySystem & will continue to be updated. In order these are the next steps to be implemented;
* Deployment on public URL
* Addition of SSL Certifications
* Utilizing Google SMTP server for user email authentication
* Password and email reset priveleges
* Username deletion
* Displaying a 'To' and 'From' address box for users
* Displaying Google Maps API results on User Page
* Implementing Messaging System
* Post Board of requested user walks
* Display of walks in the area on Map

## Main Resources
* Steven Garcia (Mentorship) [@stvngrcia](https://github.com/stvngrcia)
* Flask Web Development by Michael Grinberg

## License
To the extent possible under law, Rene Goertzen has waived all copyright and related or neighboring rights to this work at the present time. Change is subject to notice
