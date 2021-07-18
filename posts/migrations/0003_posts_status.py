# Generated by Django 3.2.5 on 2021-07-18 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_posts_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='status',
            field=models.CharField(choices=[('d', 'draft'), ('p', 'published'), ('w', 'withdraw')], default='jamshid', max_length=1),
            preserve_default=False,
        ),
    ]