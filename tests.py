import json
from unittest import TestCase
from main import app


class MathTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        cls.client = app.test_client()

    def test_get_math_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertDictEqual(
            json.loads(response.data.decode()),
            {
                'math': [
                    'add', # Sum of a list of elements
                    'bhaskara', # Finds the roots of a quadratic equation
                    'cos',
                    'division', # Division of two numbers
                    'get_change', # Change (in percent) for each two values of a list
                    'mean', # Mean of a list of numbers
                    'pow', # x raised to the power y
                    'sin',
                    'sqrt', # Square root of a number
                    'stdev', # Standart Deviation of a list of numbers
                    'tan'
                ]
            }
        )

    def test_get_division(self):
        response = self.client.post('/', json={'operation': 'division', 'param': [1, 2]})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertDictEqual(json.loads(response.data.decode()), {'result': 0.5})

    def test_division_by_zero(self):
        response = self.client.post('/', json={'operation': 'division', 'param': [10, 0]})
        self.assertEqual(response.status_code, 500)

    def test_get_mean(self):
        response = self.client.post('/', json={'operation': 'mean', 'param': [1, 2, 3, 4, 5, 6, 7, 8, 9]})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertDictEqual(json.loads(response.data.decode()), {'result': 5.0})

    def test_get_pow(self):
        response = self.client.post('/', json={'operation': 'pow', 'param': [2, 8]})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertDictEqual(json.loads(response.data.decode()), {'result': 256.0})

    def test_get_stdev(self):
        response = self.client.post('/', json={'operation': 'stdev', 'param': [1, 2, 3, 4, 5, 6, 7, 8, 9]})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertDictEqual(json.loads(response.data.decode()), {'result': 2.7386127875258306})

    def test_get_sqrt(self):
        response = self.client.post('/', json={'operation': 'sqrt', 'param': [15]})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertDictEqual(json.loads(response.data.decode()), {'result': 3.872983346207417})

    def test_get_sum(self):
        response = self.client.post('/', json={'operation': 'add', 'param': [1, 2, 3, 4, 5, 6, 7, 8, 9]})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertDictEqual(json.loads(response.data.decode()), {'result': 45.0})

    def test_get_bhaskara(self):
        response = self.client.post('/', json={'operation': 'bhaskara', 'param': ['x2 + 8x - 9 = 0']})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertDictEqual(json.loads(response.data.decode()), {'result': {'x1': 1, 'x2': -9}})

        response = self.client.post('/', json={'operation': 'bhaskara', 'param': ['2x2+x+9=0']})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertDictEqual(json.loads(response.data.decode()), {'result': 'non real roots'})

        response = self.client.post('/', json={'operation': 'bhaskara', 'param': ['x2-9=0']})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertDictEqual(json.loads(response.data.decode()), {'result': {'x1': 3.0, 'x2': -3.0}})

    def test_get_bhaskara_invalid_expression(self):
        response = self.client.post('/', json={'operation': 'bhaskara', 'param': ['2x3+x+9=0']})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertDictEqual(json.loads(response.data.decode()), {'result': 'invalid expression'})

        response = self.client.post('/', json={'operation': 'bhaskara', 'param': ['x2+x+9=12']})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertDictEqual(json.loads(response.data.decode()), {'result': 'invalid expression'})

    def test_get_sin(self):
        response = self.client.post('/', json={'operation': 'sin', 'param': [30]})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertDictEqual(json.loads(response.data.decode()), {'result': 0.5})

    def test_get_cos(self):
        response = self.client.post('/', json={'operation': 'cos', 'param': [30]})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertDictEqual(json.loads(response.data.decode()), {'result': 0.87})

    def test_get_tan(self):
        response = self.client.post('/', json={'operation': 'tan', 'param': [30]})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertDictEqual(json.loads(response.data.decode()), {'result': 0.58})

    def test_get_change(self):
        response = self.client.post('/', json={'operation': 'get_change', 'param': [1,1,2,4,2,8,2]})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertDictEqual(json.loads(response.data.decode()), {'result': ['None', '0%', '100%', '100%', '-50%', '300%', '-75%']})

        response = self.client.post('/', json={'operation': 'get_change', 'param': [1,2,4,8,0,2]})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertDictEqual(json.loads(response.data.decode()), {'result': 'error: zero found'})
    
    def test_invalid_operation(self):
        response = self.client.post('/', json={'operation': 'subtraction', 'param': [1, 7]})
        self.assertEqual(response.status_code, 404)