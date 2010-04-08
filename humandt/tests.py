from django.test import TestCase
from parser import parse
from datetime import datetime

class HumanTests(TestCase):
    def setUp(self):
        self.now = datetime.now()
        
    def test_tomorrow(self):
        t = parse('tomorrow 4PM')
        self.assertEqual(t.day, self.now.day+1)
        self.assertEqual(t.hour, 16)
        
