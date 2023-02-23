from wagtail.core import blocks


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


class OneColumnTexteBlock(blocks.StructBlock):
    content = blocks.StreamBlock(
        [
            (
                "paragraph",
                blocks.RichTextBlock(),
            ),
        ],
    )

    class Meta:
        template = "home/blocks/one_column_texte_block.html"


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
