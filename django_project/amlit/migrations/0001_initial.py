# Generated by Django 2.2.15 on 2020-09-11 05:31

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='Administrative code', max_length=128, unique=True)),
                ('name', models.CharField(max_length=512)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'community',
            },
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('description', models.TextField(blank=True, null=True)),
                ('value', models.IntegerField()),
            ],
            options={
                'db_table': 'condition',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'configuration',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('description', models.TextField(blank=True, null=True)),
                ('code', models.CharField(max_length=512)),
            ],
            options={
                'db_table': 'currency',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Deterioration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('description', models.TextField(blank=True, null=True)),
                ('equation', models.CharField(max_length=512)),
            ],
            options={
                'db_table': 'deterioration',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='FeatureClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'asset_class',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='FeatureLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(blank=True, help_text='unique asset ID', max_length=256, null=True)),
                ('date_installed', models.DateField(help_text='When this feature is installed')),
                ('quantity', models.FloatField(help_text='Quantity of the feature. The unit is based on the sub class')),
                ('description', models.TextField(blank=True, null=True)),
                ('age', models.FloatField(blank=True, null=True)),
                ('remaining_life', models.FloatField(blank=True, help_text='How much remaining life for the feature', null=True)),
                ('remaining_life_percent', models.FloatField(blank=True, help_text='How much remaining life in percent for the feature', null=True)),
                ('annual_reserve_cost', models.FloatField(blank=True, help_text='How much cost should be reserved annually', null=True)),
                ('replacement_cost', models.FloatField(blank=True, help_text='How much cost for replacing the feature with all quantity', null=True)),
                ('maintenance_cost', models.FloatField(blank=True, help_text='How much cost to maintenance the feature with all quantity', null=True)),
                ('geometry', django.contrib.gis.db.models.fields.MultiLineStringField(help_text='Multiline Geometry.', srid=4326)),
            ],
            options={
                'db_table': 'feature_line',
            },
        ),
        migrations.CreateModel(
            name='FeaturePoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(blank=True, help_text='unique asset ID', max_length=256, null=True)),
                ('date_installed', models.DateField(help_text='When this feature is installed')),
                ('quantity', models.FloatField(help_text='Quantity of the feature. The unit is based on the sub class')),
                ('description', models.TextField(blank=True, null=True)),
                ('age', models.FloatField(blank=True, null=True)),
                ('remaining_life', models.FloatField(blank=True, help_text='How much remaining life for the feature', null=True)),
                ('remaining_life_percent', models.FloatField(blank=True, help_text='How much remaining life in percent for the feature', null=True)),
                ('annual_reserve_cost', models.FloatField(blank=True, help_text='How much cost should be reserved annually', null=True)),
                ('replacement_cost', models.FloatField(blank=True, help_text='How much cost for replacing the feature with all quantity', null=True)),
                ('maintenance_cost', models.FloatField(blank=True, help_text='How much cost to maintenance the feature with all quantity', null=True)),
                ('geometry', django.contrib.gis.db.models.fields.MultiPointField(help_text='Multipoint Geometry.', srid=4326)),
            ],
            options={
                'db_table': 'feature_point',
            },
        ),
        migrations.CreateModel(
            name='FeaturePolygon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(blank=True, help_text='unique asset ID', max_length=256, null=True)),
                ('date_installed', models.DateField(help_text='When this feature is installed')),
                ('quantity', models.FloatField(help_text='Quantity of the feature. The unit is based on the sub class')),
                ('description', models.TextField(blank=True, null=True)),
                ('age', models.FloatField(blank=True, null=True)),
                ('remaining_life', models.FloatField(blank=True, help_text='How much remaining life for the feature', null=True)),
                ('remaining_life_percent', models.FloatField(blank=True, help_text='How much remaining life in percent for the feature', null=True)),
                ('annual_reserve_cost', models.FloatField(blank=True, help_text='How much cost should be reserved annually', null=True)),
                ('replacement_cost', models.FloatField(blank=True, help_text='How much cost for replacing the feature with all quantity', null=True)),
                ('maintenance_cost', models.FloatField(blank=True, help_text='How much cost to maintenance the feature with all quantity', null=True)),
                ('geometry', django.contrib.gis.db.models.fields.MultiPolygonField(help_text='Multipolygon Geometry.', srid=4326)),
            ],
            options={
                'db_table': 'feature_polygon',
            },
        ),
        migrations.CreateModel(
            name='FeatureSubClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('description', models.TextField(blank=True, null=True)),
                ('deterioration', models.ForeignKey(blank=True, help_text='Deterioration of this sub class', null=True, on_delete=django.db.models.deletion.SET_NULL, to='amlit.Deterioration')),
            ],
            options={
                'db_table': 'asset_sub_class',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='FeatureType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('description', models.TextField(blank=True, null=True)),
                ('lifespan', models.FloatField(blank=True, help_text='Total estimated life span of asset in years', null=True)),
            ],
            options={
                'db_table': 'asset_type',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='GeneralBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'general_brand',
            },
        ),
        migrations.CreateModel(
            name='GeneralMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'general_material',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='Administrative code', max_length=128, unique=True)),
                ('name', models.CharField(max_length=512)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'province',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'unit',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('description', models.TextField(blank=True, null=True)),
                ('community', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='amlit.Community')),
            ],
            options={
                'db_table': 'system',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='Administrative code', max_length=128, unique=True)),
                ('name', models.CharField(max_length=512)),
                ('description', models.TextField(blank=True, null=True)),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amlit.Province')),
            ],
            options={
                'db_table': 'region',
            },
        ),
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='amlit.Unit')),
            ],
            options={
                'db_table': 'quantity',
            },
        ),
        migrations.CreateModel(
            name='Money',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='amlit.Currency')),
            ],
            options={
                'db_table': 'money',
            },
        ),
        migrations.CreateModel(
            name='FeatureTypeCombination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('description', models.TextField(blank=True, null=True)),
                ('sub_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amlit.FeatureSubClass')),
                ('the_class', models.ForeignKey(db_column='class', on_delete=django.db.models.deletion.CASCADE, to='amlit.FeatureClass', verbose_name='class')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amlit.FeatureType')),
            ],
            options={
                'db_table': 'asset_type_combination',
                'ordering': ('the_class', 'sub_class', 'type'),
                'unique_together': {('the_class', 'sub_class', 'type')},
            },
        ),
        migrations.AddField(
            model_name='featuretype',
            name='maintenance_cost',
            field=models.OneToOneField(blank=True, help_text='Annual operation and maintenance cost (Default in canadian dollars)', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='type_maintenance_cost', to='amlit.Money'),
        ),
        migrations.AddField(
            model_name='featuretype',
            name='renewal_cost',
            field=models.OneToOneField(blank=True, help_text='Renewal cost (Default in canadian dollars)', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='type_renewal_cost', to='amlit.Money'),
        ),
        migrations.CreateModel(
            name='FeatureSubType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('description', models.TextField(blank=True, null=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amlit.FeatureType')),
            ],
            options={
                'db_table': 'asset_sub_type',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='featuresubclass',
            name='unit',
            field=models.ForeignKey(blank=True, help_text='Default unit for this sub_class', null=True, on_delete=django.db.models.deletion.SET_NULL, to='amlit.Unit'),
        ),
        migrations.CreateModel(
            name='FeaturePolygonProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('value', models.CharField(max_length=512)),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amlit.FeaturePolygon')),
            ],
            options={
                'db_table': 'feature_polygon_property',
            },
        ),
        migrations.AddField(
            model_name='featurepolygon',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='amlit.GeneralBrand'),
        ),
        migrations.AddField(
            model_name='featurepolygon',
            name='condition',
            field=models.ForeignKey(blank=True, help_text='Condition of the feature', null=True, on_delete=django.db.models.deletion.SET_NULL, to='amlit.Condition'),
        ),
        migrations.AddField(
            model_name='featurepolygon',
            name='material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='amlit.GeneralMaterial'),
        ),
        migrations.AddField(
            model_name='featurepolygon',
            name='system',
            field=models.ForeignKey(blank=True, help_text='What system the feature belongs to', null=True, on_delete=django.db.models.deletion.SET_NULL, to='amlit.System'),
        ),
        migrations.AddField(
            model_name='featurepolygon',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amlit.FeatureTypeCombination'),
        ),
        migrations.CreateModel(
            name='FeaturePointProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('value', models.CharField(max_length=512)),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amlit.FeaturePoint')),
            ],
            options={
                'db_table': 'feature_point_property',
            },
        ),
        migrations.AddField(
            model_name='featurepoint',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='amlit.GeneralBrand'),
        ),
        migrations.AddField(
            model_name='featurepoint',
            name='condition',
            field=models.ForeignKey(blank=True, help_text='Condition of the feature', null=True, on_delete=django.db.models.deletion.SET_NULL, to='amlit.Condition'),
        ),
        migrations.AddField(
            model_name='featurepoint',
            name='material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='amlit.GeneralMaterial'),
        ),
        migrations.AddField(
            model_name='featurepoint',
            name='system',
            field=models.ForeignKey(blank=True, help_text='What system the feature belongs to', null=True, on_delete=django.db.models.deletion.SET_NULL, to='amlit.System'),
        ),
        migrations.AddField(
            model_name='featurepoint',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amlit.FeatureTypeCombination'),
        ),
        migrations.CreateModel(
            name='FeatureLineProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('value', models.CharField(max_length=512)),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amlit.FeatureLine')),
            ],
            options={
                'db_table': 'feature_line_property',
            },
        ),
        migrations.AddField(
            model_name='featureline',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='amlit.GeneralBrand'),
        ),
        migrations.AddField(
            model_name='featureline',
            name='condition',
            field=models.ForeignKey(blank=True, help_text='Condition of the feature', null=True, on_delete=django.db.models.deletion.SET_NULL, to='amlit.Condition'),
        ),
        migrations.AddField(
            model_name='featureline',
            name='material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='amlit.GeneralMaterial'),
        ),
        migrations.AddField(
            model_name='featureline',
            name='system',
            field=models.ForeignKey(blank=True, help_text='What system the feature belongs to', null=True, on_delete=django.db.models.deletion.SET_NULL, to='amlit.System'),
        ),
        migrations.AddField(
            model_name='featureline',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amlit.FeatureTypeCombination'),
        ),
        migrations.AddField(
            model_name='community',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amlit.Region'),
        ),
    ]
