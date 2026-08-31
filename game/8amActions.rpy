#==========================================================
# 8 AM: ACTION CUTSCENES
# =========================================================

# --- 1. GO TO SCHOOL ---
label act8amSchoolPass:
    $ Energy += 0
    $ Social += 0
    $ Readiness += 0
    $ Focus += 10
    $ currentTime += 1
    
    scene school front with dissolve
    "Eliza caught the early train!"
    "She managed to get a seat, and now she's happy"
    "You got:+0 Energy, +0 Social, +0 Readiness, +10 Focus"

    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack

label act8amSchoolFail:
    $ Energy -= 10
    $ Social += 0
    $ Readiness += 0
    $ Focus -= 10
    $ currentTime += 1
    
    scene school front with dissolve
    "Eliza just missed her train... and it was delayed by 20 mins.."
    "The train was so full she couldn't sit!!"
    "You got: -10 Energy, +0 Social, +0 Readiness, -10 Focus"

    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize with fade
    jump goBack