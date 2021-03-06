# Generated by Django 2.2 on 2019-04-04 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gift', '0002_auto_20190404_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='occasion',
            field=models.CharField(choices=[('All occasions', 'ALLOCCASIONS'), ('Birthday', 'BIRTHDAY'), ('Cheer Up', 'CHEERUP'), ('Congratulations', 'CONGRATULATIONS'), ('New Baby', 'NEWBABY'), ('Housewarming', 'HOUSEWARMING'), ('Breakup', 'BREAKUP'), ('Engagement', 'ENGAGEMENT'), ('Holiday', 'HOLIDAY'), ('New Job', 'NEWJOB'), ("Galentine's Day", 'GALENTINESDAY'), ('For Mom', 'FORMOM'), ('For Dad', 'FORDAD'), ('Lux Box', 'LUXBOX')], default='All Occasions', max_length=100),
        ),
        migrations.AlterField(
            model_name='giftcard',
            name='store',
            field=models.CharField(choices=[('Postmates', 'POSTMATES'), ('Starbucks', 'STARBUCKS'), ('Airline', 'AIRLINE'), ('Nordstrom', 'NORDSTROM')], default='Postmates', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='occasion',
            field=models.CharField(choices=[('All occasions', 'ALLOCCASIONS'), ('Birthday', 'BIRTHDAY'), ('Cheer Up', 'CHEERUP'), ('Congratulations', 'CONGRATULATIONS'), ('New Baby', 'NEWBABY'), ('Housewarming', 'HOUSEWARMING'), ('Breakup', 'BREAKUP'), ('Engagement', 'ENGAGEMENT'), ('Holiday', 'HOLIDAY'), ('New Job', 'NEWJOB'), ("Galentine's Day", 'GALENTINESDAY'), ('For Mom', 'FORMOM'), ('For Dad', 'FORDAD'), ('Lux Box', 'LUXBOX')], default='All Occasions', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('All Types', 'ALLTYPES'), ('Party Supply', 'PARTY SUPPLY'), ('Accessories', 'ACCESSORIES'), ('Jewelry', 'JEWELRY'), ('Houseware', 'HOUSEWARE'), ('Spa', 'SPA'), ('Candles', 'CANDLES'), ('Stationary', 'STATIONARY')], default='All Types', max_length=100),
        ),
    ]
