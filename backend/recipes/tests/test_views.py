from .test_setup import TestViewsSetup


class TestViews(TestViewsSetup):
    def test_all_recipes(self):
        res = self.client.get(self.list_or_create_url)
        data = res.json()
        self.assertEqual(len(data), 3)
        self.assertEqual(data[0]['name'], self.recipe1.name)

    def test_create_recipe_without_name_should_not_allow(self):
        expected = "{'name': ['This field is required.']}"
        self.recipe_data.pop('name', None)
        res = self.client.post(self.list_or_create_url, data=self.recipe_data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(str(res.json()), expected)
    
    def test_create_recipe_without_ingridients_should_not_allow(self):
        expected = "{'ingridients': ['This field is required.']}"
        self.recipe_data.pop('ingridients', None)
        res = self.client.post(self.list_or_create_url, data=self.recipe_data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(str(res.json()), expected)
    
    def test_create_recipe_with_duplicated_ingridients_should_create_without_duplicates(self):
        self.recipe_data['ingridients'] = [
            "Milk",
            "Milk",
        ]
        res = self.client.post(self.list_or_create_url, data=self.recipe_data)
        data = res.json()
        self.assertEqual(res.status_code, 201)
        self.assertEqual(len(data['ingridients']), 1)
    
    def test_create_recipe_should_be_done_successfully(self):
        res = self.client.post(self.list_or_create_url, data=self.recipe_data)
        data = res.json()
        self.assertEqual(res.status_code, 201)
        self.assertEqual(len(data['ingridients']), 2)
        self.assertEqual(data['name'], self.recipe_data['name'])
        self.assertEqual(data['text'], self.recipe_data['text'])

    def test_own_recipes(self):
        res = self.client.get(self.own_list_url)
        data = res.json()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['name'], self.recipe1.name)
        self.assertEqual(data[0]['text'], self.recipe1.text)

    def test_retrieve_with_valid_key(self):
        res = self.client.get(self.detail_url)
        data = res.json()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['name'], self.recipe3.name)
        self.assertEqual(data['text'], self.recipe3.text)

    def test_rate_own_recipe_should_not_allow(self):
        expected = "{'message': 'You are not able to rate your own recipes'}"
        res = self.client.post(self.rate_url, data=self.invalid_recipe_id_rate_data)
        data = res.json()
        self.assertEqual(res.status_code, 400)
        self.assertEqual(str(data), expected)

    def test_rate_recipe_with_rating_value_less_than_one_should_not_allow(self):
        expected = "{'rating': ['Ensure this value is greater than or equal to 1.']}"
        res = self.client.post(self.rate_url, data=self.less_than_one_data)
        data = res.json()
        self.assertEqual(res.status_code, 400)
        self.assertEqual(str(data), expected)

    def test_rate_recipe_with_rating_value_greater_than_five_should_not_allow(self):
        expected = "{'rating': ['Ensure this value is less than or equal to 5.']}"
        res = self.client.post(self.rate_url, data=self.greater_than_five_data)
        data = res.json()
        self.assertEqual(res.status_code, 400)
        self.assertEqual(str(data), expected)