# Generated by Django 4.2.1 on 2023-06-06 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='sinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=60)),
                ('mother', models.CharField(max_length=15)),
                ('class_div', models.CharField(max_length=10)),
                ('roll_no', models.CharField(max_length=5)),
                ('reg_no', models.CharField(max_length=30)),
                ('mobile_no', models.CharField(max_length=13)),
                ('b_day', models.DateField()),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='tt',
        ),
    ]