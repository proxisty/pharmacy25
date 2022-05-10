# Generated by Django 4.0.4 on 2022-05-09 14:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания статьи')),
                ('title', models.CharField(blank=True, default='', max_length=100, verbose_name='Заголовок статьи')),
                ('body', models.TextField(blank=True, default='', verbose_name='Текст статьи')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='Автор статьи')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
