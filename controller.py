import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None


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

    def handleLanguageSelection(self, e):
        self._view.t.value = f"the selected language is {self._view._ddLanguage.value}"
        self._view.update()

    def handleSearchType(self,e):
        self._view.t2.value = f"The search type selected is {self._view._ddSearchType.value}"
        self._view.update()

    def handleSpellCheck(self,e):

        lan = self._view._ddLanguage.value
        if lan == "":
            self._view._lvOut.controls.append(ft.Text("You must select a language", color='red'))
            self._view.update()
            return

        searchType = self._view._ddSearchType.value
        if searchType == "":
            self._view._lvOut.controls.append(ft.Text("You must select a  search's type", color='red'))
            self._view.update()
            return

        toCorrect = self._view._txtIn.value
        if toCorrect == "":
            self._view._lvOut.controls.append(ft.Text("You must submit a text", color='red'))
            self._view.update()
            return

        (wrongWords, exTime) = self.handleSentence(toCorrect,lan,searchType)
        self._view._lvOut.controls.append(ft.Text(f"The text to be corrected is: {toCorrect}"))
        self._view._lvOut.controls.append(ft.Text(wrongWords))
        self._view._lvOut.controls.append(ft.Text())

        self._view._txtIn.value = ""
        self._view.update()
def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text

