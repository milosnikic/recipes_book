# Generated by Django 4.0.4 on 2022-05-09 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0003_alter_rating_recipe_alter_rating_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='user',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='recipts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to=settings.AUTH_USER_MODEL),
        ),
    ]
