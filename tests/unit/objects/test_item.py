import unittest

from quickbooks.objects.item import Item


class ItemTests(unittest.TestCase):
    def test_unicode(self):
        item = Item()
        item.Name = "test"

        self.assertEquals(unicode(item), "test")

    def test_to_ref(self):
        item = Item()
        item.Name = "test"
        item.Id = 100

        ref = item.to_ref()

        self.assertEquals(ref.name, "test")
        self.assertEquals(ref.type, "Item")
        self.assertEquals(ref.value, 100)
