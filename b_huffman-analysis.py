# huffman-analysis.py
## author - nick s.
### get huffman.py working first, then work on this file

import matplotlib.pyplot as plt

# DATA - lyrics
POKEMON_LYRICS = 'I wanna be the very best. Like no one ever was. To catch them is my real test. To train them is my cause. I will travel across the land. Searching far and wide. Each Pokemon to understand. The power that\'s inside. (Pokemon, gotta catch \'em all.) Its you and me. I know it\'s my destiny. (Pokemon.) Oh, you\'re my best friend. In a world we must defend. (Pokemon, gotta catch \'em all.) A heart so true. Our courage will pull us through. You teach me and I\'ll teach you. Pokemon. (gotta catch \'em all.) Gotta catch \'em all. Yeah. Every challenge along the way. With courage I will face. I will battle every day. To claim my rightful place. Come with me, the time is right. There\'s no better team. Arm in arm we\'ll win the fight. It\'s always been our dream. (Pokemon, gotta catch \'em all.) Its you and me. I know it\'s my destiny (Pokemon.) Oh, you\'re my best friend. In a world we must defend. (Pokemon, gotta catch \'em all.) A heart so true. Our courage will pull us through. You teach me and I\'ll teach you. Pokemon (gotta catch \'em all.) Gotta catch \'em all. Gotta catch \'em all. Gotta catch \'em all. Gotta catch \'em all. Yeah! (Pokemon, gotta catch \'em all). Its you and me. I know it\'s my destiny. (Pokemon) Oh, you\'re my best friend. In a world we must defend. (Pokemon, gotta catch \'em all.) A heart so true. Our courage will pull us through. You teach me and I\'ll teach you Pokemon. (gotta catch \'em all). Gotta catch \'em all. (Pokemon)'
JIGGLE_JIGGLE = 'You have to have something that sticks. You have to have something that\'s monumental. When you walk out on stage, that\'s been monumental. (Jiggle, jiggle) Can you remember any of the rap that you did? My money don\'t jiggle, jiggle, it folds. I like to see you wiggle, wiggle, for sure. It makes me want to dribble, dribble, you know. Riding in my Fiat, you really have to see it. Six feet two in a compact, no slack. But luckily the seats go back. I got a knack to relax in my mind. Sipping some red, red wine. I sip booze from chalices, holding my palaces. Crib is so crampy suckers suffer from paralysis. Rhymes, I write them in the castle. You try to diss me and pretty soon your ass. Will squat in a cell \'cause I can tell you it\'s illegal. Treason, that\'s the reason I\'m regal. You do the time for the crime of lèse-majesté. And **** the police \'cause they can\'t arrest me. (They can\'t arrest me, they can\'t arrest me). (I like to see you wiggle, it makes me dribble, fancy a fiddle?). My money don\'t jiggle, jiggle, it folds. I like to see you wiggle, wiggle, for sure. It makes me want to dribble, dribble, you know. Riding in my Fiat, you really have to see it. Six feet two in a compact, no slack. But luckily the seats go back. I got a knack to relax in my mind. Sipping some red, red wine. (I like to see you wiggle, it makes me dribble, fancy a fiddle?). (I like to see you wiggle, it makes me dribble, fancy a fiddle?). (I like to see you wiggle, it makes me dribble, fancy a fiddle?). (I like to see you wiggle, it makes me dribble, fancy a fiddle?)'
ALPHABET = 'Now it\'s time for our wrap up. Let\'s give it everything we\'ve got. Ready, begin. Artificial amateurs aren\'t at all amazing. Analytically, I assault, animate things. Broken barriers bounded by the bomb beat. Buildings are broken, basically I\'m bombarding. Casually create catastrophes, casualties. Canceling cats got their canopies collapsing. Detonate a dime of dank daily doin\' dough. Demonstrations, Don Dada on the down low. Eatin\' other editors with each and every energetic. Epileptic episode, elevated etiquette. Furious fat fabulous fantastic. Flurries of funk felt feeding the fanatics. Imitators idolize, I intimidate. In a instant, I\'ll rise in a irate state. Juiced on my jams like jheri curls, jockin\' joints. Justly, it\'s just me, writin\' my journals. Kindly I\'m kindling all kinds of ink on. Karate kick type Brits in my kingdom. Let me live a long life, lyrically lessons is. Learned lame louses just lose to my livery. My mind makes marvelous moves, masses. Marvel and move, many mock what I\'ve mastered.  Niggas nap knowin\' I\'m nice naturally. Knack, never lack, make noise nationally.  Operation, opposition, off, not optional. Out of sight, out of mind, wide beaming opticals. Perfected poem, powerful punchlines. Pummeling petty powder puffs in my prime. Quite quaint quotes keep quiet it\'s Quannum Quarrelers ain\'t got a quarter of what we got, uh. Really raw raps, risin\' up rapidly. Riding the rushing radioactivity. Super scientifical sound search sought. Silencing super fire saps that are soft. Tales ten times talented, they\'re too tough. Take that, challengers, get a tune up. Universal, unique untouched. Unadulterated, the raw uncut. Verb vice Lord victorious valid. Violate vibes that are vain make \'em vanished. Why I\'m all well, would a wise wordsmith. Just weaving up words weeded up, on my work shift. Xerox, my X-ray-diation holes extra large. X-height letters and xylophone tones.'

# DATA - mantras
GREEN_LATTERN = 'In brightest day, in blackest night, No evil shall escape my sight. Let those who worship evil\'s might, Beware my power... Green Lantern\'s light!'
JEDI_CODE = 'Emotion, yet peace. Ignorance, yet knowledge. Passion, yet serenity. Chaos, yet harmony. Death, yet the Force.'
SITH_CODE = 'Peace is a lie. There is only Passion. Through Passion, I gain Strength. Through Strength, I gain Power. Through Power, I gain Victory. Through Victory my chains are Broken. The Force shall free me.'

# SONGS FOR MY REPORT
LIGHT_SWITCH = 'Yeah. Why you callin\' at 11:30. When you only wanna do me dirty? But I hit right back \'cause you got that, that, yeah. Why you always wanna act like lovers. But you never wanna be each other\'s? I say, \"Don\'t look back\" but I go right back and. All of a sudden, I\'m hypnotized. You\'re the one that I can\'t deny. Every time that I say I\'m gonna walk away. You turn me on like a light switch. When you\'re movin\' your body around and around. Now, I don\'t wanna fight this (no). You know how to just make me want. You turn me on like a light switch When you\'re movin\' your body around and around. You got me in a tight grip (yeah) You know how to just make me want you, baby. Do you love it when you keep me guessin\'? (Me guessin\') When you leave, and then you leave me stressin\' (me stressin\'). But I can\'t stay mad when you walk like that, no (uh). Why you always wanna act like lovers. But you never wanna be each other\'s? I say don\'t look back, but I go right back and all of a sudden, I\'m hypnotized (hypnotized). You\'re the one that I can\'t deny (can\'t deny). Every time that I say I\'m gonna walk away (yeah). You turn me on like a light switch. When you\'re movin\' your body around and around. Now, I don\'t wanna fight this (no). You know how to just make me want. You turn me on like a light switch (switch). When you\'re movin\' your body around and around. You got me in a tight grip (grip). You know how to just make me want you, baby. C\'mon, c\'mon, c\'mon, c\'mon. C\'mon and show me how you do (do). You want, you want, you want, you want. You wanna keep me wantin\' you (me wantin\' you, girl). C\'mon, c\'mon, c\'mon, c\'mon. C\'mon and show me how you do (you do). You want, you want, you want, you want. You wanna keep me wantin\' you. You turn me on like a light switch. When you\'re movin\' your body around and around. Now, I don\'t wanna fight this. You know how to just make me want you. You turn me on like a light switch. When you\'re movin\' your body around and around. You got me in a tight grip. You know how to just make me want you, baby. C\'mon, c\'mon, c\'mon, c\'mon. C\'mon and show me how you do (how you do). You want, you want, you want, you want. You wanna keep me wantin\' you (baby). C\'mon, c\'mon, c\'mon, c\'mon. C\'mon and show me how you do (how you do).You want, you want, you want, you want. You wanna keep me wantin\' you'
BIRTHDAY = 'I heard you\'re feeling nothing\'s going right. Why don\'t you let me stop by? The clock is ticking, running out of time. So we should party all night. So cover your eyes, I have a surprise. I hope you got a healthy appetite. If you wanna dance, if you want it all. You know that I\'m the girl that you should call. Boy, when you\'re with me. I\'ll give you a taste. Make it like your birthday everyday. I know you like it sweet. So you can have your cake. Give you something good to celebrate. So make a wish. I\'ll make it like your birthday everyday. I\'ll be your gift. Give you something good to celebrate. Pop your confetti, pop your Pérignon. So hot and heavy \'til dawn. I got you spinning like a disco ball. All night, they\'re playing your song. We\'re living the life, we\'re doing it right. You\'re never gonna be unsatisfied. If you wanna dance, if you want it all. You know I\'m the girl that you should call. Boy, when you\'re with me. I\'ll give you a taste. Make it like your birthday everyday. I know you like it sweet. So you can have your cake. Give you something good to celebrate. So make (so make) a wish (a wish). I\'ll make it like your birthday everyday. I\'ll be (I\'ll be) your gift (your gift). Give you something good to celebrate. Happy birthday. So let me get you in your birthday suit. It\'s time to bring out the big balloons. So let me get you in your birthday suit. It\'s time to bring out the big, big, big, big, big, big balloons. Boy, when you\'re with me. I\'ll give you a taste. Make it like your birthday everyday. I know you like it sweet. So you can have your cake. Give you something good to celebrate. Boy, when you\'re with me. I\'ll give you a taste. Make it like your birthday everyday. I know you like it sweet. So you can have your cake. Give you something good to celebrate. So make (so make) a wish (a wish). I\'ll make it like your birthday everyday. I\'ll be (I\'ll be) your gift (your gift). Give you something good to celebrate. Happy birthday'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
CUPS = 'I got my ticket for the long way \'round. Two bottle o\' whiskey for the way. And I sure would like some sweet company. And I\'m leavin\' tomorrow, what do you say? When I\'m gone. When I\'m gone. You\'re gonna miss me when I\'m gone. You\'re gonna miss me by my hair. You\'re gonna miss me everywhere, oh. You\'re gonna miss me when I\'m gone. When I\'m gone. When I\'m gone. You\'re gonna miss me when I\'m gone. You\'re gonna miss me by my walk. You\'re gonna miss me by my talk, oh. You\'re gonna miss me when I\'m gone. I got my ticket for the long way \'round. The one with the prettiest of views. It\'s got mountains, it\'s got rivers. It\'s got sights to give you shivers. But it sure would be prettier with you. When I\'m gone. When I\'m gone. You\'re gonna miss me when I\'m gone. You\'re gonna miss me by my walk. You\'re gonna miss me by my talk, oh. You\'re gonna miss me when I\'m gone. When I\'m gone. When I\'m gone. You\'re gonna miss me when I\'m gone. You\'re gonna miss me by my hair. You\'re gonna miss me everywhere. Oh, you\'re sure gonna miss me when I\'m gone. When I\'m gone. When I\'m gone. You\'re gonna miss me when I\'m gone. You\'re gonna miss me by my walk. You\'re gonna miss me by my talk, oh. You\'re gonna miss me when I\'m gone'

# MANTRAS FOR MY REPORT
FIRST = 'E+R=O, there is always an (E)vent and there will always be an (O)utcome but how you (R)espond determines what happens!'
SECOND = 'If opportunity doesn\'t knock, then build a new door.'
THIRD = 'Don\'t worry about failures, worry about the chances you miss when you don\'t even try.'

#global count
# the input, what we want to encode
def huffman(message:str) -> float:
    message = message.upper()

    # the output, should be all 0's and 1s
    result: str = str()

    # for counting the letter frequencies
    freq: dict = dict() # key  -> a letter
                        # item -> num of occurences

    # for holding the nodes of the huffman tree
    nodes: list = list() 

    # for storing the code for each letter
    coding: dict = dict()   # key  -> a letter
                            # item -> a binary encoding

# PART A CODE
    class Node:
        def __init__(self, letter, weight, left: any = None, right: any = None):
            # defining variables
            self.weight = weight
            self.letter = letter
            self.right = right
            self.left  = left
            return
    
    def retrieve_codes(v: Node, path: str=''):
        if len(v.letter) == 1:
            coding[v.letter] = path
        if v.left != None:
            retrieve_codes(v.left, path + '0')
        if v.right != None:
            retrieve_codes(v.right, path + '1')
    count = 0
    message = message.upper()
    for i in message:
        if i not in freq:
            count += 1
            freq[i] = 0
        freq[i] += 1

    nodes = list()
    for i in freq:
        nodes.append(Node(i, freq[i], None, None))

    while len(nodes) > 1:
        ## sort based on weight
        nodes.sort(key=lambda x: x.weight, reverse=True)

        ## get the first min
        min_a: Node = nodes.pop()

        ## get the second min
        min_b: Node = nodes.pop()
        
        ## combine the two
        combined: Node = Node(min_a.letter + min_b.letter, min_a.weight + min_b.weight, min_a, min_b) # TODO

        ## put the combined nodes back in the list of nodes
        nodes.append(combined)

    huff_root = nodes[0]
    retrieve_codes(huff_root)
    newmessage = ""
    for i in message: newmessage += coding[i]
    result: str = str(newmessage)
    # END OF PART A CODE
    
    n_original_bits: int = len(message) * 8
    n_encoded_bits: int = len(result)
    compression_ratio: float = 1 - (n_encoded_bits / n_original_bits)

    return result, coding, compression_ratio, count

# LYRICS
plt.subplot(2, 1, 1)
plt.suptitle('Lab 7 - Chang Analyzing Huffman')

MAX_N: int = int(128 * 3 / 2)
 
# PLOT 1
## POKEMON
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = LIGHT_SWITCH[0:i]
    _, _, ratio, count = huffman(sub_message)
    ratios.append(ratio)
x = plt.plot([i for i in range(191)], [i for i in ratios], color='red')
plt.setp(x, linestyle='dashdot')
print(count)

## JIGGLE JIGGLE
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = BIRTHDAY[0:i]
    _, _, ratio, count = huffman(sub_message)
    ratios.append(ratio)
print(count)
x = plt.plot([i for i in range(191)], [i for i in ratios], color='green')
plt.setp(x, linestyle='dashdot')

## ALPHABET
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = CUPS[0:i]
    _, _, ratio, count = huffman(sub_message)
    ratios.append(ratio)
x = plt.plot([i for i in range(191)], [i for i in ratios], color='blue')
plt.setp(x, linestyle='dashdot')
print(count)

plt.legend(["LIGHT SWITCH (n=29)", "BIRTHDAY (n=27)", "CUPS (n=27)"], loc="upper right")
values = []
for i in range(0, 9):
    values.append(i*25)
plt.xticks([i for i in values])

values = []
x = 0.4
for i in range(0, 4):
    values.append(x)
    x += 0.2
plt.yticks([i for i in values])

# PLOT 2
plt.subplot(2, 1, 2)

## SITH CODE
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = FIRST[0:i]
    _, _, ratio, count = huffman(sub_message)
    ratios.append(ratio)
x = plt.plot([i for i in range(191)], [i for i in ratios], color='red')
plt.setp(x, linestyle='dashdot')
print(count)

## GREEN LATERN'S OATH
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = SECOND[0:i]
    _, _, ratio, count = huffman(sub_message)
    ratios.append(ratio)
x = plt.plot([i for i in range(191)], [i for i in ratios], color='green')
plt.setp(x, linestyle='dashdot')
print(count)

## JEDI CODE
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = THIRD[0:i]
    _, _, ratio, count = huffman(sub_message)
    ratios.append(ratio)
x = plt.plot([i for i in range(191)], [i for i in ratios], color='blue')
plt.setp(x, linestyle='dashdot')
print(count)
values = []
for i in range(0, 9):
    values.append(i*25)
plt.xticks([i for i in values])

values = []
x = 0.4
for i in range(0, 4):
    values.append(x)
    x += 0.2
plt.yticks([i for i in values])

plt.legend(["FIRST (n=26)", "SECOND (n=23)", "THIRD (n=23)"], loc="upper right")

plt.gcf().supxlabel("length of message")
plt.gcf().supylabel("compression %")

plt.savefig("./figs/lab7_mydata_chang.png")
plt.show()