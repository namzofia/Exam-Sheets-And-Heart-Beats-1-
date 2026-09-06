# =========================================================
# 1 PM: ACTION CUTSCENES
# =========================================================

# --- 1. study wth Kristen ---
label act1pmKristenPass:
    $ Energy -= 20
    $ Social += 10
    $ Readiness += 20
    $ Focus += 10
    $ currentTime += 1
    

    scene library with dissolve
    show kristen smileteeth at npcSize with dissolve
    show eliza smilepray at elizaSize with dissolve
    k "Okay let's lock in!!"
    show kristen smilenoteeth at npcSize
    show eliza blushsmile at elizaSize
    e "Yep!!"
    hide eliza with dissolve
    hide kristen with dissolve
    "Eliza and Kristed managed to get 2 hours of work done!"
    "You got: -20 Energy, +10 Social, +20 Readiness, +10 Focus"
    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack

label act1pmKristenFail:
    $ Energy -= 20
    $ Social -= 20
    $ Readiness += 0
    $ Focus -= 20
    $ currentTime += 1
    
    scene library with dissolve
    show eliza smilepray at elizaSize with dissolve
    show kristen scared at npcSize with dissolve
    e "Kristen omg you won't believe this..!"
    show kristen mad at npcSize
    show eliza shocked at elizaSize
    k "Eliza. I have a math test in 10 minutes and you distracted me from studying."
    show eliza shockedpray at elizaSize
    show kristen pissed at npcSize
    e "Oh..! Sorry..."
    hide eliza with dissolve 
    hide kristen with dissolve
    "You got: -10 Energy, -20 Social, +0 Readiness, -20 Focus"
    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack

# --- 2. Nap in classroom ---
label act1pmNapPass:
    $ Energy += 30
    $ Social += 0
    $ Readiness += 0
    $ Focus += 10
    $ currentTime += 1

    scene classroom with dissolve
    "Eliza napped for 1 hour! She feels so much more refreshed!! :D"
    "You got: +30 Energy, +0 Social, +0 Readiness, +10 Focus"

    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack

label act1pmNapFail:
    $ Energy -= 20
    $ Social += 0
    $ Readiness += 0
    $ Focus -= 10
    $ currentTime += 1
    
    scene classroom at bgSize with dissolve
    "Eliza tried to sleep but there was a bird chirping at the window..."
    "She couldn't get a wink of sleep :("
    "You got:  -20 Energy, +0 Social, +0 Readiness, -10 Focus"
    
    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack


# --- 3. Go to the Library and Study ---
label act1pmStudyPass:
    $ Energy -= 10
    $ Social += 0
    $ Readiness += 10
    $ Focus += 10
    $ currentTime += 1

    scene library with dissolve
    "Eliza studied for 1 hour very productively!! ( • u < )"
    "You got: -10 Energy, +0 Social, +10 Readiness, +10 Focus"

    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack

label act1pmStudyFail:
    $ Energy -= 10
    $ Social += 0
    $ Readiness += 0
    $ Focus -= 10
    $ currentTime += 1
    
    scene classroom with dissolve
    "Eliza tried to study but she was zoned out the whole time... (• o •)"
    "You got:  -10 Energy, +0 Social, +0 Readiness, -10 Focus"

    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack