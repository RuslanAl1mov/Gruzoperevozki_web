# Generated by Django 4.1.4 on 2022-12-14 01:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gruz',
            name='manufacture_time',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='Время отправки заявки'),
        ),
        migrations.AlterField(
            model_name='gruz',
            name='sent_to_position_date',
            field=models.DateField(null=True, verbose_name='Время отправки на место назначения'),
        ),
    ]