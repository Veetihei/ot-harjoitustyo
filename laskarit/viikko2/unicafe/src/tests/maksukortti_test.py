import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_rahan_lataaminen_nostaa_saldoa(self):
        self.maksukortti.lataa_rahaa(500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 15.00 euroa")

    def test_saldo_vahenee_kun_on_rahaa(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")

    def test_saldo_ei_muutu_ilman_rahaa(self):
        maksukortti = Maksukortti(200)
        maksukortti.ota_rahaa(500)

        self.assertEqual(str(maksukortti), "Kortilla on rahaa 2.00 euroa")

    def test_palauttaa_true_jos_on_rahaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(200), True)

    def test_palauttaa_false_jos_ei_rahaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1500), False)