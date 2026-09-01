#=========================================================
# 9 AM: ACTION CUTSCENES
# =========================================================

# --- 1. STUDY IN THE LIBRARY ---
label act9amStudyPass:
    $ Energy -= 10
    $ Social += 0
    $ Readiness += 20
    $ Focus += 10
    $ currentTime += 1
    
    scene library with dissolve
    "Eliza locked in and studied for the whole time!"
    "She's very proud of her studious efforts :3'"
    "You got: -10 Energy, +0 Social, +20 Readiness, +10 Focus"

    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack

label act9amStudyFail:
    $ Energy -= 10
    $ Social += 0
    $ Readiness += 0
    $ Focus -= 10
    $ currentTime += 1
    
    scene library with dissolve
    "Eliza couldn't concentrate for the whole hour!"
    "She's even more lost than before.."
    "You got: -10 Energy, +0 Social, +0 Readiness, -10 Focus"

    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack


# --- 1. TALK TO KRISTEN ---
label act9amKristenPass:
    $ Energy -= 10
    $ Social += 0
    $ Readiness += 20
    $ Focus += 10
    $ currentTime += 1
    
    scene hallway2 at bgSize with dissolve
    "Eliza approaches Kristen in the hallway"
    show eliza smilepray at elizaSize with dissolve
    show kristen smileteeth at npcSize with dissolve
    e "Hey Kristen!"
    show eliza smileteeth at elizaSize
    show kristen hehehe at npcSize
    k "Eliza! Hi!!"
    show eliza smilenoteeth at elizaSize
    show kristen thinsmile at npcSize
    e "How are you?"
    show eliza neutral at elizaSize
    show kristen scared at npcSize
    k "Tiredddd. My hamsters woke me up at 4am because they were hungry."
    show eliza shockedpray at elizaSize
    show kristen scared at npcSize
    e "Oh no! That's so sad"
    show eliza excited
    show kristen neutral
    "{shader=wave}*RIIIIING*{/shader}"
    show eliza smilenoteeth at elizaSize
    show kristen smileteeth at npcSize
    k "We better head to class!!"
    hide kristen with dissolve
    hide eliza with dissolve
    "You got: -10 Energy, +20 Social, +0 Readiness, +10 Focus"

    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack

label act9amKristenFail:
    $ Energy -= 10
    $ Social += 0
    $ Readiness += 0
    $ Focus -= 10
    $ currentTime += 1
    
    scene hallway2 at bgSize with dissolve
    "Eliza approaches Kristen in the hallway"
    show eliza smilenoteeth at elizaSize with dissolve
    show kristen neutral at npcSize with dissolve
    e "Hey Kristen!"
    show eliza shocked at elizaSize
    show kristen mad at npcSize
    k "What do you want."
    show eliza embarrassed at elizaSize
    show kristen pissed at npcSize
    e "Oh... I just wanted to say hi..!"
    hide kristen mad with dissolve
    "Kristen glares at Eliza then walks away."
    show eliza shockedpray at elizaSize
    e "Yikes! She's in a bad mood.."

    hide eliza with dissolve
    "You got: -10 Energy, -20 Social, +0 Readiness, -10 Focus"

    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack


# --- 3. GREET THOMAS GOODMORNING :3 ---
label act9amThomasPass:
    $ Energy -= 10
    $ Social += 10
    $ Readiness += 0
    $ Focus += 10
    $ currentTime += 1
    
    scene hallway1 at bgSize with dissolve
    "Eliza waits by Thomas' locker in the hallway, hoping he'll say hi...."
    show thomas smilenoteeth at npc2Size with dissolve
    show eliza neutral at elizaSize with dissolve
    t "Hi Eliza"
    show thomas thinsmile at npc2Size
    show eliza blushsmile at elizaSize
    e "Oh..! Hi Thomas!"
    show thomas mouthopen at npc2Size
    show eliza blushsmile at elizaSize
    t "Ready for the exams today?"
    show thomas thinsmile at npc2Size
    show eliza embarrassed at elizaSize
    e "O-oh yes..! Yes of course! How about you?"
    show thomas hehehe at npc2Size
    show eliza blushsmile at elizaSize
    t "Yeah, I'm ready."
    show thomas bigsmile at npc2Size
    show eliza lovesmilepray at elizaSize
    e "A-ah good luck Thomas then..!"
    show thomas smileheart at npc2Size
    show eliza blushsmile at elizaSize
    t "Thanks Eliza! Catch you around later?"
    show thomas thinsmile at npc2Size
    show eliza lovesmilepray at elizaSize
    e "Y-yes of course! Hehe!"
    hide thomas with dissolve
    hide eliza with dissolve
    "You got: -10 Energy, +10 Social, +0 Readiness, +10 Focus"

    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack

label act9amThomasFail:
    $ Energy -= 10
    $ Social += 0
    $ Readiness += 0
    $ Focus -= 10
    $ currentTime += 1
    
    scene hallway1 at bgSize with dissolve
    "Eliza waits by Thomas' locker in the hallway, hoping he'll say hi...."
    "..."
    "He doesn't say hi! So Eliza will just approach him herself."
    show eliza smileteeth at elizaSize with dissolve
    show thomas neutral at npc2Size with dissolve
    e "Hi Thomas!"
    show eliza blushsmile at elizaSize
    show thomas pissed at npc2Size
    t "Oh... Hi"
    show eliza lovesmilepray at elizaSize
    show thomas pissed at npc2Size
    e "How are you--"
    hide thomas with dissolve
    "He turns and leaves without another word."
    show eliza shocked at elizaSize
    e "..."
    show eliza distraught at elizaSize
    e "O-oh, okay, bye Thomas!"
    hide eliza with dissolve
    "You got: -10 Energy, +0 Social, +0 Readiness, -10 Focus"

    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack