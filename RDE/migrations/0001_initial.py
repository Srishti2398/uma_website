# Generated by Django 2.2.9 on 2020-01-24 12:42

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
    ]

    operations = [
        migrations.CreateModel(
            name='RDEPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('subtitle', models.CharField(blank=True, max_length=100, null=True)),
                ('content', wagtail.core.fields.StreamField([('resources', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('points_r', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('point', wagtail.core.blocks.CharBlock(max_length=200, required=True)), ('pdf', wagtail.documents.blocks.DocumentChooserBlock(required=True))])))]))], blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Resources for Development and Engineering Page',
                'verbose_name_plural': 'Resources for Development and Engineering Pages',
            },
            bases=('wagtailcore.page',),
        ),
    ]
