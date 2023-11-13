import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    # tehtävä 6
    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_lataa_rahaa_kortille(self):
        self.maksukortti.lataa_rahaa(2000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 30.0)

    def test_ota_rahaa_kun_saldo_riittava(self):
        self.maksukortti.ota_rahaa(200)
        self.assertEqual(self.maksukortti.saldo_euroina(), 8.0)
    
    def test_ota_rahaa_kun_saldo_ei_riittaa(self):
        self.maksukortti.ota_rahaa(30000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_ota_rahaa_true_kun_riittaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(200), True)
    
    def test_ota_rahaa_false_kun_ei_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(30000), False)

    # tehtävä 7
    def test_saldo_euroissa_tulostaa_lauseen(self):
        oikea_merkkijono = "Kortilla on rahaa 10.00 euroa"
        self.assertEqual(self.maksukortti.__str__(), oikea_merkkijono)
