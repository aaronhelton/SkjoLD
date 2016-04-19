# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 15:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssertionStatement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.URLField()),
                ('predicate', models.URLField()),
                ('object', models.URLField()),
                ('context', models.TextField()),
                ('termcomb', models.IntegerField()),
            ],
            options={
                'managed': False,
                'db_table': 'kb_2cba3dacfc_asserted_statements',
            },
        ),
        migrations.CreateModel(
            name='LiteralStatement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.URLField()),
                ('predicate', models.URLField()),
                ('object', models.TextField()),
                ('context', models.TextField()),
                ('termcomb', models.IntegerField()),
                ('objlanguage', models.CharField(max_length=255)),
                ('objdatatype', models.CharField(max_length=255)),
            ],
            options={
                'managed': False,
                'db_table': 'kb_2cba3dacfc_literal_statements',
            },
        ),
        migrations.CreateModel(
            name='Namespace',
            fields=[
                ('prefix', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('uri', models.CharField(max_length=200)),
            ],
            options={
                'managed': False,
                'db_table': 'kb_2cba3dacfc_namespace_binds',
            },
        ),
        migrations.CreateModel(
            name='QuotedStatement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.URLField()),
                ('predicate', models.URLField()),
                ('object', models.TextField()),
                ('context', models.TextField()),
                ('termcomb', models.IntegerField()),
                ('objlanguage', models.CharField(max_length=255)),
                ('objdatatype', models.CharField(max_length=255)),
            ],
            options={
                'managed': False,
                'db_table': 'kb_2cba3dacfc_quoted_statements',
            },
        ),
        migrations.CreateModel(
            name='TypeStatement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('member', models.URLField()),
                ('klass', models.URLField()),
                ('context', models.TextField()),
                ('termcomb', models.IntegerField()),
            ],
            options={
                'managed': False,
                'db_table': 'kb_2cba3dacfc_type_statements',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField()),
                ('namespace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='semantic.Namespace')),
            ],
        ),
    ]