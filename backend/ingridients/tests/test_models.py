from .test_setup import TestModelsSetup


class TestModels(TestModelsSetup):
    def test_str_method_should_be_successful(self):
        self.assertTrue(self.ingridient1.name, str(self.ingridient1))

    def test_number_of_recipes(self):
        self.assertTrue(self.ingridient5.number_of_recipes, 3)