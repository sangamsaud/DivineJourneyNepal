# Generated by Django 4.2.5 on 2023-09-26 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_rename_description_about_description_1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destination',
            old_name='description',
            new_name='description_1',
        ),
        migrations.AddField(
            model_name='destination',
            name='description_2',
            field=models.TextField(default=5),
            preserve_default=False,
        ),
    ]