
def get_num_words(text):
    words = text.split()    
    return len(words)

def get_num_char(text):
    characters = text.lower()
    character_dict = {}
    for char in characters:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict


def sort_on(items):
    return items["num"]

def char_sort(counts):
    sorted_counts = []
    for ch, num in counts.items():
        sorted_counts.append({"char": ch, "num": num})
            
    sorted_counts.sort(key=sort_on, reverse=True)
    return sorted_counts

    


    
