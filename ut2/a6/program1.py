import sys

def count_words(sentence):
    summary = {}
    sentence_roster = sentence.split()
    for word in sentence_roster:
        summary[word] = 0
        for i in range(0, len(sentence_roster)):
            if word == sentence_roster[i]:
                summary[word] += 1
    return summary

if __name__ == '__main__':
    sentence = sys.argv[1]
    for word, count in count_words(sentence).items():
        print('{}: {}'.format(word, count))
