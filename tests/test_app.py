from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import TouristSites, Locations


class TestBase(TestCase):
    
    def create_app(self):

        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app
        
    def setUp(self):

        db.create_all()

        location1 = Locations(country="new country", city= "new city")
        db.session.add(location1)
        db.session.commit()

        site1 = TouristSites(location_id="1", site_name="site1", favourite_part="the weather")
        db.session.add(site1)
        db.session.commit()

    def tearDown(self):

        db.drop_all()

class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)
    
    def test_create_location_get(self):
        response = self.client.get(url_for('create_location'))
        self.assert200(response)

    def test_create_site_get(self):
        response = self.client.get(url_for('create_site'))
        self.assert200(response)

    def test_updatesite_get(self):
        response = self.client.get(url_for('updatesite', id=1))
        self.assert200(response)

class TestRead(TestBase):

    def test_read_home_locations(self):
        response = self.client.get(url_for('home'))
        self.assertIn('new country', str(response.data))
        self.assertIn('new city', str(response.data))
        
    def test_read_home_site(self):
        response = self.client.get(url_for('home'))
        self.assertIn('1', str(response.data))
        self.assertIn('site1', str(response.data))
        self.assertIn('the weather', str(response.data))

class TestCreate(TestBase):

    def test_create_location(self):
        response = self.client.post(
            url_for('create_location'),
            data={"country": "test country", "city":"test city"},
            follow_redirects=True
        )
        self.assertIn(b"test country", response.data)
        self.assertIn(b"test city", response.data)
    
    def test_create_site(self):
        response = self.client.post(
            url_for('create_site'),
            data={"site_name": "test site", "favourite_part": "views", "location_id":"1"},
            follow_redirects=True
        )
        self.assertIn(b"test site", response.data)
        self.assertIn(b"views", response.data)
        self.assertIn(b"1", response.data)

class TestUpdate(TestBase):

    def test_updatesite(self):
        response = self.client.post(
            url_for('updatesite', id=1),
            data={"site_name": "test site", "favourite_part": "views", "location_id":"1"},
            follow_redirects=True
        )
        self.assertIn(b"test site", response.data)
        self.assertIn(b"views", response.data)
        self.assertIn(b"1", response.data)
    
class TestDelete(TestBase):

    def test_deletesite(self):
        response = self.client.get(
            url_for('deletesite', id=1),
            follow_redirects=True
        )
        self.assertNotIn(b"site1", response.data)