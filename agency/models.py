from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator, MaxValueValidator,RegexValidator
from django.utils.timezone import timezone
from tinymce.widgets import TinyMCE
from tinymce.models import HTMLField
from django.utils.timezone import now
# Create your models here.

order_status = [
        ('Pending', 'pending'),
        ('accept','accept'),
        ('Indevelop', 'Indevelop'),
        ('completed', 'completed'),
        ('delivered', 'delivered'),
    ]

order_pakage = [
        ('basic', 'Basic'),
        ('standard','Standard'),
        ('prenium', 'Orenium'),

    ]

service_type=[
        ('vedio_editing', 'vedio_editing'),
        ('Post-production','post-production'),

]

running_time=[
    ("5 min","5 min"),
    ("10 min","10 min"),
    ("15 min","15 min"),
    ("20 min","20 min"),
    ("30 min","30 min"),
]

class MyProfile(models.Model):
    name = models.CharField(max_length = 100)
    user = models.OneToOneField(to=User, on_delete=CASCADE)
    age = models.IntegerField(default=18, validators=[MinValueValidator(18)])
    city=models.CharField(max_length=250,null=True,default="")
    zipcode=models.CharField(max_length=250 , null=True)
    address = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, default="single", choices=(("single","single"), ("married","married"), ("widow","widow"), ("seprated","seprated"), ("commited","commited")))
    gender = models.CharField(max_length=20, default="female", choices=(("male","male"), ("female","female")))
    phone_no = models.CharField(max_length=15, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    pic=models.ImageField(upload_to = "", null=True)

    def __str__(self):
        return "%s" % self.user

class orders(models.Model):
    client = models.ForeignKey(MyProfile , on_delete=models.CASCADE)
    service = models.CharField(max_length=100 ,choices=service_type)
    package = models.CharField(max_length=200, choices=order_pakage)
    run_time=models.CharField(max_length=100 ,choices=running_time)
    video = models.FileField(upload_to='videos')
    sample_video = models.FileField(upload_to='videos')
    finish_date = models.DateField()
    time= models.DateTimeField(auto_now_add=True)
    Requirments = HTMLField()
    status=models.CharField(max_length=200,choices=order_status ,default='Pending' )
    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'


    @property
    def user_name(self):
        return self.client.user.username
    def __str__(self):
        return self.service