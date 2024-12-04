# Generated by Django 4.0.2 on 2022-06-17 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('introduction', '0017_cf_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cf_user',
            name='password2',
            field=models.CharField(default='ok', max_length=64),
            preserve_default=False,
        ),
        migrations.RunSQL(
            "INSERT INTO introduction_cf_user (username, password, password2) VALUES "
            "('alex', '9d6edee6ce9312981084bd98eb3751ee', '2a280ba4ff0f8c763c5b0606f40effc3319dbc4c91d4361a39990292d4b7b0cd'),"
            "('admin', 'c93ccd78b2076528346216b3b2f701e6', 'd953b4a47ce307fcb8b1b85fc6a0d34aea5585b6ad9188beb94c1eea9bbb5c7a'),"
            "('rupak', '5ee3547adb4481902349bdd0f2ffba93', 'c17cde8d179a37cad4bd93e55355fdf240eb52d585e428c1cdfecc68123e192a');"
        ),
    ]