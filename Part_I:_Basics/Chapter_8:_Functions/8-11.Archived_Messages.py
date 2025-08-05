def send_messages(short_texts, messages):    
    """Function that prints each element of the first list and move it to the second"""
    texts_copy = short_texts[:]     #   make a copy of the first list

    while texts_copy:
        current_text = texts_copy.pop()     
        print('\n', current_text)
        sent_messages.append(current_text)      
    print(f"\nFirst list: {short_texts}")       # first list
    print(f"\nSecond list: {messages}")         # second list

# List of short texts.
short_texts = [     
    "Todo lo que has vivido y sigues viviendo es una mentira, engaño, oculto de ti la vida y la muerte.",
    "Destino del hombre es vivir en las convulsiones de la angustia o en el letargo del tedio",
    "El trabajo nos libra de tres insufribles calamidades: el aburrimiento, el vicio y la necesidad.",
    "Trabajemos, pues, sin argumentar -dijo Martín- que es el único medio de que sea la vida tolerable.",
        ]
sent_messages = []


if __name__ == '__main__':  # function call
    send_messages(short_texts, sent_messages)
