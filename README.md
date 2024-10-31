# Back-End Project - Movie API

This project aims to create a comprehensive API for managing movies, allowing users to perform CRUD operations on movie data, including actors, genres, reviews, and authentication. Developed using **Python** and **Django REST Framework**, the API is designed for scalability and usability. Additionally, the project leverages **Docker** to manage the PostgreSQL container, ensuring a smooth development environment.

## Technologies Used

- **Django REST Framework**: For building the API with a clear and concise structure.
- **PostgreSQL**: As the database to store movie-related data.
- **Docker-Compose**: Used to manage the **PostgreSQL** container.
- **Class-Based Views**: To facilitate code reuse and organization within the API.
- **ModelSerializers**: To streamline the process of transforming models to JSON and vice-versa.
- **Django Validators**: For data validation directly in models and serializers.
- **SimpleJWT**: For implementing JWT authentication with refresh tokens.
- **Python**: As the programming language for backend development.

## How to Use

### Step 1: Install Dependencies

After downloading the project, open the terminal in the root folder and run the command to install the project dependencies:

```bash
pip install -r requirements.txt
```
### Step 2: Configure the `.env` File

Create a `.env` file in the root of the project containing the following environment variables:

```
DB_NAME=Database name
DB_USER=Database user name
DB_PASSWORD=Database user password
DB_HOST=Database host (e.g., db)
DB_PORT=Database port (e.g., 5432)
```

### Step 3: Start the Database

Use **Docker Compose** to start the container with the **PostgreSQL** database:

```bash
docker-compose up
```

### Step 4: Create the Database Tables

With the database running, run the migrations to create the project tables in the database:

```bash
python manage.py migrate
```

### Step 5: Create Superuser

Create a superuser to access the admin panel:

```bash
python manage.py createsuperuser
```

After creating the superuser, you can access the Django administration panel at:

```
http://127.0.0.1:8000/admin/
```

### Step 6: Run the Server

Finally, run the Django development server:

```bash
python manage.py runserver
```

### Postman Collection Documentation
- [https://documenter.getpostman.com/view/25729709/2sAXqnej4C](https://documenter.getpostman.com/view/25729709/2sAY4vi3ch)
