# Metacognitive Prompting

This notebook project serves as an implementation of the research paper titled "Violation of Expectation via Metacognitive Prompting Reduces Theory of Mind Prediction Error in Large Language Models" authored by Courtland Leer, Vincent Trost, and Vineeth Voruganti. The project aims to explore the concept of violation of expectation and its impact on reducing theory of mind prediction error in large language models. By leveraging "metacognitive prompting" – the authors' proposed framework for implementing VoE in an AI tutor – the project seeks to enhance the understanding of how these models interpret and respond to user inputs, particularly in the context of conversational interactions. Through the integration of artificial intelligence techniques, linguistic analysis, prompt engineering techniques and the practical implementation of psychological concepts and frameworks, the project provides insights into user engagement, conversational flow, and thematic consistency. Additionally, the implementation incorporates predictive coding theories to improve the accuracy of user input predictions. The project utilizes MongoDB for storing conversational data and integrates with the OpenAI API for generative capabilities.

## References

Leer, C., Trost, V., & Voruganti, V. (2023). "Violation of Expectation via Metacognitive Prompting Reduces Theory of Mind Prediction Error in Large Language Models". ArXiv preprint [arXiv:2310.06983](https://arxiv.org/abs/2310.06983)

## Installation Guide

Follow these steps to set up and run the project:

1. Set up Environment Variables:
   - Create an `.env` file in the project root directory.
   - Use the provided [`.env.example`](https://github.com/rokussadee/OpenAPI_metacognitivePrompting/blob/feat/chatbot_chat-loop/.env.example) file as a template and fill in the necessary environment variables.

2. Install Dependencies:

   Use the dependency manager [poetry](https://python-poetry.org/) to install Metacognitive Prompting.
   - Run the following command to install project dependencies using Poetry:
     ```
     poetry install
     ```

3. Set up MongoDB Database:

    It's possible to use a local MongoDB instance using cli-tools like `mongod` and `mongosh`.
   <details>
   <summary>In this case, follow the steps below.</summary>
   
   - Set the ```DB_ENV``` environment variable to "development"
   - Ensure MongoDB is installed on your system.
   - Start the MongoDB daemon by running `mongod`.
   - Open another terminal window and enter the MongoDB shell by running `mongosh`.
   - Create an admin user with appropriate privileges using MongoDB commands.
   
   ```javascript
      use admin // enter the "admin" database
      > db.createUser(
        {
          user: "mongo-admin",
          pwd: passwordPrompt(), // Or "<cleartext password>"
          roles: [ { role: "userAdminAnyDatabase", db: "admin" },
                   { role: "readWriteAnyDatabase", db: "admin" }
                 ]
        }
      )
      ```

   - Restart the MongoDB daemon with the login details for authentication.
   
   ```bash
    mongod --auth --port 27017 --dbpath ~/mongo-data/db
    ``` 
   
   - Restart the MongoDB shell with the login details for authentication.
   ```bash
    mongosh --port 27017 --authenticationDatabase "admin" -u "auth_username" -p
   ```
   
   </details>

   Otherwise, set up a remote mongodb database on the web portal and change the `.env` file with the corresponding MongoDB credentials and set the `DB_ENV` variable to an empty value. Refer to the [mongo_service](https://github.com/rokussadee/OpenAPI_metacognitivePrompting/blob/feat/chatbot_chat-loop/services/mongo_service.py) file to see how these connections are made depending on the database setup.


4. Start Jupyter Server:
   - Run the following command to start the Jupyter server:
     ```
     jupyter notebook
     ```

5. Run Notebook:
   - Open the provided Jupyter notebook in your web browser.
   - Run all cells in the notebook to execute the project code and view the results.
   - Take a look at the `DEBUG_MODE` environment variable; if set to 'true', debug print statements are appended to the output. 
   - Running all cells will start the conversation loop, after which user input can be submitted.

## Project Structure

### Services Package

The `services` package contains external tools and repetitive business logic that are not the primary focus of the notebook. It includes the following submodules:

**Mongo Service**

The `mongo_service` submodule provides functionalities related to MongoDB connection and interaction. It includes methods for establishing a connection to the MongoDB database, querying data, and performing CRUD operations.

**Prompt Builder Service**

The `prompt_builder_service` submodule is responsible for setting up prompts to pass to the OpenAI API. It includes templates for constructing prompts based on user inputs, conversation history, and other contextual information.

**Mock Service**

The `mock_service` submodule contains mock data values for unfinished functionalities. It provides dummy data to simulate real-world scenarios and test various components of the application without relying on actual external services or databases.

### Utils Package

The `utils` package includes common functions. It contains the following submodules:

**Model Operations**

The `model_operations` submodule contains common functions for performing CRUD operations on model data stored in the MongoDB database. It provides an abstraction layer that encapsulates the database interaction logic, making it easier to work with model data within the notebook.

**Helpers**

The `helpers` submodule includes utility functions that assist in various tasks throughout the application. These functions provide general-purpose functionalities such as data validation, formatting, and transformation.

### Models Package

The `models` package consists of model files with model-specific functions (not object-oriented programming). Each model file contains functions related to a specific data model or entity within the application. These functions perform operations such as data retrieval, manipulation, and transformation specific to the corresponding model.


[MIT](https://choosealicense.com/licenses/mit/)