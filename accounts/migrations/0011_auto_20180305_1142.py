# Generated by Django 2.0.2 on 2018-03-05 02:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20180305_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='電話番号はハイフンを除いた半角数字で入力してください。', regex='^[0-9]+$')], verbose_name='電話番号'),
        ),
    ]
