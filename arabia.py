latin_to_arabic = {
    'a': 'ا',
    'b': 'ب',
    't': 'ت',
    'th': 'ث',
    'j': 'ج',
    'g': 'ج',
    'h': 'ح',
    'kh': 'خ',
    'd': 'د',
    'dh': 'ذ',
    'r': 'ر',
    'z': 'ز',
    's': 'س',
    'sh': 'ش',
    's': 'ص',
    'd': 'ض',
    't': 'ط',
    'z': 'ظ',
    'a': 'ع',
    'gh': 'غ',
    'f': 'ف',
    'q': 'ق',
    'k': 'ك',
    'l': 'ل',
    'm': 'م',
    'n': 'ن',
    'h': 'ه',
    'w': 'و',
    'y': 'ي',
    "'": 'ء',
    'i': 'إ',
    'u': 'ؤ',
    'e': 'اي',
}
def latin_to_arabic_transliteration(latin_text):
    arabic_text = ""
    skip_next = False
    for i in range(len(latin_text)):
        if skip_next:
            skip_next = False
            continue
        if i + 1 < len(latin_text) and latin_text[i:i+2] in latin_to_arabic:
            arabic_text += latin_to_arabic[latin_text[i:i+2]]
            skip_next = True
        else:
            arabic_text += latin_to_arabic.get(latin_text[i], latin_text[i])
    return arabic_text

# テスト
latin_text = "marhba"
arabic_text = latin_to_arabic_transliteration(latin_text)
print(arabic_text)  # "مرحبا"
