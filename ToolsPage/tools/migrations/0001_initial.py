# Generated by Django 5.0.3 on 2024-04-04 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english_name', models.CharField(max_length=100)),
                ('english_description', models.CharField(max_length=200)),
                ('spanish_name', models.CharField(max_length=100)),
                ('spanish_description', models.CharField(max_length=200)),
                ('tool_image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
