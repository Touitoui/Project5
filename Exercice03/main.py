words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]


def count_vowels(word):
    vowels = 'aeiouyAEIOUY'
    vowel_count = sum(1 for char in word if char in vowels)
    return (word, vowel_count)

def ex03(words_list):
    vowels_list = []
    for word in words_list:
        vowels_list.append(count_vowels(word))
    return vowels_list

if __name__ == '__main__':
    print(ex03(words))
