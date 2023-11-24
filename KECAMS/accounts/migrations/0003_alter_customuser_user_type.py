# Generated by Django 4.2.4 on 2023-09-09 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_user_type_alter_student_admin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.IntegerField(choices=[(2, 'TEACHER'), (3, 'STUDENT'), (1, 'HOD')], default=1),
        ),
    ]