# Generated by Django 3.2 on 2022-05-12 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_tables', '0005_systempreference'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiningTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('total_seats', models.PositiveIntegerField()),
                ('used_seats', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['total_seats'],
            },
        ),
    ]
