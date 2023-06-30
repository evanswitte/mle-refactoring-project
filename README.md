# King County Real Estate API

This repository contains a FastAPI implementation of the King County Real Estate API. It allows users to access real estate data from King County, such as property information, prices, and locations(zipcodes), through a RESTful API.

## Prerequisites

Before running the API, make sure you have the following dependencies installed:
- Docker
- Docker Compose

## Getting Started
To get started with the King County Real Estate API, follow these steps:

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/your-username/mle-refactoring-project.git
    ```

2. Create a .env file in the project directory and provide the necessary environment variables.
    ```bash
    vim .env
    ```
    >NOTE: Make sure to update the values in the .env file according to your setup.
3. Start the application using Docker Compose:
    ```bash
    docker-compose up -d
    ```
This will start the FastAPI application and a PostgreSQL database container.

4. Wait for the containers to start up. You can check the logs using the following command:
    ```bash
    docker-compose logs -f
    ```
Once you see log messages indicating that the API is ready, you can proceed.

Access the API by opening the following URL in your web browser ```http://localhost:8000/docs```

The API documentation will be displayed, allowing you to explore the available endpoints and interact with them.


<br>

___
```
You can also use tools like cURL or Postman to make requests to the API endpoints. Refer to the API documentation for detailed information about the available endpoints and request/response formats.
```
___

<br>

5. When you're finished, you can stop the containers by running the following command:

```bash
docker-compose down
````

The necessary libraries are listed in the [requirements.txt](./requirements.txt) file. You can install them with the following command:

```bash
pyenv local 3.11.3
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
