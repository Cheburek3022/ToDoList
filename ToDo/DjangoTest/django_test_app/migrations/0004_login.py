# Generated by Django 5.0 on 2024-07-18 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_test_app', '0003_task_delete_author_delete_book_remove_comment_post_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=18)),
            ],
        ),
    ]
