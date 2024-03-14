from abc import ABC, abstractmethod

import spacy
import stanza
from anbani.nlp.preprocessing import word_tokenize as ka_word_tokenize
from nltk.tokenize import word_tokenize

from datatrove.utils.typeshelper import Languages


class WordTokenizer(ABC):
    @abstractmethod
    def tokenize(self, text: str) -> list[str]:
        pass


class StanzaWordTokenizer(WordTokenizer):
    def __init__(self, stanza_language: str):
        self.stanza_language = stanza_language
        self._tokenizer = None

    @property
    def tokenizer(self):
        if self._tokenizer is None:
            self._tokenizer = stanza.Pipeline(self.stanza_language, processors="tokenize")
        return self._tokenizer

    def tokenize(self, text) -> list[str]:
        doc = self.tokenizer(text)
        tokens = [token.text for sentence in doc.sentences for token in sentence.tokens]
        return tokens


class NLTKTokenizer(WordTokenizer):
    def __init__(self, punkt_language: str):
        self.punkt_language = punkt_language

    def tokenize(self, text) -> list[str]:
        return word_tokenize(text, language=self.punkt_language)


class SpaCyTokenizer(WordTokenizer):
    def __init__(self, spacy_language: str, config=None):
        if config is None:
            self.tokenizer = spacy.blank(spacy_language)
        else:
            self.tokenizer = spacy.blank(spacy_language, config=config)

    def tokenize(self, text) -> list[str]:
        return [str(token) for token in self.tokenizer(text)]


class GeorgianTokenizer(WordTokenizer):
    def tokenize(self, text) -> list[str]:
        return ka_word_tokenize(text)


WORD_TOKENIZERS = {
    Languages.english: NLTKTokenizer("english"),
    Languages.german: NLTKTokenizer("german"),
    Languages.french: NLTKTokenizer("french"),
    Languages.czech: NLTKTokenizer("czech"),
    Languages.danish: NLTKTokenizer("danish"),
    Languages.dutch: NLTKTokenizer("dutch"),
    Languages.estonian: NLTKTokenizer("estonian"),
    Languages.finnish: NLTKTokenizer("finnish"),
    Languages.greek: NLTKTokenizer("greek"),
    Languages.italian: NLTKTokenizer("italian"),
    Languages.malayalam: NLTKTokenizer("malayalam"),
    Languages.norwegian: NLTKTokenizer("norwegian"),
    Languages.polish: NLTKTokenizer("polish"),
    Languages.portuguese: NLTKTokenizer("portuguese"),
    Languages.russian: NLTKTokenizer("russian"),
    Languages.slovenian: NLTKTokenizer("slovene"),
    Languages.spanish: NLTKTokenizer("spanish"),
    Languages.swedish: NLTKTokenizer("swedish"),
    Languages.turkish: NLTKTokenizer("turkish"),
    Languages.chinese: SpaCyTokenizer("zh", {"nlp": {"tokenizer": {"segmenter": "jieba"}}}),
    Languages.japanese: SpaCyTokenizer("ja"),
    Languages.vietnamese: SpaCyTokenizer("vi"),
    Languages.indonesian: SpaCyTokenizer("id"),
    Languages.persian: SpaCyTokenizer("fa"),
    Languages.korean: SpaCyTokenizer("ko"),
    Languages.arabic: SpaCyTokenizer("ar"),
    Languages.hindi: SpaCyTokenizer("hi"),
    Languages.tamil: SpaCyTokenizer("ta"),
    Languages.urdu: SpaCyTokenizer("ur"),
    Languages.marathi: SpaCyTokenizer("mr"),
    Languages.telugu: SpaCyTokenizer("te"),
    Languages.hungarian: SpaCyTokenizer("hu"),
    Languages.romanian: SpaCyTokenizer("ro"),
    Languages.ukrainian: SpaCyTokenizer("uk"),
    Languages.slovak: SpaCyTokenizer("sk"),
    Languages.bulgarian: SpaCyTokenizer("bg"),
    Languages.catalan: SpaCyTokenizer("ca"),
    Languages.croatian: SpaCyTokenizer("hr"),
    Languages.latin: SpaCyTokenizer("la"),
    Languages.serbian: SpaCyTokenizer("sr"),
    Languages.lithuanian: SpaCyTokenizer("lt"),
    Languages.hebrew: SpaCyTokenizer("he"),
    Languages.latvian: SpaCyTokenizer("lv"),
    Languages.icelandic: SpaCyTokenizer("is"),
    Languages.armenian: SpaCyTokenizer("hy"),
    Languages.basque: SpaCyTokenizer("eu"),
    Languages.thai: SpaCyTokenizer("th"),
    Languages.georgian: GeorgianTokenizer(),
    Languages.tagalog: SpaCyTokenizer("tl"),
    Languages.albanian: SpaCyTokenizer("sq"),
    Languages.macedonian: SpaCyTokenizer("mk"),
    Languages.azerbaijani: SpaCyTokenizer("az"),
    Languages.amharic: SpaCyTokenizer("am"),
    Languages.bengali: SpaCyTokenizer("bn"),
    Languages.malay: SpaCyTokenizer("ms"),
    Languages.urdu: SpaCyTokenizer("ur"),
    Languages.nepali: SpaCyTokenizer("ne"),
    Languages.kazakh: StanzaWordTokenizer("kk"),
    Languages.belarusian: StanzaWordTokenizer("be"),
    Languages.gujarati: SpaCyTokenizer("gu"),
    Languages.kannada: SpaCyTokenizer("kn"),
    Languages.welsh: StanzaWordTokenizer("cy"),
    Languages.norwegian_nynorsk: NLTKTokenizer("norwegian"),
    Languages.sinhala: SpaCyTokenizer("si"),
    Languages.tatar: SpaCyTokenizer("tt"),
    Languages.afrikaans: SpaCyTokenizer("af"),
    Languages.kirghiz: SpaCyTokenizer("ky"),
    Languages.irish: SpaCyTokenizer("ga"),
    Languages.luxembourgish: SpaCyTokenizer("lb"),
    Languages.maltese: StanzaWordTokenizer("mt"),
    Languages.sanskrit: SpaCyTokenizer("sa"),
    Languages.yoruba: SpaCyTokenizer("yo"),
    Languages.south_azerbaijani: SpaCyTokenizer("az"),
    Languages.serbocroatian: SpaCyTokenizer("sr"),
    Languages.bosnian: SpaCyTokenizer("hr"),  # Proxy language
    Languages.swahili: NLTKTokenizer("english"),  # Proxy language
    Languages.javanese: NLTKTokenizer("english"),  # Proxy language
    Languages.esperanto: NLTKTokenizer("english"),  # Proxy language
    Languages.uzbek: SpaCyTokenizer("tr"),  # Proxy language, alternative ru
    Languages.tajik: SpaCyTokenizer("ru"),  # Proxy language
    Languages.punjabi: SpaCyTokenizer("sa"),  # Proxy language
    Languages.occitan: NLTKTokenizer("italian"),  # Proxy language
    Languages.kurdish: NLTKTokenizer("english"),  # Proxy language, multiple scripts
    Languages.galician: NLTKTokenizer("portuguese"),  # Proxy language
}


def get_word_tokenizer(language: Languages | str):
    if language in WORD_TOKENIZERS:
        return WORD_TOKENIZERS[language]
    else:
        return WORD_TOKENIZERS[Languages.english]
