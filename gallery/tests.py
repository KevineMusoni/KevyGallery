from django.test import TestCase
from .models import Location, Category, Image

# Create your tests here.

class LocationTestClass(TestCase):

    # Testing location and its functions

    #Set up method
    def setUp(self):
        self.locale = Location(id='1',location='rwanda',)

    def test_instance(self):
        self.assertTrue(isinstance(self.locale, Location))

    def test_save_method(self):
        # test for checking whether the location saves
        self.locale.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        # test for location delete function
        self.locale.save_location()
        locations = Location.objects.all()
        self.locale.delete_location()
        self.assertTrue(len(locations) == 0)
    
    def test_update_method(self):
        """
        Function to test that a location's details can be updates
        """
        self.locale.save_location()
        new_place = Location.objects.filter(location='rwanda').update(location='rwanda')
        locations = Location.objects.get(location='rwanda')
        self.assertTrue(locations.location, 'rwanda')


class CategoryTestClass(TestCase):
# Test for category function

    #Set up method

    def setUp(self):
        self.cat = Category(id='1',category='nature')
    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.cat, Category))
    
    def test_save_method(self):
        """
        Function to test that category is being saved
        """
        self.cat.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_method(self):
        """
        Function to test that a category can be deleted
        """
        self.cat.save_category()
        self.cat.delete_category()

    def test_update_method(self):
        """
        Function to test that a category's details can be updates
        """
        self.cat.save_category()
        new_cat = Category.objects.filter(category='nature').update(category='nature')
        categories = Category.objects.get(category='nature')
        self.assertTrue(categories.category, 'nature')


class ImageTestClass(TestCase):
    """
    Tests Image class and its functions
    """
    #Set up method
    def setUp(self):
        #creating a new location and saving it
        self.locale = Location(location='rwanda')
        self.locale.save_location()

        #creating a new category and saving it
        self.cat = Category(category='nature')
        self.cat.save_category()

        #creating an new image 
        self.image = Image(id='1', image_name='name', description ='this photo', location=self.locale, photo='test.jpg')

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_save_method(self):
        """
        Function to test an image and its details is being saved
        """
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_method(self):
        """
        Function to test if an image can be deleted
        """
        self.image.save_image()
        self.image.delete_image()

    def test_update_method(self):
    #    testing image upgates
        self.image.save_image()
        new_image = Image.objects.filter(photo='test.jpg').update(photo='banana.jpg')
        images = Image.objects.get(photo='banana.jpg')
        self.assertTrue(images.photo, 'banana.jpg')

    def test_get_image_by_id(self):
        """
        Function to test if you can get an image by its id
        """
        self.image.save_image()
        this_img= self.image.get_image_by_id(self.image.id)
        image = Image.objects.get(id=self.image.id)
        self.assertTrue(this_img, image)

    def test_filter_by_location(self):
        """
        Function to test if you can get an image by its location
        """
        self.image.save_image()
        this_img = self.image.filter_by_location(self.image.location)
        image = Image.objects.filter(location=self.image.location)
        self.assertTrue(this_img, image)