# Generated by Django 4.0.5 on 2022-07-07 01:25

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
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.IntegerField(default=0)),
                ('in_ex', models.CharField(choices=[('income', '수입'), ('expense', '지출')], default='income', max_length=20)),
                ('method', models.CharField(choices=[('cash', '현금'), ('card', '카드'), ('transfer', '이체')], default='cash', max_length=20)),
                ('memo', models.CharField(blank=True, max_length=300, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]