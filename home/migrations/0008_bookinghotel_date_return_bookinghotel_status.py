# Generated by Django 4.2.5 on 2023-10-27 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_bookinghotel_booking_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinghotel',
            name='date_return',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='bookinghotel',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]