# Generated by Django 3.2.5 on 2021-07-14 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='classification',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='description',
            field=models.TextField(blank=True, default='No Description', max_length=1000, null=True),
        ),
    ]
