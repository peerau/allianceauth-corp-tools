# Generated by Django 3.2.12 on 2022-02-14 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eveonline', '0015_factions'),
        ('corptools', '0068_rename_note_text_notification_notification_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='CorptoolsConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('holding_corps', models.ManyToManyField(
                    to='eveonline.EveCorporationInfo')),
            ],
            options={
                'permissions': (('holding_corp_structures', 'Can access configured holding corp structure data.'), ('holding_corp_wallets', 'Can access configured holding corp wallet data.'), ('holding_corp_asset', 'Can access configured holding corp wallet data.')),
                'default_permissions': [],
            },
        ),
    ]