import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.multiDictionary = md.MultiDictionary()

    def handleSentence(self, txtIn, language):
        print("-----CONTAINS-----")
        tic1 = time.time()
        errori = self.multiDictionary.searchWord(txtIn, language)
        toc1 = time.time()
        for e in errori:
            print(e)
        print(f"Contains: {toc1 - tic1} secondi")

        print("-----RICERCA LINEARE-----")
        tic2 = time.time()
        errori = self.multiDictionary.searchWordLinear(txtIn, language)
        toc2 = time.time()
        for e in errori:
            print(e)
        print(f"Contains: {toc2 - tic2} secondi")

        print("-----RICERCA DICOTOMICA-----")
        tic3 = time.time()
        errori = self.multiDictionary.searchWordDichotomic(txtIn, language)
        toc3 = time.time()
        for e in errori:
            print(e)
        print(f"Contains: {toc3 - tic3} secondi")


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    pass