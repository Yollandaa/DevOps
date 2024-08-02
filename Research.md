# Code Review Research
1. Does routes belong in scripts folder or its own?
- **Personal or Team Preference**: Ultimately, the choice between placing routes in the scripts folder or their own dedicated folder comes down to personal or team preference. Some teams might prefer keeping everything related to HTTP request handling (including routes and possibly view functions) together, while others might want to separate business logic, data access layers, and HTTP handling for clarity.
- We've decided to keep the routes folder in the scripts.


2. Where do we need an __init__.py file?
- The ```__init__.py``` file in Python serves several purposes, primarily related to package initialization and namespace management.
- Using the application Factories (https://flask.palletsprojects.com/en/3.0.x/patterns/appfactories/) it seems where __init__ is, is appropriate.
- The __init__.py file serves as the entry point for the package, allowing other modules within the app directory (or subdirectories) to be imported as part of the package.
- The presence of a main.py file outside the app directory project uses an application factory pattern, where main.py creates and configures the Flask application by calling the create_app() function defined in app/__init__.py.


3. Draw graphs for ap to live in different env e.g. cloud vs on prem


## On-Premises Deployment Architecture


```plaintext
+-----------------------+          +--------------------------+
|                       |          |                          |
|  On-Premises Data     |          |   On-Premises Data       |
|     Center            |          |      Center              |
|                       |          |                          |
|  +-----------------+  |          |    +-----------------+   |
|  | Load Balancer   |  |          |    | Load Balancer   |   |
|  +--------+--------+  |          |    +--------+--------+   |
|           |            |          |             |           |
|           |            |          |             |           |
|  +--------v--------+  |          |    +---------v---------+ |
|  |  Flask App      |  |          |    |   Flask App       | |
|  |  (Dockerized)   |  |          |    |   (Dockerized)    | |
|  +--------+--------+  |          |    +---------+---------+ |
|           |            |          |             |           |
|           |            |          |             |           |
|  +--------v--------+  |          |    +---------v---------+ |
|  |  Local Storage   |  |          |    |  Local Storage     | |
|  |  (JSON Files)    |  |          |    |  (JSON Files)      | |
|  +--------+--------+  |          |    +---------+---------+ |
|           |            |          |             |           |
|           |            |          |             |           |
|  +--------v--------+  |          |    +---------v---------+ |
|  | External API    |  |          |    | External API      | |
|  +-----------------+  |          |    +-------------------+ |
|                       |          |                          |
+-----------------------+          +--------------------------+
```
- **Load Balancer**: Manages traffic to the Flask app instances.
- **Flask App (Dockerized)**: The application containerized for consistent deployment.
- **Local Storage (JSON Files)**: Stores additional product data in local JSON files.
- **External API**: Provides initial product data (fakestore).

## Cloud Deployment Architecture

```plaintext
+-----------------------+          +--------------------------+
|                       |          |                          |
|     Cloud Provider    |          |       Cloud Provider     |
|                       |          |                          |
|  +-----------------+  |          |    +-----------------+   |
|  | Load Balancer   |  |          |    | Load Balancer   |   |
|  +--------+--------+  |          |    +--------+--------+   |
|           |            |          |             |           |
|           |            |          |             |           |
|  +--------v--------+  |          |    +---------v---------+ |
|  |  Flask App      |  |          |    |   Flask App       | |
|  |  (Dockerized)   |  |          |    |   (Dockerized)    | |
|  +--------+--------+  |          |    +---------+---------+ |
|           |            |          |             |           |
|           |            |          |             |           |
|  +--------v--------+  |          |    +---------v---------+ |
|  |  JSON Storage   |  |          |    |  JSON Storage     | |
|  |  (e.g., S3)     |  |          |    |  (e.g., S3)       | |
|  +--------+--------+  |          |    +---------+---------+ |
|           |            |          |             |           |
|           |            |          |             |           |
|  +--------v--------+  |          |    +---------v---------+ |
|  | External API    |  |          |    | External API      | |
|  +-----------------+  |          |    +-------------------+ |
|                       |          |                          |
+-----------------------+          +--------------------------+
```
- **The Load Balancer** distributes incoming traffic to multiple instances of the Flask app to ensure high availability and reliability.
- **Flask App**: The core application containerized using Docker for consistent deployment across environments.
- **JSON Storage**: Stores the additional data fetched from the external API and any updates made to it. In a cloud environment, this could be a service like S3. In an on-premises environment, it could be local file storage.
- **External API**: The fakestore data.

### Explaination
- The load balancer receives incoming requests and routes them to one of the flask app instance. The flask instances then fetches the data from the external API, and store additional data in the JSON file. The flask instances also handles the CRUD operations. The JSON storage updates the file based on the CRUD operations. The External API provides the initial data.


4. Look at O(n) time complexity
- O(n) time complexity denotes that the execution time of an algorithm grows linearly with the size of the input data. This means that if the input size doubles, the execution time will approximately double as well. It's characterized by operations that iterate over each element in the input once.


5. Research absolute vs relative paths
    ###   **Absolute path** 
    - specifies the exact location of a file or directory starting from the root directory of the file system. It uniquely identifies a file or directory regardless of the current working directory. e.g., ```C:\Users\Username\Documents\file.txt```
    - Usage: Absolute paths are used when you need to specify the exact location of a file or directory, especially when referencing files from different machines or environments where the relative path might not be valid.

    ### **Relative path**
    - describes the location of a file or directory relative to the current working directory. It does not start from the root directory. e.g., 
    ```./subfolder/file.txt```
    - Usage: Relative paths are convenient for navigating within a project or when the script's execution location may change. They are particularly useful in scripting and development environments where the working directory might differ across executions.
