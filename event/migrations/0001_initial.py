# Generated by Django 3.2 on 2022-12-05 10:17

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('theater', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=300)),
                ('state', models.CharField(max_length=300)),
                ('country', models.CharField(max_length=300)),
                ('location', models.CharField(max_length=1000)),
                ('detailes', models.TextField(max_length=3000)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(auto_now_add=True)),
                ('available_seats', models.IntegerField(default=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('price', models.IntegerField()),
                ('ticket', models.CharField(choices=[('Regular', 'Regular'), ('Bronze', 'Bronze'), ('Gold', 'Gold'), ('platinum', 'platinum'), ('Black', 'Black'), ('Vip', 'Vip')], max_length=20)),
                ('total_seats', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('number_tickets', models.IntegerField()),
                ('active', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ticket_Type', to='event.event')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('on_tickets', models.IntegerField()),
                ('first_name', models.CharField(max_length=300)),
                ('last_name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=500)),
                ('tranx_code', models.CharField(max_length=200)),
                ('paid', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='event.ticket')),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
    ]
