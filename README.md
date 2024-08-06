# FakeAPI

![Static Badge](https://img.shields.io/badge/Current_Version%3A-v1.0-blue)


## Table of Contents
- [Title and Description](#title-and-description)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Environmental Variables](#environmental-variables)
- [Project Spec](#project-spec)
- [To Run The Project](#to-run-the-project)

## Title and Description
FakeAPI is an API service that uses data from [Fake Store API](https://fakestoreapi.com/). This project provides endpoints to get users, products, and carts, which can be tested using Postman or other API testing tools. The API is designed to facilitate CRUD operations and is configured to be deployed in a DevOps environment.


## Usage

## Installation
To install FakeAPI, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Yollandaa/DevOps.git
   ```

## Contributing

1. Contact project admin to be added to the project
2. Create a new branch
3. Edit new branch as necessary
4. Commit code
5. Create a pull request with an administrator for approval

## Environmental Variables

## Project Spec
### Main goal:
 
1. Develop an API using Python and Flask for a DevOps environment.
2. API needs to facilitate CRUD operations
3. API will be using fake data from github repo

### Tech Specifications:
1. Use python to create the API according to Flask framework
2. Use branching strategies
3. URL links for API needs to be parameterized and have multiple versions to replicate DEV, PPE, PRD scenarios
4. Autoconfig for environmental variables (from decouple import AutoConfig)
5. Make the app as modular as possible using custom made libraries and functions

- autoConfig library takes the data from the .env 

## To Run The Project
``` sh
// cd to DevOps folder
// pip install -r requirements.txt
// cd src
// run the command
python main.py
```

