#!/usr/bin/env python3
"""
Define the supported languages

As of September 2023 supported languages cannot be
dynamically queried, so:

Implemented according to this list: https://www.deepl.com/docs-api/translate-text
"""
from collections import namedtuple
from enum import StrEnum

Language = namedtuple("Language", ["code", "name"])


class LanguageType(StrEnum):
    """divide target and source without magic strings"""

    SOURCE = "source"
    TARGET = "target"


arabic = Language("AR", "Arabic")
bulgarian = Language("BG", "Bulgarian")
czech = Language("CS", "Czech")
danish = Language("DA", "Danish")
german = Language("DE", "German")
greek = Language("EL", "Greek")
english = Language("EN", "English")
english_gb = Language("EN-GB", "English (British)")
english_us = Language("EN-US", "English (American)")
spanish = Language("ES", "Spanish")
estonian = Language("ET", "Estonian")
finnish = Language("FI", "Finnish")
french = Language("FR", "French")
hungarian = Language("HU", "Hungarian")
indonesian = Language("ID", "Indonesian")
italian = Language("IT", "Italian")
japanese = Language("JA", "Japanese")
korean = Language("KO", "Korean")
lithuanian = Language("LT", "Lithuanian")
latvian = Language("LV", "Latvian")
norwegian = Language("NB", "Norwegian")
dutch = Language("NL", "Dutch")
polish = Language("PL", "Polish")
portugese = Language("PT", "Portuguese")
portugese_br = Language("PT-BR", "Portuguese (Brazilian)")
portugese_pt = Language("PT-PT", "Portuguese (all excluding Brazilian)")
romanian = Language("RO", "Romanian")
russian = Language("RU", "Russian")
slovak = Language("SK", "Slovak")
slovenian = Language("SL", "Slovenian")
swedish = Language("SV", "Swedish")
turkish = Language("TR", "Turkish")
ukranian = Language("UK", "Ukrainian")
chinese = Language("ZH", "Chinese")

source_languages = {}
source_languages[arabic.code] = arabic
source_languages[bulgarian.code] = bulgarian
source_languages[czech.code] = czech
source_languages[danish.code] = danish
source_languages[german.code] = german
source_languages[greek.code] = greek
source_languages[english.code] = english
source_languages[spanish.code] = spanish
source_languages[estonian.code] = estonian
source_languages[finnish.code] = finnish
source_languages[french.code] = french
source_languages[hungarian.code] = hungarian
source_languages[indonesian.code] = indonesian
source_languages[italian.code] = italian
source_languages[japanese.code] = japanese
source_languages[korean.code] = korean
source_languages[lithuanian.code] = lithuanian
source_languages[latvian.code] = latvian
source_languages[norwegian.code] = norwegian
source_languages[dutch.code] = dutch
source_languages[polish.code] = polish
source_languages[portugese.code] = portugese
source_languages[romanian.code] = romanian
source_languages[russian.code] = russian
source_languages[slovak.code] = slovak
source_languages[slovenian.code] = slovenian
source_languages[swedish.code] = swedish
source_languages[turkish.code] = turkish
source_languages[ukranian.code] = ukranian
source_languages[chinese.code] = chinese


target_languages = {}
target_languages[arabic.code] = arabic
target_languages[bulgarian.code] = bulgarian
target_languages[czech.code] = czech
target_languages[danish.code] = danish
target_languages[german.code] = german
target_languages[greek.code] = greek
target_languages[english_gb.code] = english_gb
target_languages[english_us.code] = english_us
target_languages[spanish.code] = spanish
target_languages[estonian.code] = estonian
target_languages[finnish.code] = finnish
target_languages[french.code] = french
target_languages[hungarian.code] = hungarian
target_languages[indonesian.code] = indonesian
target_languages[italian.code] = italian
target_languages[japanese.code] = japanese
target_languages[korean.code] = korean
target_languages[lithuanian.code] = lithuanian
target_languages[latvian.code] = latvian
target_languages[norwegian.code] = norwegian
target_languages[dutch.code] = dutch
target_languages[polish.code] = polish
target_languages[portugese_br.code] = portugese_br
target_languages[portugese_pt.code] = portugese_pt
target_languages[romanian.code] = romanian
target_languages[russian.code] = russian
target_languages[slovak.code] = slovak
target_languages[slovenian.code] = slovenian
target_languages[swedish.code] = swedish
target_languages[turkish.code] = turkish
target_languages[ukranian.code] = ukranian
target_languages[chinese.code] = chinese
