# Generated by Django 4.0.2 on 2022-02-18 10:43

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_blog_options_alter_blog_pub_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 18, 15, 43, 15, 177596)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 18, 15, 43, 15, 178066)),
        ),
    ]
