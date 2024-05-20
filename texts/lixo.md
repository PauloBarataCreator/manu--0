https://pypi.org/project/google-play-scraper/
# Get data from applications from Play Store. Can useless in the future;





             

            #  try: detect_list_ordens
            #  except NameError: 
            #     pass
            #  else: 
            #     list_text_equals_database.append(detect_list_ordens)


            #  try: detect_list_pronomes
            #  except NameError: 
            #     pass
            #  else: 
            #     list_text_equals_database.append(detect_list_pronomes)


            #  try: detect_list_adverbios
            #  except NameError: 
            #     pass
            #  else: 
            #     list_text_equals_database.append(detect_list_adverbios)


            #  try: detect_list_verbos
            #  except NameError: 
            #     pass
            #  else: 
            #     list_text_equals_database.append(detect_list_verbos)
             # detecta quais palavras de "text" são iguais ao banco de dados

             
             # mostra igual a list_text, só que sem os substantivos;





<!-- list_text = list(text)

for vf in list_text:
    if vf == ['olá']:
    list_text.remove('olá')
    list_text = ''.join(list_text)
    
    fiveSecs = [1, 2, 3, 4, 5]
    for fv in fiveSecs:
        time.sleep(1)
        print('counting')
        if fv == 5:
        print('Deu 5 segundos')
        print("É pesquisa!")
        answer = test_eight_components(s = list_text) -->
        
        
        
        
1 - Eu quero que se disser "olá" e nada mais além disso, durante 6 segundos, se disser alguma coisa a pesquise

2 - Se disser "olá" e durante 6 segundos não disser nada, o que disser após isso não será pesquisa


 now_second = core.SystemInfo.get_second()
                  if now_second + 3 or now_second + 6  :
                      print('Pesquisar 1')
                  else:
                      print('Pesquisar 2')
