from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PostS(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'postS/', blank=True, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]

    def image_name(self):
        return self.image.name

class CommentS(models.Model):
	content = models.TextField()
	writer = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(PostS, on_delete=models.CASCADE, related_name='comments')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)


