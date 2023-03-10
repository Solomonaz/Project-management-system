# Generated by Django 4.1.6 on 2023-02-14 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('admin', 'admin'), ('manager', 'manager'), ('employee', 'employee')], max_length=30)),
                ('avatar', models.ImageField(upload_to='avatar')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
