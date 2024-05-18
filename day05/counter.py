
def number_of_words(text):
    return len(text.split())

def number_of_lines(text):
    return len(text.split("\n"))
    
def number_of_characters(text):
    text_just_char = text.replace(" ", "").replace("\n", "")
    return len(text_just_char)
        



    