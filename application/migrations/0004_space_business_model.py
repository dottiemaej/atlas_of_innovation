# Generated by Django 2.0.1 on 2018-03-28 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_space_validation_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='space',
            name='business_model',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
