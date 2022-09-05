import pickle
from modules.IslaiduIrasas import Irasas, IslaiduIrasas
from modules.PajamuIrasas import Irasas, PajamuIrasas
from modules.Biudzetas import Biudzetas

biudzetas = Biudzetas()

while True:
    ivestis = int(input(
        "Pasirinkite iš menu: 1 - Įvesti pajamas, 2 - Įvesti išlaidas, 3 - Peržiūreti balansą, 4 - Peržiūreti ataskaitą, 5 - Isvalyti biudzeta, 6 - Baigti::\n "))
    if ivestis == 1:
        pajamos = input("Iveskite pajamas: ")
        biudzetas.prideti_pajamu_irasa(pajamos)

    if ivestis == 2:
        islaidos = input("Iveskite islaidas: ")
        biudzetas.prideti_islaidu_irasa(islaidos)

    if ivestis == 3:
        biudzetas.gauti_balansa()
    if ivestis == 4:
        biudzetas.parodyti_ataskaita()
    if ivestis == 5:
        biudzetas.isvalyti()
    if ivestis == 6:
        print("Viso")
        break

