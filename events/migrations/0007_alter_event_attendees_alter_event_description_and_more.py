# Generated by Django 4.2.4 on 2023-10-11 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_alter_event_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(to='events.caluser'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='events.eventlocation'),
        ),
    ]