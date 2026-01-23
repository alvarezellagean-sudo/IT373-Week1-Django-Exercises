from django.db import models

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


class Attachment(models.Model):
    announcement = models.ForeignKey(Announcement, related_name='attachments', on_delete=models.CASCADE)
    file = models.FileField(upload_to='attachments/')
