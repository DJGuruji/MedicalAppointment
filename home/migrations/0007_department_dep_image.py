# Generated by Django 4.2.5 on 2023-10-15 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_doctor_doc_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='dep_image',
            field=models.ImageField(null=True, upload_to='dep'),
        ),
    ]
