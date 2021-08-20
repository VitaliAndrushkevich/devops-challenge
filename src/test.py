#!/usr/bin/python3
import unittest
import app


class TestMethodApp(unittest.TestCase):
    def test_method_GET(self):
        request = {"requestContext": {"http": {"method": "GET"}}}

        self.assertEqual(app.get_method(request), "GET")

    def test_method_POST(self):
        request = {"requestContext": {"http": {"method": "POST"}}}

        self.assertEqual(app.get_method(request), "POST")

    def test_invalid_format(self):
        request = "Test string"

        self.assertEqual(app.get_method(request), "Not valid query format")


class TestHeaderApp(unittest.TestCase):
    def test_headers(self):
        request = {"headers": "{'user-agent': 'unittest/x.z'}"}

        self.assertEqual(
            app.get_headers(request), "{'user-agent': 'unittest/x.z'}"
        )

    def test_invalid_headers(self):
        request = "Test string"

        self.assertEqual(app.get_headers(request), "Not valid query format")


class TestBodyApp(unittest.TestCase):
    def test_others_body(self):
        request = '{"body": {"username": "xyz", "password": "xyz"}}'

        self.assertEqual(app.get_body(request, "GET"), None)

    def test_post_body(self):
        request = {"body": {"username": "xyz", "password": "xyz"}}

        self.assertEqual(app.get_body(request, "POST"), request.get("body"))

    def test_get_valid_format(self):
        request = "Test string"
        self.assertEqual(
            app.get_body(request, "POST"), "Not valid query format"
        )


if __name__ == "__main__":
    unittest.main()
