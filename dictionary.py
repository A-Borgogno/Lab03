class Dictionary:
    def __init__(self, language, parole=[]):
        self.language = language
        self.parole = parole
        self.loadDictionary(language+".txt")

    def loadDictionary(self,path):
        try:
            filePath = f"resources/{path}"
            infile = open(filePath, "r", encoding="utf-8")
            for riga in infile:
                self.parole.append(riga.strip())
            infile.close()
        except FileNotFoundError:
            print(f"File {path} non trovato")

    def printAll(self):
        pass

    def verificaParole(self, testo):
        listaParoleErrate = []
        testoScomposto = testo.strip().split(" ")
        for p in testoScomposto:
            if not self.parole.__contains__(p.strip(",").lower()):
                listaParoleErrate.append(p.strip(","))
        return listaParoleErrate

    def verificaParoleLinear(self, testo):
        listaParoleErrate = []
        testoScomposto = testo.strip().split(" ")
        for p in testoScomposto:
            trovata = False
            i = 0
            while not trovata and i < len(self.parole):
                if p.strip(",").lower() == self.parole[i]:
                    trovata = True
                i += 1
            if not trovata:
                listaParoleErrate.append(p.strip(","))
        return listaParoleErrate

    def verificaParoleDichotomic(self, testo):
        listaParoleErrate = []
        testoScomposto = testo.strip().split(" ")
        for p in testoScomposto:
            scartate = []
            trovata = False
            min = 0
            max = len(self.parole)
            while (not trovata) and (len(scartate)<len(self.parole)-1):
                posizione = round((min+max)/2)
                if p.strip(",").lower() == self.parole[posizione]:
                    scartate.append(p)
                    trovata = True
                elif p.strip(",").lower() < self.parole[posizione]:
                    scartate += self.parole[posizione:max]
                    max = posizione
                else:
                    scartate += self.parole[min:posizione]
                    min = posizione
            if not trovata:
                listaParoleErrate.append(p.strip(","))
        return listaParoleErrate




    @property
    def dict(self):
        return self._dict