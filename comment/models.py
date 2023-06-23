from django.db import models


# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=False)
    comment = models.TextField()
    post_time = models.DateTimeField(auto_now_add=True)
    reply = models.BooleanField(default=False)

    def __str__(self):
        return str(self.email) + "(" + str(self.post_time) + ")"
