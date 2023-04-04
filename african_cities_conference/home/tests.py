from wagtail.tests.utils import WagtailPageTests

from african_cities_conference.home.models import (
    FlatPage,
    HomePage,
    PageWithSidebar,
    ProgramPage,
)


class FlatPageTests(WagtailPageTests):
    def test_can_create_a_page(self):
        for PageType in [FlatPage, PageWithSidebar, ProgramPage]:
            self.assertCanCreateAt(HomePage, PageType)
