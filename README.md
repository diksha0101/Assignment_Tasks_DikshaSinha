# Assignment_Tasks_DikshaSinha

# Responsive Webpage and Django Chat Application

This README provides step-by-step instructions for setting up, installing, and running the Django project with a responsive webpage and chat application.



## **Prerequisites**

1. **Python**:
   - Ensure Python 3.8 or later is installed. You can download it from [python.org](https://www.python.org/).
   - Verify installation:
     ```bash
     python --version
     ```

2. **Pip**:
   - Python's package manager (`pip`) should be installed.

3. **Virtual Environment (Optional but Recommended)**:
   - Install `virtualenv`:
     ```bash
     pip install virtualenv
     ```
   - Create a virtual environment:
     ```bash
     virtualenv venv
     ```
   - Activate it:
     - Windows:
       ```bash
       venv\Scripts\activate
       ```
     - macOS/Linux:
       ```bash
       source venv/bin/activate
       ```

4. **Install Redis (For WebSocket)**:
   - Use Docker to run Redis:
     ```bash
     docker run -p 6379:6379 redis
     ```
   - Or install Redis locally ([Instructions](https://redis.io/docs/getting-started/)).

---

## **Project Setup**

### Step 1: Clone the Repository
```bash
git clone <repository_url>
cd <repository_folder>
```

### Step 2: Install Dependencies
1. Install Django and required libraries:
   ```bash
   pip install -r requirements.txt
   ```
   If `requirements.txt` does not exist, install manually:
   ```bash
   pip install django channels channels-redis
   ```

### Step 3: Set Up the Database
1. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to set up a username, email, and password.

---

## **Running the Project**

### Step 4: Start the Server
```bash
python manage.py runserver
```

### Step 5: Access the Application
1. Open your browser and navigate to:
   - Application: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Admin Panel: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

2. Log in with the superuser credentials for the admin panel.

### Step 6: Test the Chat Application
1. Sign up as multiple users using the Sign-Up page.
2. Log in with different accounts.
3. Select a user from the collapsible menu to start chatting.
4. Verify real-time messaging and message retrieval.

---

## **Project Structure**
```
chat_project/          # Root of the Django project
├── chat_project/      # Project folder (settings, urls, etc.)
│   ├── asgi.py        # For WebSocket support
│   ├── settings.py    # Django settings
│   ├── urls.py        # Project-level URLs
│   └── ...
├── chat/              # Chat application
│   ├── templates/     # HTML templates
│   │   └── chat/      # Subdirectory for chat app templates
│   │       ├── chat_home.html
│   │       └── signup.html
│   ├── static/        # Static files (CSS, JS, etc.)
│   ├── models.py      # Database models
│   ├── views.py       # Views for the app
│   ├── routing.py     # WebSocket routing
│   ├── consumers.py   # WebSocket consumers
│   └── ...
├── db.sqlite3         # SQLite database (default)
└── manage.py          # Django management script
```

---

## **Static and Media Files**
1. **Static Files**:
   Ensure `STATIC_URL` is set in `settings.py`:
   ```python
   STATIC_URL = '/static/'
   STATICFILES_DIRS = [BASE_DIR / 'chat/static']
   ```

2. **Collect Static Files** (if necessary):
   ```bash
   python manage.py collectstatic
   ```

---

## **Troubleshooting**
1. **Port Already in Use**:
   If the server fails to start, ensure no other process is using the port:
   ```bash
   lsof -i:8000
   ```
   Stop the process or run the server on a different port:
   ```bash
   python manage.py runserver 8080
   ```

2. **Static Files Not Loading**:
   - Confirm static files are properly configured.
   - Run `collectstatic` if using a production environment.

3. **WebSocket Not Working**:
   - Ensure Redis is running.
   - Verify WebSocket configuration in `asgi.py` and `routing.py`.

---
