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

## Running the app

I've saved the dependencies to requirements.txt, so quickly install all python requirements with pip install -r requirements.txt

Developed using the following versions:

* Python: 3.6
* Pip: 10.0.1