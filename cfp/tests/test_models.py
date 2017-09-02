from django.test import TestCase
from django.utils import timezone
from cfp.models import Cfp, Donor


class DonorTest(TestCase):
    """Tests for DonorTest"""

    @classmethod
    def setUpTestData(cls):
        """Set up non-modified objects used by all test methods"""
        Donor.objects.create(donor="Some Donor", donor_abbrev="DON")

    def test_name(self):
        donor = Donor.objects.get(id=1)
        field_label = donor._meta.get_field('donor').verbose_name
        self.assertEquals(field_label, 'donor')

    def test_donor_abbrev_max_length(self):
        donor = Donor.objects.get(id=1)
        max_length = donor._meta.get_field('donor_abbrev').max_length
        self.assertLessEqual(max_length, 20)


# class CfpTest(TestCase):
#     """Tests for Calls for Proposals Models"""
#
#     def create_cfp(self, cfp_title="Some CfP Title", pub_date=timezone.now()):
#         return Cfp.cfp.create(cfp_title=cfp_title, pub_date=pub_date)
#
#     def test_cfp_creattion(self):
#         cfp = self.create_cfp()
#         self.assertTrue(isinstance(cfp, Cfp))
#         self.assertEqual(cfp.__str__(), cfp.cfp_title)


# class YourTestClass(TestCase):
#
#     @classmethod
#     def setUpTestData(cls):
#         print("setUpTestData: Run once to set up non-modified data for all class methods.")
#         pass
#
#     def setUp(self):
#         print("setUp: Run once for every test method to setup clean data.")
#         pass
#
#     def test_false_is_false(self):
#         print("Method: test_false_is_false.")
#         self.assertFalse(False)
#
#     def test_false_is_true(self):
#         print("Method: test_false_is_true.")
#         self.assertTrue(True)
#
#     def test_one_plus_one_equals_two(self):
#         print("Method: test_one_plus_one_equals_two.")
#         self.assertEqual(1 + 1, 2)
