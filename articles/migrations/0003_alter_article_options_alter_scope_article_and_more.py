# Generated by Django 5.1.3 on 2024-12-12 14:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag_alter_article_published_at_scope_article_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published_at'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterField(
            model_name='scope',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article'),
        ),
        migrations.AlterField(
            model_name='scope',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Тег'),
        ),
    ]
