# Generated by Django 5.0.6 on 2024-06-27 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fechaCompletada',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
