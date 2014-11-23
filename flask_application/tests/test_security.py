import re

from flask import url_for

from flask_application.tests import FlaskTest


class TestSecurity(FlaskTest):

    def login(self, username, password):
        return self.client.post(url_for('security.login'), data=dict(
            email=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.client.get(
            url_for('security.logout'),
            follow_redirects=True
        )

    def assertLoggedIn(self, email, rv=None):
        if rv is None:
            rv = self.client.get('/')
        self.assertTrue(('Hello %s' % email) in rv.data)

    def test_login(self):
        print self.app
        rv = self.login('jimbob@example.com', 'password')
        self.assertTrue('Specified user does not exist' in rv.data)

        rv = self.login('jill@lp.com', 'password')
        self.assertTrue('Hello jill@lp.com' in rv.data)

        self.assertLoggedIn('jill@lp.com')

        self.logout()

        rv = self.client.get('/')
        self.assertFalse('Hello jill@lp.com' in rv.data)

    def test_register(self):

        rv = self.login('jimbob@example.com', 'password')
        self.assertTrue('Specified user does not exist' in rv.data)

        with self.app.mail.record_messages() as outbox:
            self.assertEqual(len(outbox), 0)

            self.client.post(url_for('security.register'), data=dict(
                email='jimbob@example.com',
                password='password'
            ), follow_redirects=True)

            self.assertEqual(len(outbox), 1)

            rv = self.login('jimbob@example.com', 'password')
            self.assertTrue('Email requires confirmation' in rv.data)

            urls = re.findall(r'<a href="(.+)">\1</a>', outbox[0].body)

            rv = self.client.get(urls[0], follow_redirects=True)
            self.assertLoggedIn('jimbob@example.com', rv)

            self.logout()

            rv = self.login('jimbob@example.com', 'password')
            self.assertLoggedIn('jimbob@example.com', rv)
