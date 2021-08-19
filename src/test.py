#!/usr/bin/python3
import unittest
import app


class TestApplication(unittest.TestCase):

    def test_get(self):
        get_request = {
            'requestContext': {
                'http': {
                    'method': "GET"
                }
            },
            'headers': {
                'user-agent': 'unittest/x.z'
            }
        }

        self.assertEqual(
            app.lambda_handler(get_request, ''),
            'Welcome to our demo API, here are the details of your request:\n\
Headers: {\'user-agent\': \'unittest/x.z\'}\nMethod: GET'
        )

    def test_post(self):
        post_request = {
            'requestContext': {
                'http': {
                    'method': "POST"
                }
            },
            'headers': {
                'user-agent': 'unittest/x.z'
            },
            'body': {
                "username": "xyz",
                "password": "xyz"
            }
        }

        self.assertEqual(
            app.lambda_handler(post_request, ''),
            'Welcome to our demo API, here are the details of your request:\n\
Headers: {\'user-agent\': \'unittest/x.z\'}\n\
Method: POST Body: {\'username\': \'xyz\', \'password\': \'xyz\'}'
        )

    def test_error_handler(self):
        get_request = {
            'test': 'test'
        }

        self.assertEqual(
            app.lambda_handler(get_request, ''),
            'Make sure you send correct http request'
        )

    def test_others(self):
        head_request = {
            'requestContext': {
                'http': {
                    'method': "HEAD"
                }
            },
            'headers': {
                'user-agent': 'unittest/x.z'
            }
        }
        self.assertEqual(
            app.lambda_handler(head_request, ''),
            'This method currently not supported'
        )


if __name__ == '__main__':
    unittest.main()
