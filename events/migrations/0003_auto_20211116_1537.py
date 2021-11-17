# Generated by Django 3.2.8 on 2021-11-16 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20211116_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='color',
            field=models.CharField(default='#F3AD18', editable=False, max_length=30),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='notes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.notes'),
        ),
    ]
