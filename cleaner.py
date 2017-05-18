# encoding=utf8
# /Users/vneck/Drive/Spring 2017/Ling 472/Final Project
import os, re, codecs, io

PATH = "corpora/test"
BANNED = ["Icon\r"]

def clean_dir(directory):
    return not(directory.startswith('.') \
    or "\r" in directory \
    or directory == 'clean')

if __name__ == "__main__":
    language_folders = os.listdir(PATH)
    language_folders = [folder for folder in language_folders if clean_dir(folder)]

    print language_folders

    for language in language_folders:
        folder_path = os.path.join(PATH, language)
        clean_file_path = os.path.join(PATH, "clean")
        clean_file = open(clean_file_path + "/%s.txt"%(language), "w+")

        language_text_files = [path for path in os.listdir(os.path.join(PATH, language)) if clean_dir(path)]

        for text_file in language_text_files:
            print "cleaning %s..." % text_file
            clean_text = open(os.path.join(folder_path, text_file)).read()
            clean_text = re.sub(r'(\s+|\.\.\.)', " ", clean_text)
            clean_text = re.sub(r'(_|-)*([A-Za-z]+)(_|-)*', r'\g<2>', clean_text)
            clean_text = re.sub(r' ([^A-Za-z.!?,]{2})+(.| )', " ", clean_text)
            clean_file.write(clean_text)
