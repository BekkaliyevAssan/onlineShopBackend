# Generated by Django 3.0.4 on 2020-04-25 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=500)),
                ('phoneNumber', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=500)),
            ],
        ),
    ]
