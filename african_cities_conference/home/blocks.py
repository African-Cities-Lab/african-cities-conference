from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class ColumnBlock(blocks.StructBlock):
    content = blocks.ListBlock(
        blocks.RichTextBlock(label="paragraph"),
    )
    extra_classes = blocks.CharBlock(required=False, label="extra classes")

    class Meta:
        template = "home/blocks/column_block.html"

    def render(self, value, context=None):
        return super().render(value, context={"col_classes": self.col_classes})


class OneColumnBlock(ColumnBlock):
    col_classes = "col-12"


class TwoColumnBlock(ColumnBlock):
    col_classes = "col-12 col-lg-6"


class ThreeColumnBlock(ColumnBlock):
    col_classes = "col-lg-4 col-md-5"


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
                    blocks.ListBlock(
                        blocks.StructBlock(
                            [
                                ("social_network", blocks.CharBlock()),
                                ("profile_link", blocks.CharBlock()),
                            ]
                        ),
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
