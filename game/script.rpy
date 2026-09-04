#script for the game goes here!
# Global Variables
default persistent_study_notes = ""
default player_answer = ""
default ai_question = ""

transform bgSize: 
    #makes the background the perfect size in the middle
    zoom 0.8
    xanchor 0.5
    xpos 0.5
    yanchor 0.5  
    ypos 0.5 

# Input Notes Screen Definition
screen input_notes_screen():
    modal True
    add "classroom" at bgSize
    add "#3f3b3b41" # Optional dark overlay for contrast

    frame:
        xalign 0.5
        yalign 0.5
        padding (40, 30)
        xsize 1100              # Expanded main frame width
        ysize 650               # Added fixed height for scale
        background "#ffffff"

        vbox:
            spacing 25
            text "Paste or enter your study notes below:" color "#553a3a" size 32 xalign 0.5

            frame:
                xsize 1020      # Expanded inner box width
                ysize 420       # Expanded inner box height
                background "#ffe9f3"
                padding (20, 20)

                hbox:
                    spacing 15

                    viewport id "notes_vp":
                        mousewheel True
                        draggable True

                        input:
                            value VariableInputValue("persistent_study_notes")
                            length 2000
                            size 24     # Increased text font size
                            color "#694e4e"
                            multiline True

                    vbar:
                        value YScrollValue("notes_vp")
                        xsize 16        # Made scrollbar wider to match
                        base_bar Frame(Solid("#e8d8d8"), 0, 0)
                        thumb Frame(Solid("#b58294"), 0, 0)
                        hover_thumb Frame(Solid("#dfa0ba"), 0, 0)

            hbox:
                xalign 0.5
                spacing 30      # More breathing room between buttons

                textbutton "Paste Notes":
                    padding (25, 12)
                    text_size 24
                    background "#dbe8eb"
                    hover_background "#ebf2f6"
                    text_color "#4a3939"
                    action Function(paste_clipboard_to_notes)

                textbutton "Start Game":
                    padding (25, 12)
                    text_size 24
                    background "#ffe6ef"
                    hover_background "#fde2f0"
                    text_color "#4a3939"
                    action Return()

#====================================================================================================================================================================================================

#====================================================================================================================================================================================================

#so theres no random fade??
define config.window_show_transition = None
define config.window_hide_transition = None

#declairing the characters
define e = Character("Eliza", color="#da88aa") 
define k = Character("Kristen", color="#8858b0") 
define t = Character("Thomas", color="#39547c") 

#function to help the sprites scale down 
transform pinkBgSize:
    zoom 100
transform fbSpriteSize: 
    #makes it smaller since image is very big
    zoom 0.5 
    xpos 0.04
transform elizaFbSize: 
    zoom 0.5
transform elizaSize:
    zoom 0.2
    ypos 0.14
    xpos 0.04
transform npcSize:
    zoom 0.28
    ypos 0.15
    xpos 0.69
transform npc2Size:
    zoom 0.3
    ypos 0.1
    xpos 0.63
transform buttonSize: 
    zoom 0.6
    align (0.5, 0.5)

#perfect place for the x
transform xSize:
    zoom 0.45
    xpos 0.708
    ypos 0.2488
transform clockSize:
    zoom 0.32 #dont change!!
    xanchor -1
    xpos 0.73    
    yanchor 0.5  
    ypos 0.65
transform barSize:
    zoom 0.6
    xpos 0.07
transform actionSize:
    zoom 0.35

#---------------------------------------------------------------------------------------------------------
#TIME AND STATS

#trakcs statistics
default Energy = 90
default Social = 50
default Readiness = 10
default Focus = 10
default currentTime = 6
default selectedAction = "" #to choose the action



#main menu with all the stats, buttons, ect
screen cs_mainmenu(): 

    # Chaning clock display
    $ pm_time = currentTime - 12
    if currentTime <= 11:
        add "[currentTime]am" at clockSize
    elif currentTime == 12:
        add "12pm" at clockSize
    else:
        add "[pm_time]pm" at clockSize

    #BAR STATS
    vbox:
        xpos 690   
        ypos 150             
        spacing 15

        hbox:
            spacing 10
            text "Energy       " size 30 color "#3a2b2b"
            add "[Energy]bar" at barSize

        hbox:
            spacing 10
            text "Readiness" size 30 color "#3a2b2b"
            add "[Readiness]bar" at barSize

        hbox:
            spacing 10
            text "Social          " size 30 color "#3a2b2b"
            add "[Social]bar" at barSize

        hbox:
            spacing 10
            text "Focus          " size 30 color "#3a2b2b"
            add "[Focus]bar" at barSize


    #resizes it to be in the right place 
    vbox: 
        xalign 0.55
        yalign 0.7
        spacing 40

        #shows the buttons on the UI
        imagebutton at buttonSize: 
            idle "actions"
            hover "actions_hvr" #changed the colour when hovering 
            action Show("actionsPopup") #brings user to label

        imagebutton at buttonSize:
            idle "relationships"
            hover "relationships_hvr"
            action Show("rsPopup")
        
        imagebutton at buttonSize:
            idle "learnings"
            hover "learnings_hvr"
            action Show("learningsPopup")


transform charShake:
    linear 0.05 xoffset 15
    linear 0.05 xoffset -15
    linear 0.05 xoffset 10
    linear 0.05 xoffset -10
    linear 0.05 xoffset 5
    linear 0.05 xoffset -5
    linear 0.05 xoffset 0
    zoom 0.2
    ypos 0.14
    xpos 0.04
    

#---------------------------------------------------------------------------------------------------------------



#--------
screen rsPopup():
    modal True #so that you can't interact outside of it
    add "relationships_pop" at buttonSize

    imagebutton at xSize:
        idle "x"
        hover "x_hvr"
        action Hide("rsPopup")
#--------
screen learningsPopup():
    modal True #so that you can't interact outside of it
    add "learnings_pop" at buttonSize
    text "Sorry! \n Nothing to see here! :)":
        align (0.5, 0.5)
        size 50
        color "#3d2727" # dark text for contrast

    imagebutton at xSize:
        idle "x"
        hover "x_hvr"
        action Hide("learningsPopup")

define config.default_textshader = "typewriter"

#-----------------------------------------------------------------------------------DAMAGE CONTROL
#====================================================================================================





# This is so that all the actions can be seen 
screen actionsPopup():
    modal True # so that you can't interact outside of it
    
    # The background image (like the other pop ups)
    add "actions_pop" at buttonSize

    # So that it can close using the x 
    imagebutton at xSize: # makes the x button
        idle "x"
        hover "x_hvr"
        action Hide("actionsPopup") # hides the pop up

# Action buttons placement being in 2x2 
    grid 2 2 at actionSize:
        xalign 0.5
        yalign 0.55   
        spacing 40   

        # 6 AM Actions
        if currentTime == 6:
            imagebutton idle "6amstudy" hover "6amstudy_hvr" action [SetVariable("selectedAction", "6amStudy"), Hide("actionsPopup"), Jump("triggerAiAction")]
            imagebutton idle "6amkristen" hover "6amkristen_hvr" action [SetVariable("selectedAction", "6amKristen"), Hide("actionsPopup"), Jump("triggerAiAction")]
            imagebutton idle "6amsleep" hover "6amsleep_hvr" action [SetVariable("selectedAction", "6amSleep"), Hide("actionsPopup"), Jump("triggerAiAction")]
            imagebutton idle "6amthomas" hover "6amthomas_hvr" action [SetVariable("selectedAction", "6amThomas"), Hide("actionsPopup"), Jump("triggerAiAction")]

        # 8 AM Actions
        elif currentTime == 8:
            imagebutton idle "8amschool" hover "8amschool_hvr" action [SetVariable("selectedAction", "8amSchool"), Hide("actionsPopup"), Jump("triggerAiAction")]
            null
            null
            null

        # 9 AM Actions
        elif currentTime == 9:
            imagebutton idle "9amstudy" hover "9amstudy_hvr" action [SetVariable("selectedAction", "9amStudy"), Hide("actionsPopup"), Jump("triggerAiAction")]
            imagebutton idle "9amkristen" hover "9amkristen_hvr" action [SetVariable("selectedAction", "9amKristen"), Hide("actionsPopup"), Jump("triggerAiAction")]
            imagebutton idle "9amthomas" hover "9amthomas_hvr" action [SetVariable("selectedAction", "9amThomas"), Hide("actionsPopup"), Jump("triggerAiAction")]
            null

        # 10 AM Actions
        elif currentTime == 10:
            imagebutton idle "10amkristen" hover "10amkristen_hvr" action [SetVariable("selectedAction", "10amKristen"), Hide("actionsPopup"), Jump("triggerAiAction")]
            imagebutton idle "10amstudy" hover "10amstudy_hvr" action [SetVariable("selectedAction", "10amStudy"), Hide("actionsPopup"), Jump("triggerAiAction")]
            imagebutton idle "10amthomas" hover "10amthomas_hvr" action [SetVariable("selectedAction", "10amThomas"), Hide("actionsPopup"), Jump("triggerAiAction")]
            null

        # 11 AM Actions
        elif currentTime == 11:
            imagebutton idle "11amkristen" hover "11amkristen_hvr" action [SetVariable("selectedAction", "11amKristen"), Hide("actionsPopup"), Jump("triggerAiAction")]
            imagebutton idle "11amstudy" hover "11amstudy_hvr" action [SetVariable("selectedAction", "11amStudy"), Hide("actionsPopup"), Jump("triggerAiAction")]
            imagebutton idle "11amthomas" hover "11amthomas_hvr" action [SetVariable("selectedAction", "11amThomas"), Hide("actionsPopup"), Jump("triggerAiAction")]
            null

        # 12 PM Actions
        elif currentTime == 12:
            imagebutton idle "12pminsta" hover "12pminsta_hvr" action [SetVariable("selectedAction", "12pmInsta"), Hide("actionsPopup"), Jump("triggerAiAction")]
            imagebutton idle "12pmkristen" hover "12pmkristen_hvr" action [SetVariable("selectedAction", "12pmKristen"), Hide("actionsPopup"), Jump("triggerAiAction")]
            imagebutton idle "12pmstudy" hover "12pmstudy_hvr" action [SetVariable("selectedAction", "12pmStudy"), Hide("actionsPopup"), Jump("triggerAiAction")]
            null

        # 1 PM Actions
        elif currentTime == 13:
            imagebutton idle "1pmkristen" hover "1pmkristen_hvr" action [SetVariable("selectedAction", "1pmKristen"), Hide("actionsPopup"), Jump("triggerAiAction")]
            imagebutton idle "1pmnap" hover "1pmnap_hvr" action [SetVariable("selectedAction", "1pmNap"), Hide("actionsPopup"), Jump("triggerAiAction")]
            imagebutton idle "1pmstudy" hover "1pmstudy_hvr" action [SetVariable("selectedAction", "1pmStudy"), Hide("actionsPopup"), Jump("triggerAiAction")]
            null

        # 2 PM Actions
        elif currentTime == 14:
            imagebutton idle "2pmcram" hover "2pmcram_hvr" action [SetVariable("selectedAction", "2pmCram"), Hide("actionsPopup"), Jump("triggerAiAction")]
            imagebutton idle "2pmkristen" hover "2pmkristen_hvr" action [SetVariable("selectedAction", "2pmKristen"), Hide("actionsPopup"), Jump("triggerAiAction")]
            imagebutton idle "2pmthomas" hover "2pmthomas_hvr" action [SetVariable("selectedAction", "2pmThomas"), Hide("actionsPopup"), Jump("triggerAiAction")]
            null


#RESULT TEST POPUP
# RESULT TEST POPUP
screen resultTestPopup():
    modal True
    add "#e0d0d0ff"

    frame:
        xalign 0.5
        yalign 0.5
        padding (40, 30)
        xsize 1100              # Expanded frame width
        background "#ffffff"

        vbox:
            spacing 25

            text "[ai_question]" xalign 0.5 size 26 color "#000000" text_align 0.5

            frame:
                xalign 0.5
                xsize 1020      # Expanded input box width
                ysize 120       # Expanded height for multiline text support
                background "#2a2a38"
                padding (15, 15)

                viewport id "answer_vp":
                    mousewheel True
                    draggable True

                    input:
                        value VariableInputValue("player_answer")
                        length 300
                        size 22
                        color "#f7efef"
                        multiline True

            # Buttons Row
            hbox:
                xalign 0.5
                spacing 30

                # Paste Button
                textbutton "Paste":
                    padding (25, 12)
                    text_size 24
                    background "#a8bfc5"
                    hover_background "#cfdbe0"
                    text_color "#4a3939"
                    action Function(paste_clipboard_to_answer)

                # Submit Button
                textbutton "Submit Answer":
                    padding (25, 12)
                    text_size 24
                    background "#ffd4e4"
                    hover_background "#fde2f0"
                    text_color "#4a3939"
                    action [
                        Hide("resultTestPopup"),
                        Jump("evaluateActionAnswer")
                    ]

#====================================================================================================
#-------------------------------------------------------------------------------------------------------------------
label start:
    # 1. Ask player to enter/paste notes first
    call screen input_notes_screen

    # Fallback default text if they didn't paste anything
    if persistent_study_notes.strip() == "":
        $ persistent_study_notes = "Photosynthesis is the process used by plants to convert light energy into chemical energy."

    # Intro sequence
    scene bedroom at bgSize with fade
    "6:00 AM..."
    show eliza sleepshockedeyesclosed at elizaSize with dissolve
    e "ughhh i'm so tired.. is it 6 already?"
    e "..."
    show eliza sleepdistraught at charShake
    e "OH MY GOSH I HAVE MY EXAM TODAY!!"
    show eliza sleepshocked
    e "I really need to study"
    show eliza sleepshockedeyesclosed
    e "but I REALLY don't want to..!"
    e "I wonder what I should do..."
    hide eliza sleepshockedeyesclosed with dissolve
    ""
    "Welcome to   {shader=wave}Exam Sheets & Heartbeats!{/shader}"
    "Can you help Eliza prepare for her exam today at 3?"
    "Goodluck!"

    # Main game loop
    scene bedroom at bgSize
    show eliza fb sleepneutral at fbSpriteSize
    call screen cs_mainmenu with fade
    

#==========MAIN MENU THINGY
    scene bedroom at bgSize
    show eliza fb sleepneutral at fbSpriteSize



    call screen cs_mainmenu with fade
    




    #STAT CHECKER - END GAME OR PAUSE AT 100
    
    label goBack:
    # cap so that it doesn't exceed 100
    $ Energy = min(100, Energy)
    $ Readiness = min(100, Readiness)
    $ Social = min(100, Social)
    $ Focus = min(100, Focus)

    # chacks if the stats go bellow 0 cuz then it ends the game
    if Energy < 0 or Readiness < 0 or Social < 0 or Focus < 0:
        jump gameOver

    # ends the game at 3 (Exam time)
    if currentTime >= 15:
        jump finalExam_scene
    else:
        call screen cs_mainmenu


    label gameOver:
        show expression Solid("#2b2a2aff")
        "Eliza completely burned out before taking her exam..."
        "GAME OVER"
        return  # Returns to main menu title screen


label gameEnd:
    scene solid pink at pinkBgSize with dissolve
    "The exam at 3 begins...!!"

    if Energy <= 20:
        show eliza distraught at elizaSize with dissolve
        "Eliza is super tired...!"
        "Halfway through question three, her head hits the desk and she passes out!"
    elif Focus <= 20:
        show eliza shocked at elizaSize with dissolve
        "Oh no, Eliza can't focus at all!"
        "Every tiny noise in the room distracts her. Hmmm, what colour is pikachu's tail again?"
    elif Social <= 20:
        show eliza embarrassed at elizaSize with dissolve
        "Eliza feels super embarassed with all her terrible relationships..."
        "Thinking about what will happen after the test makes her so nervous!!"
    elif Readiness <= 20:
        show eliza distraught at elizaSize with dissolve
        "Eliza flips through the exam pages in panic..."
        "None of these topics look familiar! She's forced to blindly guess on every single question."
    else:
        show eliza blushsmile at elizaSize with dissolve
        "Eliza takes a deep breath before opening the paper..."
        "...."
        "Oh, she knows these topics!"

    # 2. OVERALL SCORE EVALUATION
    $ totalScore = Energy + Focus + Social + Readiness

    if totalScore >= 200 and Readiness >= 50:
        show eliza excited at elizaSize with dissolve
        "BEST ENDING: She managed to concentrate and get through it!!"
        "Eliza got a A+ on her test :DDDD"

    elif totalScore >= 120:
        show eliza smilenoteeth at elizaSize with dissolve
        "GOOD ENDING: Passed!"
        "It wasn't a perfect day, but Eliza still managed to get a passing grade anyways!"

    else:
        show eliza distraught at elizaSize with dissolve
        "BAD ENDING: Exam Failed..."
        "NOOOOO....."
        "Eliza failed her exam, now she's very sad :("

    "--- GAME OVER ---"
    return

