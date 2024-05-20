Aplicativos para ajudar nas tarefas diárias

https://www.youtube.com/watch?v=7s27O0v26ME
https://www.youtube.com/watch?v=eQXwHigKCT0








- Método para fazer pesquisas utilizando o subprocess:
    
    1 - Capturar fala;
    2 - Enviar fala para o arquivo;
    3 - selenium_searches_google.py ser ativo pelo subprocess;
    4 - selenium_searches_google.py capturar texto do arquivo;
    5 - Automaticamente a pesquisa irá ser feita;
    6 - Após a captura para pesquisa, main_test.py irá apagar todo o conteúdo de texto do arquivo, apenas.
     
- Forma para capturar a current URL
    
    Basta adicionar a extensão:
     https://chrome.google.com/webstore/detail/add-url-to-window-title/ndiaggkadcioihmhghipjmgfeamgjeoi/related
     https://github.com/erichgoldman/add-url-to-window-title

     Ao habilitar essa extensão, a URL atual vai diretamente para o "title" da janela;
     Aí utilizando o pygetwindow consigo capturar essas URLs;
     Vai ser totalmente útil para o LinkedNotes, o qual guardará anotações que o usuário fará para determinada URL

     Vai ser útil para o gerenciador de senhas;

- Extensões interessantes para Chrome

    https://chrome.google.com/webstore/detail/the-great-grouper/pjkamnkpdfckpgjdlpebdnfgiecgfglj/related



Run a Python script
import os

os.chdir('D:')
os.chdir('D:\Paulos Projects\Personal-Projects\MANU(0.0)\APPs\SmartinWindow')
os.system("python main.py")



Abre um arquivo específico direto no VScode
import os

os.chdir('D:')
os.chdir('D:\Paulos Projects\Personal-Projects\MANU(0.0)\APPs\SmartinWindow')
os.system("main.py")


Abre o Explorador de arquivos em um caminho específico
Linha de comando:
"explorer C:\Apps"

Funciona mesmo tu tanto no C:
Linha de comando:
"explorer D:\Paulos Projects\Projetos-Manu\Teste-Projeto-Paint\teste-img"







- Fazer o subprocess em uma função em um mesmo arquivo;
https://docs.python.org/3/library/subprocess.html

- Usar Classe, assim como o Código Logo fez para chamar a função;

- Implemento : controlar o Google Cast com Python;
https://pypi.org/project/PyChromecast/
https://github.com/topics/chromecast?l=python


# abre calculadora
- >>> subprocess.Popen(r"C:\Windows\System32\calc.exe")


		PRIORIDADE NOW
1 - New way to make Google searches with Manu:

  Example:
 
  - "Interrogação Google";
  - "Rochedo de Gibraltar Google";
  - "Senhor dos Anéis o filme Google";
   
2 - Take pictures and prints and transforms to text archive:

  - O usuário tirará fotos ou prints e o programa transformará para texto;   
  - O programa perguntará e mostrará as pastas do dispositivo e o usuário poderá anexar seu/s arquivo/s;
  - E o programa mostra a opção de criar uma nova pasta;

3 - Acess and control OS:
  
  - pyControlOS;
  - os.walk() : permite ver pastas, subpastas e arquivos com Python.
    https://www.youtube.com/watch?v=cemxColh0NI

    Forma para implementar:
      Acessar pastas, se dentro de uma pasta ele não conseguir encontrar outra pasta, então ele vai mostrar os arquivos presentes.

  - os.listdir() : mostra todos os arquivos de um determinado diretório(pasta);
    https://www.youtube.com/watch?v=Db5GoOvyxow

    O "os.listdir()", mostra todos os arquivos e suas terminações, independente se estão dentro de pastas mostra todos os arquivos.


   
   
. - Future implementations:
  
  Psutil - Pode ser útil; Pesquisar mais sobre
  https://pypi.org/project/psutil/
  
  
  https://mixkit.co/free-sound-effects/robot/


	Para limpar o Cache CPU com Python:
	https://community.esri.com/t5/python-questions/clear-memory-cache-arcpy/td-p/745078
	https://gis.stackexchange.com/questions/19684/clearing-cache-memory-using-python


   Problema/bug "não chamada na conversa": 
   caso alguém fale, 'tudo encerrado'. Pode não estar se referindo à manu.
   o ideal seria ter o termo manu adicionando probabilidade ao reconhecimento, além de caixa de pergunta para confirmação da ordem.

**NEXT STEPS**
  Amanhã: 
  
  !! Terminar de ver curso os.listdir :  https://www.youtube.com/watch?v=Db5GoOvyxow !!
  
  Ter uma lista de dados apenas para identificadores de pesquisa.
  É mais fácil trabalhar com listas a strings;
  1- Refatorar todas as variáveis;
  2- Colocar partes do projeto(funções) em outros arquivos;
  3- Comentar onde precisa, para facilitar o entendimento;
  4- Colocar todas as variáveis no idioma Romeno;





1 - Título:
    
    Detectar com maior precisão o que está sendo dito.
    
Conteúdo:
    
    I - Ao ouvir um comando é repetitivo que de uma até todas as palavras identificadas sejam aproximações das palavras realmente ditas;
      
      Visto que, em por exemplo: 
             
             - "reiniciar tudo"
             - "iniciar tudo"
      
        Possuem pequenos detalhes os quais são os caracteres que os diferenciam;
        
        Entretanto, racionalmente falando, caso tudo já estaja iniciado, não é necessário inicializar de novo. Então o comando possui altíssima probabilidade de ser o comando mais semelhante à ele numericamente, que é "reinciar tudo";
        
        
   I - Implementação:     criar um programa, o qual análisa matemáticamente e enumera a semelhança entre o que foi captado e comandos preexistentes;
      
      - Comparando os caracteres de ambos;
      - A posição dos caracteres em comum;
      - (TALVEZ) Comparar o tempo de execução do reconhecimento, se for igual ou quase, aumenta a chance de ser o mesmo.
        Ex.: pode ser que o tempo o qual uso para dizer a frase, "reiniciar tudo", seja bem próximo da captação feita pelo reoconhecedor dessa mesma frase e da captação da frase, "iniciar tudo". Entretanto um pequeno desvio pode fazer ele reconhecer "iniciar tudo" ao invés de "reiniciar tudo";

     