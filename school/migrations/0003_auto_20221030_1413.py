# Generated by Django 3.1.2 on 2022-10-30 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20221030_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teacher',
            field=models.ManyToManyField(related_name='students', to='school.Teacher', verbose_name='Учитель'),
        ),
    ]