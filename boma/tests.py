from django.test import TestCase
from.models import *

# Create your tests here.
class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.user = User(username='sandra')
        self.user.save()

        self.profile_test = Profile(id=1, user=self.user , profile_picture='default.jpg', bio='this is a test profile',
                                    location='Nairobi',email='email')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))

    def test_save_profile(self):
        self.profile_test.save_profile()
        after = Profile.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_profile(self):
        self.profile_test.delete_profile()
        after = Profile.objects.all()
        self.assertTrue(len(after) == 0)

class NeighbourhoodTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='sandra')
        self.neighbourhood = NeighbourHood.objects.create(id=1, name='pipeline', hood_logo='https://ucarecdn.com/0ccf61ff-508e-46c6-b713-db51daa6626e', description='desc',
                                        user=self.user, health_tell='+254',police_number='999',Count='20000')
    
    
        self.neigbourhood_test = NeighbourHood(id=1, user=self.user , hood_logo='default.jpg', description='desc',
                                    name='pipeline',health_tell='+254',police_number='999',Count='20000')
                                    
    def test_instance(self):
        self.assertTrue(isinstance(self.name, NeighbourHood))
    
    def test_save_neighbourhood(self):
        self.neighbourhood_test.save_neighbourhood()
        hoods = NeighbourHood.objects.all()
        self.assertTrue(len(hoods) > 0)

    def test_delete_neighbourhood(self):
        self.neighbourhood_test.delete_neighbourhood()
        hoods = NeighbourHood.objects.all()
        self.assertTrue(len(hoods)==0)

class BusinessTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='sandra')
        self.business = Business.objects.create(id=1, name='vege fresh',description='fresh veges for sale',email='sadindi03@gmail.com',
                                        user=self.user)
    
    
        self.business_test = Business(id=1, user=self.user , name='veges',description='fresh veges for sale',email='sadindi03@gmail.com',)
    
    def test_create_business(self):
        self.business_test.create_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) > 0) 

    def test_delete_business(self):
        self.business_test.delete_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) == 0) 

class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='sandra')
        self.post = Post.objects.create(id=1,title='test post', post='test post',
                                        user=self.user)
        self.post_test = Post.objects.create(id=1,title='test post', post='test post',
                                        user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_save_post(self):
        self.post_test.save_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts) > 0)

    def test_delete_post(self, id):
        self.post_test.delete_post()
        posts = Post.get_posts(posts_id=id)
        self.assertTrue(len(posts) == 0)                              


