# Generated by Django 2.0.4 on 2018-04-14 07:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0019_auto_20180412_1727'),
        ('transaction', '0008_order_status_deadline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user_address',
        ),
        migrations.AddField(
            model_name='order',
            name='postage',
            field=models.IntegerField(default=0, verbose_name='送料'),
        ),
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='価格'),
        ),
        migrations.AddField(
            model_name='order',
            name='requester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requester_set', to=settings.AUTH_USER_MODEL, verbose_name='リクエスターID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='requester_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.UserAddress', verbose_name='リクエスター住所ID'),
        ),
        migrations.AddField(
            model_name='order',
            name='traveller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='traveller_set', to=settings.AUTH_USER_MODEL, verbose_name='トラベラーID'),
        ),
    ]
