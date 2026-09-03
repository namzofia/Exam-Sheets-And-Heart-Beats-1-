# =========================================================
# 2 PM: ACTION CUTSCENES
# =========================================================

# --- 1. Do Last Minute Cram Study ---
label act2pmCramPass:
    $ Energy -= 20
    $ Social += 0
    $ Readiness += 30
    $ Focus += 10
    $ currentTime += 1

    scene library at bgSize with dissolve
    "Eliza only had an hour left before the exam, so she decided to try and memorise some stuff!"
    "She did it, and now she's super ready :3"
    "You got: -20 Energy, +0 Social, +30 Readiness, +10 Focus"

    jump gameEnd

label act2pmCramFail:
    $ Energy -= 10
    $ Social += 0
    $ Readiness -= 10
    $ Focus -= 30
    $ currentTime += 1

    scene library at bgSize with dissolve
    "Yikes! Eliza's getting cold feet..."
    "She forgot everything because of how nervous she was, and there's no time to study!! (•- •;)"
    "You got: -10 Energy, +0 Social, -10 Readiness, -30 Focus"

    jump gameEnd


# --- 2. Hype Thomas up before his exam ---
label act2pmThomasPass:
    $ Energy += 10
    $ Social += 20
    $ Readiness += 0
    $ Focus += 10
    $ currentTime += 1

    scene classroom with dissolve
    show thomas neutral at npc2Size with dissolve
    show eliza lovesmilepray at elizaSize with dissolve
    e "Good luck Thomas!"
    show thomas bigsmile at npc2Size
    show eliza neutral at elizaSize
    t "Thanks, you too, Eliza"
    show thomas neutral at npc2Size
    show eliza blushsmile at elizaSize
    "..."
    show thomas embarrassed at npc2Size
    show eliza embarrassed at elizaSize
    ".................."
    show thomas smileheart at npc2Size
    show eliza neutral at elizaSize
    t "oookay, see you later..!"
    hide thomas with dissolve
    hide eliza with dissolve
    "You got: +10 Energy, +20 Social, +0 Readiness, +10 Focus"

    jump gameEnd

label act2pmThomasFail:
    $ Energy -= 10
    $ Social -= 10
    $ Readiness += 0
    $ Focus -= 10
    $ currentTime += 1
    
    scene classroom with dissolve
    show thomas worried at npc2Size with dissolve
    show eliza blushsmile at elizaSize with dissolve
    e "Good luck Thomas!"
    show thomas pissed at npc2Size
    show eliza shocked at elizaSize
    t "Yeah whatever..."
    hide thomas with dissolve
    show eliza shockedpray
    e "Oh no why does Thomas hate me...!"
    hide eliza with dissolve
    "You got: -10 Energy, -10 Social, +0 Readiness, -10 Focus"

    jump gameEnd


# --- 3. Do a good luck ritual with Kristen ---
label act2pmKristenPass:
    $ Energy += 20
    $ Social += 10
    $ Readiness += 10
    $ Focus += 10
    $ currentTime += 1

    scene classroom with dissolve
    "Eliza and Kristen decided to each eat a Kopiko just before the exam to keep them awake!! :P"
    "Now they feel super alive yaho!"
    "You got: +20 Energy, +10 Social, +10 Readiness, +10 Focus"

    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump gameEnd

label act2pmKristenFail:
    $ Energy -= 20
    $ Social += 10
    $ Readiness -= 10
    $ Focus -= 10
    $ currentTime += 1
    
    scene classroom with dissolve
    "Eliza and Kristen spin around 10 times clockwise then 10 times anticlockwise.."
    "But now they feel sick!! :((("
    "You got: -20 Energy, +10 Social, -10 Readiness, -10 Focus"

    jump gameEnd