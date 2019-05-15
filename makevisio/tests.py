from django.test import TestCase
from makevisio.models import *
from makevisio.page import Page

# Create your tests here.
class PageModelTest(TestCase):
    def test_if_retrun_a_title_page(self):
        page = Page('http://localhost/ifpi.html')
        self.assertIs(page.title,'Home — IFPI Instituto Federal do Piauí')