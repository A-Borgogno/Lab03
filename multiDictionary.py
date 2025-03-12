import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self, diz={}):
       self.diz = diz
       self.diz["italian"] = d.Dictionary("italian")
       self.diz["english"] = d.Dictionary("english")
       self.diz["spanish"] = d.Dictionary("spanish")



    def printDic(self, language):
        pass

    def searchWord(self, words, language):
        dictionaryLingua = self.diz.get(language)
        errori = dictionaryLingua.verificaParole(words)
        return errori

    def searchWordLinear(self, words, language):
        dictionaryLingua = self.diz.get(language)
        errori = dictionaryLingua.verificaParoleLinear(words)
        return errori

    def searchWordDichotomic(self, words, language):
        dictionaryLingua = self.diz.get(language)
        errori = dictionaryLingua.verificaParoleDichotomic(words)
        return errori
