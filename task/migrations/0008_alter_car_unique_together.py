# Generated by Django 4.1.5 on 2023-02-02 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_alter_car_options'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='car',
            unique_together={('type_of_car', 'model')},
        ),
    ]
