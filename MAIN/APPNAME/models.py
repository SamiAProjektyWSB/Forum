from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django_resized import ResizedImageField
from tinymce.models import HTMLField
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from taggit.managers import TaggableManager
from django.shortcuts import reverse

User = get_user_model()

class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=40, blank=True)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    bio = HTMLField()
    profile_pic = ResizedImageField(size=[50, 80], quality=100, upload_to="authors", default="None", null=True, blank=True)

    def __str__(self):
        return self.fullname

    def save(self):
        if not self.slug:
            self.slug = slugify(self.fullname)
        super(Author, self).save()

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    discription = models.TextField(default="discription")

    class Meta:
        verbose_name_plural = "categories"
    def __str__(self):
        return self.title

    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save()

    def get_url(self):
        return reverse("posts" ,kwargs={
            "slug":self.slug
        })
    
    @property
    def num_posts(self):
        return Post.objects.filter(categores=self).count()

    @property
    def last_post(self):
        return Post.objects.filter(categores=self).latest("date")       

    


class Post(models.Model):
    title = models.CharField(max_length=400)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = HTMLField()
    categores = models.ManyToManyField(Category)
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    tags = TaggableManager()


    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save()

    def __str__(self):
        return self.title
    
    def get_url(self):
        return reverse("detail" ,kwargs={
            "slug":self.slug
        })
