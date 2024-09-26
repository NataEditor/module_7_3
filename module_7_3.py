import io

class WordsFinder:

    def __init__(self, file_names):
        self.file_names = file_names

    def get_all_words(self):
        punkt = [',', '.', '=', '!', '?', ';', ':', ' - ']
        Op_dict = {}
        lw=''
        with open(self.file_names, 'r+', encoding='utf-8') as file:
            for line in file:
                for char in line:
                    line = line.lower()
                    if char in punkt:
                        line = line.replace(char, '')
                    lw = lw + line
                    Op_dict.update({self.file_names: lw.split()})
        return Op_dict

    def find(self, word):
        find_in = {}
        for self.file_num in self.file_names:
            for key, value in self.get_all_words().items():
                word = word.upper()
                if word in [x.upper() for x in value]:
                    find_in[key] = (value.index(word.lower()) + 1)
            return find_in

    def count(self, word):
        count_in = {}
        for self.file_num in self.file_names:
            for key, value in self.get_all_words().items():
                word = word.upper()
                if word in [x.upper() for x in value]:
                    count_in[key] = value.count(word.lower())
            return count_in


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
