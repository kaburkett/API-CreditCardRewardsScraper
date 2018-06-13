# Credit Card Rewards Scraper API

This api scrapes credit card websites to pull down the monthly rewards and return them as a json object.

## Technologies Used

This project uses

* Selenium: for web scraping (grab the text from websites)
* Falcon: the lightest weight python api framework I could find
* Venv: linux virtual environment to maintain easily deployable container
* Gunicorn: run the falcon api locally

## How to use

Run python app on webserver, then make a get request to /

    http.get('yourwebserver/').response(success=>{
        console.log(success);
    }.error=>{
        console.log(error);
    }

    //output
    {
        "Discover":"Home Improvement",
        "Citi":"Gas Stations"
    }

## App Requirements

I've saved the dependencies to requirements.txt, so quickly install all python requirements with pip install -r requirements.txt

Developed using the following versions:

* Python: 3.6
* Pip: 10.0.1
* Firefox: 60.0.2
* Gunicorn: 19.8.1

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
    (venv) $ gunicorn -b 0.0.0.0:80 main:app 

Now the api should be running on localhost!