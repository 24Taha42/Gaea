# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define nar = Character("Unknown Caller", color = "#aaaaaa")
define newsie = Character("Newsperson", color = "#ca5ccd")
define merchant = Character("Merchant", color = "#ece911")
define attacker = Character("Attacker", color = "#ff0000")
define sailor = Character("Shorter ticketholder", color = "#0000ff")
image s0p1 = "phonev2.png"
image blackbg = "#000"



# The game starts here.

label start:
    call vars

    scene blackbg
    show s0p1

    "ring ring, ring ring"
    
    pause 5
    "Left-click to continue"

    menu:
        "Pick up":
            #call s0
            call s1(True)
            
        "Don't Pick Up":
            pause 1

    "Congratulations! You have finished the game."

    return

label vars:
    $ year = 1066
    $ xp = 0
    $ hp = 10
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

label s1x1(firsttime):
    merchant "Hello, excuse me for a second- I just have to pack this last thing up"
    pause 1
    if firsttime == True:
        merchant "Thanks for waiting. You came at the perfect time!"
        merchant "I- well I guess just me now-"
        merchant "I am having a barbarian apocalypse clearance sale. Everything is 50\% off!"
        merchant "How many silver pieces do you have?"
    menu:
        "20":
            pause 0.0001
        "None":
            merchant "Are you sure? Why don't you check the top bar of your screen?"
        "No idea":
            merchant "Well, why don't you check at the top bar of the screen?"
    merchant "Good, what would you like to buy?"
    menu:
        "The Analects of Confucious (a book) -- 5 silver pieces":
            $ sp -= 5
            merchant "Thank you for visiting!"
        "A yard of silk -- 3 silver pieces":
            $ sp -= 3
            merchant "Thank you for visiting!"
        "Simple medicine -- 2 silver pieces":
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
    return
label s1x3(firsttime):
    if firsttime == True:
        "off to the army you go!"
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