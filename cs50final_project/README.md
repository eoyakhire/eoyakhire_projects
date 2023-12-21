---
files: [app.py]
url: 
---

# Final Project: Break the Internet

For my final project, I created a web application that builds off of the website I created in Problem Set 8: Homepage. However, I added more features that allow for more user interaction and fixing the bugs of the previous website.


## Background

My website from Problem Set 8: Homepage was all about the user getting to know me through my interests in fashion and style in the Y2K era. I had a tab where users could see my vision board, past nail designs, and drop down features to display my favorite artists’ songs. Additionally, user’s could type their favorite thing about the Y2K era in a text box and submit. It contained an about section that included the mission statement and information about myself and my self-discovery journey in fashion.

In this new website users are encouged to will encourage young girls, women, femmes, and womanhood-identifying individuals, especially of color, to have a space to unload their creativity and to see themselves in a world that often tries to blind them.

This website will use languages and computer files such as Python, CSS, JavaScript, HTML, and Flask.

### Running Break the Internet

Start Flask's built-in web server (within `final_project/`) by entering into the directory:

$ cd final_project

```
$ flask run
```

#### Creating a database

In order for me to implment a user register/log in feature I created an SQL data similar to the one used in Problem Set 9: Finance.
If you would like to see the amount of users or access the database within `final_project/`, run `sqlite3 finance.db` to open `finance.db` with `sqlite3` and run .
`.schema` in the SQLite prompt to access a table called `users`. In 'users' you will see that there are 3 columns, username (a user's username for their account), hash (the user's password that is hashed for security), and diary (user's diary entry that is stored).

#### `app.py`

This python file contains numerous imports that allow for many of the functions and routes to be executed. Many include as `check_password_hash` to compare hashes of users' passwords and the use of session to remmeber that a user is logged in. by storing that person's user_id in a session. Many of the routes are created in order to direct the user to that specific html page through the render_template() function such as @app.route("/more"), @app.route("/logout"), and @app.route("/register", methods=["GET", "POST"]). Some of these routes use GET and POST and the db.execute to query `finance.db` so that way I am able to insert or select data needed like in login and register.


#### `helpers.py`

This python file contains two functions (technically three because apology contains another inside of it called escape). One called apology that helps to create and render an aoplogy to the user. This becamed very useful when alreting the user of errors when trying to store their information into the database and is credited to Github (https://github.com/jacebrowning/memegen). Additionally, it contains the function is `login_required` whereby a function can return another function. This function is very useful in app.py as it basically tells the computer when each template should be asscess by the user if the user is logged in and if the user tries to access a page that requires a log in it will redirect the user to the log in page.

#### `static`

Static contains the styles.css file which stores all the code that creates the aestehtic of the website from font size to background images. Additonally, it contains the images and video that I used throughout the css and index.html code.


#### `templates/`

This folder contains all the html pages: about, apology, diary, index, layout, login, and register.

## Code in app.py

### `register`

The objective of 'register' was to succesfully register a user. I did this by prompting the user to input a username, password, and a confirmation of that password whereby the user inputs their password again in order to ensure the corrrect one was entered. After the user is registered they are redirected to the log in page where they are able to log into their newly created account. This code is implmented in an html page called register.html.

It requries that a user input a username, implemented as a text field whose `name` is `username`, a password, implemented as a text field whose `name` is `password`, and password confirmation. If the user fails to input text into these fields, submits a username that is already taken, or does not input the same password as the confirmation password they are rendered an apology to inform them to change accordingly as seen in my app.py file. Once correct, their information is inserted into the database.


### `log in`

The Log In feature is essentially the same as register in terms of code and format on the website. However, it just prompts the user for their username and password. If the user fails to input the correct username or password the user is rendered an aplogy as seen in my app.py file. If logged in succesfully the user is redirected to the homepage of my site, known as index.html in the zip file and /homepage in the funtion homepage as in in my app.py file.

### `index, layout, an apology html files`

The index.html file contains code that displays the layout of the homepage once the user logs in. Once accessed the user is able to still read about the mission statement through the about page, the listen to playlists via the music tab, and create a visionboard by being redirected to a link that allows for it. Additionally, they are able to create a diary entry and of course log out of their account if they wish to. Once logged out the user is redirected to the layout.html page which is esseentially the base or introduction page of the site. This code can be found in the app.py file.


### `script.js`

This was not essential but still something I wanted to implement as a part of my homepage. The script.js file contains the JavaScript code I used in my index.html page. It contains one function that allows a user to type, submit an answer, and recieve feedback about a question I asked.