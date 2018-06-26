News Handy
===================

- - - -
Author: [Anilla Busolo](https://github.com/Anillab)
## Description
[News Handy](https://github.com/Anillab/News_Handy) is a web appliction that displays a list of news sources from around the world. A user is able to click on a news source and view a list of articles from that source. Clicking on the news article will then redirect you to the news article's web page.

------------------------------------------------------------------------

## User Requirements

1. One should see various news sources and select the ones they prefer
2. One should  see all the news articles from that news source
3. One should see the image description and time the news article was created.
4. In addition,the user should  be able to click on an article and read it fully from the news source.

## Features

+ [x] List various news sources.
+ [x] List articles from the selected news source
+ [x] Redirect user to the actual article
+ [x] Categorize news sources
+ [ ] Use flask sessions to save a users article snippet
+ [ ] Use browser cookies to store favourite news sources


## Installation

### Requirements
This project was created on a linux terminal using atom editor and coded with Python
version 3.6

### Cloning the repository
```bash
git clone https://github.com/Anillab/News_Handy.git
```

### Creating a virtual environment
```bash
sudo apt-get install python3.6-venv
python3.6 -m venv virtual
source virtual/bin/activate
```

### Installing dependencies
```bash
pip3 install -r requirements
```
The following libraries are required
* Flask==0.12.2
* Flask-Bootstrap==3.3.7.1
* Flask-Script==2.0.6



### Running Tests
```bash
python3 manage.py test
```

### Running the web app in development
```bash
python ./start.sh
```
Open the app on your browser, by default on `127.0.0.1:5000`.

<!-- ## Live Demo -->





## Technology used

* [Python3.6](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)

## Contributing

- Git clone [https://github.com/Anillab/News_Handy.git](https://github.com/Anillab/News_Handy.git) and make the changes.
- Write your tests on `tests/`
- If everything is OK. push your changes and make a pull request. ;)

## License ([MIT License](http://choosealicense.com/licenses/mit/))

This project is licensed under the MIT Open Source license, (c) [Anilla Busolo ](https://github.com/Anillab)
