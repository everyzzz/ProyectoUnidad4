# Generated by Django 4.1.4 on 2022-12-11 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='ip',
            name='last_connection',
            field=models.DateTimeField(auto_now=True),
        ),
    ]