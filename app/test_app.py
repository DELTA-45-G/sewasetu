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

    def test_reset_queries_are_parameterized(self):
        import inspect
        source = inspect.getsource(portal.reset_password)
        self.assertNotIn("mobile = '%s'", source)
        self.assertIn("mobile = %s", source)

    def test_admin_actions_require_admin_session(self):
        import inspect
        approve = inspect.getsource(portal.admin_approve)
        reject = inspect.getsource(portal.admin_reject)
        self.assertIn("admin_logged_in", approve)
        self.assertIn("admin_logged_in", reject)

    def test_apply_validates_captcha(self):
        import inspect
        source = inspect.getsource(portal.apply)
        self.assertIn("captcha_answer", source)
        self.assertIn("Security check failed", source)

    def test_upload_accepts_supported_documents(self):
        import inspect
        source = inspect.getsource(portal.upload)
        self.assertIn(".jpg", source)
        self.assertIn("5 * 1024 * 1024", source)

    def test_pending_application_can_be_edited_or_cancelled(self):
        import inspect
        edit_source = inspect.getsource(portal.edit_application)
        cancel_source = inspect.getsource(portal.cancel_application)
        self.assertIn("status='PENDING'", edit_source)
        self.assertIn("status='PENDING'", cancel_source)

if __name__ == "__main__":
    unittest.main()
