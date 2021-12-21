# Generated by Django 3.1.14 on 2021-12-21 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('wagtailcore', '0059_apply_collection_ordering'),
        ('home', '0034_v1pageurltov2pagemap'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image_icon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='iogtflatmenuitem',
            name='image_icon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='offlineapppage',
            name='image_icon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='pagelinkpage',
            name='external_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pagelinkpage',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='pagelinkpage',
            name='image_icon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='section',
            name='image_icon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AlterField(
            model_name='pagelinkpage',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='page_link_pages', to='wagtailcore.page'),
        ),
    ]
