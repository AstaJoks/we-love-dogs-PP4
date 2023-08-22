from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
from django.template.defaultfilters import slugify


STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    A class for the post model
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-created_on"]
    """
    Returns post title, number of likes and comments
    """
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.author) + " Blog Title: " + self.title

    def get_absolute_url(self):
        return reverse('blog')

    def number_of_likes(self):
        return self.likes.count()

    def number_of_comments(self):
        return self.comments.count()


class Comment(models.Model):
    """
    A class for the comment model
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]
    """
    Returns users name and comment
    """
    def __str__(self):
        return f"Comment {self.body} by {self.name}"
