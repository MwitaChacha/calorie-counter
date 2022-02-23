# Generated by Django 3.2.9 on 2022-02-20 20:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_alter_user_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Profile',
        ),
        migrations.AlterField(
            model_name='food',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eater', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='meal',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eatee', to=settings.AUTH_USER_MODEL),
        ),
    ]