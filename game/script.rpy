#script for the game goes here!

#declairing the characters
define e = Character("Eliza", color="#F8C8DC") 
define k = Character("Kristen", color="#cfb6e4") 
define t = Character("Thomas", color="#abc4ea") 

#function to help the sprites scale down 
transform fbSpriteSize: 
    #makes it smaller since image is very big
    zoom 0.5 
    xpos 0.04
transform spriteSize: 
    zoom 0.5
transform buttonSize: 
    zoom 0.6
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



#main menu with all the stats, buttons, ect
screen cs_mainmenu(): 
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

#---------------------------------------------------------------------------------------------------------------

#this is where all the actions can be seen
screen actionsPopup():
    modal True #so that you can't interact outside of it
    add "actions_pop" align (0.5, 0.5) at buttonSize

    imagebutton at xSize: #makes the x button 
        idle "x"
        hover "x_hvr"
        action Hide("actionsPopup") #hides the pop up
#--------
screen rsPopup():
    modal True #so that you can't interact outside of it
    add "relationships_pop" align (0.5, 0.5) at buttonSize

    imagebutton at xSize:
        idle "x"
        hover "x_hvr"
        action Hide("rsPopup")
#--------
screen learningsPopup():
    modal True #so that you can't interact outside of it
    add "learnings_pop" align (0.5, 0.5) at buttonSize
    text "Sorry! \n Nothing to see here! :)":
        align (0.5, 0.5)
        size 50
        color "#3d2727" # dark text for contrast

    imagebutton at xSize:
        idle "x"
        hover "x_hvr"
        action Hide("learningsPopup")

#-------------------------------------------------------------------------------------------------------------------
label start: 
    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize

    call screen cs_mainmenu

    return