# Credit Card Rewards Scraper API

This api scrapes credit card websites to pull down the monthly rewards and return them as a json object.

## Technologies Used

This project uses

* Selenium: for web scraping (grab the text from websites)
* Falcon: the lightest weight python api framework I could find
* Venv: linux virtual environment to maintain easily deployable container
* Gunicorn: run the falcon api locally
* Sqlite: storing the categories

## How to use

fetch_categories.py should be ran every week with a cronjob to update the sqlite database (this gives us a faster response because it prevents the selenium test from running on each request as the test takes a few seconds to complete).

Run python app on webserver, then make a get request to /rewards

    http.get('yourwebserver/rewards').response(success=>{
        console.log(success);
    }.error=>{
        console.log(error);
    }

    //output
    [
        [1, "Discover", "it", "Grocery Stores"],
        [2, "Citi", "Simplicity", "Home Furnishing Stores"]
    ]

## App Requirements

I've saved the dependencies to requirements.txt, so quickly install all python requirements with pip install -r requirements.txt

Developed using the following versions:

* Python: 3.6
* Pip: 10.0.1
* Firefox: 60.0.2
* Gunicorn: 19.8.1
* Sqlite: 3

## Install guide

    $ apt-get install virtualenv
    $ git clone https://github.com/kaburkett/API-CreditCardRewardsScraper.git
    $ cd API-CreditCardRewardsScraper/falcon_api
    $ virtualenv venv -p /user/bin/python3
    $ . ven/bin/activate
    (venv) $ apt-get install build-essentials python3-dev
    (venv) $ pip install cython
    (venv) $ pip install --no-binary :all: falcon
    (venv) $ pip install gunicorn
    (venv) $ gunicorn -b 127.0.0.1:8080 main:app 

Now the api should be running on localhost:8080!

## Additional Info

Great write up on running falcon apps with gunicorn: https://www.digitalocean.com/community/tutorials/how-to-deploy-falcon-web-applications-with-gunicorn-and-nginx-on-ubuntu-16-04
