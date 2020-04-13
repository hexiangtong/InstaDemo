from django.db import models
from imagekit.models import ProcessedImageField
from django.urls import reverse

from django.contrib.auth.models import AbstractUser

# Create your models here.

class InstaUser(AbstractUser): #self-define user model
    profile_pic = ProcessedImageField(
        upload_to = 'static/images/profiles',
        format = 'JPEG',
        options = {'quality': 100},
        blank = True,
        null = True,
    )

    # def get_absolute_url(self):
    #     return reverse('posts', args=[str(self.id)])
    
    # def __str__(self):
    #     return self.title

class Post(models.Model):
    author = models.ForeignKey(
        InstaUser,
        on_delete = models.CASCADE,
        related_name = 'my_post'
    )
    title = models.TextField(blank=True, null=True)
    image = ProcessedImageField(
        upload_to = 'static/images/posts',
        format = 'JPEG',
        options = {'quality': 100},
        blank = True,
        null = True,
        )


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])

class Like(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name = 'likes')
    user = models.ForeignKey(
        InstaUser,
        on_delete = models.CASCADE,
        related_name = 'likes')
    
    class Meta:
        unique_together = ("post", "user")

    def __str__(self):
        return 'Like: ' + self.user.username + ' Likes ' +  self.post.title

