# Generated by Django 4.1 on 2022-08-16 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('identityNumber', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200, null=True)),
                ('department', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
