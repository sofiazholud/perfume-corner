# Generated by Django 5.1.2 on 2024-10-14 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfume',
            name='image',
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to='images/'
            ),
        ),
    ]
