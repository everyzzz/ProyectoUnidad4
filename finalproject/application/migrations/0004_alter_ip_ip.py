# Generated by Django 4.1.4 on 2022-12-11 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_ip_last_connection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ip',
            name='ip',
            field=models.CharField(max_length=20),
        ),
    ]
