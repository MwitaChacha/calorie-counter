# Generated by Django 3.2.9 on 2022-02-23 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='food',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='foo', to='core.food'),
        ),
    ]