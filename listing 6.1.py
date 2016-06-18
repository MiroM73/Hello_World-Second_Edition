import easygui
flavor = easygui.buttonbox(msg='What is your favorite ice cream vlavour?',
                           choices=['Vanilla','Chocolate','Strawberry'])
easygui.msgbox(msg='You picked ' + flavor)
