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
    e "Yep!!"
    scene school front with dissolve
    "You manage to get 2 hours of work done!"
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
    show kristen mad at npcSize with dissolve
    k "Eliza. I have a math test in 10 minutes and you distracted me from studying."
    show eliza sleepshockedeyesclosed at elizaSize with dissolve
    e "Oh..! Sorry..."
    scene school front with dissolve
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
    "You napped for 1 hour! You feel refreshed!! :D"
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
    "You tried to sleep but there was a bird chirping the whole time!!"
    "Eliza couldn't get a wink of sleep :("
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
    "You studied for 1 hour!! ( • u < )"
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
    "You zoned out for 1 hour! (• o •)"
    "You got:  -10 Energy, +0 Social, +0 Readiness, -10 Focus"

    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack