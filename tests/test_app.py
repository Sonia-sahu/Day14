import unittest 
from app import app 

class CalculatorFlaskTestCase(unittest.TestCase): 
    def setUp(self): 
        app.config['TESTING'] = True 
        self.client = app.test_client() 
 
    def test_template_contains_form_fields(self): 
        resp = self.client.get('/') 
        self.assertEqual(resp.status_code, 200) 
        data = resp.get_data(as_text=True) 
        self.assertIn('name="a"', data) 
        self.assertIn('name="b"', data) 
        self.assertIn('name="operation"', data) 

    def test_multiple_cases(self): 
        cases = [ 
            ('1', '2', 'add', '3'),
            ('5', '3', 'subtract', '2'), 
            ('2', '3', 'multiply', '6'), 
            ('7', '2', 'divide', '3.5'), 
        ] 
        for a, b, op, expected in cases: 
            with self.subTest(a=a, b=b, op=op): 
                resp = self.client.post('/', data={'a': a, 'b': b, 'operation': op}) 
                self.assertEqual(resp.status_code, 200) 
                self.assertIn(f'Result: {expected}', resp.get_data(as_text=True)) 

    def test_divide_by_zero(self): 
        resp = self.client.post('/', data={'a': '5', 'b': '0', 'operation': 'divide'})
        self.assertEqual(resp.status_code, 200) 
        self.assertIn('Cannot divide by zero', resp.get_data(as_text=True)) 

    def test_invalid_input(self): 
        resp = self.client.post('/', data={'a': 'abc', 'b': '2', 'operation': 'add'}) 
        self.assertIn('Invalid input', resp.get_data(as_text=True)) 

if __name__ == '__main__': 
    unittest.main() 