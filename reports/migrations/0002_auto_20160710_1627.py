# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-07-10 16:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientha',
            name='age',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patientha',
            name='derived_n',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patientha',
            name='derived_o',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patientha',
            name='derived_p',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patientha',
            name='derived_q',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patientha',
            name='derived_r',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patientha',
            name='derived_s',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patientha',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient_has', to='location.District'),
        ),
        migrations.AlterField(
            model_name='patientha',
            name='gender',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patientha',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient_has', to='reports.Group'),
        ),
        migrations.AlterField(
            model_name='patientha',
            name='ha_provider_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patientha',
            name='icd',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient_has', to='reports.ICD'),
        ),
        migrations.AlterField(
            model_name='patientha',
            name='obs_k',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patientha',
            name='obs_l',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patientha',
            name='obs_m',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patientha',
            name='patient_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patientha',
            name='unit',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patientha',
            name='ward',
            field=models.IntegerField(null=True),
        ),
    ]
