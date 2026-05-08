from django.db import models
from django.conf import settings


class Subject(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='subjects',
        limit_choices_to={"role":'teacher'}
    )
    
    def __str__(self):
        return self.name 
    

class Grade(models.Model):

    class Score(models.IntegerChoices):
        TWO = 2, '2'
        THREE = 3, '3'
        FOUR = 4, '4'
        FIVE = 5, '5'
    
    student = models.ForeignKey(
        'students.Student',
        on_delete=models.CASCADE,
        related_name='grades'
    )
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, 
        related_name='grades'
    )
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='given_grades',
        limit_choices_to={'role': 'teacher'}
    )
    score = models.PositiveSmallIntegerField(
        choices=Score.choices
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student} | {self.subject} | {self.score}'