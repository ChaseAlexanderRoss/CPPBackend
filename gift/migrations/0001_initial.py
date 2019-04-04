# Generated by Django 2.2 on 2019-04-04 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('street_1', models.CharField(max_length=100)),
                ('street_2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('zip_code', models.IntegerField()),
                ('state', models.CharField(max_length=2)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('total_cost', models.IntegerField()),
                ('shipping_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipping_address', to='gift.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('credit_card_num', models.IntegerField()),
                ('credit_card_sec_code', models.IntegerField()),
                ('credit_card_exp_date', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('picture', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('occasion', models.CharField(max_length=100)),
                ('product_type', models.CharField(max_length=100)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_item_id', to='gift.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('box_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_box_id', to='gift.Box')),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_item_id', to='gift.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Giftcard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='giftcard_item_id', to='gift.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('picture', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('occasion', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=200)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card_item_id', to='gift.Item')),
            ],
        ),
    ]