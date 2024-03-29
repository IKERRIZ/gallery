from django.test import TestCase
from .models import Location,Category,Image

# Create your tests here.
class LocationTestClass(TestCase):

    # set up method
    def setUp(self):
        self.nairobi= Location(location='nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location))

    def tearDown(self):
        Location.objects.all().delete()

    def test_save_method(self):
        self.nairobi.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_delete_method(self):
        self.nairobi.delete_location('nairobi')
        locations = Location.objects.all()
        self.assertTrue(len(locations)==0)

class CategoryTestClass(TestCase):

    
    def setUp(self):
        self.name= Category(name="food")

    def test_instance(self):
        self.assertTrue(isinstance(self.name,Category))

    def tearDown(self):
        Category.objects.all().delete()

    def test_save_method(self):
        self.name.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category)>0)

    def test_delete_method(self):
        self.name.delete_category('food')
        category = Category.objects.all()
        self.assertTrue(len(category)==0)