# =========================================================
# 6 AM: ACTION
# =========================================================

# --- 1. SLEEP MORE ---
label act6amSleepPass:
    $ Energy += 20
    $ Social += 0
    $ Readiness += 0
    $ Focus += 10
    $ currentTime += 2
    
    scene bedroom with dissolve
    "Eliza slept in for another hour and woke up feeling refreshed!"
    "She's super ready now for the long day ahead >w<"
    "You got:+20 Energy, +0 Social, +0 Readiness, +10 Focus"

    scene bedroom at bgSize
    show eliza fb sleepneutral at fbSpriteSize with fade
    jump goBack

label act6amSleepFail:
    $ Energy -= 10
    $ Social += 0
    $ Readiness += 0
    $ Focus -= 10
    $ currentTime += 2
    
    scene bedroom with dissolve
    "Eliza had a nightmare that she failed her test today..."
    "Oops, maybe she shouldn't have slept again!"
    "You got: -10 Energy, +0 Social, +0 Readiness, -10 Focus"

    scene bedroom at bgSize
    show eliza fb sleepneutral at fbSpriteSize with fade
    jump goBack


# --- 2. CALL KRISTEN ---
label act6amKristenPass:
    $ Energy += 10
    $ Social += 20
    $ Readiness += 0
    $ Focus -= 10
    $ currentTime += 2
    
    scene callroom with fade
    "Eliza calls Kristen"
    "{shader=wave}*riiiiiing riiiiiing*{/shader}"
    show eliza sleepsmileteeth at elizaSize with dissolve 
    show kristen sleepsmilenoteeth at npcSize with dissolve
    k "Heyyy Eliza!"
    show eliza sleeplovesmilepray at elizaSize
    show kristen sleepsmileteeth at npcSize
    e "Good morning Kristen! Whatcha doing?"
    show eliza sleepsmileteeth at elizaSize
    show kristen sleephehehe at npcSize
    k "I just fed my hamsters. And I’m probably going to go shower and watch something"
    show kristen sleepsmileteeth at npcSize
    show eliza sleeplovesmilepray at elizaSize
    e "Awwww so cute! What did you feed them?"
    show eliza sleepsmileteeth at elizaSize
    show kristen sleepmouthopen at npcSize
    k "Some lettuce and a small piece of banana as a treat"
    show kristen sleepsmileteeth at npcSize
    show eliza sleepexcited at elizaSize
    e "Oh thats cool!"
    show kristen sleepscared at npcSize
    show eliza sleepneutral at elizaSize
    k "Yeah, okay I’m gonna go shower before my Mom shouts at me..."
    show kristen sleepsmilenoteeth at npcSize
    show eliza sleepsmileteeth at elizaSize
    k "I’ll see you later at school!!"
    show kristen sleepsmileteeth at npcSize
    show eliza sleeplovesmilepray at elizaSize
    e "Ok, have fun! Bye!!!"
    hide kristen sleepsmileteeth with dissolve 
    hide eliza sleeplovesmilepray with dissolve 
    "Calling Kristen BOOSTED your energy!! :D"
    "You got: +10 Energy, +20 Social, +0 Readiness, -10 Focus"

    scene bedroom at bgSize
    show eliza fb sleepneutral at fbSpriteSize with fade
    jump goBack

label act6amKristenFail:
    $ Energy -= 20
    $ Social -= 20
    $ Readiness += 0
    $ Focus -= 10
    $ currentTime += 2
    
    scene callroom with fade
    "Eliza calls Kristen"
    "{shader=wave}*riiiiiing riiiiiing*{/shader}"
    show eliza sleeplovesmilepray at elizaSize with dissolve
    show kristen sleepmad at npcSize with dissolve
    e "Hey Kristen!!!"
    show eliza sleepneutral at elizaSize
    show kristen sleeppissed at npcSize
    k "WHAT..."
    show eliza sleepembarrassed at elizaSize
    show kristen sleepmad at npcSize
    e "Oh... sorry were you sleeping?"
    show eliza sleepshockedeyesclosed at elizaSize
    show kristen sleeppissed at npcSize
    k "Yeah I WAS until you woke me up"
    show eliza sleepdistraught at elizaSize
    show kristen sleepmad at npcSize
    e "Sorry, I'll go now..."
    show eliza sleepdistraught at elizaSize
    show kristen sleeppissed at npcSize
    k "Yeah you better go"
    hide kristen sleeppissed with dissolve
    hide eliza sleepdistraught with dissolve
    "Calling Kristen made her mad at you... :("
    "You got: -20 Energy, -20 Social, +0 Readiness, -10 Focus"

    scene bedroom at bgSize
    show eliza fb sleepneutral at fbSpriteSize with fade
    jump goBack


# --- 3. EARLY STUDY ---
# Requirements: Energy >= 20
label act6amStudyPass:
    $ Energy -= 20
    $ Social += 0
    $ Readiness += 20
    $ Focus += 20
    $ currentTime += 2
    
    scene bedroom with dissolve
    "Early studying did her very well!"
    "Eliza locked in and managed to get through 3 practice tests in the morning"
    "What a clever little ducky she is."
    "You got: +20 Energy, +0 Social, +0 Readiness, +10 Focus"

    scene bedroom at bgSize
    show eliza fb sleepneutral at fbSpriteSize with fade
    jump goBack

label act6amStudyFail:
    $ Energy -= 10
    $ Social += 0
    $ Readiness += 0
    $ Focus -= 20
    $ currentTime += 2
    
    scene bedroom with dissolve
    "Eliza got distracted and she ended up doodling in her dictionary..."
    "Yikes! How's she going to bring that in the exam for later?"
    "You got: +10 Energy, +0 Social, +0 Readiness, -10 Focus"

    scene bedroom at bgSize
    show eliza fb sleepneutral at fbSpriteSize with fade
    jump goBack


# --- 4. STALK THOMAS ONLINE ---
# Requirements: Energy >= 10
label act6amThomasPass:
    $ Energy -= 10
    $ Social += 20
    $ Readiness += 0
    $ Focus -= 10
    $ currentTime += 2
    
    scene bedroom with dissolve
    "Eliza found Thomas’ instagram account! Now they're friends online"
    "She's one step closer to dating him! Yahooo :D"
    "You got: -10 Energy, +20 Social, +0 Readiness, -10 Focus"

    scene bedroom at bgSize
    show eliza fb sleepneutral at fbSpriteSize with fade
    jump goBack

label act6amThomasFail:
    $ Energy -= 20
    $ Social -= 10
    $ Readiness += 0
    $ Focus -= 10
    $ currentTime += 2
    
    scene bedroom with dissolve
    "Eliza spent 30 minutes trying to find Thomas’ account on Instagram.."
    "but she couldn’t find him, now her phone died!! (° O °)"
    "You got: -20 Energy, -10 Social, +0 Readiness, -10 Focus"

    scene bedroom at bgSize
    show eliza fb sleepneutral at fbSpriteSize with fade
    jump goBack