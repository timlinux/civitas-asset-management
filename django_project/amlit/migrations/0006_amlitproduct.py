# Generated by Django 2.2.15 on 2021-04-17 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0007_2_4'),
        ('amlit', '0005_organisation_subscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmlitProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_user', models.IntegerField(verbose_name='Max user')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='djstripe.Product', verbose_name='Product')),
            ],
        ),
    ]