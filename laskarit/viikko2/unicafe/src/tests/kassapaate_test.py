import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
    
    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_kassapaatteen_saldo_alussa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
    
    def test_myytyja_lounaita_on_alussa_nolla(self):
        aterioita_myyty = self.kassapaate.edulliset + self.kassapaate.maukkaat
        self.assertEqual(aterioita_myyty, 0)
    
    def test_kateisella_ostettu_edullinen(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(1000)
        self.assertEqual(vaihtoraha, 760)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisella_ostettu_maukas(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(1000)
        self.assertEqual(vaihtoraha, 600)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.0)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisella_ostettu_edullinen_rahat_ei_riita(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateisella_ostettu_maukas_rahat_ei_riita(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortilla_ostettu_edullinen(self):
        kortti = Maksukortti(1000)
        onnistuiko_korttiosto = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(onnistuiko_korttiosto, True)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
    
    def test_kortilla_ostettu_maukas(self):
        kortti = Maksukortti(1000)
        onnistuiko_korttiosto = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(onnistuiko_korttiosto, True)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
    
    def test_kortilla_ostettu_edullinen_ei_katetta(self):
        kortti = Maksukortti(150)
        onnistuiko_korttiosto = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(onnistuiko_korttiosto, False)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
    
    def test_kortilla_ostettu_maukas_ei_katetta(self):
        kortti = Maksukortti(150)
        onnistuiko_korttiosto = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(onnistuiko_korttiosto, False)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
    
    def test_rahan_lataaminen_kortille(self):
        kortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti, 2000)
        self.assertEqual(kortti.saldo_euroina(), 30.0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1020.0)

    def test_negatiivisen_summan_lataaminen_kortille(self):
        kortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti, -2000)
        self.assertEqual(kortti.saldo_euroina(), 10.0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
