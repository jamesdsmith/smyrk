zwj = u'\U0000200D'
text = u'\U0000FE0E'
emoji = u'\U0000FE0F'

modifiers = {'🏿', '🏼', '🏽', '🏻', '🏾'}
combiners = {'⃣', '⃠'}
regional_indicators = {'🇦', '🇧', '🇨', '🇩', '🇪', '🇫', '🇬', '🇭', '🇮', '🇯', '🇰', '🇱', '🇲', '🇳', '🇴', '🇵', '🇶', '🇷', '🇸', '🇹', '🇺', '🇻', '🇼', '🇽', '🇾', '🇿'}
variations = {text, emoji}
zwjs = {zwj}

def all_chars(line):
    """Generator that properly iterates a string that contains emojis
    """
    def get_char_at(i):
        return line[i:i+1]

    while len(line) > 0:
        # Check for flag sequence
        if get_char_at(0) in regional_indicators:
            yield get_char_at(0) + get_char_at(1)
            line = line[2:]
        else:
            next_emoji = get_char_at(0)
            i = 1
            zwj_sequence = get_char_at(i) in zwjs
            while get_char_at(i) in modifiers | variations | combiners | zwjs or zwj_sequence:
                next_emoji += get_char_at(i)
                zwj_sequence = get_char_at(i) in zwjs
                i += 1
            yield next_emoji
            line = line[i:]

def is_digit(char):
    return char[:1] in '0123456789'