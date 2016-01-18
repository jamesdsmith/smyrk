zwj = u'\U0000200D'
text = u'\U0000FE0E'
emoji = u'\U0000FE0F'

modifiers = {'🏿', '🏼', '🏽', '🏻', '🏾'}
combiners = {'⃣', '⃠'}
regional_indicators = {'🇦', '🇧', '🇨', '🇩', '🇪', '🇫', '🇬', '🇭', '🇮', '🇯', '🇰', '🇱', '🇲', '🇳', '🇴', '🇵', '🇶', '🇷', '🇸', '🇹', '🇺', '🇻', '🇼', '🇽', '🇾', '🇿'}
variations = {text, emoji}
zwjs = {zwj}

num_to_emoji = {0: '0️⃣', 1: '1️⃣', 2: '2️⃣', 3: '3️⃣', 4: '4️⃣', 5: '5️⃣', 6: '6️⃣', 7: '7️⃣', 8: '8️⃣', 9: '9️⃣'}
emoji_to_num = {v: k for k, v in num_to_emoji.items()}

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

def to_num(line):
    # Implicitly convert true/false to numbers for comparison
    if line == '' or line[0] == '👎':
        return 0
    elif line[0] == '👍':
        return 1
    else:
        num = 0
        for char in all_chars(line):
            num = num * 10 + emoji_to_num[char]
        return num

def to_emoji(num):
    line = ''
    while num > 0:
        num, line = num//10, num_to_emoji[num%10] + line
    return line

def bool_to_emoji(boolean):
    if boolean == True:
        return '👍'
    else:
        return '👎'

