from django.db import models
from django.conf import settings

# Группа
# Студентов
# Родственников

class Group(models.Model):
    name = models.CharField(max_length=100, unique=True)
    course = models.PositiveSmallIntegerField()
    curator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True, 
        related_name='curated_groups',
        limit_choices_to={'role':'teacher'}
    )

    def __str__(self):
        return self.name
    

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    inn = models.CharField(max_length=14, unique=True)
    id_cart = models.CharField(max_length=9, unique=True)
    phone = models.CharField(max_length=12)
    second_phone = models.CharField(
        max_length=12, null=True, blank=True
    )
    group = models.ForeignKey(
        Group, on_delete=models.PROTECT,
        related_name='students'
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class ContactPerson(models.Model):
    
    class Relation(models.TextChoices):
        FATHER = 'father', 'Папа'
        MOTHER = 'mother', 'Мама'
        BROTHER = 'brother', 'Брат'
        SISTER = 'sister', 'Сестра'
        GRANDFATHER = 'grandfather', 'Дедушка'
        GRANDMOTHER = 'grandmother', 'Бабушка'
        UNCLE = 'uncle', 'Дядя'
        AUNT = 'aunt', 'Тётя'
        OTHER = 'other', 'Другое'

    student = models.ForeignKey(
        Student, on_delete=models.CASCADE,
        related_name='contacts'
    )
    full_name = models.CharField(max_length=255)
    relation = models.CharField(
        max_length=30, choices=Relation.choices
    )
    phone = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.full_name} ({self.relation})"