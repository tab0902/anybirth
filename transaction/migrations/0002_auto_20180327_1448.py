# Generated by Django 2.0.3 on 2018-03-27 05:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20180327_1448'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_auto_20180327_1448'),
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='提案タイトル')),
                ('description', models.TextField(blank=True, verbose_name='提案説明文')),
                ('delivery_method', models.SmallIntegerField(verbose_name='配送方法')),
                ('payment_method', models.SmallIntegerField(verbose_name='支払方法')),
                ('price_proposal', models.IntegerField(blank=True, verbose_name='価格提案')),
                ('hand_place', models.CharField(blank=True, max_length=255, verbose_name='商品手渡し場所')),
                ('delivered_at', models.DateTimeField(blank=True, null=True, verbose_name='予定お届け日時')),
                ('status', models.SmallIntegerField(default=0, verbose_name='状態')),
                ('expired_at', models.DateTimeField(blank=True, verbose_name='掲載終了日')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Item', verbose_name='商品ID')),
                ('itinerary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Itinerary', verbose_name='旅程ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザーID')),
            ],
            options={
                'verbose_name': '提案',
                'verbose_name_plural': '提案',
            },
        ),
        migrations.AlterModelOptions(
            name='agreement',
            options={'verbose_name': '成約', 'verbose_name_plural': '成約'},
        ),
        migrations.AlterModelOptions(
            name='request',
            options={'verbose_name': '依頼', 'verbose_name_plural': '依頼'},
        ),
        migrations.RemoveField(
            model_name='agreement',
            name='arriving_at',
        ),
        migrations.AddField(
            model_name='request',
            name='delivered_request',
            field=models.DateTimeField(blank=True, null=True, verbose_name='希望お届け日時'),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='作成日時'),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='postage',
            field=models.IntegerField(default=0, verbose_name='送料'),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='price',
            field=models.IntegerField(blank=True, verbose_name='価格'),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='request',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='transaction.Request', verbose_name='依頼ID'),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='更新日時'),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザーID'),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='user_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.UserAddress', verbose_name='ユーザー住所ID'),
        ),
        migrations.AlterField(
            model_name='request',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='作成日時'),
        ),
        migrations.AlterField(
            model_name='request',
            name='delivery_method',
            field=models.SmallIntegerField(verbose_name='配送方法'),
        ),
        migrations.AlterField(
            model_name='request',
            name='description',
            field=models.TextField(blank=True, verbose_name='リクエスト説明文'),
        ),
        migrations.AlterField(
            model_name='request',
            name='expired_at',
            field=models.DateTimeField(blank=True, verbose_name='掲載終了日'),
        ),
        migrations.AlterField(
            model_name='request',
            name='hand_place',
            field=models.CharField(blank=True, max_length=255, verbose_name='商品手渡し場所'),
        ),
        migrations.AlterField(
            model_name='request',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Item', verbose_name='商品ID'),
        ),
        migrations.AlterField(
            model_name='request',
            name='payment_method',
            field=models.SmallIntegerField(verbose_name='支払方法'),
        ),
        migrations.AlterField(
            model_name='request',
            name='price_request',
            field=models.IntegerField(blank=True, verbose_name='希望価格'),
        ),
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.SmallIntegerField(default=0, verbose_name='状態'),
        ),
        migrations.AlterField(
            model_name='request',
            name='title',
            field=models.CharField(max_length=50, verbose_name='リクエストタイトル'),
        ),
        migrations.AlterField(
            model_name='request',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='更新日時'),
        ),
        migrations.AlterField(
            model_name='request',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザーID'),
        ),
        migrations.AlterField(
            model_name='request',
            name='user_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.UserAddress', verbose_name='ユーザー住所ID'),
        ),
        migrations.AddField(
            model_name='request',
            name='proposal',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='transaction.Proposal', verbose_name='提案ID'),
        ),
    ]