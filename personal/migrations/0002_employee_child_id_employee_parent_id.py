# Generated by Django 4.1.3 on 2022-11-02 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='child_id',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='employee',
            name='parent_id',
            field=models.PositiveIntegerField(default=1),
        ),
    ]