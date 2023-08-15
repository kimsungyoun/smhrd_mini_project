from django.db import models

# Create your models here.

class News(models.Model):
    news_index = models.BigAutoField(primary_key=True)
    news_name = models.CharField(max_length=512, blank=True, null=True)
    news_content = models.CharField(max_length=1024, blank=True, null=True)
    news_href = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news'