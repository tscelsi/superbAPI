# Generated by Django 4.0.3 on 2022-03-12 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_person_id_alter_person_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(choices=[('VIC', 'Victoria'), ('NSW', 'New South Wales'), ('QLD', 'Queensland'), ('TAS', 'Tasmania'), ('WA', 'Western Australia'), ('NT', 'Northern Territory'), ('SA', 'South Australia')], max_length=3),
        ),
    ]
