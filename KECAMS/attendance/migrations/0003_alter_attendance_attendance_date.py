# Generated by Django 4.2.4 on 2023-09-09 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_alter_attend_pic_attend_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='attendance_date',
            field=models.DateField(),
        ),
    ]