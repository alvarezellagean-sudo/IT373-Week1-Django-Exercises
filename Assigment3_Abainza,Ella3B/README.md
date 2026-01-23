# Announcement Project

This is a simple Django project for managing announcements. It includes a home page, a list of announcements, and detailed views for each announcement.

## Project Structure

```
announcement
├── manage.py
├── README.md
├── requirements.txt
├── venv/
├── announcement/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── announcements/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── navbar.html
│   │   ├── home.html
│   │   └── announcements/
│   │       ├── list.html
│   │       └── detail.html
│   └── static/
│       └── announcements/
│           └── js/
│               └── toggle.js
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd announcement
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```

5. **Run the migrations:**
   ```
   python manage.py migrate
   ```

6. **Start the development server:**
   ```
   python manage.py runserver
   ```

## Usage

- Navigate to `http://127.0.0.1:8000/` to access the home page.
- Go to `http://127.0.0.1:8000/announcements/` to view the list of announcements.
- Click on an announcement to view its details.

## Features

- **Home Page:** A simple landing page.
- **Announcements List:** Displays all announcements.
- **Announcement Detail:** Shows detailed information about a specific announcement with a "Read more/Show less" toggle feature.

## License

This project is licensed under the MIT License.