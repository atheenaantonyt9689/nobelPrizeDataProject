# Generated by Django 3.1.5 on 2021-05-28 06:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('prize', '0008_remove_laureate_affiliation'),
    ]

    operations = [
        migrations.AddField(
            model_name='laureate',
            name='affiliation',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='laureate',
            name='firstname',
            field=models.CharField(default='', editable=False, max_length=100),
        ),
    ]
