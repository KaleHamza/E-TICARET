# Generated by Django 4.2.2 on 2023-06-13 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticaretSitesi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AktifKullanici',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='basket',
            field=models.JSONField(default=list, null=True),
        ),
    ]
