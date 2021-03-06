[![Coverage Status](https://coveralls.io/repos/github/Teddykavooh/Ride-My-Way-Project/badge.svg?branch=apiv2)](https://coveralls.io/github/Teddykavooh/Ride-My-Way-Project?branch=apiv2)
[![Build Status](https://travis-ci.org/Teddykavooh/Ride-My-Way-Project.svg?branch=apiv2)](https://travis-ci.org/Teddykavooh/Ride-My-Way-Project)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
# ***Ride-My-Way***
***
![Home Image](https://raw.github.com/Teddykavooh/Ride-My-Way-Project/apiv2/2.jpg)

* Ride-my App is a carpooling application that provides drivers with the ability to create ride oﬀers and passengers to join the available ride oﬀers.
## Getting Started
1. Clone the repository to your machine;
    *https://github.com/Teddykavooh/Ride-My-Way.git
2. Open the repo with an IDE of your choice as a project.     
## Prerequisites
* Python 3
* Virtual environment.
* Flask
* flask rest-plus
* Postman
* Browser of your liking 
## Setup
1 Open cmd. In the root directory folder;
* Run the command: virtualenv venv,  to create a virtual <br/>
 environment with the name venv. Folder with the name venv will <br>
 created.
* Activate the virtual environment by moving to the Script directory i.e. cd venv\Scripts, and running <br>
activate.
* Create a database as per the database.ini file.

## Application Requirements
* The application requirements are clearly listed in the ***requirents.txt*** document.
   * To install them run the following cmd command:
     * pip install -r requirements.txt
   * Run the command: 'python run_my_tables.py' to create the necessary tables.  
## End-Points
|Requests     |   EndPoint                          | Functionality
|:-----------:|:-----------------------------------:|:--------------:
   GET        |  api/v2/rides                       | Get all Rides 
   GET        |  api/v2/rides/{ride_id}             | Get a specific ride
   DELETE     |  api/v2/rides/{ride_id}             | Delete ride          
   POST       |  api/v2//rides                      | Add a ride                  
   POST       |  api/v2/rides/{ride_id}/requests    | Request to join a ride
   PUT        |  api/v2/rides/{ride_id}             | Edit ride details
   POST       |  api/v2/users                       | Register users
   POST       |  api/v2/users/login                 | Login user                       
   DELETE     |  api/v2/users/{username}            | Delete a user
* The above endpoints can be tested by Postman.

## Running Of Tests
* Running of tests can be done by unittest.
* To run tests, run the following command in cmd:
    * coverage run -m unittest
* A test report can be acquire by the ***coverage report*** cmd command.
* Finally a better view can be acquired by the ***python -m http.server*** cmd command.

## Version Control
* This was done by GitHub

## Github link
* https://github.com/Teddykavooh/Ride-My-Way-Project/tree/apiv2

## Pivotal Tracker link
* https://www.pivotaltracker.com/n/projects/2177587

## Heroku
* https://ride-my-way-project-apiv2.herokuapp.com/api/v2/documentation

## Author
* Antony Kavoo

## License
* This project is licensed under the MIT License - see the LICENSE file for details

## Acknowledgement
* Great appreciation to everyone who assisted in willing this project to its current glory.Thank you.

![Home Image](https://raw.github.com/Teddykavooh/Ride-My-Way-Project/apiv2/1.jpg)
