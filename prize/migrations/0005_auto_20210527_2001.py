# Generated by Django 3.1.5 on 2021-05-27 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prize', '0004_remove_laureate_affiliation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='laureate',
            old_name='firtname',
            new_name='firstname',
        ),
    ]
