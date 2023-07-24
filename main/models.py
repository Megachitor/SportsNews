from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.urls import reverse
# Create your models here.


class CustomUser(AbstractUser):

    age = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to="posts/",null=True, blank=True,default="user-avatar.png")
    

    class Meta:
        verbose_name = ("CustomUser")
        verbose_name_plural = ("CustomUsers")

    def __str__(self):
        return self.username



class Club(models.Model):

    name = models.CharField("Name", max_length=50)
    code = models.CharField("Code", max_length=3)
    index = models.IntegerField("ID")
    image = models.CharField('Image', max_length=200)

    class Meta:
        verbose_name = ("Club")
        verbose_name_plural = ("Clubs")

    def __str__(self):
        return self.name



class Player(models.Model):

    name = models.CharField("Name", max_length=50)
    # surname = models.CharField("Surname", max_length=50)
    age = models.IntegerField("Age",null=True)
    number = models.IntegerField("Number", null=True)
    position = models.CharField("Position", max_length=30)
    index = models.IntegerField("Index", null=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    image = models.CharField("image", max_length=200)


    class Meta:
        verbose_name = ("Player")
        verbose_name_plural = ("Players")

    def __str__(self):
        return self.name

class News(models.Model):

    name = models.CharField('News', max_length=159)
    description = models.TextField("Description")
    # image = models.ImageField("Image", upload_to='news/', height_field=None, width_field=None, max_length=None)
    image_url = models.CharField("Image", max_length=400, default="https://www.imgacademy.com/sites/default/files/styles/scale_2500w/public/2020-08/rsz_esx_9767.jpg?itok=A4WOOH5W", null=True)
    source = models.CharField("Source", max_length=300)  
    date = models.DateTimeField("Date", auto_now=False, auto_now_add=True)
    content = models.TextField('Content')

    class Meta:
        verbose_name = ("News")
        verbose_name_plural = ("News's")

    def __str__(self):
        return self.name
    
class Post(models.Model):

    name = models.CharField("Name", max_length=200)
    description = models.TextField("Description")
    image = models.ImageField("Image", upload_to='post/', height_field=None, width_field=None, max_length=None)
    date = models.DateTimeField("date", auto_now=False, auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.name
    
class Comment(models.Model):

    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.TextField("Comment", null=True)
    date = models.DateTimeField("Date", auto_now=False, auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Comment")
        verbose_name_plural = ("Comments")

    def __str__(self):
        return self.comment
    

class Match(models.Model):

    home = models.ForeignKey(Club,  on_delete=models.CASCADE, related_name="Home")
    away = models.ForeignKey(Club,  on_delete=models.CASCADE, related_name="Away")
    date = models.DateTimeField("Date", auto_now=False, auto_now_add=False)
    index = models.IntegerField('Index')

    class Meta:
        verbose_name = ("Match")
        verbose_name_plural = ("Matchs")

    def __str__(self):
        return f'{self.home} -- {self.away} at: {self.date}'
    

class Standings(models.Model):

    rank = models.IntegerField("Rank")
    team = models.ForeignKey(Club, on_delete=models.CASCADE)
    played = models.IntegerField('Played')
    won = models.IntegerField('won')
    lost = models.IntegerField('lost')

    class Meta:
        verbose_name = ("Standings")
        verbose_name_plural = ("Standingss")

    def __str__(self):
        return f'{self.rank} -- {self.team}'



class Contact(models.Model):

    name = models.CharField("Name", max_length=50)
    email = models.EmailField("Email", max_length=254)
    address = models.CharField("Address", max_length=50)
    content = models.TextField("Content")


    class Meta:
        verbose_name = ("Contact")
        verbose_name_plural = ("Contacts")

    def __str__(self):
        return self.name

class LastUpdated(models.Model):

    name = models.CharField("Name of function", max_length=50)
    time = models.DateTimeField("DateTime", auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = ("LastUpdated")
        verbose_name_plural = ("LastUpdateds")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("LastUpdated_detail", kwargs={"pk": self.pk})



