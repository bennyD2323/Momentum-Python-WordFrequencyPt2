STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
]
import string

class FileReader:
    def __init__(self, filename):
        self.filename = filename.open()
        


    def read_contents(self):
        """
        This should read all the contents of the file
        and return them as one string.
        """
        contents = self.filename.read()
        
        # print(contents)
        return contents
        


class WordList:
    def __init__(self, text):
        self.text = text

    def extract_words(self):
        """
        This should get all words from the text. This method
        is responsible for lowercasing all words and stripping
        them of punctuation.
        """
        words = self.text.lower().split()
        good_to_go = [word.strip(string.punctuation) for word in words]
        self.good_to_go = good_to_go
        
        
        

    def remove_stop_words(self):
        """
        Removes all stop words from our word list. Expected to
        be run after extract_words.
        """
        go_words = []
        for word in self.good_to_go:
           if not word in STOP_WORDS:
               go_words.append(word)
        self.go_words = go_words
        # print(self.go_words)


    def get_freqs(self):
        """
        Returns a data structure of word frequencies that
        FreqPrinter can handle. Expected to be run after
        extract_words and remove_stop_words. The data structure
        could be a dictionary or another type of object.
        """
        word_freq_list = dict()
        for word in self.go_words:
            if word in word_freq_list:
                word_freq_list[word] += 1
            else:
                word_freq_list[word] = 1
        
        self.sorted_freq_list = sorted(word_freq_list.items(), key = lambda seq: seq[1], reverse=True)
        # print(self.sorted_freq_list)
        return self.sorted_freq_list
        


class FreqPrinter:
    def __init__(self, freqs):
        self.freqs = freqs

    def print_freqs(self):
        """
        Prints out a frequency chart of the top 10 items
        in our frequencies data structure.

        Example:
          her | 33   *********************************
        which | 12   ************
          all | 12   ************
         they | 7    *******
        their | 7    *******
          she | 7    *******
         them | 6    ******
         such | 6    ******
       rights | 6    ******
        right | 6    ******
        """
        for key, value in self.freqs[:10]:
            print(key.rjust(20), " | ", value, value * ("*"))


if __name__ == "__main__":
    import argparse
    import sys
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        reader = FileReader(file)
        word_list = WordList(reader.read_contents())
        word_list.extract_words()
        word_list.remove_stop_words()
        printer = FreqPrinter(word_list.get_freqs())
        printer.print_freqs()
    else:
        print(f"{file} does not exist!")
        sys.exit(1)
