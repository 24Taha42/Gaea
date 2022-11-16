# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define nar = Character("Unknown Caller", color = "#aaaaaa")
define newsie = Character("Newsperson", color = "#ca5ccd")
define merchant = Character("Merchant", color = "#ece911")
define merch2 = Character("Other merchant", color = "#0ce911")
define merch3 = Character("Other other merchant", color = "#ec0911")
define merch4 = Character("Other other other merchant", color = "#ece900")
define attacker = Character("Attacker", color = "#ff0000")
define guard = Character("Guard", color = "#ff0000")
define sailor = Character("Shorter ticketholder", color = "#0000ff")
define soldier = Character("Soldier", color = "#b34545ff")
define ju = Character("General Ju", color = "#bb1174")
define tian = Character("Captain Tian", color = "#bb1174")
define bataar = Character("General Bataar", color = "#208f20")
define trivier = Character("Ferdinand", color = "#ffffff")
define ach = Character("Achiyaku", color = "#dd0f35")
define sailwa = Character("Ticket Officer", color = "#3d06f2")
define isabella = Character("Isabella", color = "ffaaaa")
define rando = Character("Random Person", color = "#dc4fda")
define rando2 = Character("Other Random Person", color = "#0c4fda")
define abd = Character("Abdullah", color = "#ad4592")
define brb = Character("Corsair", color = "#cccccc")
define aminah = Character("Amina", color = "#f36a7f")
image s0p1 = "phonev2.png"
image s1x2 = im.Scale("boats.png", 1000, 1000)
image s2y1 = "noyellow.png"
image s2y2 = "littleyellow.png"
image s2y3 = "smallyellow.png"
image s2y4 = "mediumyellow.png"
image s2y5 = "bigyellow.png"
image s2y6 = "phoneyellow.png"
image s2p1 = im.Scale("shipwrecked.png", 960, 960)
image s2p2 = im.Scale("landho.png", 768, 960)
image blackbg = "#000"


# The game starts here.

label start:
    call vars

    scene blackbg
    show s0p1
    with fade

    "ring ring, ring ring"
    
    pause 5
    "Left-click to continue"

    menu:
        "Pick up":
            #call s0
            #call s1(True)
            #call s2(True)
            $ sp = 10
            call s3x1(True)
            scene blackbg
            show s0p1
            nar "Congratulations! You have finished the game with [xp] expierence points."
            nar "Submit feedback at tinyurl.com/whagfeedback"
        "Don't Pick Up":
            pause 1
    return

label vars:
    $ year = 1066
    $ xp = 0
    $ hp = 10
    $ defense = 100
    $ sp = 0
    $ itemsval = 0
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
    with dissolve
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
            $ xp += 1
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
    if firsttime == True:
        scene blackbg
        show s2y1
        with fade
        "It is a cool night, and you are standing on the deck of the boat with beautiful constilations twinkling above your head."
        guard "Looks like you're about done. I'll be off to bed, then."
        hide s2y1
        show s2y2
        "As they leave, a star begins to twinkle aggresively." 
        hide s2y2
        show s2y3
        hide s2y3
        show s2y4
        "It expands until it's the size of the moon."
        hide s2y4
        show s2y5
        "The light swirls and creates a vortex."
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
                "The cellphone crashes smashes into the floor and cracks."
                "The wind seems to sigh in disappointment."
                hide s2y6
                show s2y5
                with fade
                "Then, from the vortex, another cellphone drops."
        
        scene blackbg
        show s0p1
        "ring ring, ring ring"
        nar "It seems you know Song Dynasty China pretty well. Let's go over what you learned (or what you could have learned)."
        nar "1. -oh and you might want to write these down- The Song Dynasty was under attack by the Mongols in the 1200s."
        nar "2. By 1273, the Northern half of the empire was gone and in 1273 the battle of Xianyang occured."
        nar "3. Babarians are humans. The Mongols are humans."
        nar "4. The battle of Xianyang was the first recorded use of gunpowder in battle."
        nar "5. Related to that, China had made significant technological advancements by the time of the Mongols, such as the ship you're standing on."
        nar "6. Silk was abundant enough in Song Dynasty China for many people to wear it."
        nar "7. Song Dynasty China had a large population, and this was due to the introduction of Champa Rice"
        nar "8. Metalworking in China reached new heights during the Song Dynasty, allowing armor to be bought by even common soldiers."
        $ xp += 2
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
        
        $ year = 1545
        scene blackbg
        with dissolve
        "You wake up in a thick morning fog, with just the company of Song Dynasty Captian Tian in a small lifeboat."
        tian "Ah, yes, you're awake."
        menu:
            "What happened?!":
                pause 0.0001
            "What the ---- happened?!":
                pause 0.0001
            "Not you again...":
                tian "Well, thank you very much."
                tian "I don't really want to be here either, if that makes you feel any better."
                tian "But, well..."
        "He points behind you."
        scene blackbg
        show s2p1
        "You see your ship, the mighty Green Opal, sinking into the sea."
        hide s2p1
        show s2p2
        with dissolve
        "As you look past Tian, though, you see land and a hint of civilization in the background."
        "You pull up to the small, newly built port after a hard 20 minutes of rowing."
        $ xp += 1
        "As you get out of your boat, you realize that you are standing in the town square, along with a handful of other people and llamas."
        tian "I'm going to see if I can talk to the captain of that boat over there."
        tian "I don't think we'll have much luck in this tiny town."
    menu:
        "Deal with the merchant":
            call s2x1(True, False)
        "Attempt a trivia test to turn your fortunes around":
            call s2x2(True, False)
        "Go with Captain Tian":
            call s2x3(True)
        "Talk to the person waving a \"looking to hire\" sign":
            call s2x4(True)
    return     
label s3(firsttime):
    trivier "This ship will take you to Valencia in the mother country!"
    trivier "Give these letters of recommendation to the priest of the Catedral de Valencia"
    trivier "Oh, and take this, but don't open it until you get to the Atlantic."
    menu:
        "Open it now":
            trivier "Hey!"
            "Ferdinand slaps your hand away"
            trivier "What are you doing?"
            trivier "I just told you {i}not{/i} to open it."
            menu: 
                "Wait until they are out of sight":
                    "As soon as Ferdinand leaves you open the box"
                "Follow their instructions":
                    "You board the caravel with your letters of recommendation along with a handful of others"
                    "For weeks, you travel into increasingly cold and choppy seas as you make your way South"
                    "Then one day, the captain announces you have reached the Atlantic"
                    "You open the box"
        "Wait until they are out of sight":
            "As soon as Ferdinand leaves you open the box"
        "Follow their instructions":
            "You board the caravel with your letters of recommendation along with a handful of others"
            "For weeks, you travel into increasingly cold and choppy seas as you make your way South"
            "Then one day, the captain announces you have reached the Atlantic"
            "you open the box"
    "and see"
    scene blackbg
    show s0p1
    "a phone."
    "The phone starts ringing."
    nar "Good day!"
    nar "I'm glad to see you made it through another chapter of your epic adventure!"
    nar "Would you like me to summarize what you (may have) learned?"
    menu:
        "Yes":
            nar "Yay!"
            nar "1. The Incan Empire was conquered in the early 16th century"
            nar "2. Lima was a small city in the 16th century"
            nar "3. Gold, Potatoes, and textiles were large industries in Peru"
            nar "4. Terrace farms were common in Peru"
            nar "5. Potatoes and quinoa were two of the principle crops of the region"
            nar "6. Llamas and Alpacas were also key to Peruvian agriculture"
            nar "7. Although they could be ridden and used to carry things, travelling on foot was the most commmon choice"
            nar "8. Smallpox ravaged the Americas"
            nar "9. King Charles V was ruler of the Holy Roman Empire & Spain during the early/ mid 1500s"
            $ xp += 1
        "No":
            nar "Okay"
    nar "Now, where next?"
    nar "I do like the idea of Europe, but you've already been immersed in Spanish culture."
    nar "Ah! I have the perfect idea."
    scene blackbg
    with fade
    $ year = 1660
    "You and many others around you are kneeling on the deck of the caravel, although it looks older now."
    "The air is much warmer and the sea is much calmer than before."
    "You realize everybody is praying."
    "One by one, they begin to stand."
    "As they stand you notice several blips on the horizon."
    "A fleet of ships sails into view, headed to you at full speed."
    "As the people around you look up, the mass descends into chaos."
    rando "It's the corsairs!"
    rando "We're all going to die!"
    "In a matter of minutes, the enemy encircles you and begin boarding"
    abd "Listen up here!"
    abd "We are siezing this ship."
    abd "Comply or die."
    abd "Now, we need 1/2 of the people to volunteer to join us."
    abd "Who will it be?"
    abd "..."
    abd "Or would you like us to decide?"
    menu:
        "Volunteer":
            abd "Very good?"
            abd "Who else?"
            "Several people volunteer and the pirates are satisfied."
            call s3x4(True)
        "Don't volunteer":
            abd "Guess we'll decide."
            "A pirate comes up to you and sizes you up."
            if renpy.random.randint(1,10) == 1:
                brb "This person seems like they'd be a good fit!"
                "The corsair takes you by the wrist to Abdullah."
                menu: 
                    "Resist":
                        $ hp -= 1
                        "The corsair quickly overpowers you."
                        brb "Resistance is futile."
                    "Go along with it":
                        pause 0.001
                "Through a mix of volunteering and force, Abdullah gets his required number of recruits."
                call s3x4(True)
            else:
                brb "Too weak"
                menu:
                    "Dispute the insult":
                        brb "Okay, so you're cool with coming, then."
                        abd "Great!"
                        call s3x4(True)
                    "Accept the insult":
                        "Through a mix of volunteering and force, Abdullah gets his required number of recruits."
    "Now manned by the corsairs, your ship is taken East for a couple of weeks."
    "On a sunny morning, Abdullah calls the remaining passangers to the deck."
    abd "We are almost to the jewel of the Mediterranian, Constantinople."
    abd "There, you will be set free..."
    abd "Once we have everything you own."
    abd "Any objections?"
    menu:
        "Object":
            pause 0.001
        "Don't object":
            pause 0.001
    abd "Since there are no objections, I think we can move on."
    "In just a couple of hours, the minarets of mosques jutting out into the sea become clear"
    "Hundreds of buildings envelop the straight ahead of you and ships swarm the coast"
    "Yours pulls into the harbor in a horn-shaped inlet."
    abd "Nice meeting you all."
    abd "Time to go!"
    menu:
        "Leave behind everything you have":
            $ sp = 0
            $ itemsval = 0
            $ defense = 100
            "As you leave, a corsair pats you down"
            brb "Nothing?"
            brb "That's a shame."
            brb "Next!"
        "Try to slip through the cracks":
            "How much money do you take?"
            menu:
                "All of it":
                    pause 0.001
                "Half of it":
                    $ sp = sp/2
                "A tenth of it":
                    $ sp = sp/10
            $ defense -= sp/2
            if renpy.random.randint(1,50) > (defense/2)-itemsval:
                "A guard catches you just as you get onto solid ground."
                "You lose everything."
                $ sp = 0
                $ itemsval = 0
                $ defense = 100
            else:
                "You make it by successfully."
                $ defense += itemsval
    "The cobbled streets of the biggest city in the world lie ahead of you."
    "Which direction do you go?"
    menu:
        "Southwest, to the Grand Bazaar":
            call s1x1(True, False)
        "Southeast, to the biggest mosques":
            call s3x3(True, False)
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
            $ xp += 3
            $ itemsval += 2
            $ defense += 8
            merchant "Thank you for visiting!"
        "A yard of silk -- 3 paper monies":
            $ sp -= 3
            $ itemsval += 2
            $ xp += 1
            merchant "Thank you for visiting!"
        "Year of the Water Rooster Calendar -- 2 paper monies":
            $ sp -= 2
            $ itemsval += 1
            $ xp += 1
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
                    $ hp -= 1
                    $ xp += 1
                    "You are beaten"
                    "..."
                    if renpy.random.randint(1,10) >= 6*(defense/100):
                        $ hp -= 1
                        "It\'s not even close"
        "Head for the worse looking boat":
            pause 0.001
    sailor "C'mon. The Green Opal\'s not as bad as she looks."
    $ xp += 1
    sailor "We have a compass {i}and{/i} a star chart."
    sailor "You'll be safe with us"
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
    $ xp += 1
    ju "Now, on to more practical matters. You can join for free and get no armor, or you can fork over 20 paper monies and get a helmet"
    menu:
        "Give 20 sp for a helmet":
            $ sp -= 20
            $ defense += 20
        "A helmet's not going to do much anyway":
            pause 0.001
        "The less armor, the less to weigh me down":
            pause 0.001
    ju "Captain Tian, get this person their equipment and tattoo. They look strong enough for a crossbow, don't you think?"
    tian "But sir, my platoon already has 60 people"
    ju "And that will be reflected in your bonus"
    tian "Yes, SIR!"
    tian "Come with me private. Let's start the training montage"
    $ xp += 1
    "(Insert Training Montage)"
    tian "Excellent training! Our platoon is needed to support a battle 50 miles North. Shall we have a marching montage?"
    menu:
        "Yes!":
            $ xp += 1
            "(Insert Marching Montage)"
        "Neh":
            pause 0.0001
    "You arrive at the battle site after a week through the hot summer air"
    tian "The battle is going well! Look, they are retreating. Hahaha"
    tian "Let us join our bretheren in the fight against evil."
    menu:
        "Hurrah!":
            pause 0.001
        "Hurr... ah?":
            if renpy.random.randint(1,10) < 4:
                tian "C'mon, let me hear you one more time"
                menu:
                    "Hurrah!":
                        pause 0.001
    "General Tian leads you to the center, which is lagging behind the flanks"
    tian "You're going face some of the fiercest infantry, but at least it's not the Mongolian Keshigs"
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
                    if renpy.random.randint(1,100) <= 5*(defense/100):
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
            if renpy.random.randint(1,10) <= 6*(defense/100):
                "You manage to get to the back of the lines before-"
                tian "What are you doing private! I thought you were hear to FIGHT!"
            else:
                $ hp -= 3
                "As you try to escape, an arrow pierces your side"
                "You look up and realize that the keshigs have arrived"
    $ xp += 2
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
            tian "Don't you see- they'll probably kill me if they know I'm a captian"
            tian "Think about your country. A captain would be a greater loss than a private"
            menu: 
                "Okay":
                    tian "Thank you, thank you"
                    tian "Your service will be rewarded"
                "No way!":
                    tian "Very well, they captive takers are here already anyway"
        "What the... no way!":
            tian "Don't you see- they'll probably kill me if they know I'm a captian"
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
    $ xp += 1
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
            $ xp += 1
            newsie "Well, as you know they've been in control of the northern empire for many years now."
            newsie "But it was only a few months ago that they managed to raid into the Southern half."
            newsie "And just a few days ago, they managed to take over the strategic city of Xiangyang."
            newsie "The whole Yangtze basin is ripe for the picking!"
            newsie "I reckon we've got only a couple of weeks until the army comes here"
        "Where everyone is going":
            newsie "Everybody is fleeing to the port, of course!"
            newsie "You're not planning on staying are you?"
        "The barbarians":
            $ xp += 1
            newsie "The barbarians come from the far North, beyond the borders of the Middle Kingdom."
            newsie "Their leader's name is Kublai Khan"
            newsie "Now, this isn't official or anything, but I heard they rip off the heads of defeated enemies and eat them"
            newsie "But one of my cousins was in the army and she said they were just human. So how bad could they be right?"
            newsie "..."
            newsie "right?"
    call s1(False)
    return

label s2x1(firsttime, lasttime):
    scene blackbg
    merchant "Hello there."
    merchant "What would you like to purchase?"
    menu:
        "Bag of Potatoes (2 silver monies)":
            $ sp -= 2
            $ itemsval += 1
            $ xp += 1
            merchant "Thank you for visiting!"
        "Warm, hand-knit gloves (1 silver monies)":
            $ sp -= 1
            $ itemsval += 1
            $ xp += 1
            $ defense += 4
            merchant "Thank you for visiting!"
        "Gold Bar (15 silver monies)":
            $ sp -= 15
            $ xp += 7
            $ itemsval += 5
            $ defense -= 6
            merchant "Thank you for visiting!"
        "Nothing, thank you":
            pause 0.001
    if lasttime == True:
        menu:
            "Deal with the merchant":
                call s2x1(False, True)
            "Take a trivia test to get an all-expense paid vacation":
                call s2x2(False, True)
    elif lasttime == False:
        call s2(False)
    return
label s2x2(firsttime, lasttime):
    scene blackbg
    if firsttime == True:
        trivier "Hello, welcome to Ferdinand's trivia game!"
        trivier "You will have questions about the world in the 15th & 16th centuries."
        trivier "Answer them, and you'll get a cash prize along with a free trip to meet our king-"
        trivier "Charles, by the grace of God, Holy Roman Emperor, forever August, King of Germany, King of Italy, King of all Spains, of Castile, Aragon, León, Navarra,"
        trivier "Grenada, Toledo, Valencia, Galicia, Majorca, Sevilla, Cordova, Murcia, Jaén, Algarves, Algeciras, Gibraltar, the Canary Islands,"
        trivier "King of Two Sicilies, of Sardinia, Corsica, King of Jerusalem, King of the Western and Eastern Indies, Lord of the Islands and Main Ocean Sea, Archduke of Austria"
        trivier "Duke of Burgundy, Brabant, Lorraine, Styria, Carinthia, Carniola, Limburg, Luxembourg, Gelderland, Neopatria, Württemberg," 
        trivier "Landgrave of Alsace, Prince of Swabia, Asturia and Catalonia, Count of Flanders, Habsburg, Tyrol, Gorizia, Barcelona, Artois, Burgundy Palatine, Hainaut," 
        trivier "Holland, Seeland, Ferrette, Kyburg, Namur, Roussillon, Cerdagne, Zutphen, Margrave of the Holy Roman Empire, Burgau, Oristano and Gociano, Lord of Frisia, the Wendish March, Pordenone, Biscay, Molin, Salins, Tripoli,"
        $ xp += 1
        trivier "and Mechelen."
        trivier "Ready?"
        menu:
            "Yes!":
                pause 0.001
            "Sure...":
                pause 0.001
            "Nope":
                if lasttime == True:
                    menu:
                        "Deal with the merchant":
                            call s2x1(False, True)
                        "Take a trivia test to get an all-expense paid vacation":
                            call s2x2(True)
                elif lasttime == False:
                    call s2(False)
                elif lasttime == 3:
                    trivier "I'll wait"
                    menu:
                        "Play the game":
                            pause 0.001
                        "Make him (and yourself) wait":
                            pause 5
    $ score = 0
    trivier "Question number one:"
    trivier "Which of these people is a leader of the Protestant Reformation?"
    menu:
        "John of Arc":
            $ score += 0.5
            trivier "Sorry, the answer we were looking for was Martin Luther."
        "Martin Luther":
            $ score += 1
            trivier "Nice!"
        "Martin Luther King Jr.":
            trivier "Sorry, the answer we were looking for was Martin Luther."
        "James of St. George":
            trivier "Sorry, the answer we were looking for was Martin Luther."
    trivier "Next Question:"
    trivier "Why are the Europeans invading the Americas?"
    menu:
        "They want a new vacation place":
            trivier "I think they're good with their pristine Mediterranian beaches."
            $ score += 0.5
        "They want all the tasty maize":
            $ score += 0.5
            trivier "I guess that's a possibility, but the answer we were looking for was they want silver"
        "They want gold and silver":
            trivier "Correct!"
            $ score += 1
        "They're seeking a better understanding of our world":
            trivier "Ha, I wish."
            trivier "But I don't think that conquering is what you would do if you want to understand a place better"
            $ score += 0.5
    trivier "Which of these isn't native to the Incan Empire?"
    menu:
        "Llamas":
            trivier "Sorry, the answer we were looking for was Yams"
        "Quinoa":
            $ score += 0.5
            trivier "Sorry, the answer we were looking for was Yams"
        "Potatoes":
            trivier "Sorry, the answer we were looking for was Yams"
        "Yams":
            trivier "Correct!"
            $ score += 1
    "What is the capital of the Aztec Empire?"
    menu:
        "Tenochticlan":
            trivier "Yup!"
            $ score += 1
        "Teotehicuan":
            trivier "Close, but it was actually Tenochticlan"
            $ score += 0.5
        "Tikal":
            trivier "Sorry, that was actually a Mayan city"
        "Calakmul":
            trivier "Sorry, that was actually a Mayan city"
    trivier "What labor system do the Incans use?"
    menu:
        "Chattel Slavery":
            trivier "No, sorry. The Incans use the Mita System to build their epic infrastructure."
            $ score += 0.5
        "Mita":
            trivier "Yes!"
            $ score += 1
        "Indentured Servitude":
            trivier "That's more of a European thing"
            $ score += 0.5
        "Serfdom":
            trivier "That's more of a European and Chinese thing"
    trivier "Which European explorer sailed around Africa to India?"
    menu:
        "Christopher Columbus":
            trivier "Christopher Columbus sailed to the Americas."
            trivier "The answer we were looking for was either Vasco da Gama or Prince Henry."
        "Hernan Cortes":
            trivier "Hernan Cortes just sailed to the Americas and murdered a bunch of people."
            trivier "The answer we were looking for was either Vasco da Gama or Prince Henry."
        "Vasco da Gama":
            $ score += 1
            trivier "Correct!"
            trivier "Both da Gama and Henry sailed around Africa to India."
        "Prince Henry the Navigator":
            $ score += 1
            trivier "Correct!"
            trivier "Both da Gama and Henry sailed around Africa to India."
    trivier "Which of these is the main export of the Viceroyalty of Peru?"
    menu:
        "Coffee":
            $ score += 0.5
            trivier "Although Peruvian coffee is very good, it wasn't colonial Peru's largest export"
        "Salt":
            trivier "There aren't that many salt deposits in the viceroyalty of Peru"
            trivier "The answer we were looking for was Silver"
            trivier "It's all about the silver"
        "Ivory":
            trivier "There aren't that many elephants in the viceroyalty of Peru"
            trivier "The answer we were looking for was Silver"
            trivier "It's all about the silver"
        "Silver":
            trivier "Good Job!"
            $ score += 1
    trivier "Which of these regions did Zheng He {i}not{/i} visit?"
    menu:
        "East Africa":
            trivier "Zheng He did visit East Africa and he got some lovely gold"
            trivier "The answer we were looking for was West Africa"
        "West Africa":
            trivier "Nice!"
            $ score += 1
        "Indonesia":
            trivier "Zheng He did visit Indonesia and he got some lovely spices"
            trivier "The answer we were looking for was West Africa"
        "South Asia":
            trivier "Zheng He did visit South Asia and he got some lovely cotton"
            trivier "The answer we were looking for was West Africa"
    trivier "Congratulations, you have finished my trivia test!"
    $ xp += 7-score
    $ score *= 2
    $ sp += score
    
    trivier "You get a cash prize of [score] silver monies and the afformentioned trip to the court of the Holy Roman Emperor!"
    

    if lasttime == 3:
        call s2x4(False)
        trivier "Oh look!"
        trivier "What a coincidence."
        trivier "The ship to take you to Seville has arrived!"
        "Behind you, gliding over the waves, is a magnificent ship flying the family colors of the Hapsburgs"
    else:
        call s3(True)

    return
label s2x3(firsttime):
    scene blackbg
    ach "Hello, are you in need of some cash?"
    menu:
        "Yes!":
            pause 0.001
        "Nah":
            ach "Well do you want to explore the Andes?"
            menu:
                "Yeah!":
                    pause 0.001
                "Nah":
                    ach "Okay, then"
                    ach "Bye!"
                    call s2(False)
    ach "Well, we have the perfect job for you!"
    ach "My partner and I recently lost our assistant to smallpox"
    ach "Will you help us take these tools to Huanaco and bring back some silver?"
    ach "We will give you 20 silver monies in return"
    menu:
        "Yes":
            pause 0.001
        "No":
            call s2(False)
    ach "Okie dokie, let's go then." 
    ach "You pull the cart with the pickaxes"
    "For many days, you walk through ancient river beds and along fast-flowing streams."
    "No matter how high you seem to climb, the mountains still seem impossibly tall."
    "Your group passes many other, some with messangers gleaming with sweat after running through the thin air"
    "All along the path, there are too many terrace farms to count."
    "Hundreds of thousands of quinoa and potatoes stick out above each step, water trickling down"
    "At last, you walk in between two particularly tall mountains into a valley filled with the stone buildings of a large town"
    $ xp += 1
    ach "Here we are, Huanaco"
    #"Achiyaku takes a look at you"
    #ach "Have you heard the story of Pachacuti?"
    #menu: 
    #    "No, please tell me":
    #        ach "Well, Pachacuti was born in the magnificent city- Cuzco"
    #        ach "When he was a kid"
    #        $ xp += 1
    #    "No, and I don't want to hear it":
    #        ach "Okay, then"
    #    "Of course I have!":
    #        pause 0.001
    "You continue into the town"
    "Achiyaku leads you to a merchant's stall with a particularly friendly-looking salesperson"
    ach "Hello there old friend!"
    ach "We have another shipment of tools."
    merchant "Good good."
    merchant "I have the usual 10 pounds of silver."
    merchant "Hey, what happened to Lllapa?"
    ach "Smallpox. :("
    merchant "Oh, I'm sorry."
    ach "I know, it's killed so many people"
    ach "Sometimes I worry we may never return to our glory days"
    merchant "Yes. I hear the people from across the sea can be very harsh."
    ach "We will see what happens."
    $ xp += 1
    merchant "May Inti keep us ever blooming."
    ach "Indeed"
    "Achiyaku loads the silver into the carts."
    ach "Well, I suppose it is time to go to Lima once again."
    "For days you trek until you eventually get out of the Andean highlands and return to the coastal lowlands"
    "Then, just a day away from Lima, your group is ambushed!"
    "Five people with bone-tipped spears quickly surround your group."
    if renpy.random.randint(1,10) >= 6*(defense/100):
        $ hp -= 1
        "One of them forces the blunt part of their spear into your chest, knocking you into the ground"
    "Achiyaku and their partner quickly pull out daggers that they'd been concealing."
    ach "I don't want this to get bloody."
    ach "How 'bout we just give you 1/10 of our goods and call it a day?"
    "The attackers look toward each other and nod their heads"
    attacker "Sure."
    attacker "What'cha got under that blanket of yours?"
    "Achiyaku pulls out 5 silver bars, only about 1/2 pound."
    ach "4 pounds of silver and a bunch of potatoes"
    attacker "Likely story."
    "The speaker makes a small movement and one of the attackers stabs at your leg..."
    if renpy.random.randint(1,10) <= 6*(defense/100):
        "and misses"
        "Achiyaku and his partner swing into action"
        menu:
            "Fight back":
                $ hp -= 1
                $ xp += 1
                "After a few minutes, Achiyaku manages to put his dagger on his opponent's throat without giving the fatal blow"
                ach "Leave, or they die."
                "The attackers relent and leave"
            "Dodge":
                "You successfully divert the few attacks that come your way"
    else:
        $ hp -= 3
        "and pierces it painfully"       
        $ xp += 1
        attacker "What do you really have!?"
        ach "Achiyaku pauses."
        "You can see them considering your life's worth."
        "He throws his dagger on the ground, relenting."
        ach "10 pounds of silver."
        "The attackers swarm the carts and take 2 pounds of it."
    "The three of you return to the port on high guard, but nobody attacks you."
    ach "Thank you."
    $ sp += 20
    ach "Here's your money."
    menu:
        "Deal with the merchant":
            call s2x1(True, True)
        "Attempt a trivia test to get an all-expense paid vacation":
            call s2x2(True, True)
    return
label s2x4(firsttime):
    if firsttime == False:
        "Once you get to Guayaquil, Ferdinand leads you to a boat with the Spanish Flag and the royal colors of the Hapsburgs"
    
    sailwa "Good day to you!"
    tian "Hello!"
    menu:
        "Greet the ticketholder":
            pause 0.001
        "Don't greet the ticketholder":
            pause 0.001
    tian "We would like two spots aboard this vessel"
    sailwa "Sure, it's only 10 silver monies!"
    tian "10 monies!" 
    tian "Where's this ship going? Majapahit?!"
    sailwa "Not quite."
    sailwa "Just to Guayaquil."
    tian "Where is Guayaquil?"
    menu:
        "Tell Tian where Guayaquil is":
            tian "Of course, I knew that."
        "Let them be embarassed":
            sailwa "Just a thousand or so miles up the coast"
    tian "Very well"
    tian "I will pay for both of us."
    tian "Not because I like you."
    tian "Because I respect the power of karma."
    sailwa "Come aboard the Maria, also known as the finest carrack in the Pacific Ocean"
    "For many days, you ride aboard the Maria, the rocking of the boat in the waves driving Captain Tian to the side of the ship more times than you can count."
    "On the voyage, you meet a woman who says she's the wife of a conquistador"
    isabella "He is not the best guy, but there's not much I can do about it."
    isabella "Plus, this gives me the oppurtunity to further the cause of Christianity."
    isabella "That's actually why I'm headed to Guayaquil, to oversee one of my husband's encomiendas"
    menu:
        "What's an encomienda?":
            $ xp += 2
            isabella "It's a grant from the king"
            isabella "He gives us control over all the indios in a certain area, and we protect them and show them the light of God"
            isabella "My husband said they don't even have a chapel where I'm headed."
            isabella "I'll have to make the indios to build one."
            menu:
                "That is so messed up":
                    isabella "Why?"
                    isabella "It's much better than the slavery in Hispanola."
                    isabella "All were asking of them is that they do a little bit of work in exchange for safety and enlightenment."
                    isabella "We wouldn't want the natives to get lazy or complacent, now would we?"
                "Yes, very... interesting":
                    isabella "It is, isn't it."
            isabella "Well, it's almost dinner time."
            isabella "Nice to meet you!"
        "Go away girl":
            isabella "Fine"
            isabella "It's almost dinner time anyway"
        "Slay for you":
            isabella "Why, thank you."
            isabella "Well, it's almost dinner time."
            isabella "Nice to meet you!"
    "The next day, when you are walking around the ship, you bump into Isabella again, this time accompanied by a friend."
    isabella "Oh, hello!"
    isabella "Have you met my cousin Ferdinand?"
    trivier "I don't believe we've met."
    isabella "He's offering the {b}experience{/b} of a lifetime"
    trivier "Yes I am!"
    call s2x2(True, 3)

    return

label s3x1(firsttime, lasttime):
    if firsttime:
        "The streets of the city get more and more packed as you approach the source of the chatter of thousands of people."
        "It is nothing compared to when you step into the huge complex of buildings, though."
        "Beautiful geometric art is painted along the ceilings and the walls are lined with goods."
        "Merchants shout for your attention."
        merchant "Would you like to buy some of the finest quality fur in the world?"
        merch2 "No!"
        merch2 "Don't get his cheap fur!"
        merch2 "Buy some of the most flavorful spices in the world from me!"
        merch3 "She has terrible products!"
        merch3 "Buy the most comfortable and beautiful fez in the world right here."
        merch4 "Trust me," 
        merch4 "all of their products suck!"
        merch4 "At my stall, you can get 15 ounces of olive oil for just 2 silver monies."
    $ continuer = True
    # This interaction doesn't add much depth/ gets boring fast, but was challenging to code
    if sp > 0 and continuer == True:
        menu:
            "Bargain for the furs":
                merchant "Thank you choosing my stall!"
                call s3x1y1(5,2)
            "Bargain for the spices":
                merch2 "Thanks for choosing my stall!"
                call s3x1y1(9,3)
            "Bargain for the fez":
                merch3 "Congratulations on choosing the best stall!"
                call s3x1y1(4,1)
            "Bargain for the olive oil":
                merch4 "I'm glad you chose my stall!"
                call s3x1y1(2,1)
            "Don't buy anything":
                $ continuer = False
    if lasttime:
        "Over the aromas of cooking kebabs and dried fruits, a strong burning smell fills your nose"
        "The chatter of the market turns to screams"
        rando "FIIIIRE!"
        call s3x2(True)
    else:
        "As you continue through the bazaar, you here more and more people talking about the military celebration"
        rando "I heard they're going to use the newest cannons from the Transylvanian frontline!"
        rando2 "Oh, this is so cool." 
        rando2 "I'm so glad we're living under Mehmed IV."
        menu:
            "Go to the military celebration":
                call s3x3(True, True)
            "Head to the tall mosques":
                call s3x3(True, True)
    return
label s3x2(firsttime):
    "The whole scene descends into chaos worse than middle schoolers when the lunch bell rings."
    "You are pushed from every which way, and you find yourself pushing back."
    rando "North! To the docks!"
    menu:
        "Go with the flow of the crowd":
            "You try your best to get through this situation unscathed and alive."
            $ hp -= 1
            "Unfortunetely, by the time you return to the docks, you do have a number of bruises."
        "Fight for the first spot":
            if renpy.random.randint(1,20) > 14*defense:
                "You successfully win the scuffles you get into, accelerating your way to the front of the mob."
            else:
                $ hp -= 2
                "Although you win a few of the fights that break out along the way, you lose many as well."
    "As you step onto the last bits of land between yourself and the churning sea, you are reminded of previous times."
    "You are once again a refugee, a captive to the actions taken by the society surrounding you."
    "This time, though, there is no orderely boarding with ticketholders."
    "It is every person for themselves, and you see ships leaving with people barely hanging on to the railings."
    "Slaves, merchants, artisans, peasants"
    "..."
    "All fearing the same all-consuming invention of humanity."
    menu:
        "Take a moment to be humbled":
            "A phone appears in your hand and you are taken away from the grip of death once again."
        "Board the closest ship":
            "You race your way to a large cargo ship bearing the British flag."
            "Nobody is there to check your passanger status, so you make it on smoothly."
            "But as you look back, you notice that if you tried just a few moments later you would have fallen into the sea."
            guard "Are you headed to Egypt?"
            menu:
                "Yes, exactly":
                    guard "Good."
                "I wasn't planning on it":
                    guard "Well that's where you're going."
            guard "You can sleep on the floor, if you can find space."
            "You do find space."
            "As you lay down your head after another long day, something hard and cool appears beneath."
            "It's a phone."
    nar "Hello!"

    return
label s3x3(firsttime, lasttime):
    "You go with the flow of the crowd through the winding streets of the city, keeping the minarets ahead of you."
    "The first mosque you walk to is a central cylinder of pinkinsh stone capped by a light blue dome that shines in the sun"
    "Attatched to it are dozens of smaller buildings, also made from the pinkish stone."
    "And, of course, at each corner stands tall a minaret."
    aminah "Isn't the Hagia Sophia so beautiful?"
    menu:
        "Yes, indeed":
            pause 0.001
        "Meh":
            aminah "Well what about the Blue Mosque?"
    "Standing across from the Hagia Sophia, the Blue Mosque rises dome stacked above dome reaching toward the rising moon."
    "Each of the dome and minaret has a perfect symmetry and pierces elegantly into the sky just a few shades lighter than the domes"
    "And closer to eye level, arches adorn every entrance and balcony on the ginormous structure"
    aminah "What do ya think about this one?"
    menu:
        "It's amazing":
            pause 0.001
        "I'm not really sold on it":
            aminah "Okay, mister opinions."
    aminah "Look, the parade is starting!"
    "A band of soldiers comes out as dozens of drums beat in the park between the two striking mosques."
    soldier "We are the Janissaries!"
    "From behind him, hundreds of Janissaries file into the cleared out space, all marching with a single terryfyingly loud beat."
    "Each of them carry a rifle and wear their signature tunics and tall bork hats."
    "Another nearby soldier shouts."
    soldier "We are the Sipahi!"
    "Hundreds of horsemen ride in to the Janissary's left flank."
    soldier "We are the Corsairs!"
    "At the front of this group you see Abdullah, your former captor."
    "And trailing behind him are some of the people from the caravel you were aboard, gleaming in new uniforms."
    menu:
        "Boo":
            aminah "Shush!"
            aminah "What are you doing?!"
        "Cheer":
            aminah "I have a friend whose cousin has a friend who is a corsair."
    "Soldiers come for a couple dozen minutes until the area is filled with military men from across the empire."
    "Each group has its own smug aura, comparing their achievements to those of their counterparts."
    if lasttime:
        "Just as the military people begin to march, you notice a large glowing in the distance."
        "At first, it seems ignorable- perhaps just a large party at the bazaar."
        "Soon, however, the glowing climbs to the rooftops and you begin to make out it's source."
        "It is an enormous fire, crawling through the heart of the Capital."
        rando "Do you hear that?"
        "In between the drumming and singing in front of you, distant and desperate screams stab through your heart."
        "Slowly, the realization of the fire spreads through the crowd."
        "Confusion turns to fear and the crowd seems to freeze."
        "Now, even the drummers have stopped their beating."
        "It seems that the the whole audience is now made of gunpowder, ready to ignite at the slightest of sparks."
        menu:
            "Scream \"FIIIIRE\"":
                pause 0.001
            "Watch & Wait":
                "And then the spark is lit."
                rando "RUUUUUUN!"
    else:
        "Marching ensues for half an hour, with epic displays of artillery and discipline as the sun falls to the horizon."
        "Just as the last beat of the last song echoed through the crowd, the minarets began to yell."
        "From high up, a dozen of men begin azaan, the call to prayer."
        "A large, but not certainly not complete, portion of the people around you enter the mosques."
        menu:
            "Join them for namaaz.":
                "As people enter, you notice they take off their shoes and step in with their right foot."
                "People line up in rows of many dozen people each, packed in shoulder to shoulder."
                "A person in the front, the Imam, leads the legions of people in prayer."
                "The prayer is wrapped up in ten minutes and most people stream back outside to the sounds of fireworks."
                aminah "Hey!" 
                aminah "You come to the Grand Bazaar with my friends and I!"
                aminah "Were going to get dinner and do some \"light\" shopping!"
                menu:
                    "That sounds fun!":
                        pause 0.001
                    "Ohhh kay":
                        pause 0.001
                call s3x1(True, True)
            "Go to the grand bazaar":
                call s3x1(True, True)
    return
label s3x4(firsttime):

    return

label s3x1y1(fincost, valu):
    $ continuer2 = True
    while continuer2 == True:
        merchant "That'll be [fincost] silver monies"
        menu:
            "Go lower":
                if renpy.random.randint(1,10) <= 4:
                    "Very well"
                else:
                    "Fine, but this is as low as I'll go."
                    $ continuer2 = False
            "Buy":
                $ fincost += 1
                $ continuer2 = False
        $ fincost -= 1
    $ sp -= fincost
    $ xp += valu
    $ itemsval += valu
    call s3x1(False)
    return
