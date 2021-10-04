# Generated by Django 3.2.5 on 2021-10-04 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_admin_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='details',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='regular',
            name='meet_link',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='admin',
            name='address',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='regular',
            name='default_msg',
            field=models.TextField(blank=True, default='I am fine'),
        ),
    ]