# ==========================================
# 11:00 AM ACTIONS
# ==========================================

# --- LUNCH WITH THOMAS ---
label act11amThomasPass:
    $ Energy += 20
    $ Social += 20
    $ Readiness += 0
    $ Focus += 10
    $ currentTime += 1
    
    scene lunch at bgSize with dissolve
    "Eliza's not hungry, but she saw Thomas eating early..!"
    "She lingers by the lunch table hoping he'll approach her.."
    show eliza neutral at elizaSize with dissolve
    show thomas smilenoteeth at npc2Size with dissolve
    t "Hey Eliza, do you mind if I sit with you?"
    show eliza excited at elizaSize
    show thomas thinsmile at npc2Size
    e "S-sure!!"
    show eliza blushsmile at elizaSize
    show thomas mouthopen at npc2Size
    t "Thanks, Jacob's busy playing baseball so.."
    show eliza lovesmilepray at elizaSize
    show thomas thinsmile at npc2Size
    e "I see! That sounds fun"
    show eliza embarrassed at elizaSize
    show thomas bigsmile at npc2Size
    e "Well you can sit with me anytime..!"
    hide thomas with dissolve
    hide eliza with dissolve
    "You got: +20 Energy, +20 Social, +0 Readiness, +10 Focus"

    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack

label act11amThomasFail:
    $ Energy -= 10
    $ Social -= 20
    $ Readiness += 0
    $ Focus -= 20
    $ currentTime += 1
    
    scene lunch at bgSize with dissolve
    "Eliza's not hungry, but she saw Thomas eating early..!"
    "She lingers by the lunch table hoping he'll approach her.."
    "...."
    "He doesn't approach her."
    "So she'll just approach him!"
    show eliza embarrassed at elizaSize with dissolve
    show thomas neutral at npc2Size with dissolve
    e "Hi Thomas! Is it okay if I sit with you?"
    show eliza shocked at elizaSize
    show thomas pissed at npcSize
    t "Actually, I'd rather you not. Sorry."
    show eliza distraught at elizaSize
    show thomas worried at npcSize
    e "Oh..."
    show eliza shockedeyesclosed
    show thomas worried at npcSize
    e "okay.. thanks anywyas"
    hide thomas with dissolve
    hide eliza with dissolve
    "You got: -10 Energy, -20 Social, +0 Readiness, -20 Focus"

    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack


# --- DISTURB KRISTEN ---
label act11amKristenPass:
    $ Energy -= 10
    $ Social -= 10
    $ Readiness += 0
    $ Focus -= 10
    $ currentTime += 1
    
    scene library at bgSize with dissolve
    "Eliza just remembered something she needed to tell Kristen!"
    "She found her deep in studying, but decided to disturb her anyways."
    show eliza smilepray at elizaSize with dissolve
    show kristen neutral at npcSize with dissolve
    e "Kristen! I've got something important to tell you!"
    show eliza shocked at elizaSize
    show kristen mad at npcSize
    k "Eliza, can't you see I'm studying? Just tell me later"
    show eliza distraught at elizaSize
    show kristen pissed at npcSize
    e "Oh... right sorry"
    hide kristen with dissolve
    hide eliza with dissolve
    "You got: -10 Energy, -10 Social, +0 Readiness, -10 Focus"

    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack

label act11amKristenFail:
    $ Energy -= 10
    $ Social -= 30
    $ Readiness += 0
    $ Focus -= 10
    $ currentTime += 1
    
    scene library at bgSize with dissolve
    show eliza smilepray at elizaSize with dissolve
    show kristen neutral at npcSize with dissolve
    e "Kristen! I've got something important to tell you!"
    show eliza shocked at elizaSize
    show kristen mad at npcSize
    k "Eliza, can't you see I'm studying? Just tell me later"
    show eliza distraught at elizaSize
    show kristen pissed at npcSize
    "Kristen glares intensely at Eliza before putting her headphones on."
    show kristen mad at npcSize
    show eliza shockedpray
    k "Go away Eliza I'm not talking to you anymore!"
    show eliza shockedeyesclosed at elizaSize
    e "Oh... sorry..."
    hide kristen with dissolve
    hide eliza with dissolve
    "You got: -10 Energy, -30 Social, +0 Readiness, -10 Focus"

    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack


# --- STUDY (11 AM) ---
label act11amStudyPass:
    $ Energy -= 10
    $ Social += 0
    $ Readiness += 20
    $ Focus += 10
    $ currentTime += 1
    
    scene library at bgSize with dissolve
    "Eliza spent the whole hour studying without distractions!"
    "Since her exam is approaching, she's been getting far more motivated."
    "You got: -10 Energy, +0 Social, +20 Readiness, +10 Focus"

    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack

label act11amStudyFail:
    $ Energy -= 10
    $ Social += 0
    $ Readiness += 0
    $ Focus -= 10
    $ currentTime += 1
    
    scene library at bgSize with dissolve
    "Since the exam is approaching, Eliza's been getting too nervous!"
    "With all this stress, she couldn't focus on her studies :<"
    "You got: -10 Energy, +0 Social, +0 Readiness, -10 Focus"

    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack