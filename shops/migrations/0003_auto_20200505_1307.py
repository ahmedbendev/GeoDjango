# Generated by Django 3.0.5 on 2020-05-05 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0002_auto_20200424_0517'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='shopimg',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
        migrations.AddField(
            model_name='shop',
            name='shopkeeper',
            field=models.CharField(default='shopkeeper', max_length=100),
        ),
    ]
