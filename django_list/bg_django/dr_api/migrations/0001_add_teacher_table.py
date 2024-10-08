# Generated by Django 5.1.1 on 2024-09-15 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=20)),
                ('course_name', models.CharField(max_length=25)),
                ('course_duration', models.IntegerField(default=0)),
                ('seat', models.IntegerField(default=0)),
            ],
        ),
    ]
