# Generated by Django 2.0.1 on 2018-03-31 00:27

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_auto_20180330_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='space',
            name='operational_status',
            field=models.CharField(blank=True, choices=[('OP', 'In Operation'), ('PL', 'Planned'), ('CL', 'Closed')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='space',
            name='ownership_type',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('PRI', 'Private Sector: a for-profit business, corporation, or startup'), ('NON', 'Non-Profit: a registered non-profit organization'), ('EP', 'Educational: primary school'), ('ES', 'Educational: secondary school'), ('EU', 'Educational: university'), ('EV', 'Educational: vocational school'), ('GL', 'Government: Local or Municipal'), ('GP', 'Government: Provincial'), ('GN', 'Government: National'), ('UN', 'Unincorporated'), ('LIB', 'Library')], max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='space',
            name='validation_status',
            field=models.CharField(blank=True, choices=[('VE', 'Verified Address and Operation Status'), ('FL', 'Flagged')], max_length=2, null=True),
        ),
    ]
