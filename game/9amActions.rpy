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