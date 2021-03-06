# Generated by Django 2.2.13 on 2021-01-25 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0004_listwidget_textwidget_widgetlistitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='widgetlistitem',
            name='widget_number',
        ),
        migrations.RemoveField(
            model_name='widgetlistitem',
            name='widget_title',
        ),
        migrations.RemoveField(
            model_name='widgetlistitem',
            name='widget_type',
        ),
        migrations.AddField(
            model_name='listwidget',
            name='widget_number',
            field=models.PositiveSmallIntegerField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listwidget',
            name='widget_title',
            field=models.CharField(default='Dummy', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listwidget',
            name='widget_type',
            field=models.CharField(choices=[('text', 'Text Content'), ('list', 'List Items')], default='text', max_length=10),
        ),
    ]
