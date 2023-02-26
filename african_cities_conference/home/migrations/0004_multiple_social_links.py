# Generated by Django 4.0.8 on 2023-02-24 12:07

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_flatpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flatpage',
            name='body',
            field=wagtail.fields.StreamField([('one_column_block', wagtail.blocks.StructBlock([('content', wagtail.blocks.ListBlock(wagtail.blocks.RichTextBlock(label='paragraph'))), ('extra_classes', wagtail.blocks.CharBlock(label='extra classes', required=False))])), ('three_column_block', wagtail.blocks.StructBlock([('content', wagtail.blocks.ListBlock(wagtail.blocks.RichTextBlock(label='paragraph'))), ('extra_classes', wagtail.blocks.CharBlock(label='extra classes', required=False))])), ('card_layout_block', wagtail.blocks.StructBlock([('content', wagtail.blocks.StreamBlock([('block', wagtail.blocks.RichTextBlock())]))])), ('cfp_card_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(blank=True)), ('content', wagtail.blocks.StreamBlock([('block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Title')), ('learn_more_url', wagtail.blocks.PageChooserBlock(label='Page Link')), ('description', wagtail.blocks.RichTextBlock(label='Description'))]))]))])), ('speaker_layout_block', wagtail.blocks.StructBlock([('speakers', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('name', wagtail.blocks.CharBlock()), ('designation', wagtail.blocks.RichTextBlock()), ('social_links', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('social_network', wagtail.blocks.CharBlock()), ('profile_link', wagtail.blocks.CharBlock())]))), ('biography', wagtail.blocks.RichTextBlock())])))]))], blank=True, use_json_field=None),
        ),
    ]
