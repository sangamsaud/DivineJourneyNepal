# Generated by Django 4.2.5 on 2023-09-26 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_packagedetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='media')),
                ('url', models.URLField(blank=True, max_length=500)),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Slide',
        ),
    ]
