# Generated by Django 3.2 on 2022-05-12 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_tables', '0002_auto_20220512_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuffetPeriods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(unique=True)),
            ],
        ),
    ]
