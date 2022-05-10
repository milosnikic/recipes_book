from .test_setup import TestViewsSetup


class TestViews(TestViewsSetup):
    def test_user_cannot_register_without_data(self):
        expected = "{'first_name': ['This field is required.'], 'last_name': ['This field is required.'], 'username': ['This field is required.'], 'email': ['This field is required.'], 'password': ['This field is required.'], 'confirm_password': ['This field is required.']}"
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(str(res.json()), expected)

    def test_user_cannot_register_if_username_already_exist(self):
        self.client.post(
            self.register_url, self.user_data)
        res = self.client.post(self.register_url, self.new_user_same_username)
        self.assertEqual(res.status_code, 400)

    def test_user_cannot_register_with_invalid_email(self):
        self.user_data['email'] = "test@test.com"
        res = self.client.post(self.register_url, self.user_data)
        self.assertEqual(res.status_code, 400)

    def test_user_can_register_successfully(self):
        res = self.client.post(
            self.register_url, self.user_data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data['first_name'], self.user_data['first_name'])
        self.assertEqual(res.data['last_name'], self.user_data['last_name'])
        self.assertEqual(res.data['username'], self.user_data['username'])
        self.assertEqual(res.data['email'], self.user_data['email'])

    def test_user_cannot_login_with_invalid_password(self):
        expected = "No active account found with the given credentials"
        self.client.post(self.register_url, self.user_data)
        self.user_data['password'] = "invalid_password"
        res = self.client.post(self.login_url, self.user_data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(res.json()['detail'], expected)

    def test_user_can_login(self):
        self.client.post(self.register_url, self.user_data)
        res = self.client.post(self.login_url, self.user_data)
        self.assertEqual(res.status_code, 200)
        self.assertIsNotNone(res.json()['access'])
        self.assertIsNotNone(res.json()['refresh'])

    def test_user_can_refresh_token_successfully(self):
        self.client.post(self.register_url, self.user_data)
        res = self.client.post(self.login_url, self.user_data)
        refresh = res.json()['refresh']
        res = self.client.post(
            self.refresh_url, {'refresh': refresh})
        self.assertEqual(res.status_code, 200)
        self.assertIsNotNone(res.json()['access'])

    def test_user_cannot_refresh_token_when_refresh_token_is_invalid(self):
        self.client.post(self.register_url, self.user_data)
        res = self.client.post(self.login_url, self.user_data)
        refresh = "invalid_refresh_token"
        res = self.client.post(
            self.refresh_url, {'refresh': refresh})
        self.assertEqual(res.status_code, 401)
