# Generated by Django 3.1.2 on 2020-12-16 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20201216_1954'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GPA', models.FloatField()),
                ('Term', models.CharField(default='Fall', max_length=50)),
                ('student_level', models.IntegerField(default=1)),
            ],
        ),
    ]
