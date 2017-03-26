from graphasadjacency import Graph


def build_graph(word_file):
    d = {}
    g = Graph()

    wfile = open(word_file, 'r')

    for line in wfile:
        print line
        word = line[:-1]
        print word

        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i + 1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]

    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.add_edge(word1,word2)
    return g



