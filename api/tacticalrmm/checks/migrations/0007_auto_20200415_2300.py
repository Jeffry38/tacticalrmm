# Generated by Django 3.0.5 on 2020-04-15 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0001_initial'),
        ('checks', '0006_auto_20200415_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpuloadcheck',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cpuloadchecks', to='agents.Agent'),
        ),
        migrations.AlterField(
            model_name='diskcheck',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='diskchecks', to='agents.Agent'),
        ),
        migrations.AlterField(
            model_name='memcheck',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='memchecks', to='agents.Agent'),
        ),
        migrations.AlterField(
            model_name='pingcheck',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pingchecks', to='agents.Agent'),
        ),
        migrations.AlterField(
            model_name='scriptcheck',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scriptchecks', to='agents.Agent'),
        ),
        migrations.AlterField(
            model_name='winservicecheck',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winservicechecks', to='agents.Agent'),
        ),
    ]
