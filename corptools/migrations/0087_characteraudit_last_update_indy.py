# Generated by Django 4.0.10 on 2023-05-22 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corptools', '0086_characterindustryjob'),
    ]

    operations = [
        migrations.AddField(
            model_name='characteraudit',
            name='last_update_indy',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]