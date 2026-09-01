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
    
    scene library at bgSize with dissolve
    "."
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
    
    scene library at bgSize with dissolve
    "."
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
    "."
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
    "."
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
    "."
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
    "."
    "You got: -20 Energy, +0 Social, +0 Readiness, -20 Focus"

    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack