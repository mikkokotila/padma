def initialize_dictionary():

    from .create_dictionary import create_dictionary
    dictionary = create_dictionary()
    return dictionary

def initialize_texts():

    from .create_texts import create_texts
    texts = create_texts()
    return texts

def initialize_tokens():

    from .create_tokens import create_tokens
    tokens = create_tokens()
    return tokens
