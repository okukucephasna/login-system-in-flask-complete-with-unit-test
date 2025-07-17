import unittest
from app import app, get_connection

class FlaskLoginTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE email=%s", ('testuser@example.com',))
        conn.commit()
        cursor.close()
        conn.close()

    def test_signup(self):
        response = self.app.post('/signup', data=dict(email='testuser@example.com', password='pass1234'), follow_redirects=True)
        self.assertIn(b'Account created successfully!', response.data)

    def test_signin_success(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", ('testuser@example.com', 'pass1234'))
        conn.commit()
        cursor.close()
        conn.close()

        response = self.app.post('/signin', data=dict(email='testuser@example.com', password='pass1234'), follow_redirects=True)
        self.assertIn(b'Logged in successfully!', response.data)

    def test_signin_fail(self):
        response = self.app.post('/signin', data=dict(email='wrong@example.com', password='wrong'), follow_redirects=True)
        self.assertIn(b'Wrong email or password!', response.data)

    def test_logout(self):
        with self.app.session_transaction() as sess:
            sess['email'] = 'testuser@example.com'
        response = self.app.get('/logout', follow_redirects=True)
        self.assertIn(b'Logged out successfully.', response.data)

if __name__ == '__main__':
    unittest.main()
