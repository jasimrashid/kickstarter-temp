# twitoff-15

## Installation

Download the repo and navigate there from the command line:

```sh
git clone git@github.com:s2t2/twitoff-15.git
cd twitoff-15
```

## Setup

Setup a virtual environment and install required packages

```sh
pipenv --python 3.7
pipenv install Flask pandas numpy
pipenv shell
```



## Run the app locally

Run the web app:

```sh
FLASK_APP=web_app flask run
```

## Deploy the app to Heroku

Install the Heroku CLI
Download and install the Heroku CLI.

If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.

```sh
 $ heroku login 
 ```

Create a new Git repository
Initialize a git repository in a new or existing directory

```sh
$ cd my-project/
$ git init
```

```sh
$ heroku git:remote -a kickstarter-ds15
```
Deploy your application
Commit your code to the repository and deploy it to Heroku using Git.

```sh
$ git add .
$ git commit -am "make it better"
$ git push heroku master
```
Existing Git repository
For existing repositories, simply add the heroku remote

```sh
$ heroku git:remote -a kickstarter-ds15
```

