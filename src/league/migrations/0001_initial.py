# Generated by Django 4.1.2 on 2022-10-25 05:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('api_id', models.IntegerField(unique=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('nationality', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('area', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('api_id', models.IntegerField(unique=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('short_name', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('tla', models.CharField(blank=True, max_length=20, null=True)),
                ('area', models.CharField(blank=True, max_length=50, null=True)),
                ('coach', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coach', to='league.coach')),
                ('competitions', models.ManyToManyField(related_name='teams', to='league.competition')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('api_id', models.IntegerField(unique=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('nationality', models.CharField(blank=True, max_length=200, null=True)),
                ('position', models.CharField(blank=True, max_length=100, null=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='league.team')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
