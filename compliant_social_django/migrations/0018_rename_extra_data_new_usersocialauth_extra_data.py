# Generated by Django 4.0 on 2023-06-10 07:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("compliant_social_django", "0017_remove_usersocialauth_extra_data"),
    ]

    operations = [
        migrations.RenameField(
            model_name="usersocialauth",
            old_name="extra_data_new",
            new_name="extra_data",
        ),
        migrations.RenameField(
            model_name="partial",
            old_name="data_new",
            new_name="data",
        ),
    ]
