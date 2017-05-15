<h3>Exemplos de uso</h3>

Busca todas que possuirem a palavra 'soldier':

<pre>
$ python3 vagalume-crawler.py -m soldier -b 'system of a down'

Buscando por System Of A Down...

Resultado: 
82) Soldier Side
83) Soldier Side - Intro
</pre>


Busca as 10 primeiras da lista de mais conhecidas:

<pre>
$ python3 vagalume-crawler.py -b 'black sabbath' -n 10

Buscando por Black Sabbath...

01) Iron Man
02) Paranoid
03) War Pigs
04) Changes
05) Black Sabbath
06) Heaven And Hell
07) N.I.B.
08) Children Of The Grave
09) God Is Dead?
10) Children Of The Sea
</pre>



Busca as 10 primeiras da lista de todas as musicas:

<pre>
$ python3 vagalume-crawler.py -b 'black sabbath' -tn 10 

Buscando por Black Sabbath...

01) A Hard Road
02) A National Acrobat
03) A National Acrobat (tablatura)
04) After All
05) After All (tablatura)
06) After Forever
07) After Forever (tablatura)
08) Age Of Reason
09) Air Dance
10) Air Dance (tablatura)
</pre>


Busca uma lista de bandas em um arquivo e pede para o usuario selecionar uma para ver as musicas:

<pre>
$ python3 vagalume-crawler.py -a ./src/resources/bandas.txt -n5

01) Black Sabbath
02) System Of A Down
03) Linkin Park
04) Evanescense
05) Metallica
06) U2
07) Led Zeppelin
08) Pink Floyd
09) Guns N Roses
10) Korn
11) Titãs
12) Kiss
13) Aerosmith
14) Legião Urbana

  Número da banda a pesquisar: 10

Buscando por Korn...

01) Freak On A Leash
02) Blind
03) Falling Away From Me
04) A Different World (Feat. Corey Taylor)
05) Word Up
</pre>

Se chamado sem passar a opção -b ou a -a, pede para o usuário inserir o nome da banda, se não fornecido -n, mostra as 15 primeiras musicas:

<pre>
$ python3 vagalume-crawler.py
 Buscar: 'linkin park'   

Buscando por 'Linkin Park'...

01) Numb
02) In The End
03) Heavy (feat. Kiiara)
04) Heavy (Feat. Waxx)
05) Leave Out All The Rest
06) Castle Of Glass
07) Battle Symphony
08) What I've Done
09) Crawling
10) Faint
11) Burn It Down
12) Somewhere I Belong
13) Breaking The Habit
14) From The Inside
15) New Divide
</pre>

Mostra a tela de ajuda:

<pre>
python3 vagalume-crawler.py -h
</pre>

Mostra a versão do programa:

<pre>
python3 vagalume-crawler.py -v
</pre>





