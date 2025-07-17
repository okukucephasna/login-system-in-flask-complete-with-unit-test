from flask import Flask, render_template, request, redirect, url_for, flash, session
import pymysql

app = Flask(__name__)
app.secret_key = 'super_secret_key'

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'flask_login_db'
}

def get_connection():
    return pymysql.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database']
    )

@app.route('/')
def home():
    return redirect(url_for('signin'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, password))
            conn.commit()
            flash('Account created successfully!', 'success')
            return redirect(url_for('signin'))
        except pymysql.err.IntegrityError:
            flash('Email already exists!', 'danger')
        finally:
            cursor.close()
            conn.close()
    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        if user:
            session['email'] = email
            flash('Logged in successfully!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Wrong email or password!', 'danger')
    return render_template('signin.html')

@app.route('/dashboard')
def dashboard():
    if 'email' not in session:
        flash('Please log in first.', 'danger')
        return redirect(url_for('signin'))
    return render_template('dashboard.html', email=session['email'])

@app.route('/logout')
def logout():
    session.pop('email', None)
    flash('Logged out successfully.', 'success')
    return redirect(url_for('signin'))

if __name__ == '__main__':
    app.run(debug=True)
