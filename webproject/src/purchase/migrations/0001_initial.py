# Generated by Django 2.2.4 on 2019-08-29 08:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(max_length=100, unique=True)),
                ('quantity', models.IntegerField()),
                ('cost_price', models.FloatField(verbose_name='cost price')),
                ('current_stock_level', models.IntegerField(verbose_name='current stock level')),
                ('total_stock_level', models.IntegerField(verbose_name='total stock level')),
                ('supplier_tel', models.CharField(max_length=13, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
