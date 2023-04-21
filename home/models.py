from django.db import models


class Lesson(models.Model):
    img = models.FileField('')
    number_lesson = models.IntegerField(verbose_name='Номер урока')
    desc = models.TextField()

    def __str__(self):
        return f"Урок {self.number_lesson}"

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Form(models.Model):
    email = models.EmailField()
    name = models.TextField()
    number = models.TextField()

    def __str__(self):
        return f"{self.email} {self.name} {self.number}"

    class Meta:
        verbose_name = 'Форма'
        verbose_name_plural = 'Форма'