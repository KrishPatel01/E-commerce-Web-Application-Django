# Generated by Django 3.2 on 2021-07-19 09:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('Fashion', 'Fashion'), ('Electronics', 'Electronics'), ('Appliances', 'Appliances'), ('Mobiles', 'Mobiles')], max_length=15)),
                ('subcategory', models.CharField(default='', max_length=50)),
                ('brand', models.CharField(default='', max_length=50)),
                ('description', models.TextField()),
                ('price', models.IntegerField(default=0)),
                ('slug', models.CharField(max_length=150)),
                ('publish_date', models.DateField()),
                ('image', models.ImageField(default='loading', upload_to='kdstore/images')),
            ],
        ),
        migrations.CreateModel(
            name='ProductRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(default='0')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kdstore.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductComment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('timeStamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kdstore.productcomment')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kdstore.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head1', models.TextField(max_length=100)),
                ('head2', models.TextField(max_length=100)),
                ('offers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kdstore.product')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=10)),
                ('subject', models.CharField(default='', max_length=100)),
                ('message', models.CharField(default='', max_length=1000)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderId', models.CharField(max_length=50)),
                ('orderItem', models.CharField(max_length=5000)),
                ('amount', models.IntegerField(default='')),
                ('email', models.CharField(max_length=111)),
                ('address', models.CharField(max_length=111)),
                ('state', models.CharField(max_length=111)),
                ('zip_code', models.CharField(max_length=100)),
                ('phone', models.CharField(default='', max_length=111)),
                ('orderTime', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
