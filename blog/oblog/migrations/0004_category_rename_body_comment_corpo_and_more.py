# Generated by Django 4.2.7 on 2023-11-17 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oblog', '0003_alter_post_titulo_url_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='corpo',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='date_added',
            new_name='data_adicionado',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='nome',
        ),
    ]
