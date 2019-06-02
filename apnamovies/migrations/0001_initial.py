# Generated by Django 2.1.4 on 2019-05-05 09:03

import college.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('star_cast', models.TextField()),
                ('description', models.TextField()),
                ('img', models.ImageField(blank=True, null=True, upload_to='images\\', validators=[college.models.validate_img])),
                ('ulink', models.URLField(blank=True, null=True)),
                ('language', models.CharField(max_length=50, null=True)),
                ('genre', models.CharField(choices=[('Comedy', 'Comedy'), ('Horor', 'Horor'), ('SciFi', 'SciFi'), ('Action', 'Action'), ('Drama', 'Drama'), ('Romantic', 'Romantic'), ('Other', 'Other')], max_length=40)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
