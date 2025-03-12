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
            if not self.parole.__contains__(p.lower()):
                listaParoleErrate.append(p)
        return listaParoleErrate

    def verificaParoleLinear(self, testo):
        listaParoleErrate = []
        testoScomposto = testo.strip().split(" ")
        for p in testoScomposto:
            trovata = False
            i = 0
            while not trovata and i < len(self.parole):
                if p.lower() == self.parole[i]:
                    trovata = True
                i += 1
            if not trovata:
                listaParoleErrate.append(p)
        return listaParoleErrate

    def verificaParoleDichotomic(self, testo):
        listaParoleErrate = []
        testoScomposto = testo.strip().split(" ")
        for p in testoScomposto:
            scartate = []
            trovata = False
            posizione = len(self.parole)//2
            while (not trovata) and (len(scartate)<len(self.parole)):
                print(f"{len(scartate)}    {len(self.parole)}")
                print(posizione)
                if p.lower() == self.parole[posizione]:
                    scartate.append(p)
                    trovata = True
                elif p.lower() < self.parole[posizione]:
                    scartate += self.parole[posizione:]
                    posizione = posizione//2
                else:
                    scartate += self.parole[:posizione]
                    posizione = posizione*2
            if not trovata:
                listaParoleErrate.append(p)
        return listaParoleErrate




    @property
    def dict(self):
        return self._dict