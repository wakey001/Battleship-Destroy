# Card 
* [insert ami]()
# Goal for this project
* This project will be a python terminal battleship game where the player will face the computer.
The player gets 10 turns to find all randomly placed ships on a 2d style grid. The player finds the ships by entering the row and column co-ordinates as numbers. The game ends when either the turns are used up or the player hits all the computers ships. 
# Table of Contents
* [UX](#ux "UX")
    * [User Goals](#user-goals "User Goals")
    * [User Stories](#user-stories "User Stories")
    * [Site Owners Goals](#site-owners-goals)
    * [User Requirements and Expectations](#user-requirements-and-expectations)
         * [Requirements](#requirements)
         * [Expectations](#expectations)
    * [How to Play](#how-to-play)
    * [Wireframes](#wireframes)
    * [Features](#features)
        * [Existing Features](#existing-features)
        * [Features to be implemented](#features-to-be-implemented)
    * [Technologies used](#technologies-used)
        * [Languages](#languages)
        * [Libraries and Frameworks](#libraries-and-frameworks)
        * [Tools](#tools)
    * [Testing](#testing))
        * [Code Validation](#code-validation)
        * [Bugs](#bugs)
        * [Unfixed Bugs](#unfixed-bugs)
    * [Deployment](#deployment)
    * [Credits](#credits)

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

# Ux
## User Goals
* Know when it is the users go and not
* Clear instruction as to how to play the game
* Know the outcome of the game, win, lose or draw
## User stories
* As a user, I want to be able to personalise my game
* As a user, I want to be clearly navigated through the game
* As a user, I want to skip through game instructions if required
* As a user, I want to have continual feedback on my score
* As a user, I want to know the outcome of the game
## Site owner goals
* Make the rules clear to understand
* Have the game display the score clearly so the user can understand who is winning.
* Ensure that there is validation for expected answers on all user inputs.

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

# User requirements and expectations
## Requriements
* Clear instruction as to when the game starts and finishes
* Validation of user inputs
* Feedback to the user on their input to the game
## Expectations
* I expect to know that it is my game based on a username
* I expect to know when the game starts and finishes
* I expect to have the option of reading the rules or not
* I expect not to be able to make any typing errors
# How to play
The user is prompted for their name, this is then shown above there board. They are then asked which row they would like to guess, row and column and also the number of turns is displayed. The user is then told if they hit or missed the computers ships and told of thier turns remaining, and subsequently told if they try to use the same co-ordinates later on. If the user hits all the ships they win, and the game is over, it is also over if they run out of turns.

## Wireframes

## Existing features
* 
## Features to be implemented
*

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

# Technologies used
## Languages
* [HTML](https://en.wikipedia.org/wiki/HTML5) for the structure of the site
* [CSS](https://en.wikipedia.org/wiki/CSS) for the design of the site
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript) was built into the template supplied by Code Institute
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) for the game code
* [Markdown](https://en.wikipedia.org/wiki/Markdown) for the content in my README file
## Libaries and frameworks
* Import Random, for selecting a random card from the deck python random library
## Tools
* For construction [Gitpod]()
* For wireframes [Balsamic](https://balsamiq.com/wireframes/)
* For python validation [PEP8 online](http://pep8online.com/)
* For HTML validation [W3C HTML Validation Service](https://validator.w3.org/)
* For CSS validation [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
* For python code validation [PEP8 online](http://pep8online.com/)
* For general code queries [W3Schools](https://www.w3schools.com/)
* For spell checking [Grammarly](https://www.grammarly.com/?&utm_source=google&utm_medium=cpc&utm_campaign=10531689996&utm_targetid=aud-332195722204:dsa-915389969968&gclid=CjwKCAiArOqOBhBmEiwAsgeLmf6WBpNM8xWU9Gif_6buwExECbE12BjfjeGQ3iyruQf4xasnRCJfZxoCW6QQAvD_BwE&gclsrc=aw.ds)

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

# Testing
## Code validation
## Bugs

* One of bugs I had was when guessing a co-ordinate eg row 1 column 1, the - sign used to display a miss on the board would move the existing O over one place. Instead of the grid being a 8x8 that particular row would become a 9.

* As it appeared to be to do with the miss part of the code i narrowed it down by changing the symbol to a backslash as there were two pieces of code with misses. The bug had not changed and so was obvious it was the other line with the - part once a miss had been logged.
Once focused on that line of code it was then quite obvious that I had put space around the - so instead of "-" I had put " - ". I simply deleted the code.

* This then fixed the problem and the miss then logged the "-" as it should have. And did not displace the grid anymore.



## Deployment
The site was deployed via Heroku. Here is the live link - []()

The project repository was created using the *Code-Institute-Org/python-essentials-template* on GitHub and edited using GitPod.

### Deployment via Heroku
* Visit [heroku.com](https://www.heroku.com/home "Heroku")
* Create a new account or sign in
* From the dashboard, select **New** and then **Create new app**
* Enter an individual app name into the text box, select a region from the dropdown and then press **Create app**
* A Heroku app has now been created and the **Deploy** tab is opened. 
* Select the **Settings** tab
* Click on the **Reveal Config Vars** button
* In the textbox with KEY as the placeholder, enter *CREDS*
* In the textbox with VALUE as the placeholder, enter the content from the creds.json file and press **Add**
* In the textbox with KEY as the placeholder, enter *PORT*
* In the textbox with VALUE as the placeholder, enter *8000*
* press **Add**
* In the buildpacks section of the settings tab, click on **Add Buildpack**, select **python** and then save changes
* Click on **Add Buildpack** again, select **node.js** and then save changes
* When they are on the dashboard, ensure that python is above node.js on the list
* Open the **Deploy** tab
* In the deployment method section, select **GitHub** and confirm the connection.
* Enter the repo-name into the text box and click **Search**. When the correct repo appears below, click **Connect**
* In the Automatic deploys section, click **Enable Automatic Deploys**. This updates every time GitHub code is pushed
* To complete the process click on the **Deploy Brach** button in the Manual deploy section, this will take a few seconds to complete while Heroku builds the app
* A message will appear informing you that the app was successfully deployed and a **View** button will bring you to the live site


## Credits