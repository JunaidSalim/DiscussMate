# DiscussMate
DiscussMate is a real-time chatting app where users can discuss various topics in specialized rooms. The app features an API built with Django Rest Framework and includes a user authentication system.

## Live Preview: [discussmate.onrender.com](https://discussmate.onrender.com)

## Repository Structure

```
├── base/
│ ├── admin.py
│ ├── api/
│ │ ├── serializers.py
│ │ ├── urls.py
│ │ ├── views.py
│ │ └── init.py
│ ├── apps.py
│ ├── forms.py
│ ├── migrations/
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ ├── views.py
│ └── init.py
├── manage.py
├── mate/
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── init.py
├── requirements.txt
├── static/
│ ├── js/
│ │ └── script.js
│ └── styles/
│ ├── main.css
│ └── style.css
└── templates/
├── base/
│ ├── activity.html
│ ├── activity_component.html
│ ├── delete.html
│ ├── feed_component.html
│ ├── home.html
│ ├── login_register.html
│ ├── profile.html
│ ├── room.html
│ ├── room_form.html
│ ├── topics.html
│ ├── topics_component.html
│ └── update-user.html
├── main.html
└── navbar.html
```

## Features

- Real-time chat functionality
- Topic-specific chat rooms
- User authentication system
- API built with Django Rest Framework

## Project Hosting

App Hosting: [Render](https://render.com).
<br/>
Media Storage: [Cloudinary](https://cloudinary.com/)

## Inspiration

The idea for this project was inspired by a [YouTube tutorial](https://www.youtube.com/watch?v=PtQiiknWUcI) on Traversy Media by [Dennis Ivy](https://github.com/divanov11). The theme is adapted from his [repository](https://github.com/divanov11/StudyBud).

## Learning Experience

During this project, I enhanced my knowledge of Django and learned new things such as Django Rest Framework. This project has been a valuable learning experience.

## Setup Instructions

To set up this project locally, follow these steps:

1. **Clone the repository**

   ```bash
   git clone https://github.com/JunaidSalim/DiscussMate.git
   cd discussmate

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install the required packages**
   ```bash
   pip install -r requirements.txt

4. **Set up the environment variables**
   Create a .env file in the root directory and add the necessary environment variables:
   ```bash
   ENVIRONMENT=development
   SECRET_KEY=your_secret_key
   DATABASE_URL=your_database_url
   CLOUD_NAME=your_cloud_name
   API_KEY=your_cloud_api_key
   API_SECRET=your_cloud_api_secret

5. **Apply the database migrations**
   ```bash
   python manage.py migrate

6. **Create a superuser**
   ```bash
   python manage.py createsuperuser

7. **Run the development server**
   ```bash
   python manage.py runserver

8. **Access the application**
   
   Open your web browser and navigate to http://127.0.0.1:8000 to access the application.

## Contributing

Contributions are welcome! Feel free to submit issues, fork the repository, and send pull requests. For major changes, please open an issue first to discuss what you would like to change.

