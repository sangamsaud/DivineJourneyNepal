# Generated by Django 4.2.5 on 2023-09-26 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_rename_description_destination_description_1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description_1', models.TextField()),
                ('description_2', models.TextField()),
            ],
        ),
    ]
