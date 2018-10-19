## StoreManager-API  :department_store:
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) [![PEP8](https://img.shields.io/badge/code%20style-pep8-green.svg)](https://www.python.org/dev/peps/pep-0008/) [![Build Status](https://travis-ci.com/kwanj-k/storemanager-API.svg?branch=ft-readme-%23161244054)](https://travis-ci.com/kwanj-k/storemanager-API) [![Coverage Status](https://coveralls.io/repos/github/kwanj-k/storemanager-API/badge.svg?branch=ft-heroku-%23161256506)](https://coveralls.io/github/kwanj-k/storemanager-API?branch=ft-heroku-%23161256506) [![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/codeclimate/codeclimate/maintainability)

## Summary

Store Manager is a web application that helps store owners manage sales and product inventory records. 

## NOTE
* The project is managed using PivotalTracker board [click here](https://www.pivotaltracker.com/n/projects/2202775)

* To see documentation [click here](https://storemanager-v1.herokuapp.com/api/v1/)

* To see API on heroku [click here](https://storemanager-v1.herokuapp.com/api/v1/)

## Getting Started 

* Clone the repository: 

    ```https://github.com/kwanj-k/storemanager-API.git```

* Navigate to the cloned repo. 

### Prerequisites

```
1. Python3
2. Flask
3. Postman
```

## Installation 
After navigating to the cloned repo;

Create a virtualenv and activate it ::

    create a directory 
    cd into the directory
    virtualenv -p python3 venv
    source venv/bin activate

Install the dependencies::

    pip install -r requirements.txt 


## Configuration

After activativating the virtualenv, run:

    ```
    export FLASK_APP="run.py"
    export FLASK_DEBUG=1
    export APP_SETTINGS="development"
    ```
## Running Tests

Run:
```
pytest --cov-report term-missing --cov=app
```

### Testing on Postman/Docs
Fire up postman and start the development server by:
  ```
  $ flask run
  ```

To use the docs [click here]( http://127.0.0.1:5000/api/v1/)

On Post man:

    Navigate to  http://127.0.0.1:5000/api/v1/


Test the following endpoints:
### Note

* A super admin can access both admin and attendant routes
* An admin can access his/her routes and attendant routes only
* An attendant can only access her routes


### Unsrestricted endpoints

| EndPoint                       | Functionality                           |
| -------------------------------|:---------------------------------------:|
| POST     /stores               | Create a store                          |
| POST     /login                | Login a user                            |


### Attendant endpoints

| EndPoint                       | Functionality                           |
| -------------------------------|:---------------------------------------:|                                                                 
| GET      /products             | Get all the products                    |
| GET      /products/Id/         | Get  a product by id                    |
| POST     /products/Id/         | Sell a product                          |
|                                                                          |

### Admin endpoints

| EndPoint                       | Functionality                           |
| -------------------------------|:---------------------------------------:|                                                                 
| POST     /attendant/           | Add a store attendant                   | 
| POST     /products/            | Add a product                           | 
| PUT      /products/Id/         | Update the information of a product     |
| DELETE   /products/Id/         | Remove a product                        |
| GET      /sales/               | Get all the the sale records            |
| GET      /sales/Id/            | Get a specific sale                     |
| PUT      /sales/Id/            | Update a specific sale                  |
| DELETE   /sales/id             | Delete a specific sale                  |


### Super Admin endpoint

| EndPoint                       | Functionality                           |
| -------------------------------|:---------------------------------------:|
| POST     /admin/               | Add an admin                            | 




## Authors

* **Kelvin Mwangi** - *Initial work* - [kwanj-k](https://github.com/kwanj-k)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

#### Contribution
Fork the repo, create a PR to this repository's develop.