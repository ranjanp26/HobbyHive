# Generated by Django 5.1.3 on 2024-12-10 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hhHobbies", "0001_initial"),
        ("hhMain", "0004_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="hobbies",
            field=models.ManyToManyField(
                blank=True, related_name="profiles", to="hhHobbies.hobby"
            ),
        ),
    ]
