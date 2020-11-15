# Generated by Django 3.1.2 on 2020-11-15 20:08

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
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=13, unique=True, verbose_name='isbn')),
                ('title', models.CharField(max_length=30, verbose_name='title')),
            ],
        ),
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='category name')),
                ('abbrev', models.CharField(max_length=3, verbose_name='abbreviation')),
                ('description', models.CharField(max_length=150, verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='PolyPhrase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phrase', models.CharField(max_length=150, verbose_name='phrase')),
                ('said_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='said by')),
            ],
        ),
        migrations.CreateModel(
            name='BookPage',
            fields=[
                ('page_id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField(blank=True, max_length=600, verbose_name='page content')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persistence.book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(to='persistence.BookCategory'),
        ),
    ]
