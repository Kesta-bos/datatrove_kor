from dataclasses import dataclass


@dataclass
class NiceRepr:
    emoji: str
    name: str

    def __post_init__(self):
        self.name = self.name.capitalize()

    def get_name(self):
        return f"---> {self.emoji} {self.name}\n"


class Languages:
    english = "en"
    spanish = "es"
    portuguese = "pt"
    italian = "it"
    french = "fr"
    romanian = "ro"
    german = "de"
    latin = "la"
    czech = "cs"
    danish = "da"
    finnish = "fi"
    greek = "el"
    norwegian = "no"
    polish = "pl"
    russian = "ru"
    slovenian = "sl"
    swedish = "sv"
    turkish = "tr"
    dutch = "nl"
    chinese = "zh"
    japanese = "ja"
    vietnamese = "vi"
    indonesian = "id"
    persian = "fa"
    korean = "ko"
    arabic = "ar"
    thai = "th"
    hindi = "hi"
    bengali = "bn"
    tamil = "ta"
    hungarian = "hu"
    ukrainian = "uk"
    slovak = "sk"
    bulgarian = "bg"
    catalan = "ca"
    croatian = "hr"
    serbian = "sr"
    lithuanian = "lt"
    estonian = "et"
    hebrew = "he"
    latvian = "lv"
    serbocroatian = "sh"  # Deprecated
    albanian = "sq"
    azerbaijani = "az"
    icelandic = "is"
    macedonian = "mk"
    georgian = "ka"
    galician = "gl"
    armenian = "hy"
    basque = "eu"

    swahili = "sw"
    malay = "ms"
    tagalog = "tl"
    javanese = "jv"
    punjabi = "pa"
    bihari = "bh"  # Deprecated
    gujarati = "gu"
    yoruba = "yo"
    marathi = "mr"
    urdu = "ur"
    amharic = "am"
    telugu = "te"
    malayalam = "ml"
    kannada = "kn"
    nepali = "ne"
    kazakh = "kk"
    belarusian = "be"
    burmese = "my"
    esperanto = "eo"
    uzbek = "uz"
    khmer = "km"
    tajik = "tg"
    welsh = "cy"
    norwegian_nynorsk = "nn"
    bosnian = "bs"
    sinhala = "si"
    tatar = "tt"
    afrikaans = "af"
    oriya = "or"
    kirghiz = "ky"
    irish = "ga"
    occitan = "oc"
    kurdish = "ku"
    lao = "lo"
    luxembourgish = "lb"
    bashkir = "ba"
    western_frisian = "fy"
    pashto = "ps"
    maltese = "mt"
    breton = "bt"
    assamese = "as"
    malagasy = "mg"
    divehi = "dv"
    yiddish = "yi"
    somali = "so"
    sanskrit = "sa"
    sindhi = "sd"
    turkmen = "tk"
    south_azerbaijani = "azb"
    sorani = "ckb"
    cebuano = "ceb"
    war = "war"


class StatHints:
    total = "total"
    dropped = "dropped"
    forwarded = "forwarded"


class ExtensionHelperSD:
    stage_1_signature = ".c4_sig"
    stage_2_duplicates = ".c4_dup"
    index = ".c4_index"


class ExtensionHelperES:
    stage_1_sequence = ".es_sequence"
    stage_1_sequence_size = ".es_sequence.size"
    stage_2_big_sequence = ".big_sequence"
    stage_2_bytes_offset = ".info"
    stage_3_bytes_ranges = ".bytearange"
