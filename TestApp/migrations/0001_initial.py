# Generated by Django 3.2.8 on 2021-10-25 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='table1',
            fields=[
                ('tb1Id', models.AutoField(primary_key=True, serialize=False)),
                ('tb1Name', models.CharField(max_length=500)),
            ],
        ),
    ]
