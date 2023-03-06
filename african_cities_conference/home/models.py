from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page

from african_cities_conference.home.blocks import (
    AgendaLayout,
    Button,
    CardLayoutBlock,
    CfpCardBlock,
    ColumnSidebarLayoutBlock,
    OneColumnBlock,
    ParagraphLayout,
    SidebarLayout,
    SpeakerLayoutBlock,
    ThreeColumnBlock,
)


class HomePage(Page):
    subpage_types = ["home.FlatPage", "home.PageWithSideBar", "home.ProgramPage"]
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
            ("paragraph_layout", ParagraphLayout()),
            ("column_sidebar_layout_block", ColumnSidebarLayoutBlock()),
            ("button", Button()),
        ],
        blank=True,
    )
    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]
    parent_page_type = [
        "home.HomePage",
    ]


class PageWithSidebar(Page):
    """Page with sidebar model."""

    sidebar = StreamField(
        [
            ("sidebar_layout", SidebarLayout()),
        ],
        blank=True,
    )
    body = StreamField(
        [
            ("paragraph_layout", ParagraphLayout()),
            ("button", Button()),
        ],
        blank=True,
    )
    content_panels = Page.content_panels + [
        FieldPanel("sidebar"),
        FieldPanel("body"),
    ]
    parent_page_type = [
        "home.HomePage",
    ]


class ProgramPage(Page):
    """Program page model."""

    body = StreamField(
        [
            ("agenda_layout", AgendaLayout()),
            ("paragraph_layout", ParagraphLayout()),
        ],
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]
    parent_page_type = [
        "home.HomePage",
    ]
