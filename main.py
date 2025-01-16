def main():
    file = "books/frankenstein.txt"
    text = read_text(file) 
    words = num_words(text)
   
    num_of_char = num_times_char(text)
    #print(num_of_char)
    sorted = sort_dic(num_of_char)
    print(sorted)
    print(f"--- Begin report of {file} ---")
    print(f"There are {words} words in the document")
    print()
    for k in sorted:
    #    print(sorted[k])
        print(f"The {k["char"]} character was found {k["num"]} times")
    

def num_words(text):
    words = text.split()
    return len(words)

def read_text(text):
    with open(text) as f:
        file_content = f.read()
    return file_content

def num_times_char(text):
    dic = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }
    for char in text:
        lowchar = char.lower()
        if lowchar in dic:
            dic[lowchar] += 1
    return dic

def sort_on(dic):
    return dic["num"]

def sort_dic(dic):
    listdic = []
    for k in dic:
        listdic.append({"char": k, "num": dic[k]})
    listdic.sort(reverse=True, key=sort_on)
    return listdic

   
    

    
main()