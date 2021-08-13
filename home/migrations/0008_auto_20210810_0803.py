# Generated by Django 3.1.13 on 2021-08-10 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailsvg', '0002_svg_edit_code'),
        ('home', '0007_auto_20210728_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iogtflatmenuitem',
            name='icon',
            field=models.ForeignKey(blank=True, help_text='If Page link is a section page and icon is blank then the section icon will be used. Specify an icon here to override this.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailsvg.svg'),
        ),
    ]
