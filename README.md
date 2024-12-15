# JWT Authentication System

This project is a  Django REST API authentication system using JSON Web Tokens (JWT).

## Overview
This project implements a secure authentication system using JWT tokens with the following features:
- Created an unauthorized api endpoint to register a user.
- Created an unauthorized api endpoint to sign in
- Created an authorized api endpoint to get user details 
- Access token and refresh token generation
- Token-based authorization for protected routes
- Stored Token in Cookies


---

## Setup 




### Installation Steps

1. Create a virtual environment and activate it:
   ```bash
  - python -m venv env #for creation of virtual environment in window
  - source env/Scripts/activate  #for activation of virtual environment in window

2. Install dependencies:

   ```bash
   pip install -r requirements.txt

3. Set up your environment variables: Create a .env file in the project root and configure the following:

   ```env
 SECRET_KEY=
 DEBUG=
 DB_ENGINE=
 DB_NAME=
 JWT_ACCESS_TOKEN_LIFETIME=
 JWT_REFRESH_TOKEN_LIFETIME=



4. Apply migrations:

   ```bash
   python manage.py migrate

5. Run the development server:

   ```bash
   python manage.py runserver


### Endpoints
### Authentication
1. Register
### URL
POST api/auth/register

## Request Body:
```json
      {
      {
"username":"Ani",
"email":"ani@gmail.com",
"password":"123456"

}
      }
```
## Response:
```json
  {
    "message": "User registered successfully"
}
```
## Login
   ```json
   URL: POST api/auth/login
```
## Request Body:
   ```json
   {
"identifier":"Ani",
"password":"123456"

}
```
## Response:

```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczNDM2OTk4NCwiaWF0IjoxNzM0MjgzNTg0LCJqdGkiOiIyMGIzOTZiM2Q4OGU0Njc0YTU0YThmOWUwMTMyZTU2ZCIsInVzZXJfaWQiOjR9.XDes_eAhKNj9ejPqiw2kLN4ivpO6gbn2IuSbsVUy42U",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM0Mjg3MTg0LCJpYXQiOjE3MzQyODM1ODQsImp0aSI6IjIwODI1ZjY4M2FjYTRmNjc5NjFkZDZhZGQwNTU5MGViIiwidXNlcl9pZCI6NH0.kT03zeme_2idKeDT4RceslL7R4zXdtXlfeGYQTXuPhc"
}
```

## User Detail
## Get Detail
## URL: 
GET api/detail
## Headers:

## Authorization: Bearer access_token
## Response:
```json
{
    "message": "Welcome to Page",
    "user": {
        "id": 7,
        "username": "Ani",
        "email": "ani@gmail.com"
    }
}
```



## Generate Access token from refresh token
## URL: 
POST api/token/refresh

## Response:
```json
{
    "refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczNDM3MTM3NiwiaWF0IjoxNzM0Mjg0OTc2LCJqdGkiOiJhYmVkMjA0ZmRhYzM0Y2MwYWI5NDQ2OWEwYmI1MWE3OCIsInVzZXJfaWQiOjd9.93mTGHiXGmmzGrh2x1_WQwYVlYJCUKzLA2EVzMPfL4A"
}
```


## Generate  token using user credentials
## URL: 
POST api/token

## Response:
```json
{
"username":"Ani",
"password":"123456"

}
```
