# Generated by Django 4.1.3 on 2022-11-30 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NguoiDung',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_dang_nhap', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('mat_khau', models.CharField(max_length=100)),
            ],
        ),
    ]
