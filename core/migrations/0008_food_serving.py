# Generated by Django 3.2.9 on 2022-02-23 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_profile_food'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='serving',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
