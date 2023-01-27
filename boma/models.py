from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.

class NeighbourHood(models.Model):
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='hood')
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=60)
    hood_logo = models.ImageField(upload_to='photos/', default='default.png')
    description = models.TextField()
    health_tell = models.IntegerField(null=True, blank=True)
    police_number = models.IntegerField(null=True, blank=True)
    Count= models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} hood'
    def save_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighbourhood_id):
        return cls.objects.filter(id=neighbourhood_id)

    class Meta:
        # db_table = 'neighbour hoods'
        ordering = ['-id']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=80, blank=True)
    bio = models.TextField(max_length=254, blank=True)
    profile_picture = models.ImageField(upload_to='photos/', default='default.png')
    location = models.CharField(max_length=50, blank=True, null=True)
    email= models.EmailField(null=True)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)

    def __str__(self):
        return f'{self.user.username} profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profile(cls):
        profile = Profile.objects.all()

        return profile

    class Meta:
        # db_table = 'profiles'
        ordering = ['-id']


class Business(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    description = models.TextField(blank=True)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, related_name='business')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner')

    def __str__(self):
        return f'{self.name} business'

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls,search_term):
        return cls.objects.filter(name__icontains=search_term).all()
    class Meta:
        # db_table = 'businesss'
        ordering = ['-id']



class Post(models.Model):
    title = models.CharField(max_length=120, null=True)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_owner')
    hood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, related_name='hood_post')
    business = models.ManyToManyField(Business)
    def __str__(self):
        return f'{self.title} post'

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()
        
    class Meta:
        # db_table = 'posts'
        ordering = ['-id']


    

