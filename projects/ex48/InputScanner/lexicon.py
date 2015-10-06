__author__ = 'Egor'


def scan(input_sentence):
    # scan function should take words and analise them. Based on it  should return corresponding sentence
    #  consisting fromlist of tuples

    directions = ["north", "south", "east", "west", "up", "down", "left", "right"]
    verbs = ["go", "kill", "eat", "gain", "stop"]
    stops = ["the", "in", "off", "from", "at", "it"]
    nouns = ["door", "bear", "princess", "cabinet"]

    words = input_sentence.split()
    sentence = []
    for i in words:
        j = i.lower()
        converted_number = convert_numbers(i)
        is_error = True
        if j in directions:
            direction = ('directions', j)
            sentence.append(direction)
            is_error = False

        elif j in verbs:
            verb = ('verb', j)
            sentence.append(verb)
            is_error = False

        elif j in stops:
            stop = ('stop', j)
            sentence.append(stop)
            is_error = False

        elif j in nouns:
            noun = ('noun', j)
            sentence.append(noun)
            is_error = False

        elif converted_number is not None:
            number = ('number', converted_number)
            sentence.append(number)
            is_error = False

        if is_error:
            error = ('error', j)
            sentence.append(error)

    return sentence


def convert_numbers(num):
    try:
        return int(num)
    except ValueError:
        return None


input_string = raw_input('>')
scan(input_string)
