# Generated by Django 4.0.5 on 2022-06-09 16:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('predict_model', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dynasty',
            name='dynasty',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='emperoryear',
            name='dynasty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='predict_model.dynasty', to_field='dynasty'),
        ),
        migrations.AlterField(
            model_name='porcelain',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
