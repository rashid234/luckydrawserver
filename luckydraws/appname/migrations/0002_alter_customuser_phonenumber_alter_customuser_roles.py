# Generated by Django 4.2.2 on 2023-12-17 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phonenumber',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='roles',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
