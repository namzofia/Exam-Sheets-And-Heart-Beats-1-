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

#main menu with all the stats, buttons, ect
screen mainmenu(): 
    #resizes it to be in the right place 
    vbox: 
        xalign 0.55
        yalign 0.7
        spacing 40

        #shows the buttons on the UI
        imagebutton  at buttonSize: 
            idle "actions"
            hover "actions_hvr" #changed the colour when hovering 
            action Jump("actionsMenu") #brings user to label

        imagebutton  at buttonSize:
            idle "relationships"
            hover "relationships_hvr"
            action Jump("rsMenu")
        
        imagebutton  at buttonSize:
            idle "learnings"
            hover "learnings_hvr"
            action Jump("learningsMenu")



label start: 
    scene classroom at bgSize
    show eliza fb neutral at fbSpriteSize

    call screen mainmenu

label actionsMenu:
    "You opened the Actions menu!"
label rsMenu:
    "You opened the Relationships menu!"
label learningsMenu:
    "You opened the Learnings menu!"

#dialogue lines!!
    #e "Nice to meet you"

    return