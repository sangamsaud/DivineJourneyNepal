# Generated by Django 4.2.5 on 2023-09-26 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_slider_delete_slide'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='slides/')),
                ('title', models.CharField(max_length=100)),
                ('details', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Slider',
        ),
    ]
