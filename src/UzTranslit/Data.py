class Mapping:
    cyr_lat = {}  # Mapping dictionary for Cyrillic to Latin
    cyr_nlt = {}  # Mapping dictionary for Cyrillic to New Latin
    lat_cyr = {}  # Mapping dictionary for Latin to Cyrillic
    lat_nlt = {}  # Mapping dictionary for Latin to New Latin
    nlt_cyr = {}  # Mapping dictionary for New Latin to Cyrillic
    nlt_lat = {}  # Mapping dictionary for New Latin Latin
    cyr_vowel = []    # Cyrillic vowels list
    lat_vowel = []  # Latin vowels list
    nlt_vowel = []  # NewLatin vowels list
    def __init__(self):
        self.__initial_data()

    def __initial_data(self):
        self.cyr_vowel = ["а", "и", "э", "у", "ў", "о", "е", "ё", "ю", "я", "А", "И", "Э", "У", "Ў", "О", "Е", "Ё", "Ю", "Я"]
        self.lat_vowel = ["a", "i", "e", "u", "o‘", "o", "A", "I", "E", "U", "O‘", "O"]
        self.nlt_vowel = ["a", "i", "e", "u", "ō", "o", "A", "I", "E", "U", "Ō" "O"]

        self.cyr_lat = {
            'А': 'A',
            'Б': 'B',
            'Д': 'D',
            'Э': 'E',
            'Ф': 'F',
            'Г': 'G',
            'Ҳ': 'H',
            'И': 'I',
            'Ж': 'J',
            'К': 'K',
            'Л': 'L',
            'М': 'M',
            'Н': 'N',
            'О': 'O',
            'П': 'P',
            'Қ': 'Q',
            'Р': 'R',
            'С': 'S',
            'Т': 'T',
            'У': 'U',
            'В': 'V',
            'Х': 'X',
            'Й': 'Y',
            'З': 'Z',
            'Ў': 'Oʻ',
            'Ғ': 'Gʻ',
            'Ш': 'Sh',
            'Ч': 'Ch',
            'Нг': 'Ng',
            # Uzbek tildia ish yuritish 47-bet
            # 'Ё': 'Yo',
            # 'Ю': 'Yu',
            # 'Я': 'Ya',

            'а': 'a',
            'б': 'b',
            'д': 'd',
            'э': 'e',
            'ф': 'f',
            'г': 'g',
            'ҳ': 'h',
            'и': 'i',
            'ж': 'j',
            'к': 'k',
            'л': 'l',
            'м': 'm',
            'н': 'n',
            'о': 'o',
            'п': 'p',
            'қ': 'q',
            'р': 'r',
            'с': 's',
            'т': 't',
            'у': 'u',
            'в': 'v',
            'х': 'x',
            'й': 'y',
            'з': 'z',
            'ў': 'oʻ',
            'ғ': 'gʻ',
            'ш': 'sh',
            'ч': 'ch',
            'нг': 'ng',
            'ъ': 'ʼ',
            # Uzbek tildia ish yuritish 47-bet
            # 'ё': 'yo',
            # 'ю': 'yu',
            # 'я': 'ya',

            'ь': '', # independent of upper/lower case

            # rule объект [Kitob: o'zbek adabiy tili ish yuritish daftari 43,47-bet]
            'ъе': 'ye',
            'ъё': 'yo',
            'ъя': 'ya',
            'ъю': 'yu',
            'ье': 'ye',
            'ьё': 'yo',
            'ья': 'ya',
            'ью': 'yu',

            # 'Е': 'E, Ye', cyr_rule1 qoidasi asosida 47-bet
            # 'е': 'e, ye', cyr_rule1 qoidasi asosida 47-bet

            # 'Ц': 'S, TS', cyr_rule2 qoidasi asosida 48-bet
            # 'ц': 's, ts', cyr_rule2 qoidasi asosida 48-bet
        }

        self.cyr_nlt = {
            'А': 'A',
            'Б': 'B',
            'Д': 'D',
            'Э': 'E',
            'Ф': 'F',
            'Г': 'G',
            'Ҳ': 'H',
            'И': 'I',
            'Ж': 'J',
            'К': 'K',
            'Л': 'L',
            'М': 'M',
            'Н': 'N',
            'О': 'O',
            'П': 'P',
            'Қ': 'Q',
            'Р': 'R',
            'С': 'S',
            'Т': 'T',
            'У': 'U',
            'В': 'V',
            'Х': 'X',
            'Й': 'Y',
            'З': 'Z',
            'Ў': 'Ō',
            'Ғ': 'Ḡ',
            'Ш': 'Ş',
            'Ч': 'Ç',
            'Нг': 'Ng',
            # Uzbek tildia ish yuritish 47-bet
            # 'Ё': 'Yo',
            # 'Ю': 'Yu',
            # 'Я': 'Ya',

            'а': 'a',
            'б': 'b',
            'д': 'd',
            'э': 'e',
            'ф': 'f',
            'г': 'g',
            'ҳ': 'h',
            'и': 'i',
            'ж': 'j',
            'к': 'k',
            'л': 'l',
            'м': 'm',
            'н': 'n',
            'о': 'o',
            'п': 'p',
            'қ': 'q',
            'р': 'r',
            'с': 's',
            'т': 't',
            'у': 'u',
            'в': 'v',
            'х': 'x',
            'й': 'y',
            'з': 'z',
            'ў': 'ō',
            'ғ': 'ḡ',
            'ш': 'ş',
            'ч': 'ç',
            'нг': 'ng',
            'ъ': 'ʼ',
            # Uzbek tildia ish yuritish 47-bet
            # 'ё': 'yo',
            # 'ю': 'yu',
            # 'я': 'ya',

            'ь': '',  # independent of upper/lower case

            # rule объект [Kitob: o'zbek adabiy tili ish yuritish daftari 43,47-bet]
            'ъе': 'ye',
            'ъё': 'yo',
            'ъя': 'ya',
            'ъю': 'yu',
            'ье': 'ye',
            'ьё': 'yo',
            'ья': 'ya',
            'ью': 'yu',

            # 'Е': 'E, Ye', cyr_rule1 qoidasi asosida 47-bet
            # 'е': 'e, ye', cyr_rule1 qoidasi asosida 47-bet

            # 'Ц': 'S, TS', cyr_rule2 qoidasi asosida 48-bet
            # 'ц': 's, ts', cyr_rule2 qoidasi asosida 48-bet
        }

        self.lat_cyr = {
            'A': 'А',
            'B': 'Б',
            'D': 'Д',
            'F': 'Ф',
            'G': 'Г',
            'H': 'Ҳ',
            'I': 'И',
            'J': 'Ж',
            'K': 'К',
            'L': 'Л',
            'M': 'М',
            'N': 'Н',
            'O': 'О',
            'P': 'П',
            'Q': 'Қ',
            'R': 'Р',
            'S': 'С',
            'T': 'Т',
            'U': 'У',
            'V': 'В',
            'X': 'Х',
            'Y': 'Й',
            'Z': 'З',
            'Oʻ': 'Ў',
            'Gʻ': 'Ғ',
            'Sh': 'Ш',
            'Ch': 'Ч',
            'Ng': 'Нг',
            #47-bet qodiasi
            'Ye': 'Е',
            'Yo': 'Ё',
            'Yu': 'Ю',
            'Ya': 'Я',
            'Yoʻ': 'Йў',
            'YOʻ': 'ЙЎ',

            'a': 'а',
            'b': 'б',
            'd': 'д',
            'f': 'ф',
            'g': 'г',
            'h': 'ҳ',
            'i': 'и',
            'j': 'ж',
            'k': 'к',
            'l': 'л',
            'm': 'м',
            'n': 'н',
            'o': 'о',
            'p': 'п',
            'q': 'қ',
            'r': 'р',
            's': 'с',
            't': 'т',
            'u': 'у',
            'v': 'в',
            'x': 'х',
            'y': 'й',
            'z': 'з',
            'oʻ': 'ў',
            'gʻ': 'ғ',
            'sh': 'ш',
            'ch': 'ч',
            'ng': 'нг',
            'ʼ': 'ъ',
            # 47-bet qoidasi
            'ye': 'е',
            'yo': 'ё',
            'yu': 'ю',
            'ya': 'я',
            'yoʻ': 'йў',

            # 'E': 'Э', # lat_rule1 qoidasi asosida 47-bet
            # 'e': 'э', # lat_rule1 qoidasi asosida 47-bet
        }

        self.lat_nlt = {

        }

        self.nlt_cyr = {

        }
        self.nlt_lat = {

        }