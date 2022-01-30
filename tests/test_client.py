import unittest

from minio_console import MinioConsoleClient


class TestClient(unittest.TestCase):

    def test_connection_refused(self):
        try:
            MinioConsoleClient("http://localhost:12345", "admin", "admin")
            self.fail("Expected exception")
        except Exception as e:
            self.assertIn("Connection refused", str(e))


if __name__ == '__main__':
    unittest.main()
