# Generated by Django 4.1.3 on 2022-11-23 21:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0002_course_lesson_courseteacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='course',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Удалён'),
        ),
        migrations.AlterField(
            model_name='course',
            name='update_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения'),
        ),
        migrations.AlterField(
            model_name='courseteacher',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='courseteacher',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Удалён'),
        ),
        migrations.AlterField(
            model_name='courseteacher',
            name='update_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Удалён'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='update_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения'),
        ),
        migrations.AlterField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='news',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Удалён'),
        ),
        migrations.AlterField(
            model_name='news',
            name='update_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения'),
        ),
        migrations.CreateModel(
            name='CourseFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')),
                ('deleted', models.BooleanField(default=False, verbose_name='Удалён')),
                ('rating', models.SmallIntegerField(choices=[(5, '⭐⭐⭐⭐⭐'), (4, '⭐⭐⭐⭐'), (3, '⭐⭐⭐'), (2, '⭐⭐'), (1, '⭐')], default=5, verbose_name='Рейтинг')),
                ('feedback', models.TextField(default='Без отзыва', verbose_name='Отзыв')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.course', verbose_name='Курс')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
    ]
