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
