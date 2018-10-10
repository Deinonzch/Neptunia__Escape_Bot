from unittest import TestCase
from Class.ImageRecognition import is_item


class TestIsItem(TestCase):
    def test_is_item_true_for_regex_Item(self):
        score = is_item('Item')
        self.assertEqual(score, True)

    def test_is_item_true_for_regex_item(self):
        score = is_item('item')
        self.assertEqual(score, True)

    def test_is_item_false_for_regex_Itam(self):
        score = is_item('Itam')
        self.assertEqual(score, False)

    def test_is_item_false_for_regex_itam(self):
        score = is_item('itam')
        self.assertEqual(score, False)

    def test_is_item_false_for_regex_mskovmpxjR8v(self):
        score = is_item('mskovmpxjR8v')
        self.assertEqual(score, False)

    def test_is_item_true_for_regex_ItemItem(self):
        score = is_item('ItemItem')
        self.assertEqual(score, True)

    def test_is_item_true_for_regex_itemitem(self):
        score = is_item('itemitem')
        self.assertEqual(score, True)

    def test_is_item_true_for_regex_afaItemvs(self):
        score = is_item('afaItemvs')
        self.assertEqual(score, True)

    def test_is_item_true_for_regex_afaitemvs(self):
        score = is_item('afaitemvs')
        self.assertEqual(score, True)

    def test_is_item_true_for_regex_Itemfvsdbfd(self):
        score = is_item('Itemfvsdbfd')
        self.assertEqual(score, True)

    def test_is_item_true_for_regex_itemfvsdbfd(self):
        score = is_item('itemfvsdbfd')
        self.assertEqual(score, True)

    def test_is_item_true_for_regex_sdbsbItem(self):
        score = is_item('sdbsbItem')
        self.assertEqual(score, True)

    def test_is_item_true_for_regex_sdbsbitem(self):
        score = is_item('sdbsbitem')
        self.assertEqual(score, True)
