from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

#dream relay Story
class PostS(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
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

# dream relay illustration
class PostI(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'postI/', blank=True, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]
        
    def image_name(self):
        return self.image.name

class CommentI(models.Model):
	content = models.TextField()
	writer = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(PostI, on_delete=models.CASCADE, related_name='comments')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

# dream relay music

class PostM(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'postM/', blank=True, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]
        
    def image_name(self):
        return self.image.name

class CommentM(models.Model):
	content = models.TextField()
	writer = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(PostM, on_delete=models.CASCADE, related_name='comments')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)


#dream diary

class PostD(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 200)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    text = models.TextField()
    image = models.ImageField(upload_to = 'postD/', blank = True, null = True)


# 꿈도서관
class BlogS(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'blogS/', blank=True, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]
        
    def image_name(self):
        return self.image.name

class BlogM(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'blogM/', blank=True, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]
        
    def image_name(self):
        return self.image.name

class BlogI(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'blogI/', blank=True, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]
        
    def image_name(self):
        return self.image.name

#꿈거래소
class Shop(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    body = models.TextField()

    def summary(self):
        return self.body[:20]

class Comment_sh(models.Model):
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='comment_sh')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)