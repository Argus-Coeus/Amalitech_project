# Video Platform
## Project Objective

Paul Leonard, a video creator, seeks a bespoke video hosting platform to exclusively feature his brand. This platform aims to provide a unique and professional presentation, addressing branding issues with existing platforms.

# Customer Requirements

## User Features

### Signup & Login
```
Email and password-based signup and login.
Account verification required.
Password reset feature.
```

### Video Navigation
```
Users can navigate through video pages.
```
### Video Sharing
```
Users can share links to videos on different pages.
```
## Admin Features
### Video Upload
```
Admins can upload videos with a title and description.

```
### Video Page Features
#### Single Video Display
```
Each page displays only one video.
```
#### Navigation Buttons
```
Next and Previous buttons for navigation.
Buttons hidden if no further video exists.
```
#### Video Controls
```
Common video control buttons.
```
#### Branding
```
Prominent business logo display.
```
#### Share Button
```
Button to share the video page link.
```
#### Deliverables
##### Web Application Source Code
```
Implement Git flow with detailed commits.
Include a comprehensive README file.
```
##### ER Diagram
```

```

##### Deployed Link
```
The web application is deployed on Render.
```

# Video Platform API
## Overview
The Video Platform API is a Django-based application providing endpoints for user authentication, video management, and user management.

## Features
### User Authentication
```
Register, login, logout, password reset, token verification.
```

### Video Management
```
Upload, update, delete, list videos.
```
### User Profile Management
```
View, update, delete profiles.
```
### Admin Functionalities

#### Installation
#### Prerequisites
#### Python 3.8 or higher
```
pip
Django
Django Rest Framework
```

#### Steps
##### Clone the repository:
```
sh
Copy code
git clone https://github.com/yourusername/videoplatform-api.git
cd videoplatform-api
Create a virtual environment and activate it:
sh
```
#### Copy code
```
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required dependencies:
sh
Copy code
pip install -r requirements.txt
```
#### Apply migrations:
```
sh
Copy code
python manage.py migrate
Create a superuser:
sh
```

#### Copy code
```
python manage.py createsuperuser
Run the server:
sh
```

#### Copy code
```
python manage.py runserver
```

## API Endpoints
### User Authentication
```
Register: POST /auth/register/
Login: POST /auth/login/
Logout: POST /auth/logout/
Password Reset Request: POST /api/password_reset/
Password Reset Confirm: POST /api/password_reset/confirm/
Validate Token: POST /api/password_reset/validate_token/
```

### Video Management
```
List Videos: GET /api/v1/vd/
Read Video: GET /api/v1/vd/{id}/
Create Video: POST /api/v1/create/
Update Video: PUT /api/v1/vd/{id}/
Partial Update Video: PATCH /api/v1/vd/{id}/
Delete Video: DELETE /api/v1/vd/{id}/
```

### User Management
```
List Users: GET /api/v1/users/
Read User: GET /api/v1/users/{id}/
Update User: PUT /api/v1/users/{id}/
Partial Update User: PATCH /api/v1/users/{id}/
Delete User: DELETE /api/v1/users/{id}/
```

### Usage
#### Interact with the API using coreapi-cli.

### Example Requests
#### Password Reset Request
```

Copy code
coreapi action api password_reset create -p email=example@example.com
Password Reset Confirm

```

#### Copy code
```
coreapi action api password_reset confirm create -p password=newpassword -p token=your-token
List Videos

```
#### Copy code
```
coreapi action api v1 vd list
Create Video

```
#### Copy code
```
coreapi action api v1 create create -p author=1 -p title="New Video" -p description="Video Description" -p video_file="video.mp4" -p thumbnail="thumbnail.jpg"
```
#### Running Tests
##### Ensure API correctness with included unit tests.

#### Running Unit Tests
##### Install test dependencies:

###### Copy code
```
pip install -r requirements-test.txt
```
######  Run the tests:


##### Copy code
```
python manage.py test
```
# Unit Testing
## Basic unit tests for API endpoints:
```
tests/test_auth.py
```
### python
#### Copy code
```
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class AuthTests(APITestCase):

    def test_register(self):
        url = reverse('register')
        data = {
            "username": "testuser",
            "password": "testpassword",
            "password2": "testpassword",
            "email": "test@example.com",
            "first_name": "Test",
            "last_name": "User"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        url = reverse('login')
        data = {
            "username": "testuser",
            "password": "testpassword"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
```
tests/test_video.py
#### Copy code
```
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Video

class VideoTests(APITestCase):

    def test_create_video(self):
        url = reverse('video-create')
        data = {
            "author": 1,
            "title": "Test Video",
            "description": "This is a test video",
            "video_file": "test_video.mp4",
            "thumbnail": "test_thumbnail.jpg"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_videos(self):
        url = reverse('video-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        ```

