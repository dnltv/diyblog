# Generated by Django 4.0.2 on 2022-02-18 10:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_blog_pub_date_alter_comment_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 18, 15, 45, 34, 473618)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 18, 15, 45, 34, 474214)),
        ),
    ]