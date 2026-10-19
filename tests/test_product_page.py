from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class ProductPageTests(unittest.TestCase):
    def test_product_page_has_purchase_link_and_disclosure(self):
        page = (ROOT / 'docs/_pages/msr-x6-bluetooth.md').read_text()
        for value in ['permalink: /msr-x6-bluetooth/', 'B08T9B9VSD', 'tag=blackpill07-20', 'linkId=0ffded125c88442f006e64282a88a069', 'sponsored', 'As an Amazon Associate', '/bluetooth-software/', '/software-download/', 'msrx6bt.jpg']:
            self.assertIn(value, page)

    def test_home_product_follows_software(self):
        home = (ROOT / 'docs/_pages/home.md').read_text()
        self.assertLess(home.index('title: "Software Downloads"'), home.index('title: "MSR X6 Bluetooth"'))
        self.assertLess(home.index('title: "MSR X6 Bluetooth"'), home.index('title: "Bluetooth Setup"'))
        self.assertIn('url: "/msr-x6-bluetooth/"', home)

    def test_home_uses_full_card_links_and_responsive_grid(self):
        layout = (ROOT / 'docs/_layouts/home.html').read_text()
        self.assertIn('col-md-6', layout)
        self.assertIn('class="feature-link', layout)
        self.assertNotIn('truncate: 10', layout)
        self.assertIn('f_row.img_alt | escape', layout)

if __name__ == '__main__':
    unittest.main()
