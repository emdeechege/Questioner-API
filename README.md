# Questionaire API

Crowd-source questions for a meetup. Questioner helps the meetup organizer prioritize questions to be answered. Other users can vote on asked questions and they bubble to the top or bottom of the log.

Badges
----------------
[![Build Status](https://www.travis-ci.org/emdeechege/Questionaire-API.svg?branch=develop)](https://www.travis-ci.org/emdeechege/Questionaire-API)
[![Coverage Status](https://coveralls.io/repos/github/emdeechege/Questionaire-API/badge.svg)](https://coveralls.io/github/emdeechege/Questionaire-API)
[![codecov](https://codecov.io/gh/emdeechege/Questionaire-API/branch/develop/graph/badge.svg)](https://codecov.io/gh/emdeechege/Questionaire-API)
[![Maintainability](https://api.codeclimate.com/v1/badges/ffd17ba2407696810c0d/maintainability)](https://codeclimate.com/github/emdeechege/Questionaire-API/maintainability)
![](https://img.shields.io/github/license/emdeechege/Questionaire-API.svg)


Summary
--------
Questioner allows the meetup organizer to prioritize questions to be answered. Users vote on asked questions, and they bubble to the top or the bottom of the log.

Find the UI [here](https://github.com/emdeechege/Questioner/tree/gh-pages)

This project is managed using a pivotal tracker board. [View the board here](https://www.pivotaltracker.com/n/projects/2235156)

Find the documentation [here](https://documenter.getpostman.com/view/5550526/RznHGwbr)

[![Website](https://www.herokucdn.com/deploy/button.png)](https://uniquequestioner.herokuapp.com)

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/71ff9e20905a7f90c3a6)

Pre-requisites
----------------------
1. Python3
2. Flask
3. Postman

Getting started
--------------------
1. Clone this repository
```
    https://github.com/emdeechege/Questionaire-API
```

2. Navigate to the cloned repository
```
    cd Questionaire-API
```

Installation
---------------------------------
1. Create a virtual environment
```
    virtualenv -p python3 venv
```

2. Activate the virtual environment
```
    source venv/bin/activate
```

3. Install git
```
    sudo apt-get install git-all
```

4. Switch to 'develop' branch
```
    git checkout develop
```

5. Install requirements
```
    pip install -r requirements.txt
```
Run the application
---------------------------------
```
    python3 run.py
```

When you run this application, you can test the following API endpoints using postman
-----------------------------------------------

| Endpoint | Functionality |
----------|---------------
POST/meetups | Create a meetup record
GET/meetups/&lt;meetup_id&gt; | Fetch a specific meetup record
GET /meetups/upcoming/ | Fetch all upcoming meetup records
POST /questions | Create a question for a specific meetup
PATCH /questions/&lt;question_id&gt;/upvote | Upvote (increase votes by 1) a specific question
PATCH /questions/&lt;question_id&gt;/downvote | Downvote (decrease votes by 1) a specific question
POST /meetups/&lt;meetup_id&gt;/rsvps | Create RSVP

Acknowledgements
--------------------------------
1. Andela Workshops
2. Team 8
