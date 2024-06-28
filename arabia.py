arabic_to_latin = {
    'ا': 'a',
    'ب': 'b',
    'ت': 't',
    'ث': 'th',
    'ج': 'j',
    'ح': 'h',
    'خ': 'kh',
    'د': 'd',
    'ذ': 'dh',
    'ر': 'r',
    'ز': 'z',
    'س': 's',
    'ش': 'sh',
    'ص': 's',
    'ض': 'd',
    'ط': 't',
    'ظ': 'z',
    'ع': 'a',
    'غ': 'gh',
    'ف': 'f',
    'ق': 'q',
    'ك': 'k',
    'ل': 'l',
    'م': 'm',
    'ن': 'n',
    'ه': 'h',
    'و': 'w',
    'ي': 'y',
    'ى': 'a',
    'ء': "'",
    'أ': 'a',
    'إ': 'i',
    'ؤ': 'u',
    'ئ': 'i',
}

def arabic_to_latin_transliteration(arabic_text):
    latin_text = ""
    for char in arabic_text:
        latin_text += arabic_to_latin.get(char, char)
    return latin_text

# テスト
arabic_text = "مرحبا"
latin_text = arabic_to_latin_transliteration(arabic_text)
print(latin_text)  # "mrhb"
