from wagtail.core import blocks


class OneColumnBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    content = blocks.StreamBlock(
        [
            ("paragraph", blocks.RichTextBlock()),
        ],
    )

    class Meta:
        template = "home/blocks/one_column_block.html"


class ThreeColumnBlock(blocks.StructBlock):
    content = blocks.StreamBlock(
        [
            ("body", blocks.RichTextBlock()),
        ],
    )

    class Meta:
        template = "home/blocks/three_column_block.html"
