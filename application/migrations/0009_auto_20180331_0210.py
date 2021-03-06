# Generated by Django 2.0.1 on 2018-03-31 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0008_auto_20180331_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='space',
            name='operational_status',
            field=models.CharField(blank=True, choices=[('In operation', 'In Operation'), ('Planned', 'Planned'), ('Closed', 'Closed')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='space',
            name='validation_status',
            field=models.CharField(blank=True, choices=[('Verified', 'Verified Address and Operation Status'), ('Flagged', 'Flagged')], max_length=8, null=True),
        ),
    ]
