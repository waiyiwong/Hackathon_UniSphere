# Generated by Django 4.2.7 on 2025-01-16 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_alter_community_options_remove_community_created_on'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='community',
            options={'ordering': ['-updated_at']},
        ),
        migrations.AlterField(
            model_name='community',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(default='Describe Event'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='comment',
            field=models.TextField(blank=True),
        ),
    ]
