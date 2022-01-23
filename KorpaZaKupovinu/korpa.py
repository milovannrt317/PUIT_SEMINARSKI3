from decimal import Decimal
from django.conf import settings
from ProdavnicaTrotineta.models import Trotinet

class Korpa(object):
    def __init__(self, request):
        self.sesija = request.session
        korpa = self.sesija.get(settings.KORPA_ZA_KUPOVINU_SESSION_KEY)
        if not korpa:
            korpa = self.sesija[settings.KORPA_ZA_KUPOVINU_SESSION_KEY] = {}

        self.korpa = korpa

    def __iter__(self):
        trotineti_ids = self.korpa.keys()
        trotineti = Trotinet.objects.filter(id__in=trotineti_ids)
        korpakopija = self.korpa.copy()

        for trotinet in trotineti:
            korpakopija[str(trotinet.id)]['trotinet'] = trotinet

        for stavka in korpakopija.values():
            stavka['cena'] = Decimal(stavka['cena'])
            stavka['ukupna_cena'] = stavka['cena'] * stavka['kolicina']
            yield stavka

    def __len__(self):
        return sum(stavka['kolicina'] for stavka in self.korpa.values())

    def Dodaj(self, trotinet, kolicina=1, dodati_na_kolicinu=True):
        trotinet_id = str(trotinet.id)

        if trotinet_id not in self.korpa:
            self.korpa[trotinet_id] = {'kolicina':0, 'cena': str(trotinet.cena)}

        if dodati_na_kolicinu:
            self.korpa[trotinet_id]['kolicina'] += kolicina
        else:
            self.korpa[trotinet_id]['kolicina'] = kolicina

        self.sesija.modified = True

    def Ukloni(self, trotinet):
        trotinet_id = str(trotinet.id)
        if trotinet_id in self.korpa:
            del self.korpa[trotinet_id]
            self.sesija.modified=True

    def ObrisiJeIzSesije(self):
        del self.sesija[settings.KORPA_ZA_KUPOVINU_SESSION_KEY]
        self.sesija.modified = True

    def UzmiUkupnuCenu(self):
        return sum(Decimal(stavka['cena']) * stavka['kolicina'] for stavka in self.korpa.values())

