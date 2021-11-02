# NPS Info Center

A Flask based web application that allows users to find parks based on activities, search for parks, and learn more information about them. 

# Website
You can see the web application in action in the following link: 
https://npsinfocenter.herokuapp.com/

## Description

As a submission for the Capital One Winter Cohort, this project aims at giving clients the most ease when trying to learn more about the National Parks in the United States and what types of activities people participate in from boating to camping. This web application provides an easy to use interface along with a sophisticated backend system to allow more optimal efficiency. The actual app itself features a home page that displays a slideshow of features, a page titled "Find Parks by Activity" that allows users to search through a list of 70+ activities from the National Park Service and find parks that provide that particular activity, and a page titled "Find Parks" that allow users to search from over 400 parks within the app alone. 

## API Used
This project uses the National Park Service API that allows clients to obtain information such as parks, activities, webcam data, and much more. The link can be [accessed here!](https://www.nps.gov/subjects/developer/api-documentation.htm)

## Tech Stack
At its core, this web app is built using Python, Flask, BootStrap, JavaScript, and the Jinja2 web templating engine. Flask was used due to its full compatability with Python code and its efficient routing and full-stack development capabilities. BootStrap was used in order to develop reusable code that can be used for other projects or systems. JavaScript, specifically JQuery, was used to implement the search feature since it is efficient and works well with HTML markup. Finally, the Jinja2 web templating engine was used to achieve logic on the front-end without using too much JavaScript, which allowed for higher degrees of code maintanance and readability. This web application was deployed on Heroku due to its Python compatability and cloud architecture. 

## Testing
The Python code that parses the API data and sends it to each endpoint has 100% code coverage, achieved by Python based unit testing. This ensures that the logic for obtaining the data critical for the web app is not flawed. 

## Getting Started

### Dependencies

A 'requirements.txt' file is located at the root of the directory, and it contains all the Python modules necessary to initiate the development of this project. 

### Installing

* One can enter the following command into their terminal, VSCode terminal, PyCharm terminal, etc to clone this repository to their local machine: https://github.com/rayb26/CapitalOneSummitProject.git
* Also, one needs to obtain a free National Park Service API key [here!](https://www.nps.gov/subjects/developer/get-started.htm)
* After, a folder will be created called CapitalOneSummitProject, which will then be accessible. 
* One needs to change the following line in api/nps_api_functions.py file, "api_key = os.environ['KEY']" to "api_key = your_api_key" or you can store your National Park Service API key as an environment variable. 

### Executing program

* To execute the program, make sure you are in your root folder of the project. 
* If you are in PyCharm or any other IDE, attempt to locate your "run" button. If you cannot find it, please consult online documentation regarding the "run" button on your IDE. Make sure you are running the "main.py" file. 



## Authors

Rayhan Biju || 
[LinkedIn](https://www.linkedin.com/in/rayhanbiju/)

