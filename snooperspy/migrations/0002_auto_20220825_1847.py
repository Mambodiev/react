# Generated by Django 3.2 on 2022-08-25 18:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('snooperspy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('male', models.IntegerField(default=0)),
                ('female', models.IntegerField(default=0)),
                ('unknown', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Gender',
            },
        ),
        migrations.RenameModel(
            old_name='TopCustomerCountries',
            new_name='Countries',
        ),
        migrations.AlterModelOptions(
            name='countries',
            options={'verbose_name_plural': 'Countries'},
        ),
        migrations.RenameField(
            model_name='countries',
            old_name='competiton',
            new_name='countries',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='top_customer_countries',
            new_name='countries',
        ),
        migrations.RemoveField(
            model_name='product',
            name='competitor_meter',
        ),
        migrations.RemoveField(
            model_name='product',
            name='facebook_target_area',
        ),
        migrations.RemoveField(
            model_name='product',
            name='number_of_store_selling',
        ),
        migrations.RemoveField(
            model_name='product',
            name='orders',
        ),
        migrations.RemoveField(
            model_name='product',
            name='orders_statistics',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_insights',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_insights_rating',
        ),
        migrations.RemoveField(
            model_name='product',
            name='total_sales',
        ),
        migrations.RemoveField(
            model_name='product',
            name='view_facebook_ads',
        ),
        migrations.RemoveField(
            model_name='product',
            name='view_on_amazon',
        ),
        migrations.RemoveField(
            model_name='product',
            name='view_on_youtube',
        ),
        migrations.RemoveField(
            model_name='product',
            name='view_pinterest_ads',
        ),
        migrations.RemoveField(
            model_name='product',
            name='view_tiktok_ads',
        ),
        migrations.AddField(
            model_name='product',
            name='kind_ads',
            field=models.CharField(blank=True, help_text='FaceBook, Instagram, tiktok...', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='likes',
            field=models.IntegerField(default=0, help_text='Amount of likes generated'),
        ),
        migrations.AddField(
            model_name='product',
            name='media_ads',
            field=models.CharField(blank=True, help_text='Video, Photo, both', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='number_of_suppliers',
            field=models.IntegerField(default=0, help_text='Number of suppliers we get for this product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_cost',
            field=models.IntegerField(default=0, help_text='Price pay to buy this product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='profit_margin',
            field=models.IntegerField(default=0, help_text='Profit you get from this product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='First time we saw this ads'),
        ),
        migrations.AlterField(
            model_name='product',
            name='selling_price',
            field=models.IntegerField(default=0, help_text='Price you can sell this product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(help_text='This refer to the name of the product', max_length=250),
        ),
        migrations.AlterField(
            model_name='product',
            name='we_found',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='This ads wa created between'),
        ),
        migrations.DeleteModel(
            name='CompetitorMeter',
        ),
        migrations.DeleteModel(
            name='FacebookTargetArea',
        ),
        migrations.DeleteModel(
            name='OrdersStatistics',
        ),
        migrations.DeleteModel(
            name='ProductInsights',
        ),
        migrations.DeleteModel(
            name='ProductInsightsRating',
        ),
        migrations.AddField(
            model_name='product',
            name='gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='snooperspy.gender'),
        ),
    ]
