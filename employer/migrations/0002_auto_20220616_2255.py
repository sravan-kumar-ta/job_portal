# Generated by Django 3.2.13 on 2022-06-16 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='status',
            field=models.CharField(choices=[('Applied', 'applied'), ('Accepted', 'accepted'), ('Rejected', 'rejected'), ('Pending', 'pending'), ('Cancelled', 'cancelled')], default='applied', max_length=120),
        ),
        migrations.AlterField(
            model_name='companyprofiles',
            name='logo',
            field=models.ImageField(null=True, upload_to='files/company_logo'),
        ),
    ]
