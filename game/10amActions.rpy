#=========================================================
# 8 AM: ACTION CUTSCENES
# =========================================================

# --- 1. GOSSIP WITH KRISTEN ---
label act10amKristenPass:
    $ Energy += 10
    $ Social += 20
    $ Readiness += 0
    $ Focus -= 10
    $ currentTime += 1
    
    scene library at bgSize with dissolve
    "Eliza and Kristen were supposed to be studying, but unfortunatley they got distracted talking!"
    show eliza neutral at elizaSize with dissolve
    show kristen hehehe at npcSize with dissolve
    k "Hey Eliza! Look! Thomas is behind that shelf over there!"
    show eliza excited at elizaSize
    show kristen thinsmile at npcSize
    e "Really?"
    show eliza blushsmile at elizaSize
    show kristen hehehe at npcSize
    k "Yeah, look but don't make it obvious!"
    hide kristen with dissolve
    hide eliza with dissolve
    "You got:+10 Energy, +20 Social, +0 Readiness, -10 Focus"

    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack

label act10amKristenFail:
    $ Energy -= 10
    $ Social -= 10
    $ Readiness += 0
    $ Focus -= 10
    $ currentTime += 1
    
    scene library at bgSize with dissolve
    "Eliza and Kristen were supposed to be studying, but unfortunatley they got distracted talking!"
    show eliza smilepray at elizaSize with dissolve
    show kristen hehehe at npcSize with dissolve
    e "heheheheheh that's so funny!!"
    k "yeah, i know right?"
    show eliza neutral at elizaSize
    show kristen mouthopen at npcSize
    k "Ohmygosh Eliza, I just remembered something...."
    show eliza shocked at elizaSize
    show kristen scared at npcSize
    k "did you know I saw Thomas with another girl and they hugging"
    show eliza distraught at elizaSize
    show kristen scared at npcSize
    e "WHAT?!"
    show eliza shockedeyesclosed at elizaSize
    show kristen pissed at npcSize
    k "Shhh!"
    show eliza shockedpray at elizaSize
    show kristen scared at npcSize
    e "When??"
    show eliza shockedpray at elizaSize
    show kristen mouthopen at npcSize
    k "Before I came to the library!"

    hide kristen with dissolve
    hide eliza with dissolve
    "Yikes! Eliza's sad now :("
    "-10 Energy, -10 Social, +0 Readiness, -10 Focus"

    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack


# --- STALK THOMAS ---
label act10amThomasPass:
    $ Energy -= 10
    $ Social += 10
    $ Readiness += 10
    $ Focus += 10
    $ currentTime += 1
    
    scene school front at bgSize with dissolve
    "Eliza is waiting around the front of the school - hoping to find Thomas there!"
    show eliza lovesmilepray at elizaSize with dissolve
    show thomas neutral at npc2Size with dissolve
    e "Hi Thomas!"
    show eliza blushsmile at elizaSize
    show thomas mouthopen at npc2Size
    t "Hi Eliza, do you know what we have next period?"
    show eliza mouthopen at elizaSize
    show thomas neutral at npc2Size
    e "I'm pretty sure it's maths?"
    show eliza blushsmile at elizaSize
    show thomas bigsmile at npc2Size
    t "Phew thanks, I thought we had english"
    show eliza excited at elizaSize
    show thomas thinsmile at npc2Size
    e "Oh right! I still haven't finished the homework!"
    show eliza blushsmile at elizaSize
    show thomas hehehe at npc2Size
    t "Yeah me neither haha"
    hide thomas with dissolve
    hide eliza with dissolve
    "Nice! Eliza just had a chat with her crush..!"
    "You got: -10 Energy, +10 Social, +10 Readiness, +10 Focus"

    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack

label act10amThomasFail:
    $ Energy -= 10
    $ Social -= 10
    $ Readiness += 0
    $ Focus -= 10
    $ currentTime += 1
    
    scene school front at bgSize with dissolve
    "Eliza is waiting around the front of the school - hoping to find Thomas there!"
    show eliza lovesmilepray at elizaSize with dissolve
    show thomas neutral at npc2Size with dissolve
    e "Hi Thomas!"
    show eliza blushsmile at elizaSize
    show thomas mouthopen at npc2Size
    t "Oh... Hi?"
    show eliza smilenoteeth at elizaSize
    show thomas pissed at npc2Size
    e "How was the weekend?"
    show eliza shocked at elizaSize
    show thomas worried at npc2Size
    t "Oh it was ok. I've got to go, bye."
    show eliza distraught at elizaSize
    hide thomas with dissolve
    e "Oh... bye"
    hide eliza with dissolve
    "Ouch! That's got to hurt."
    "You got: -10 Energy, -10 Social, +0 Readiness, -10 Focus"

    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack


# --- STUDY ---
label act10amStudyPass:
    $ Energy -= 10
    $ Social += 0
    $ Readiness += 20
    $ Focus += 10
    $ currentTime += 1
    
    scene classroom at bgSize with dissolve
    "Eliza managed to find an empty classroom to study in!"
    "She locked in for the whole hour :3"
    "You got: -10 Energy, +0 Social, +20 Readiness, +10 Focus"

    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack

label act10amStudyFail:
    $ Energy -= 10
    $ Social += 0
    $ Readiness += 0
    $ Focus -= 10
    $ currentTime += 1
    
    scene classroom at bgSize with dissolve
    "Eliza couldn't find a single quiet classroom..."
    "She had to study with all the loud kids in the same room..!!"
    "In the end, she got absolutley no work done :("
    "You got: -10 Energy, +0 Social, +0 Readiness, -10 Focus"

    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack