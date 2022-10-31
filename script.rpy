# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define nar = Character("Unknown Caller", color = "#aaaaaa")
define newsie = Character("Newsperson", color = "#ca5ccd")
define merchant = Character("Merchant", color = "#ece911")
define attacker = Character("Attacker", color = "#ff0000")
define guard = Character("Guard", color = "#ff0000")
define sailor = Character("Shorter ticketholder", color = "#0000ff")
define soldier = Character("Soldier", color = "#b34545ff")
define ju = Character("General Ju", color = "#bb1174")
define tian = Character("Captain Tian", color = "#bb1174")
define bataar = Character("General Bataar", color = "#208f20")
image s0p1 = "phonev2.png"
image s1x2 = im.Scale("boats.png", 1000, 1000)
image s2y1 = "noyellow.png"
image s2y2 = "littleyellow.png"
image s2y3 = "smallyellow.png"
image s2y4 = "mediumyellow.png"
image s2y5 = "bigyellow.png"
image s2y6 = "phoneyellow.png"
image blackbg = "#000"



# The game starts here.

label start:
    call vars

    scene blackbg
    show s0p1

    #"ring ring, ring ring"
    
    #pause 5
    #"Left-click to continue"

    menu:
        "Pick up":
            #call s0
            #call s1(True)
            call s2(True)
            
        "Don't Pick Up":
            pause 1

    "Congratulations! You have finished the game."

    return

label vars:
    $ year = 1066
    $ xp = 0
    $ hp = 10
    $ defense = 100
    $ sp = 0
    return

label s0:
    nar "Hello? Ah, yes, someone finally picked up the phone. That could only mean one thing!"
    nar "You are passionate about history and want to go on an epic adventure through the world of your anscestors to discover the past, don't you!"
    menu:
        "Yes":
            nar "Fantastic! Let's get right into it then"
        "No":
            nar "That is unfortunate."
            nar "Would you be more engaged if you were trying to get to the other side of the world to save your long lost sibling?"
            menu:
                "Sure":
                    nar "Fantastic! Let's get right into it then"
                "Meh":
                    nar "My, you are hard to please. How about we say you are on a quest to pass your history exam in the least boring way?"
                    menu:
                        "Okay":
                            nar "Fantastic! Let's get right into it then"
                        "Oh my gosh that's so perfect!":
                            nar "Fantastic! Let's get right into it then"
    nar "As you go through the world, you are going to get experience points (top left)"
    nar "Put your historian hat on, because the only way to make it through the world safely (without losing health) is to apply your historical knowledge."
    nar "So here's the low down. The year is..."
    menu:
        "I don't know":
            nar "That's ok. Just check the top bar of your screen for useful information"
        "2022":
            nar "It is no longer the present. You exist in the past! Check the top bar of your screen for useful information"
        "1066":
            nar "Yes, good job. I see you checked the top right part of your screen"
    nar "The place is"
    nar "Hang on, I'm getting a phone call; got to go. Guess you'll just have to apply your historical knowledge!"
    return

label s1(firsttime):
    scene blackbg
    $ year = 1273
    $ xp = 0
    $ hp = 10
    $ sp = 20
    if  firsttime == True:
        "You open your eyes to see a bustling market around you"
        "Everyone around you wears silk that shines in the warm afternoon sun"
        "As you come into focus, though, you notice that the people aren't behaving normally"
        "Those who are not trampling over each other to go into an alleyway to the East are hurridely trying to sell their wares"

    menu:
        "Join the crowd":
            call s1x2(True)
        "Listen for more information":
            newsie "XIANGYANG HAS FALLEN TO THE BARBARIANS!"
            newsie "They have come to steal our large population and sophisticated metalworking!"
            newsie "Your emperor is asking all men between the ages of 20 & 40 to join the army and defend your homes"
            newsie "This announcement was sponsored by Raid: Shodown Legend"
            menu:
                "Visit a merchant stall":
                    call s1x1(True)
                "Enter the stream of people":
                    call s1x2(True)
                "Go to the army camp":
                    call s1x3(True)
                "Talk to the newspaper person":
                    call s1x4(True)
    return
label s2(firsttime):
    scene blackbg
    show s2y1
    "It is a cool night, and you are standing on the deck of the boat with beautiful constilations twinkling above your head."
    guard "Looks like you're about done. I'll be off to bed, then"
    hide s2y1
    show s2y2
    "As they leave, a star begins to twinkle aggresively." 
    hide s2y2
    show s2y3
    hide s2y3
    show s2y4
    "It expands until it's the size of the moon"
    hide s2y4
    show s2y5
    "The light swirls and creates a vortex"
    hide s2y5
    show s2y6
    "Then, pop, a cellphone falls out"
    $ cellphone = False
    while cellphone == False:
        "You stretch out your hand to catch it and..."
        hide s2y6
        show s2y5
        if renpy.random.randint(1,4) != 1:
            "You catch it"
            $ cellphone = True
        else:
            "The cellphone crashes smashes into the floor and cracks"
            "The wind seems to sigh in disappointment"
            "Then, from the vortex, another cellphone drops"
    
    scene blackbg
    show s0p1
    "ring ring, ring ring"
    nar "It seems you know Song Dynasty China pretty well. Let's go over what you learned (or what you could have learned)"
    nar "1. -oh and you might want to write these down- The Song Dynasty was under attack by the Mongols in the 1200s"
    nar "2. By 1273, the Northern half of the empire was gone and in 1273 the battle of Xianyang occured"
    nar "3. Babarians are humans. The Mongols are humans."
    nar "4. The battle of Xianyang was the first recorded use of gunpowder in battle"
    nar "5. Related to that, China had made significant technological advancements by the time of the Mongols, such as the ship you're standing on"
    nar "6. Silk was abundant enough in Song Dynasty China for many people to wear it"
    nar "7. Song Dynasty China had a large population, and this was due to the introduction of Champa Rice"
    nar "8. Metalworking in China reached new heights during the Song Dynasty, allowing armor to be bought by even common soldiers"
    nar "I think that's about it."
    nar "Now where to go next..."
    nar "And more importantly, when?"
    menu:
        "Home!":
            nar "You are home, silly. Earth is the home of all humans."
            nar "You obviously don't know what you're talking about, so all choose for you."
        "You choose!":
            nar "Really, that's so sweet. I think I have a good idea."
    nar "But there's no way a medieval Chinese vessel could have made it there in the 1500s"
    nar "Eh, I'm sure some historian will make up a story based on flimsy evidence down the line"
    $ year = 1520
    return     

label s1x1(firsttime):
    merchant "Hello, excuse me for a second- I just have to pack this last thing up"
    pause 1
    if firsttime == True:
        merchant "Thanks for waiting. You came at the perfect time!"
        merchant "I- well I guess just me now-"
        merchant "I am having a barbarian apocalypse clearance sale. Everything is 50\% off!"
        merchant "How much money do you have?"
    menu:
        "20":
            pause 0.0001
        "None":
            merchant "Are you sure? Why don't you check the top bar of your screen?"
        "No idea":
            merchant "Well, why don't you check at the top bar of the screen?"
    merchant "Good, what would you like to buy?"
    menu:
        "The Analects of Confucious (a book) -- 5 paper monies":
            $ sp -= 5
            merchant "Thank you for visiting!"
        "A yard of silk -- 3 paper monies":
            $ sp -= 3
            merchant "Thank you for visiting!"
        "Year of the Water Rooster Calendar -- 2 paper monies":
            $ sp -= 2
            merchant "Thank you for visiting!"
        "Nothing, thank you":
            pause 0.00001
    call s1(False)
    return
label s1x2(firsttime):    
    "You enter into the flowing mass of people, whose collective body heat soaks into your skin"
    "The crowd pushes you and you find yourself pushing back, yet still you all move slowly, continuously Eastward"
    "After some time, you finally emerge onto a harbor packed with people of all ages"
    scene blackbg
    show s1x2
    "In front of you, there are two people waving one ticket each."
    "The taller one stands in front of a mighty vessel that gleams in the sun..."
    "the shorter in front of something that seems barely to be floating"
    "A twenty-something year-old pushes forward to the better looking ship"
    menu:
        "Race the twenty-something year-old to the good boat":
            "Just as the ticketholder is giving you your ticket, the person you were racing pulls your arm back."
            attacker "Please let me have this"
            menu:
                "Let them take the ticket":
                    "You watch as they take the prize"
                    attacker "Thank you, thank you so much. May fortune smile upon you."
                "Beat or be beaten":
                    "You are beaten..."
                    $ hp -= 1
                    "It\'s not even close"
        "Head for the worse looking boat":
            pause 0.001
    sailor "C'mon. The Green Opal\'s not as bad as she looks."
    sailor "We have a compass and a star chart. You'll be safe with us"
    return
label s1x3(firsttime):
    if firsttime == True:
        "You walk along a narrow, cobbled street for a few minutes before the grunts of soldiers and whistles of officers become clear."
        "As you walk, however, you notice more and more people heading in the opposite direction."
        "There's not much time to think about it, though. The street soon opens up into a large plaza filled with tents and temporary shelters"
        "A soldier approaches you"
    soldier "New Recruit, huh?"
    menu:
        "Yes":
            pause 0.0001
        "No":
            soldier "Sure"
    soldier "Go to the yellow tent in the center of camp"
    menu:
        "Turn back":
            call s1(False)
        "Continue":
            pause 0.001
    "As you approach the tent, a teenager comes out proudly donning a military uniform."
    soldier "You may enter"
    "The inside of the tent is decorated with portable but still comfortable furniture."
    "A older man is dressed in gleaming armour, chainmail covering the red tunic he wears beneath"
    ju "Greetings. You want to join the army, do you?"
    ju "Well, there's a lot you're going to have to learn. The most important thing to remember is why you are fighting."
    ju "When you look into the enemies' eyes and realize that they too are just human, remember what they have done to your emperor"
    ju "Think about the farms they've plundered, the cities they've sacked, the wives and children they have murdered"
    ju "Remember that they have EARNED every single stab you give them, every arrow that pierces their dispicable flesh"
    ju "Understand me, kid?"
    menu:
        "Say \"Yes SIR!\"":
            ju "Good"
        "Nod respectfully":
            ju "Good"
        "Back out":
            ju "Let 'em go. A coward is just another body for the Mongols to step over."
            call s1(False)
    ju "Now, on to more practical matters. You can join for free and get no armor, or you can fork over 20 silver pieces and get a helmet"
    menu:
        "Give 20 sp for a helmet":
            $ sp -= 20
            $ defense -= 20
        "A helmet's not going to do much anyway":
            pause 0.001
        "The less armor, the less to weigh me down":
            pause 0.001
    ju "Captain Tian, get this person their equipment and tattoo. They look strong enough for a crossbow, don't you think?"
    tian "But sir, my platoon already has 60 people"
    ju "And that will be reflected in your bonus"
    tian "Yes, SIR!"
    tian "Come with me private. Let's start the training montage"
    tian "Excellent training! Our platoon is needed to support a battle 50 miles North. Shall we have a marching montage?"
    menu:
        "Yes!":
            "(Insert Training Montage)"
        "Neh":
            pause 0.0001
    "You arrive at the battle site after a week through the hot summer air"
    tian "It appears the battle has already begun! Let us join our bretheren in the fight against evil."
    menu:
        "Hurrah!":
            pause 0.001
        "Hurr... ah?":
            if renpy.random.randint(1,10) < 4:
                tian "C'mon, let me hear you one more time"
                menu:
                    "Hurrah!":
                        pause 0.001
    tian "The battle is going well! Look, they are retreating. Hahaha"
    "General Tian leads you to the center, which is lagging behind the flanks"
    tian "You're going face some of the fiercest infantry, but at least it's not the infamous Mongolian Keshigs"
    attacker "AaaAAaaAH!"
    menu:
        "Dodge":
            if renpy.random.randint(1,10) <= 5:
                "You successfully avoided the attacker's curved sword, already dripping with blood"
                "As you do, you notice- with your adrenaline high supervision- an arrow sprout in the back of your attacker"
                "You look up and see that the keshigs have arrived"
                "It seems that missing is part of battle"
            else:                
                "You yank yourself away from the sword, only to tumble into one of your platoon members."
                "Unbalanced, they don't move fast enough to block a fatal blow by another of the enemy"
                "Or wait... the enemy looks so similar to the person they just killed"
                "They don't look foreign or montstorous, or even particularly mean"
                "As you begin to truly see them, however, an arrow sprouts in their back"
                "You look up and see that the keshigs have arrived"
                "It seems that missing is part of battle"
        "Block":
            "You raise up your shield and brace for impact"
            "Relief washes over you as the attacker's sword cuts a dent in the shield and not your skin"
            menu:
                "Make a retaliation attack":
                    if renpy.random.randint(1,100) <= 5*(100/defense):
                        "Just before you lower your shield, an arrow thuds in at the very top."
                        "Your momentum is thrown off, but you still manage to parry another swipe by your attacker"
                        "It all fades into the background, though, as the sight of the keshigs seems to send a chill through the whole platoon"
                    else:
                        "You stab the enemy in their stomach, but just as you do, you hear the unmistakeable whistle of an arrow"
                        $ hp -= 2
                        "It pierces you in the side and for a second your vision begins to swim"
                        "But then the world refocuses and you see what you had already figured- the keshigs have arrived"
                "Brace for the next blow":
                    "The attacker's sword is moments away from colliding with your shield when it gets deflected by a fast-moving arrow"
                    "You look up and see that the keshigs have arrived"
        "Make a \"tactical retreat\" (Run away)":
            if renpy.random.randint(1,10) <= 6*(100/defense):
                "You manage to get to the back of the lines before-"
                tian "What are you doing private! I thought you were hear to FIGHT!"
            else:
                $ hp -= 3
                "As you try to escape, an arrow pierces your side"
                "You look up and realize that the keshigs have arrived"
    tian "Tian's platoon- retreeeeeat!"
    "You and your platoon put to the test the formation you spent the most time practicing- the orderly retreat"
    "It's not enough, though."
    "The left flank, it seems, has already fallen and the Mongols soon encircle you"
    tian "Private, quick. Let us change clothes"
    menu:
        "Yes sir!":
            tian "Thank you, thank you"
            tian "Your service will be rewarded"
        "Excuse me?!":
            tian "Don't you see- they'll definetely kill me if they know I'm a captian"
            tian "Think about your country. A captain would be a greater loss than a private"
            menu: 
                "Okay":
                    tian "Thank you, thank you"
                    tian "Your service will be rewarded"
                "No way!":
                    tian "Very well, they captive takers are here already anyway"
        "What the... no way!":
            tian "Don't you see- they'll definetely kill me if they know I'm a captian"
            tian "Think about your country. A captain would be a greater loss than a private" 
            menu: 
                "Okay":
                    tian "Thank you, thank you"
                    tian "Your service will be rewarded"
                "No way!":
                    tian "Very well, they captive takers are here already anyway"
    bataar "You there, captain. And your assistant; Come with us"
    bataar "Congratulations, you have been selected to aid us in the seige of Hanoi"
    "The general moves hurridely along, and his guards prod you along with him"
    "After many months of hearing the sounds of battle while being held captive by the army, you finally recognize a familiar place:"
    "The place where you were first recruited"
    "The general comes and talks to you"
    bataar "Recognize this place. You are from Shanghai, no?"
    tian "Yes :("
    bataar "Well, you won't be here very long. You are to join some of your fellow inferiors on a ship"
    bataar "When you get where you get, do what you are told"
    "You and many others board a sad boat with many sad people and a few angry guards"

    return
label s1x4(firsttime):
    newsie "Hello, what would you like to hear about?"
    menu:
        "The war situation":
            newsie "Well, as you know they've been in control of the northern empire for many years now."
            newsie "But it was only a few months ago that they managed to raid into the Southern half."
            newsie "And just a few days ago, they managed to take over the strategic city of Xiangyang."
            newsie "The whole Yangtze basin is ripe for the picking!"
            newsie "I reckon we've got only a couple of weeks until the army comes here"
        "Where everyone is going":
            newsie "Everybody is fleeing to the port, of course!"
            newsie "You're not planning on staying are you?"
        "The barbarians":
            newsie "The barbarians come from the far North, beyond the borders of the Middle Kingdom."
            newsie "Their leader's name is Kublai Khan"
            newsie "Now, this isn't official or anything, but I heard they rip off the heads of defeated enemies and eat them"
            newsie "But one of my cousins was in the army and he said they were just human. So how bad could they be right?"
            pause 3
            newsie "... right?"
