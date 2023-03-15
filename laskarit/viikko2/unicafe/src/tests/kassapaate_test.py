import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_kassassa_oikea_maara_alussa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_ei_edullisia_lounaita_alussa(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_ei_maukkaita_lounaita_alussa(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisella_edullinen_nostaa_kassaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_kateisella_edullinen_palauttaa_vaihtorahan(self):
        vaihto = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihto, 60)

    def test_kateisella_maukas_nostaa_kassaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(4000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_kateisella_maukas_palauttaa_vaihtorahan(self):
        vaihto = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihto, 100)

    def test_kateisella_myyty_edullinen_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_kateisella_ei_myyty_edullinen_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateisella_myyty_maukas_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_kateisella_ei_myyty_maukas_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisella_ei_myyty_edullinen_antaa_vaihtorahat(self):
        vaihto = self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(vaihto, 100)

    def test_kateisella_ei_myyty_maukas_antaa_vaihtorahat(self):
        vaihto = self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(vaihto, 100)

    def test_kateisella_ei_myyty_edullinen_ei_nosta_kassaa(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateisella_ei_myyty_maukas_ei_nosta_kassaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
#Maksukortti
    def test_kortilla_edullinen_vahentaa_arvoa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 760)

    def test_kortilla_edullinen_palauttaa_true(self):
        tulos = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(tulos, True)

    def test_kortilla_myyty_edullinen_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kortilla_ei_myyty_edullinen_ei_vahenna_arvoa(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 200)
    
    def test_kortilla_ei_myyty_edullinen_palauttaa_false(self):
        tulos = self.kassapaate.syo_edullisesti_kortilla(Maksukortti(200))
        self.assertEqual(tulos, False)
    
    def test_kortilla_ei_myyty_edullinen_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kortilla(Maksukortti(200))
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kortilla_myyty_edullinen_ei_muuta_kassaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

#Maukkaat kortilla
    def test_kortilla_maukas_vahentaa_arvoa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 600)

    def test_kortilla_maukas_palauttaa_true(self):
        tulos = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(tulos, True)

    def test_kortilla_myyty_maukas_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kortilla_ei_myyty_maukas_ei_vahenna_arvoa(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 200)
    
    def test_kortilla_ei_myyty_maukas_palauttaa_false(self):
        tulos = self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(200))
        self.assertEqual(tulos, False)
    
    def test_kortilla_ei_myyty_maukas_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(200))
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortilla_myyty_maukas_ei_muuta_kassaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

#Lisätään rahaa kortille

    def test_kortille_ladattaessa_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(self.maksukortti.saldo, 1500)

    def test_kortille_ladattaessa_kassa_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)

    def test_kortille_ei_voi_ladata_negatiivista(self):
        tulos = self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(tulos, None)