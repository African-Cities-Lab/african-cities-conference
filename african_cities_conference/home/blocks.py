from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class OneColumnBlock(blocks.StructBlock):
    title = blocks.CharBlock(blank=True)
    content = blocks.StreamBlock(
        [
            (
                "paragraph",
                blocks.RichTextBlock(),
            ),
        ],
    )

    class Meta:
        template = "home/blocks/one_column_block.html"


class ThreeColumnBlock(blocks.StructBlock):
    content = blocks.StreamBlock(
        [
            (
                "block",
                blocks.RichTextBlock(),
            ),
        ],
    )

    class Meta:
        template = "home/blocks/three_column_block.html"


class CardLayoutBlock(blocks.StructBlock):
    content = blocks.StreamBlock(
        [
            (
                "block",
                blocks.RichTextBlock(),
            ),
        ],
    )

    class Meta:
        template = "home/blocks/card_layout_block.html"


class CfpCardBlock(blocks.StructBlock):
    title = blocks.CharBlock(blank=True)
    content = blocks.StreamBlock(
        [
            (
                "block",
                blocks.StructBlock(
                    [
                        ("title", blocks.CharBlock(label="Title")),
                        ("learn_more_url", blocks.PageChooserBlock(label="Page Link")),
                        ("description", blocks.RichTextBlock(label="Description")),
                    ]
                ),
            ),
        ],
    )

    class Meta:
        template = "home/blocks/cfp_card_block.html"


class SpeakerLayoutBlock(blocks.StructBlock):
    speakers = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock()),
                ("name", blocks.CharBlock()),
                (
                    "designation",
                    blocks.RichTextBlock(),
                ),
                (
                    "social_links",
                    blocks.StructBlock(
                        [
                            ("social_network", blocks.CharBlock()),
                            ("profile_link", blocks.CharBlock()),
                        ]
                    ),
                ),
                (
                    "biography",
                    blocks.RichTextBlock(),
                ),
            ],
        ),
    )

    class Meta:
        template = "home/blocks/speaker_layout_block.html"
