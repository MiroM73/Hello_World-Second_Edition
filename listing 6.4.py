import easygui
flavor = easygui.enterbox('What is your favorite ice cream vlavour?',
                          default = 'Vanilkova')
easygui.msgbox(msg='You picked ' + flavor)
