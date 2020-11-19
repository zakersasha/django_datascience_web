from django.db import models


class Article(models.Model):
    event_name = models.CharField('Название события', max_length=256)
    title = models.CharField('Название', max_length=30)
    question = models.CharField('Вопрос', max_length=256)
    full_text = models.TextField('Текст')

    def __str__(self):
        return self.event_name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def get_absolute_url(self):
        return f'/applications/{self.id}'
