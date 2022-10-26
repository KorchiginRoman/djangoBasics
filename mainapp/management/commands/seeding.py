from django.core.management import BaseCommand
from mainapp.models import News

#Используем множественную вставку.
class Command(BaseCommand):
    def handle(self, *args, **options):
        news_objects = []
        for i in range(5):
            news_objects.append(
                News(
                    title=f'Новость №{i}',
                    preamble=f'Заголовок к новости №{i}',
                    body=f'Случайная новость №{i}'
                )
            )
        News.objects.bulk_create(news_objects)