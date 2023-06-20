ELEMENTS = {
    'h', 'he', 'li', 'be', 'b', 'c', 'n', 'o', 'f', 'ne',
    'na', 'mg', 'al', 'si', 'p', 's', 'cl', 'ar', 'k', 'ca',
    'sc', 'ti', 'v', 'cr', 'mn', 'fe', 'co', 'ni', 'cu', 'zn',
    'ga', 'ge', 'as', 'se', 'br', 'kr', 'rb', 'sr', 'y', 'zr',
    'nb', 'mo', 'tc', 'ru', 'rh', 'pd', 'ag', 'cd', 'in', 'sn',
    'sb', 'te', 'i', 'xe', 'cs', 'ba', 'la', 'ce', 'pr', 'nd',
    'pm', 'sm', 'eu', 'gd', 'tb', 'dy', 'ho', 'er', 'tm', 'yb',
    'lu', 'hf', 'ta', 'w', 're', 'os', 'ir', 'pt', 'au', 'hg',
    'tl', 'pb', 'bi', 'po', 'at', 'rn', 'fr', 'ra', 'ac', 'th',
    'pa', 'u', 'np', 'pu', 'am', 'cm', 'bk', 'cf', 'es', 'fm',
    'md', 'no', 'lr', 'rf', 'db', 'sg', 'bh', 'hs', 'mt', 'ds',
    'rg', 'cn', 'nh', 'fl', 'mc', 'lv', 'ts', 'og',
}


def _enrich_word(word: str) -> str:
    chars = list(word)
    previous_char = ''
    for i, char in enumerate(chars):
        if not char.isalpha():
            previous_char = ''
            continue
        char_lower = char.lower()
        if previous_char:
            pair = previous_char + char_lower
            if pair in ELEMENTS:
                chars[i-1] = f'[{pair.title()}]'
                chars[i] = previous_char = ''
                continue
        if char_lower in ELEMENTS:
            chars[i] = f'[{char.upper()}]'
        previous_char = char_lower
    result = ''.join(chars)
    return result


def enrich_with_breaking_bad_style(text: str) -> str:
    words = text.split(' ')
    enriched_words = map(_enrich_word, words)
    enriched_text = ' '.join(enriched_words)
    return enriched_text


def breaking_bad_time():
    text_input = Element('text_input')
    text_output = Element('text_output')
    text = text_input.element.value
    text_modified = enrich_with_breaking_bad_style(text)
    text_output.write(text_modified)
