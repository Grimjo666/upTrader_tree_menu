# Generated by Django 5.0.1 on 2024-02-01 19:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree_menu_app', '0007_alter_treemenu_child'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treemenu',
            name='child',
        ),
        migrations.AddField(
            model_name='treemenu',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tree_menu_app.treemenu'),
        ),
    ]
