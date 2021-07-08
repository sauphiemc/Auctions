# Generated by Django 3.2.3 on 2021-06-30 17:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_remove_activelisting_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='articletype',
            name='img_type',
            field=models.URLField(default='google.com'),
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_w', models.BooleanField(default=False)),
                ('activelisting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.activelisting')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]