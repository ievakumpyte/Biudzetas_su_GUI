import pickle
from modules.IslaiduIrasas import IslaiduIrasas, Irasas
from modules.PajamuIrasas import PajamuIrasas


class Biudzetas:
    def __init__(self):
        self.zurnalas = self.gauti_ataskaita()

    def gauti_ataskaita(self):
        try:
            with open ('zurnalas.pkl', 'rb') as failas:
                zurnalas = pickle.load(failas)
                return zurnalas
        except:
            with open ('zurnalas.pkl', 'wb') as failas:
                zurnalas = []
                pickle.dump(zurnalas, failas)
                return zurnalas


    def irasyti_ataskaita(self):

        with open('zurnalas.pkl', 'wb') as failas:
            pickle.dump(self.zurnalas, failas)



    def prideti_pajamu_irasa(self, suma, siuntejas="darbdavys", papildoma_informacija="atlyginimas"):
        pajamos = PajamuIrasas(suma, siuntejas, papildoma_informacija)
        self.zurnalas.append(pajamos)
        self.irasyti_ataskaita()

    def prideti_islaidu_irasa(self, suma, atsiskaitymo_budas="kortele", isigyta_preke="pirkinys"):
        islaidos = IslaiduIrasas(suma, atsiskaitymo_budas, isigyta_preke)
        self.zurnalas.append(islaidos)
        self.irasyti_ataskaita()

    def gauti_balansa(self):
        bendra = 0
        for irasas in self.zurnalas:
            if type(irasas) is PajamuIrasas:
                bendra += int(irasas.suma)
            if type(irasas) is IslaiduIrasas:
                bendra -= int(irasas.suma)
        # print("Balansas: ", bendra)
        return bendra

    def parodyti_ataskaita(self):

        print("Ataskaita")
        print("---------------")
        for irasas in self.zurnalas:
            print(irasas)
        print("---------------")

    def isvalyti(self):
        self.zurnalas = []


    def __repr__(self):
        return f"{self.zurnalas}"

    def __str__(self):
        return f"{self.zurnalas}"

