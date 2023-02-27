from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page

from african_cities_conference.home.blocks import (
    CardLayoutBlock,
    CfpCardBlock,
    ColumnSidebarLayoutBlock,
    OneColumnBlock,
    SpeakerLayoutBlock,
    ThreeColumnBlock,
)


class HomePage(Page):
    subpage_types = [
        "home.FlatPage",
    ]
    parent_page_type = [
        "wagtailcore.Page",
    ]
    max_count = 1


class FlatPage(Page):
    """FlatPage page model."""

    body = StreamField(
        [
            ("one_column_block", OneColumnBlock()),
            ("three_column_block", ThreeColumnBlock()),
            ("card_layout_block", CardLayoutBlock()),
            ("cfp_card_block", CfpCardBlock()),
            ("speaker_layout_block", SpeakerLayoutBlock()),
            ("column_sidebar_layout_block", ColumnSidebarLayoutBlock()),
        ],
        blank=True,
    )
    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]
    parent_page_type = [
        "home.HomePage",
    ]
