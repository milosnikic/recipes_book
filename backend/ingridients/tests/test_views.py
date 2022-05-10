from .test_setup import TestViewsSetup


class TestViews(TestViewsSetup):
    def test_all_ingridients(self):
        res = self.client.get(self.list_or_create_url)
        data = res.json()
        self.assertEqual(len(data), 5)
        self.assertEqual(data[0]['name'], self.ingridient1.name)
    
    def test_create_ingridient_should_not_create_when_name_is_not_present(self):
        res = self.client.post(self.list_or_create_url, data={})
        self.assertEqual(res.status_code, 400)

    def test_create_ingridient_should_create_successfully(self):
        res = self.client.post(self.list_or_create_url, data={"name":"New Ingridient"})
        self.assertEqual(res.status_code, 201)

    def test_most_used_ingridients(self):
        res = self.client.get(self.most_used_url)
        data = res.json()
        self.assertEqual(len(data), 5)
        self.assertEqual(data[0]['name'], self.ingridient5.name)
        self.assertEqual(data[1]['name'], self.ingridient4.name)
