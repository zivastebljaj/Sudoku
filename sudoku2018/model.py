import random

def transponiraj(mat):
    transponiranka = []
    for i in range(len(mat[0])):
        transponirana_vrstica = []
        for vrstica in mat:
            transponirana_vrstica.append(vrstica[i])
        transponiranka.append(transponirana_vrstica)
    return transponiranka

def bloki(matrika):
    blok1 = [matrika[i][j] for i in range(3) for j in range(3)]
    blok2 = [matrika[i][j] for i in range(3) for j in range(3, 6)]
    blok3 = [matrika[i][j] for i in range(3) for j in range(6, 9)]
    blok4 = [matrika[i][j] for i in range(3, 6) for j in range(3)]
    blok5 = [matrika[i][j] for i in range(3, 6) for j in range(3, 6)]
    blok6 = [matrika[i][j] for i in range(3, 6) for j in range(6, 9)]
    blok7 = [matrika[i][j] for i in range(6, 9) for j in range(3)]
    blok8 = [matrika[i][j] for i in range(6, 9) for j in range(3, 6)]
    blok9 = [matrika[i][j] for i in range(6, 9) for j in range(6, 9)]
    return [blok1, blok2, blok3, blok4, blok5, blok6, blok7, blok8, blok9]


class Igra:

    def __init__(self, tezavnost=1):
        self.tezavnost = tezavnost
        self.tezavnosti = {0:7, 1:6, 2:5, 3:4}

    def predloga(self):
        plosca = [random.sample(list(range(1, 10)), 9)]
        plosca.append(plosca[0][3:] + plosca[0][:3])
        plosca.append(plosca[0][6:] + plosca[0][:6])
        cetrta_vrstica = (plosca[0][1:3] +
                          plosca[0][0:1] +
                          plosca[0][4:6] +
                          plosca[0][3:4] +
                          plosca[0][7:9] +
                          plosca[0][6:7])
        plosca.append(cetrta_vrstica)
        plosca.append(cetrta_vrstica[3:] + cetrta_vrstica[:3])
        plosca.append(cetrta_vrstica[6:] + cetrta_vrstica[:6])
        sedma_vrstica = (plosca[3][1:3] +
                         plosca[3][0:1] +
                         plosca[3][4:6] +
                         plosca[3][3:4] +
                         plosca[3][7:9] +
                         plosca[3][6:7])
        plosca.append(sedma_vrstica)
        plosca.append(sedma_vrstica[3:] + sedma_vrstica[:3])
        plosca.append(sedma_vrstica[6:] + sedma_vrstica[:6])
        plosca[1], plosca[2] = plosca[2], plosca[1]
        plosca[3], plosca[5] = plosca[5], plosca[3]
        plosca[6], plosca[7] = plosca[7], plosca[6]
        plosca = transponiraj(plosca)
        plosca[0], plosca[2] = plosca[2], plosca[0]
        plosca[3], plosca[4] = plosca[4], plosca[3]
        plosca[7], plosca[8] = plosca[8], plosca[7]
        plosca = transponiraj(plosca)
        return plosca

    def ustvari_zacetno_plosco(self):
        predloga = self.predloga()
        zacetna_plosca = []
        for i in range(9):
            mesta = random.sample(range(9),
                                  k=self.tezavnosti[self.tezavnost])
            vrstica = []
            for j in range(9):
                if j in mesta:
                    vrstica.append(predloga[i][j])
                else:
                    vrstica.append(None)
            zacetna_plosca.append(vrstica)
        return zacetna_plosca

    def preveri_vrstice(self, plosca):
        for vrstica in plosca:
            if set(vrstica) != set(range(1, 10)):
                return False
        return True

    def preveri_stolpce(self, plosca):
        for vrstica in transponiraj(plosca):
            if set(vrstica) != set(range(1, 10)):
                return False
        return True

    def preveri_kvadrate(self, plosca):
        for blok in bloki(plosca):
            if set(blok) != set(range(1, 10)):
                return False
        return True

    def preveri_pravilnost(self, plosca):
        return (self.preveri_vrstice(plosca) and
                self.preveri_stolpce(plosca) and
                self.preveri_kvadrate(plosca))








