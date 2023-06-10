# Generated by Django 4.2.2 on 2023-06-10 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('surname', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(max_length=30)),
                ('Current', models.FloatField()),
                ('adresses', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=400)),
                ('color', models.CharField(max_length=20)),
                ('imageUrl', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('categories', models.ManyToManyField(to='ticaretSitesi.category')),
            ],
        ),
    ]
