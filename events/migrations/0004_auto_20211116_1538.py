# Generated by Django 3.2.8 on 2021-11-16 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20211116_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='color',
            field=models.CharField(default='#9041B8', editable=False, max_length=30),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='notes',
            field=models.CharField(max_length=2, verbose_name='Notes'),
        ),
    ]
