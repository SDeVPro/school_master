# Generated by Django 3.2.5 on 2021-08-05 10:23

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=222)),
                ('email', models.EmailField(blank=True, max_length=222)),
                ('subject', models.TextField(blank=True, max_length=222)),
                ('message', models.TextField(blank=True, max_length=1000)),
                ('status', models.CharField(choices=[('Yangi', 'Yangi'), ("O'qildi", "O'qildi"), ('Yopilgan', 'Yopilgan')], default='Yangi', max_length=15)),
                ('ip', models.CharField(blank=True, max_length=222)),
                ('note', models.CharField(blank=True, max_length=222)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=222)),
                ('keywords', models.CharField(max_length=222)),
                ('description', models.CharField(max_length=222)),
                ('detail', ckeditor_uploader.fields.RichTextUploadingField()),
                ('image', models.ImageField(upload_to='images')),
                ('author', models.CharField(max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=222)),
                ('keywords', models.CharField(max_length=222)),
                ('description', models.CharField(max_length=222)),
                ('aboutus', ckeditor_uploader.fields.RichTextUploadingField()),
                ('contactus', ckeditor_uploader.fields.RichTextUploadingField()),
                ('facebook', models.CharField(blank=True, max_length=222)),
                ('instagram', models.CharField(blank=True, max_length=222)),
                ('email', models.CharField(blank=True, max_length=222)),
                ('tiktok', models.CharField(blank=True, max_length=222)),
                ('youtube', models.CharField(blank=True, max_length=222)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'setting',
                'verbose_name_plural': 'settings',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('level', models.CharField(max_length=255)),
                ('level_years', models.IntegerField()),
                ('image', models.ImageField(upload_to='images')),
                ('classes', models.CharField(max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('level', models.CharField(max_length=255)),
                ('level_years', models.IntegerField()),
                ('image', models.ImageField(upload_to='images')),
                ('classes', models.CharField(max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.teacher')),
            ],
        ),
    ]