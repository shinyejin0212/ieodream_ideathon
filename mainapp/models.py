from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
import os
# Create your models here.

#dream relay Story
class PostS(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'postS/', blank=True, null=True)
    like_user_set = models.ManyToManyField(User, blank=True, related_name='likes_user_setS',through='Like')

    @property
    def like_count(self):
        return self.like_user_set.count()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]
        
    def image_name(self):
        return self.image.name

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostS, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together =(('user','post'))


class CommentS(models.Model):
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostS, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    image = models.ImageField(upload_to = 'commentS/', blank=True, null=True)
    
    

# dream relay illustration
class PostI(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'postI/', blank=True, null=True)
    like_user_set = models.ManyToManyField(User, blank=True, related_name='likes_user_setI',through='LikeI')

    @property
    def like_count(self):
        return self.like_user_set.count()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]
        
    def image_name(self):
        return self.image.name

class LikeI(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostI, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together =(('user','post'))

class CommentI(models.Model):
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostI, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    image = models.ImageField(upload_to = 'commentI/', blank=True, null=True)

# dream relay music

class PostM(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'postM/', blank=True, null=True)
    # document = models.FileField('음악파일', upload_to='postM//', null=True) #음악첨부파일

    like_user_set = models.ManyToManyField(User, blank=True, related_name='likes_user_setM',through='LikeM')

    @property
    def like_count(self):
        return self.like_user_set.count()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]
        
    def image_name(self):
        return self.image.name
    
    # def document_name(self):
    #     return os.path.basename(self.document.name)

class LikeM(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostM, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together =(('user','post'))


class CommentM(models.Model):
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostM, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    image = models.ImageField(upload_to = 'commentM/', blank=True, null=True)


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
    pub_date = models.DateTimeField(auto_now_add = True)
    body = models.TextField()
    image = models.ImageField(upload_to = 'blogS/', blank=True, null=True)
    comment = models.TextField()
    like_user_set = models.ManyToManyField(User, blank=True, related_name='likes_user_setSL',through='LikeSL')

    @property
    def like_count(self):
        return self.like_user_set.count()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]
        
    def image_name(self):
        return self.image.name
##
class LikeSL(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogS, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together =(('user','post'))


class BlogM(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add = True)
    body = models.TextField()
    image = models.ImageField(upload_to = 'blogM/', blank=True, null=True)
    final = models.ImageField(upload_to = 'blogM/', blank=True, null=True)
    like_user_set = models.ManyToManyField(User, blank=True, related_name='likes_user_setML',through='LikeML')

    @property
    def like_count(self):
        return self.like_user_set.count()
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]
        
    def image_name(self):
        return self.image.name

class LikeML(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogM, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together =(('user','post'))


class BlogI(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add = True)
    body = models.TextField()
    image = models.ImageField(upload_to = 'blogI/', blank=True, null=True)
    final = models.ImageField(upload_to = 'blogI/', blank=True, null=True)

    like_user_set = models.ManyToManyField(User, blank=True, related_name='likes_user_setIL',through='LikeIL')

    @property
    def like_count(self):
        return self.like_user_set.count()
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]
        
    def image_name(self):
        return self.image.name

class LikeIL(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogI, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together =(('user','post'))

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

#Post별로 ..라이크..디스라이크 구현,,,
# class Like(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         unique_together =(('user', 'post'))
