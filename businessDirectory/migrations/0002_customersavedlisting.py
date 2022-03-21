# Generated by Django 3.1.5 on 2022-02-26 08:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('businessDirectory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerSavedListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saved_at', models.DateTimeField(auto_now_add=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='businessDirectory.business')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]