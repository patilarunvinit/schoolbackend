# Generated by Django 3.2.10 on 2024-01-19 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0003_alter_compmodel_complaint_date1'),
    ]

    operations = [
        migrations.AddField(
            model_name='compmodel',
            name='mobile_no',
            field=models.IntegerField(null=True),
        ),
    ]
