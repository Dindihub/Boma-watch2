## Django Template

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/GB6Eki?referralCode=U5zXSw)
# iBoma

## Description

This Application is a neighbourhood watch website that allows users to sign up and join neighbourhoods of their choice. They can create new neighbourhoods,customize their profiles,add business and random posts visible to others in their neighbourhoods.


## Author

Sandra 

You can view the site at:[iBoma]()


## User Stories
As a user I would like to:
* See various neighbourhoods and their details  
* Join various neighbourhoods 
* Allowed to Register up and Login 
* Allowed to search and create businesses
* Allowed to create a neighbourhood
* Allowed to post random posts and businesses details


## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display of neighbourhood | **On page load** | List of various neighbourhoods on site displayed on a page|
| Search for business| **On search bar click submit** | search for businesses |
| sign up | **On signin** | allowed to sign in and view neighbourhoods details|
| Create profile | **on signup and login** | update profile with details|
| Join neighbourhoods | **On log in** |  see posts and Ads from a neighbourhood|
| Create  new neighbourhoods | **On log in** |  display all neighbourhoods|
|Create random post | **on sign in** | create posts
|post business adverts | **on sign in** | business ads displayed in each hood|


## SetUp / Installation Requirements
### Prerequisites
* python3.8
* pipenv


### Cloning
* In your terminal:

        $ git clone git@github.com:Dindihub/Boma-watch.git
        $ cd boma-watch

## Running the Application
* Creating the virtual environment

        $ pip3 install pipenv 
        $ pipenv shell
        
       


* To run the application, in your terminal:

        $ python3.8 manage.py runserver
        

## Testing the Application
* To run the tests for the class files:

        $ python3.8  manage.py tests 

## Technologies Used
* Python3.8
* Django 4.0.4
* Heroku

## Known Bugs
Only search for businesses
May not be responsive on small devices

### License
MIT (c) 2022 **[Sandra Dindi](https://github.com/Dindihub/Boma-watch.git)**

