# Generated by Django 4.1.4 on 2023-01-10 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_student_class_student_gender_student_mobile_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='fees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Class', models.IntegerField()),
                ('fees', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='Gender',
            field=models.CharField(default='Other', max_length=10),
        ),
    ]
