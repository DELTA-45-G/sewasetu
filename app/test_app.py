import importlib.util
import unittest

spec = importlib.util.spec_from_file_location("portal_app", "app/app.py")
portal = importlib.util.module_from_spec(spec)
spec.loader.exec_module(portal)

class PortalFixTests(unittest.TestCase):
    def test_sanitize_preserves_unicode_name(self):
        name = "অসমীয়া জীৱন দাস"
        self.assertEqual(portal.sanitize(name), name)

    def test_scheduler_config_exists(self):
        import os
        path = os.path.join("app", "config", "app.ini")
        self.assertTrue(os.path.isfile(path))

if __name__ == "__main__":
    unittest.main()
