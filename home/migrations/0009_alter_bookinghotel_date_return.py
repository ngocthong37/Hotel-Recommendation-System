# Generated by Django 4.2.5 on 2023-10-27 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_bookinghotel_date_return_bookinghotel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinghotel',
            name='date_return',
            field=models.DateTimeField(default='', null=True),
        ),
    ]