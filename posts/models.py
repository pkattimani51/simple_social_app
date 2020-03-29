from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from groups.models import Group
# import misaka

User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    created_at = models.DateTimeField(auto_now=True)
    group = models.ForeignKey(Group, related_name='posts', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse('posts:single', kwargs={'username': self.user.username, 'pk': self.pk})

    # def save(self, *args, **kwargs):
    #     self.message_html = misaka.html(self.message)
    #     super().save(*args, **kwargs)

    class Meta:
        unique_together = ['user', 'message']
        ordering = ['-created_at']

