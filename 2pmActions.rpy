# =========================================================
# 2 PM: ACTION CUTSCENES
# =========================================================

# --- 1. Do Last Minute Cram Study ---
label act2pmStudyPass:
    $ Energy -= 20
    $ Social += 0
    $ Readiness += 30
    $ Focus += 10
    $ currentTime += 1

    scene library at bgSize with dissolve
    "You memorized all your notes!!! (  • u •  )"
    "You got: -20 Energy, +0 Social, +30 Readiness, +10 Focus"

    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack

label act2pmStudyFail:
    $ Energy -= 10
    $ Social += 0
    $ Readiness -= 10
    $ Focus -= 30
    $ currentTime += 1

    scene library at bgSize with dissolve
    "You forgot everything because of how nervous you were and there’s no time to study!! (•- •;)"
    "You got: -10 Energy, +0 Social, -10 Readiness, -30 Focus"
#finished bit above

# --- 2. Hype Thomas up before his exam ---
label act2pmThomasPass:
    $ Energy += 10
    $ Social += 20
    $ Readiness += 0
    $ Focus += 10
    $ currentTime += 1

    scene classroom with dissolve
    show thomas hehehe at npc2Size with dissolve
    show eliza lovesmilepray at elizaSize with dissolve
    e "Good luck Thomas!"
    t "Thanks, you too, Eliza"
    show thomas bigsmile at npc2Size
    show eliza blushsmile at elizaSize
    "..."
    show thomas embarrassed at npc2Size
    show eliza embarrassed at elizaSize
    ".................."
    t "oookay, see you later..!"
    hide thomas embarrassed with dissolve
    hide eliza embarrassed with dissolve

    scene classroom with dissolve
    "You got: +10 Energy, +20 Social, +0 Readiness, +10 Focus"

    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack

label act2pmThomasFail:
    $ Energy -= 10
    $ Social -= 10
    $ Readiness += 0
    $ Focus -= 10
    $ currentTime += 1
    
    scene classroom with dissolve
    show thomas pissed at npc2Size with dissolve
    show eliza blushsmile at elizaSize with dissolve
    e "Good luck Thomas!"
    t "Yeah whatever..."

    scene classroom with dissolve
    "You got:  -10 Energy, -10 Social, +0 Readiness, -10 Focus"
#UP TO HERE

# --- 3. Do a good luck ritual with Kristen ---
label act2pmKristenPass:
    $ Energy += 20
    $ Social += 10
    $ Readiness += 10
    $ Focus += 10
    $ currentTime += 1

    scene classroom with dissolve
    "They each ate a Kopiko just before the exam to keep them awake!! :P"
    "You got: +20 Energy, +10 Social, +10 Readiness, +10 Focus"

    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack

label act2pmKristenFail:
    $ Energy -= 20
    $ Social += 10
    $ Readiness -= 10
    $ Focus -= 10
    $ currentTime += 1
    
    scene classroom with dissolve
    "Eliza and Kristen spin around 10 times clockwise then 10 times anticlockwise. But now they feel sick!! <( •-•)> "
    "You got:  -20 Energy, +10 Social, -10 Readiness, -10 Focus"

    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack