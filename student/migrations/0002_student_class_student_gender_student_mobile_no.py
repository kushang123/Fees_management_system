# Generated by Django 4.1.4 on 2023-01-06 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Class',
            field=models.IntegerField(default='4'),
        ),
        migrations.AddField(
            model_name='student',
            name='Gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('Other', 'Other')], default='Other', max_length=5),
        ),
        migrations.AddField(
            model_name='student',
            name='Mobile_no',
            field=models.IntegerField(default='1234567890'),
        ),
    ]