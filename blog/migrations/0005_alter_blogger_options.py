# Generated by Django 4.0.2 on 2022-02-10 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blogger_date_of_birth'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogger',
            options={'ordering': ['last_name']},
        ),
    ]
