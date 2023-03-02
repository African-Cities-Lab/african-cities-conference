# Generated by Django 4.0.8 on 2023-03-01 10:03

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_column_sidebar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flatpage',
            name='body',
            field=wagtail.fields.StreamField([('one_column_block', wagtail.blocks.StructBlock([('content', wagtail.blocks.ListBlock(wagtail.blocks.RichTextBlock(label='paragraph'))), ('extra_classes', wagtail.blocks.CharBlock(label='extra classes', required=False))])), ('three_column_block', wagtail.blocks.StructBlock([('content', wagtail.blocks.ListBlock(wagtail.blocks.RichTextBlock(label='paragraph'))), ('extra_classes', wagtail.blocks.CharBlock(label='extra classes', required=False))])), ('card_layout_block', wagtail.blocks.StructBlock([('content', wagtail.blocks.StreamBlock([('block', wagtail.blocks.RichTextBlock())]))])), ('cfp_card_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('content', wagtail.blocks.StreamBlock([('block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Title')), ('learn_more_url', wagtail.blocks.PageChooserBlock(label='Page Link')), ('description', wagtail.blocks.RichTextBlock(label='Description'))]))]))])), ('speaker_layout_block', wagtail.blocks.StructBlock([('speakers', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('name', wagtail.blocks.CharBlock()), ('designation', wagtail.blocks.RichTextBlock()), ('social_links', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('fa_class', wagtail.blocks.CharBlock(required=False)), ('profile_link', wagtail.blocks.CharBlock(required=False))]))), ('biography', wagtail.blocks.RichTextBlock())])))])), ('column_sidebar_layout_block', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock()), ('sidebar', wagtail.blocks.StreamBlock([('block', wagtail.blocks.PageChooserBlock(label='Page Link'))]))])), ('button', wagtail.blocks.StructBlock([('self_class', wagtail.blocks.CharBlock(required=False)), ('button_type', wagtail.blocks.CharBlock(help_text='btn__primary or btn__secondary'))]))], blank=True, use_json_field=None),
        ),
    ]
