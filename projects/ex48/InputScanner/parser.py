class ParsersError(Exception):
    pass


class Sentence(object):
    def __init__(self, subject, verb, sen_object):
        self.subject = subject[1]
        self.verb = verb[1]
        self.sen_object = sen_object[1]


def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None


def match(word_list, expected_word):
    if word_list:
        word = word_list.pop(0)

        if word[0] == expected_word:
            return word
        else:
            return None
    else:
        return None


def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)


def parse_verb(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParsersError("Expected a verb")


def parse_object(word_list):
    skip(word_list, 'stop')

    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParsersError("Word for Object should be noun or direction")


def parse_subject(word_list):
    skip(word_list, 'stop')

    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParsersError("Next word for Subject should be noun or verb")


def parse_sentence(word_list):
    subject = parse_subject(word_list)
    verb = parse_verb(word_list)
    sent_object = parse_object(word_list)

    return Sentence(subject, verb, sent_object)
