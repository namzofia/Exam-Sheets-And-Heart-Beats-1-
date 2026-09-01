# ==========================================
# 12:00 PM ACTIONS
# ==========================================

# --- EAT LUNCH WITH KRISTEN ---
label act12pmKristenPass:
    $ Energy += 20
    $ Social += 20
    $ Readiness += 0
    $ Focus += 0
    $ currentTime += 1
    
    scene hallway1 with dissolve
    show kristen smilenoteeth at npcSize with dissolve
    show eliza smilepray at elizaSize with dissolve
    k "Yay! It's finally lunch! What are you eating?"
    e "I have a chicken wrap! What about you?"
    k "I'm just eating a ham and cheese sandwich haha"

    scene library at bgSize with dissolve
    "You got: +20 Energy, +20 Social, +0 Readiness, +0 Focus"

    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack

label act12pmKristenFail:
    $ Energy -= 10
    $ Social -= 20
    $ Readiness += 0
    $ Focus -= 10
    $ currentTime += 1
    
    scene hallway1 with dissolve
    show kristen mouthopen at npcSize with dissolve
    show eliza smilepray at elizaSize with dissolve
    e "It's finally lunch I'm STARVING"
    k "Well I've got things to do so see you tomorrow"
    show eliza shocked at elizaSize with dissolve #I DONT KNOW IF YOU NEED THE DISSOLVE HERE BUT I PUT IT ANYWAY
    e "What? Oh see you..!"

    scene library at bgSize with dissolve
    "You got: -10 Energy, -20 Social, +0 Readiness, -10 Focus"

    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack


# --- POST ON INSTAGRAM ---
label act12pmInstaPass:
    $ Energy += 0
    $ Social += 20
    $ Readiness += 0
    $ Focus -= 10
    $ currentTime += 1
    
    scene library at bgSize with dissolve
    "Thomas viewed the post (what she had for lunch) and liked it!"
    "You got: +0 Energy, +20 Social, +0 Readiness, -10 Focus"

    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack

label act12pmInstaFail:
    $ Energy -= 10
    $ Social -= 10
    $ Readiness += 0
    $ Focus -= 20
    $ currentTime += 1
    
    scene library at bgSize with dissolve
    "Thomas viewed the repost (with a caption saying “Future me: ” and its a video of Eliza clubbing)"
    "He messages saying, “Are you ok?”"
    "You got: -10 Energy, -10 Social, +0 Readiness, -20 Focus"

    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack


# --- STUDY (12 PM) ---
label act12pmStudyPass:
    $ Energy -= 10
    $ Social += 0
    $ Readiness += 20
    $ Focus += 20
    $ currentTime += 1
    
    scene library at bgSize with dissolve
    "You studied for 2 hours!! \(>,<)/"
    "You got: -10 Energy, +0 Social, +20 Readiness, +20 Focus"

    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack

label act12pmStudyFail:
    $ Energy -= 20
    $ Social += 0
    $ Readiness += 0
    $ Focus -= 20
    $ currentTime += 1
    
    scene library at bgSize with dissolve
    "You doom scrolled on Instagram and lost track of time!! You lost 2 hours of studying time ~(>o<)~"
    "You got: -20 Energy, +0 Social, +0 Readiness, -20 Focus"

    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack