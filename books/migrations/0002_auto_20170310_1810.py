# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('publication_date', models.DateField()),
                ('authors', models.ManyToManyField(to='books.Author')),
                ('publisher', models.ForeignKey(to='books.Publisher')),
            ],
        ),
        migrations.RemoveField(
            model_name='books',
            name='authors',
        ),
        migrations.RemoveField(
            model_name='books',
            name='publisher',
        ),
        migrations.DeleteModel(
            name='Books',
        ),
    ]
