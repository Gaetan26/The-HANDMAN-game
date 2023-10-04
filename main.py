# coding: utf-8
# check words
import random, json, os, click, time, threading

with open('words.json', 'rb') as register:
    WORDS = json.load(register)
    register.close()

global TIMES
global running
running = True
TIMES = 0

def update_time():
    global TIMES
    global running
    while running:
        time.sleep(1)
        TIMES += 1


def game():
    global TIMES
    global running
    STAR = random.choice(WORDS)
    STAR_ = list(STAR)
    FOUNDED = list()

    for i in range(0,len(STAR)):
        FOUNDED.append('_')

    click.secho('\nBienvenue sur Le Jeu du Pendu\n', fg='green')
    
    running = True
    while running:

        searched = str()        
        for index in range(0, len(FOUNDED)):
            x = FOUNDED[index]
            if index < len(FOUNDED)-1:
                if x != '_':
                    x = click.style(x,fg='green')
                else:
                    x = click.style(x,fg='red')
                searched += f'{x} '
            else:
                if x != '_':
                    x = click.style(x,fg='green')
                else:
                    x = click.style(x,fg='red')
                searched += f'{x}'
        

        if FOUNDED== STAR_:    
            running = False
            os.system('cls')
            click.secho(f"\nFelicitation! vous avez trouvez le mot : {searched.replace(' ','')}",fg='green')
            click.secho(f"Houlà vous avez mis {TIMES}s pour trouver\n", fg='yellow')
            break

        click.secho('mot recherché: '+searched)
        prop = input('essayer> ')

        if STAR_.count(prop) > 0 and STAR.count(prop) > 0:

            index = STAR.index(prop)

            if FOUNDED[index] != prop:
                FOUNDED[index] = prop
                STAR__ = str()
                for i in range(0, len(STAR)):
                    if i == index:
                        STAR__ += '*'
                    else:
                        STAR__ += STAR[i]
                STAR = STAR__
        os.system('cls')

thread_timer = threading.Thread(target=update_time)
thread_game = threading.Thread(target=game)

thread_game.start()
thread_timer.start()

# save game