# Generated by Django 2.2.5 on 2022-04-24 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.ImageField(db_index=True, upload_to='uploadedimages/', verbose_name='Путь до изображения')),
            ],
        ),
    ]
