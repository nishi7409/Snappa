[![CodeFactor](https://www.codefactor.io/repository/github/nishi7409/snappa/badge)](https://www.codefactor.io/repository/github/nishi7409/snappa)
[![Netlify Status](https://api.netlify.com/api/v1/badges/21ca5d11-14f6-4ebb-a537-fa5c2a5a5524/deploy-status)](https://app.netlify.com/sites/snappa-rpi/deploys)
<h1 align="center">🥤🎲 All Things Snappa 🎲🥤</h1>
<!-- <p align="center">
    <img width="460" height="300" src="http://www.fillmurray.com/460/300">
</p> -->

## Developers
- Nishant Srivastava
- Vincent Chen
- Christopher Ng
- Joseph Xiao
- Soorya Pari

## Vision Statement
<b>Problem Statement</b>
<br>
Throughout college campuses around the globe, “Snappa” is a popular game played by close friends and family that stimulates fast reflexes and fine motor skills. The problem found between both casual and competitive Snappa players is there is no real application that can guide their games while feasibly tracking and documenting their performance as they play games. There also does not exist an application that creates a fantasy league based on Snappa to compete with your friends as well. To best serve this growing problem, we will be developing a web application that will be used for all things Snappa such as a guide on how to play, ease of use user-inputted statistic-tracking, personalized statistics for each user, a league creation so that your friends can join a structured competition and a fantasy Snappa portion as well.

<b>Proposed Solution</b>
<br>
Our new and interactive web application will contain user-friendly features that would allow the users to easily track and publicly or privately display their information to the world or friends and family. The application will also contain a practical user-inputted statistic tracking system to help keep track of statistics, a personalized user statistic page that holds tables and charts mapping the statistics of a user, and a league creation section where users can sign up to play with their friends in a structured competition.

## Diagrams
### Sequence Diagram
https://drive.google.com/file/d/1o_fpSizzXChjeOOFMZjfQ919NSruJgVp/view
### Static Class Diagram
https://drive.google.com/file/d/1tptG2AVWkjq09E9yjmtcZ7dh78kLUUBI/view
### 

## Developmental Setup
### Frontend
1. Install the latest version of [Node.js](https://nodejs.org/en/)
2. Confirm the installation of Node.js by running `node -v` in a terminal of your choice (ie: command prompt)
3. Confirm the installation of **npm** by running `npm -v` in a terminal of your choice (ie: command prompt)
4. You should *theoretically* be on the latest version of `npm`, but you could run the following line `npm install -g npm` (optional)
5. `cd` to `/frontend/`
6. Run `npm install` to install all packages found in `package.json`.
7. Finally, run `npm run serve`
8. You should see something similar to [this](https://prnt.sc/1vmlcou), visit the local link on your preferred browser

### Backend
1. Install the latest version of [Python](https://www.python.org/downloads/)
2. Type `python` (or `python3`) in a terminal of your choice (ie: command prompt)
3. `cd` to `/server/`
4. Run `pip install -r requirements.txt`
5. Run `python manage.py makemigrations` (if python doesn't exist, try `python3`)
5. Run `python manage.py migrate` (if python doesn't exist, try `python3`)
5. Run `python manage.py runserver` (if python doesn't exist, try `python3`)
