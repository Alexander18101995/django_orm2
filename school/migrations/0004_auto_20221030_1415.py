# Generated by Django 3.1.2 on 2022-10-30 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_auto_20221030_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teacher',
            field=models.ManyToManyField(related_name='teachers', to='school.Teacher', verbose_name='Учителя'),
        ),
    ]