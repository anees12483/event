# Generated by Django 4.2.7 on 2025-01-20 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0006_alter_eventbookings_bookeddate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventbookings',
            name='expiry_date',
            field=models.DateField(blank=True, null=True, verbose_name=models.DateField()),
        ),
    ]
