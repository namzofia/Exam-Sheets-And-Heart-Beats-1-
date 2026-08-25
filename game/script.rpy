#script for the game goes here!

#so theres no random fade??
define config.window_show_transition = None
define config.window_hide_transition = None

#declairing the characters
define e = Character("Eliza", color="#da88aa") 
define k = Character("Kristen", color="#8858b0") 
define t = Character("Thomas", color="#39547c") 

#function to help the sprites scale down 
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
transform buttonSize: 
    zoom 0.6
    align (0.5, 0.5)
transform bgSize: 
    #makes the background the perfect size in the middle
    zoom 0.8
    xanchor 0.5  
    xpos 0.5     
    yanchor 0.5  
    ypos 0.5 
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
    ypos 0.5 

#---------------------------------------------------------------------------------------------------------
#TIME AND STATS

#trakcs statistics
default Energy = 90
default Social = 50
default Readiness = 10
default Focus = 10
default current_time = 6




#main menu with all the stats, buttons, ect
screen cs_mainmenu(): 

    # Chaning clock display
    if current_time <= 11:
        add "[current_time]am" at clockSize
    elif current_time == 12:
        add "12pm"  at clockSize
    else:
        add "[pm_time]pm" at clockSize

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

#this is where all the actions can be seen
screen actionsPopup():
    modal True #so that you can't interact outside of it
    add "actions_pop" at buttonSize

    imagebutton at xSize: #makes the x button 
        idle "x"
        hover "x_hvr"
        action Hide("actionsPopup") #hides the pop up
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

#-------------------------------------------------------------------------------------------------------------------
label start: 

#==========CHARACTER INTRO - ELIZA WALTON 


#==========INTRO SCENE
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
    

#==========MAIN MENU THINGY
    scene bedroom at bgSize
    show eliza fb sleepneutral at fbSpriteSize



    call screen cs_mainmenu with fade
    
    return