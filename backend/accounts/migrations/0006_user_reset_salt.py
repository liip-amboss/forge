# Generated by Django 3.2.4 on 2021-08-19 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_user_reset_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='reset_salt',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
