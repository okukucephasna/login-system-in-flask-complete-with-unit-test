A simple Flask login system with Sign Up, Sign In, and Dashboard pages using MySQL (PyMySQL) and Bootstrap. Includes session management, success/error alerts, and unit tests for signup, login, and logout. Clean UI, easy setup, ideal for beginners learning Flask authentication basics.


Flask Login System with MySQL (PyMySQL) + Unit Tests
This is a Flask-based user authentication system with full login and registration functionalities. It connects to a MySQL database using PyMySQL, displays user email on the dashboard, and provides feedback via Bootstrap alerts. The project also features unit tests for sign-up, sign-in, and logout actions to ensure reliability and ease of future code changes.
Features
•	User Registration (Sign Up): Users can register with an email and password. Duplicate accounts are prevented.
•	User Login (Sign In): Authenticated users can log in and access a personalized dashboard.
•	Dashboard Page: Displays the logged-in user's email.
•	Logout: Users can securely log out.
•	Bootstrap Styling: Clean and responsive UI for all pages.
•	Flash Alerts: Success and error messages displayed after actions.
•	Unit Testing: Automated testing for signup, login, and logout.
•	MySQL Database Connection: Secure connection using PyMySQL.
📂 Project Structure
your_project/
│
├── app.py                 # Main Flask application
├── test_app.py            # Unit tests using unittest
├── templates/             # HTML templates (signup, signin, dashboard)
│   ├── signup.html
│   ├── signin.html
│   └── dashboard.html
├── static/css/style.css   # Optional custom CSS
└── README.md              # Project description
________________________________________
⚙️ Setup Instructions
1. Clone the Repository
git clone https://github.com/your-username/your-repo.git
cd your-repo
2. Install Python Dependencies
pip install flask pymysql
3. MySQL Database Setup
CREATE DATABASE flask_login_db;
USE flask_login_db;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);
4. Update Database Credentials
In app.py, update your MySQL credentials:
db_config = {
    'host': 'localhost',
    'user': 'your_mysql_username',
    'password': 'your_mysql_password',
    'database': 'flask_login_db'
}
5. Run the Flask App
python app.py
Visit http://127.0.0.1:5000 in your browser.
________________________________________
🧪 Running Unit Tests
python test_app.py
This runs automated tests for sign-up, login, and logout processes.

