# Generated by Django 3.2.8 on 2021-11-16 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0004_auto_20211116_1538'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointments',
            options={'verbose_name_plural': 'HQ appointments'},
        ),
        migrations.AlterModelOptions(
            name='notes',
            options={'verbose_name_plural': 'Deletion notes'},
        ),
        migrations.RemoveField(
            model_name='appointments',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='notes',
            name='messageToUser',
        ),
        migrations.RemoveField(
            model_name='notes',
            name='to',
        ),
        migrations.RemoveField(
            model_name='notes',
            name='veb_field',
        ),
        migrations.AddField(
            model_name='notes',
            name='notes',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='notes',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='color',
            field=models.CharField(default='#D5423A', editable=False, max_length=30),
        ),
    ]
