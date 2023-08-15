from django.db import models

# Create your models here.
class Board(models.Model):
    board_index = models.IntegerField()
    board_title = models.CharField(max_length=1000)
    board_type = models.CharField(max_length=1000)
    board_contents = models.TextField()
    board_date = models.DateTimeField()
    user_id = models.CharField(max_length=1000)