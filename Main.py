meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso, abreviación de la frase inglesa: 'Lot of laughs', significando: 'Muchas risas'",
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

while True:
    if word in meme_dict.keys():
        # ¿Qué debemos hacer si se encuentra la palabra?
        print(meme_dict[word])
        break
    else:
        # ¿Qué hacer si no se encuentra la palabra?
        print("Error: No exite la palabra. Intentar de nuevo.")
    
