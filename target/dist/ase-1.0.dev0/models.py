from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                self).get_queryset()\
                        .filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (
            ('draft', 'Draft'),
            ('published', 'Published'),
            )
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250,
            unique_for_date='publish', default='post')
    text = models.TextField()
    created_date = models.DateTimeField(
            auto_now_add=True)
    published_date = models.DateTimeField(
            default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
            choices=STATUS_CHOICES,
            default='draft')
    objects = models.Manager()
    published = PublishedManager()
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                args=[self.published_date.year,
                    self.published_date.strftime('%m'),
                    self.published_date.strftime('%d'),
		    self.slug])
