from tkinter import CASCADE
from django.db import models
from acc.models import User

# Create your models here.
class Board(models.Model):
    subject = models.CharField(max_length=100)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="writer")
    content = models.TextField()
    pubdate = models.DateTimeField()
    likey = models.ManyToManyField(User, blank=True, related_name="likely")

    def __str(self):
        return f"{self.writer}의 {self.subject}"

class Reply(models.Model):
    # board와 replyer는 각각 다른 객체를 참조하므로 충돌하지 않는다
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    replyer = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f"{self.board}에 {self.replyer}가 남긴 댓글"