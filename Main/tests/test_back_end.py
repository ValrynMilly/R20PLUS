import unittest

from flask import url_for
from flask_testing import TestCase

from application import app, db, bcrypt
from application.models import Users, Characters, Inventory
from os import getenv

class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # ensure there is no data in the test database when the test starts
        db.session.commit()
        db.drop_all()
        db.create_all()

        # create test admin user
        hashed_pw = bcrypt.generate_password_hash('admin2016')
        admin = Users(first_name="admin", last_name="admin",username="adminusername", email="admin@admin.com", password=hashed_pw)

        # create test non-admin user
        hashed_pw_2 = bcrypt.generate_password_hash('test2016')
        employee = Users(first_name="test", last_name="user",username="testusername", email="test@user.com", password=hashed_pw_2)

        # save users to database
        db.session.add(admin)
        db.session.add(employee)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()




def logging_in(self):
   response =  self.client.post(
            '/login.html',
            data=dict(
                email = "admin@admin.com",
                password = "admin2016",               
                ),
            follow_redirects=True
            )
   return response



class TestViews(TestBase):

    def test_homepage_view(self):
        """
        Test that homepage is accessible without login
        """
        self.assertEqual(self.client.get(url_for('home')).status_code, 200)

    def test_login(self):
        self.assertEqual(self.client.get(url_for('login')).status_code, 200)

    def test_Inventory(self):
        self.assertEqual(self.client.get(url_for('Inventory')).status_code, 200)

    def test_register(self):
        self.assertEqual(self.client.get(url_for('signup')).status_code, 200)

    def test_mycharacters(self):
        logging_in(self)
        self.assertEqual(self.client.get(url_for('mycharacters')).status_code, 200)
    

    def test_charactersheet(self):
        logging_in(self)
        self.assertEqual(self.client.get(url_for('charactersheet')).status_code, 200)

        
class TestRegistration(TestBase):

    def test_registration(self):
        """
        Test that when I register a new user, it redirects me to the login page
        """
        with self.client:
            response = self.client.post(
                    '/signup.html',
                    data = dict(
                        first_name="testfirst",
                        last_name="testsur",
                        username="testusername",
                        email="test@test.com",
                        password="test123",
                        ),
                    follow_redirects=True
                    )
            self.assertIn(b'testfirst', response.data)
            self.assertIn(b'testsur', response.data)
            self.assertIn(b'testusername', response.data)
            self.assertIn(b'test@test.com', response.data)


class TestLogin(TestBase):
    def test_Login(self):
        """
        test that logging in redirects me to the character page
        """
        with self.client:
            response = self.client.post(
                    '/login.html',
                    data = dict(
                        email="admin@admin.com",
                        password = "admin2016",
                        ),
                    follow_redirects=True
                    )
            return response
        self.assertIn(b'admin@admin.com', response.data)
        self.assertIn(b'admin2016', response.data)

class TestPlaylist(TestBase):
    def test_createcharacter(self):
        """
        Test that a user can create a Character
        """
        with self.client:
            logging_in(self)
            response = self.client.post(
                    '/charactersheet.html',
                    data = dict(
                        Characte_name="test_charname",
                        first_name="test_playername",
                        char_class="test_charclass",
                        background="test_background",
                        race="test_race",
                        alignment="test_allign",
                        experience_points="test_xp",
                        strength="test_str",
                        dexterity="test_dex",
                        constitution="test_con",
                        intelligence="test_intel",
                        wisdom="test_wis",
                        charisma="test_char",
                        ),
                    follow_redirects=True
                    )
            return response
        self.assertIn(b'test_charname', response.data)
        self.assertIn(b'test_playername', response.data)
        self.assertIn(b'test_charclass', response.data)
        self.assertIn(b'test_background', response.data)
        self.assertIn(b'test_race', response.data)
        self.assertIn(b'test_allign', response.data)
        self.assertIn(b'test_xp', response.data)
        self.assertIn(b'test_str', response.data)
        self.assertIn(b'test_dex', response.data)
        self.assertIn(b'test_con', response.data)
        self.assertIn(b'test_intel', response.data)
        self.assertIn(b'test_wis', response.data)
        self.assertIn(b'test_char', response.data)
        
