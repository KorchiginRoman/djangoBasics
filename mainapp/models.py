from django.contrib.auth import get_user_model
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    deleted = models.BooleanField(default=False, verbose_name='Удалён')

    class Meta:
        abstract = True
        ordering = ('-created_at',)

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()


class NewsManager(models.Manager):

    def delete(self):
        pass

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class News(BaseModel):
    #objects = NewsManager()

    title = models.CharField(max_length=256, verbose_name='Заголовок')
    preamble = models.CharField(max_length=512, verbose_name='Вступление')
    body = models.TextField(verbose_name='Содержание')
    body_as_markdown = models.BooleanField(default=False, verbose_name='Разметка в формате Markdown')

    def __str__(self):
        return f'#{self.pk} {self.title}'

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'


class Course(BaseModel):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')

    cost = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Стоимость', default=0)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(BaseModel):

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    num = models.PositiveIntegerField(default=0, verbose_name='Номер урока')

    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'#{self.num}{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class CourseTeacher(BaseModel):
    course = models.ManyToManyField(Course)
    first_name = models.CharField(max_length=256, verbose_name='Имя')
    last_name = models.CharField(max_length=256, verbose_name='Фамилия')

    def __str__(self):
        return f'{self.first_name}{self.last_name}'

    class Meta:
        verbose_name = 'курс у учителю'
        verbose_name_plural = 'курсы к учителям'


class CourseFeedback(BaseModel):
    RATINGS = (
        (5, '⭐⭐⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (3, '⭐⭐⭐'),
        (2, '⭐⭐'),
        (1, '⭐'),
    )

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Пользователь')
    rating = models.SmallIntegerField(choices=RATINGS, default=5, verbose_name='Рейтинг')
    feedback = models.TextField(verbose_name='Отзыв', default='Без отзыва')

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''

    def __str__(self):
        return f'Отзыв на {self.course} от {self.user}'

