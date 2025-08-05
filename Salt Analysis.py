from tkinter import *

root = Tk()
root.geometry("%dx%d+%d+%d" % (1000, 1000, 2000, 150))
root.title('Salt Analysis')
def test():
    global testforanionframe
    global testforcationframe
    global testforanionframe
    global resultframe
    global possibleanionlist
    global everythingframe
    try:
        everythingframe.pack_forget()
    except:
        pass
    
    everythingframe=Frame(root)
    everythingframe.pack()
    
    
    def testforanion():
        global testforanionframe
        global possibleanionlist
        try:
            testforanionframe.pack_forget()
        except:
            pass
        try:
            testforcationframe.pack_forget()
        except:
            pass
        testforanionframe=Frame(everythingframe)
        testforanionframe.pack()
        global resultframe
        def testy():
            global resultframe
            global anionresultframe
            try:
                anionresultframe.pack_forget()
            except:
                pass
            anionresultframe=Frame(resultframe)
            anionresultframe.pack()
            #['C03','SO4','Cl','Br','I','NO3']
            bacltest=test5var.get()
            agno3test=test6var.get()
            co3test=test8var.get()
            brownringtest=test9var.get()
            resultlist=[bacltest,agno3test,co3test,brownringtest]
            if len(resultlist) != 4:
                errorlabel=Label(anionresultframe,text='All Compulsory Test not performed', fg='red')
                errorlabel.pack()
            lstresultlist=[]
            for a in resultlist:
                if a != 'nil':
                    lstresultlist.append(a)
            
            print(lstresultlist)#REMOVE REMOVE REMOVE
            if len(lstresultlist) != 1:
                errorlabel=Label(anionresultframe,text='Test for Anion not Done Properly', fg='red')
                errorlabel.pack()
            else:
                anionresultreport='The Anion is '+lstresultlist[0]
                anionresultlabel=Label(anionresultframe,text=anionresultreport, fg='green')
                anionresultlabel.pack()
            


            
        

        canvas = Canvas(testforanionframe, width=650, height=600)
        scroll_y = Scrollbar(testforanionframe, orient="vertical", command=canvas.yview)
        frameforscrollanion = Frame(canvas)
        
        #TEST 1
        test1frame=Frame(frameforscrollanion)
        test1frame.pack()
        
        test1label= Label(test1frame, text='Solubility Test', fg='blue',font= "applecherry 20")
        test1label.pack()
        pro='In a Testube add Salt and Water\n'
        test1proceduce= Label(test1frame,text=pro)
        test1proceduce.pack()

        test1var = IntVar()
    
        radiobtn1 = Radiobutton(test1frame) 
        radiobtn1.config(text='Soluble', variable=test1var, value=1)    
        radiobtn1.pack()

        radiobtn2 = Radiobutton(test1frame)
        radiobtn2.config(text='Insoluble', variable=test1var, value=0)    
        radiobtn2.pack()

        #TEST 2
        test2frame=Frame(frameforscrollanion)
        test2frame.pack()
        test2label= Label(test2frame, text='\n\nSalt + Dilute H2SO4', fg='blue',font= "applecherry 20")
        test2label.pack()
        pro2='In a Testube add Salt and Dilute H2SO4\n'
        test2proceduce= Label(test2frame,text=pro2)
        test2proceduce.pack()

        test2var = IntVar()
    
        radiobtn21 = Radiobutton(test2frame) 
        radiobtn21.config(text='Brisk Effervescence of CO2', variable=test2var, value=1)    
        radiobtn21.pack()

        radiobtn22 = Radiobutton(test2frame)
        radiobtn22.config(text='No Effervescence', variable=test2var, value=0)    
        radiobtn22.pack()

        #TEST 3
        test3frame=Frame(frameforscrollanion)
        test3frame.pack()
        test3label= Label(test3frame, text='\n\nSalt + Conc H2SO4 and Heat', fg='blue',font= "applecherry 20")
        test3label.pack()
        pro3='In a Testube orginal salt andadd Conc H2SO4 and Heat\n'
        test3proceduce= Label(test3frame,text=pro3)
        test3proceduce.pack()

        test3var = StringVar()
    
        radiobtn31 = Radiobutton(test3frame) 
        radiobtn31.config(text='Colorless gas with Pungent smell\ndense white fumes with \nglass rod dipped in ammonia solution ', variable=test3var, value=['cl'])    
        radiobtn31.pack(side=LEFT)

        radiobtn32 = Radiobutton(test3frame)
        radiobtn32.config(text='Brown Fumes', variable=test3var, value=['NO3','Br'])    
        radiobtn32.pack(side=LEFT)

        radiobtn33 = Radiobutton(test3frame)
        radiobtn33.config(text='Violet Vapours', variable=test3var, value=['I'])    
        radiobtn33.pack(side=LEFT)
        
        radiobtn34 = Radiobutton(test3frame)
        radiobtn34.config(text='None of Above', variable=test3var, value='nil')    
        radiobtn34.pack(side=LEFT)
        
        #TEST 4
        test4frame=Frame(frameforscrollanion)
        test4frame.pack()
        test4label= Label(test4frame, text='\n\nSalt + Conc H2SO4 + Cu Turnings and Heat', fg='blue',font= "applecherry 20")
        test4label.pack()
        pro4='In a Testube add original salt and Conc H2SO4  and Cu Turnings and Heat\n'
        test4proceduce= Label(test4frame,text=pro4)
        test4proceduce.pack()

        test4var = StringVar()
    
        radiobtn41 = Radiobutton(test4frame) 
        radiobtn41.config(text='Intense Brown Fumes', variable=test4var, value=['NO3'])    
        radiobtn41.pack()

        radiobtn42 = Radiobutton(test4frame)
        radiobtn42.config(text='No Brown Fumes', variable=test4var, value='nil')    
        radiobtn42.pack()

        #TEST 5
        test5frame=Frame(frameforscrollanion)
        test5frame.pack()
        
        test5label= Label(test5frame, text='\n\nS04 Test  *', fg='blue',font= "applecherry 20")
        test5label.pack()
        pro5='In a Testube add Orginal Solution and Bacl2 Solution\nIn a Testube add Orginal Solution and Lead Accetate Solution'
        test5proceduce= Label(test5frame,text=pro5)
        test5proceduce.pack()

        test5var = StringVar()
    
        radiobtn51 = Radiobutton(test5frame) 
        radiobtn51.config(text='White Precipitate', variable=test5var, value=['SO4'])    
        radiobtn51.pack()

        radiobtn52 = Radiobutton(test5frame)
        radiobtn52.config(text='No White Precipitate', variable=test5var, value='nil')    
        radiobtn52.pack()

        #TEST 6
        test6frame=Frame(frameforscrollanion)
        test6frame.pack()
        test6label= Label(test6frame, text='\n\nSalt Solution+ AgNo3 Solution  *', fg='blue',font= "applecherry 20")
        test6label.pack()
        pro6='In a Testube add Orginal Solution and AgNo3 Solution\n'
        test6proceduce= Label(test6frame,text=pro6)
        test6proceduce.pack()

        test6var = StringVar()
    
        radiobtn61 = Radiobutton(test6frame) 
        radiobtn61.config(text='Curdy White ppt', variable=test6var, value=['Cl'])    
        radiobtn61.pack(side=LEFT)

        radiobtn62 = Radiobutton(test6frame)
        radiobtn62.config(text='Pale Yellow ppt', variable=test6var, value=['Br'])    
        radiobtn62.pack(side=LEFT)

        radiobtn63 = Radiobutton(test6frame)
        radiobtn63.config(text='Dark Yellow ppt', variable=test6var, value=['I'])    
        radiobtn63.pack(side=LEFT)

        radiobtn64 = Radiobutton(test6frame)
        radiobtn64.config(text='None of Above', variable=test6var, value='nil')    
        radiobtn64.pack(side=LEFT)

        #TEST 7
        test7frame=Frame(frameforscrollanion)
        test7frame.pack()
        test7label= Label(test7frame, text='\n\nChromyl Chloride Test', fg='blue',font= "applecherry 20")
        test7label.pack()
        pro7='In a Testube add original salt and Conc H2SO4  and Pottasium Dichromate and Heat\n'
        test7proceduce= Label(test7frame,text=pro7)
        test7proceduce.pack()

        test7var = StringVar()
    
        radiobtn71 = Radiobutton(test7frame) 
        radiobtn71.config(text='Orange Red Fumes', variable=test7var, value=['Cl'])    
        radiobtn71.pack()

        radiobtn72 = Radiobutton(test7frame)
        radiobtn72.config(text='No Orange Red Fumes', variable=test7var, value='nil')    
        radiobtn72.pack()

        #TEST 8
        test8frame=Frame(frameforscrollanion)
        test8frame.pack()
        test8label= Label(test8frame, text='\n\nConfirmatory Test for Carbonate  *', fg='blue',font= "applecherry 20")
        test8label.pack()
        pro8='In a Testube add original salt and MgSo4 Solution\n'
        test8proceduce= Label(test8frame,text=pro8)
        test8proceduce.pack()

        test8var = StringVar()
    
        radiobtn81 = Radiobutton(test8frame) 
        radiobtn81.config(text='White Precipitate', variable=test8var, value=['CO3'])    
        radiobtn81.pack()

        radiobtn82 = Radiobutton(test8frame)
        radiobtn82.config(text='No White Precipitate', variable=test8var, value='nil')    
        radiobtn82.pack()

        #TEST 9
        test9frame=Frame(frameforscrollanion)
        test9frame.pack()
        test9label= Label(test9frame, text='\n\nBrown Ring Test  *', fg='blue',font= "applecherry 20")
        test9label.pack()
        pro9='In a Testube add original salt and Fresh FeSo4 Solution and add Conc H2SO4 through sides of testtube\n'
        test9proceduce= Label(test9frame,text=pro9)
        test9proceduce.pack()

        test9var = StringVar()
    
        radiobtn91 = Radiobutton(test9frame) 
        radiobtn91.config(text='Brown Ring at Junction of 2 layers', variable=test9var, value=['NO3'])    
        radiobtn91.pack()

        radiobtn92 = Radiobutton(test9frame)
        radiobtn92.config(text='No Brown Ring', variable=test9var, value='nil')    
        radiobtn92.pack()
        
        submittestbtn = Button(frameforscrollanion, text="Submit", command=testy)
        submittestbtn.pack()
        
        canvas.create_window(0, 0, anchor='nw', window=frameforscrollanion)

        
        # make sure everything is displayed before configuring the scrollregion
        canvas.update_idletasks()

        canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scroll_y.set)
                 
        canvas.pack(fill='both', expand=True, side='left')
        scroll_y.pack(fill='y', side='right')


        
        
        root.mainloop()
    def testforcation():
        global testforcationframe
        global possiblecationlist
        try:
            testforanionframe.pack_forget()
        except:
            pass
        try:
            testforcationframe.pack_forget()
        except:
            pass
        testforcationframe=Frame(everythingframe)
        testforcationframe.pack()
        global resultframe
        def testy():
            global resultframe
            global cationresultframe
            try:
                cationresultframe.pack_forget()
            except:
                pass
            cationresultframe=Frame(resultframe)
            cationresultframe.pack()
            #['NH4','Pb','Cu','Al','Fe','Zn','Mn','Ni','Ca','Ba','Sr']
            nesslertest=test3var.get()
            pbtest=test6var.get()
            cutest=test9var.get()
            gr3test=test10var.get()
            gr4test=test13var.get()
            gr5test=test17var.get()

            resultlist=[nesslertest,pbtest,cutest,gr3test,gr4test,gr5test]

            lstresultlist=[]  
            for a in resultlist:
                if a != 'nil':
                    lstresultlist.append(a)
            
            print(lstresultlist)#REMOVE REMOVE REMOVE
            if len(lstresultlist) != 1:
                errorlabel=Label(cationresultframe,text='Test for Cation not Done Properly', fg='red')
                errorlabel.pack()
            else:
                cationresultreport='The Cation is '+lstresultlist[0]
                cationresultlabel=Label(cationresultframe,text=cationresultreport, fg='green')
                cationresultlabel.pack()

        canvas = Canvas(testforcationframe, width=650, height=600)
        scroll_y = Scrollbar(testforcationframe, orient="vertical", command=canvas.yview)
        frameforscrollcation = Frame(canvas)
        
        #TEST 1
        test1frame=Frame(frameforscrollcation)
        test1frame.pack()
        
        test1label= Label(test1frame, text='\nColor of Salt', fg='blue',font= "applecherry 20")
        test1label.pack()
        pro='Observe Color of Salt\n'
        test1proceduce= Label(test1frame,text=pro)
        test1proceduce.pack()

        test1var = IntVar()
    
        radiobtn11 = Radiobutton(test1frame) 
        radiobtn11.config(text='Blue', variable=test1var, value=1)    
        radiobtn11.pack(side=LEFT)

        radiobtn12 = Radiobutton(test1frame)
        radiobtn12.config(text='Buff', variable=test1var, value=0)    
        radiobtn12.pack(side=LEFT)

        radiobtn13 = Radiobutton(test1frame) 
        radiobtn13.config(text='Greenish Blue', variable=test1var, value=2)    
        radiobtn13.pack(side=LEFT)

        radiobtn14 = Radiobutton(test1frame)
        radiobtn14.config(text='Yellow', variable=test1var, value=3)    
        radiobtn14.pack(side=LEFT)

        radiobtn15 = Radiobutton(test1frame)
        radiobtn15.config(text='None of Above', variable=test1var, value=4)    
        radiobtn15.pack(side=LEFT)

        #TEST 2
        test2frame=Frame(frameforscrollcation)
        test2frame.pack()
        
        test2label= Label(test2frame, text='\nFlame Test', fg='blue',font= "applecherry 20")
        test2label.pack()
        pro2='Make paste of salt and show it to blue flame\n'
        test2proceduce= Label(test2frame,text=pro2)
        test2proceduce.pack()

        test2var = IntVar()
    
        radiobtn21 = Radiobutton(test2frame) 
        radiobtn21.config(text='Brick Red', variable=test2var, value=1)    
        radiobtn21.pack(side=LEFT)

        radiobtn22 = Radiobutton(test2frame)
        radiobtn22.config(text='Apple Green', variable=test2var, value=0)    
        radiobtn22.pack(side=LEFT)

        radiobtn23 = Radiobutton(test2frame) 
        radiobtn23.config(text='Crimson Red', variable=test2var, value=2)    
        radiobtn23.pack(side=LEFT)

        radiobtn24 = Radiobutton(test2frame)
        radiobtn24.config(text='White', variable=test2var, value=3)    
        radiobtn24.pack(side=LEFT)

        radiobtn25 = Radiobutton(test2frame)
        radiobtn25.config(text='None of Above', variable=test2var, value=4)    
        radiobtn25.pack(side=LEFT)

        #TEST 3
        test3frame=Frame(frameforscrollcation)
        test3frame.pack()
        
        test3label= Label(test3frame, text='\nGroup Zero Test  *', fg='blue',font= "applecherry 20")
        test3label.pack()
        pro3='To Original solution add Nesslers reagent\n'
        test3proceduce= Label(test3frame,text=pro3)
        test3proceduce.pack()

        test3var = StringVar()
    
        radiobtn31 = Radiobutton(test3frame) 
        radiobtn31.config(text='Brown ppt', variable=test3var, value=['NH4'])    
        radiobtn31.pack()

        radiobtn32 = Radiobutton(test3frame)
        radiobtn32.config(text='No Brown ppt', variable=test3var, value='nil')    
        radiobtn32.pack()

        #TEST 4
        test4frame=Frame(frameforscrollcation)
        test4frame.pack()
        
        test4label= Label(test4frame, text='\nGroup Zero Test', fg='blue',font= "applecherry 20")
        test4label.pack()
        pro4='To Original add NaOH and Heat\n'
        test4proceduce= Label(test4frame,text=pro4)
        test4proceduce.pack()

        test4var = StringVar()
    
        radiobtn41 = Radiobutton(test4frame) 
        radiobtn41.config(text='Pungent smell of NH3\nwhite fumes with\nglass rod dipped in conc Hcl', variable=test4var, value=['NH4'])    
        radiobtn41.pack()

        radiobtn42 = Radiobutton(test4frame)
        radiobtn42.config(text='Nil', variable=test4var, value='nil')    
        radiobtn42.pack()

        #TEST 5
        test5frame=Frame(frameforscrollcation)
        test5frame.pack()
        
        test5label= Label(test5frame, text='\nGroup 1 Test', fg='blue',font= "applecherry 20")
        test5label.pack()
        pro5='To Original Solution add Dil Hcl\n'
        test5proceduce= Label(test5frame,text=pro5)
        test5proceduce.pack()

        test5var = StringVar()
    
        radiobtn51 = Radiobutton(test5frame) 
        radiobtn51.config(text='white ppt', variable=test5var, value=['Pb'])    
        radiobtn51.pack()

        radiobtn52 = Radiobutton(test5frame)
        radiobtn52.config(text='Nil', variable=test5var, value='nil')    
        radiobtn52.pack()

        #TEST 6
        test6frame=Frame(frameforscrollcation)#
        test6frame.pack()#
        
        test6label= Label(test6frame, text='\nGroup 1 Test  *', fg='blue',font= "applecherry 20")###
        test6label.pack()#
        pro6='To Original Solution add KI\nIn another test tube add Original Solution and pottasium Chromate\n'##
        test6proceduce= Label(test6frame,text=pro6)###
        test6proceduce.pack()#

        test6var = StringVar()#
    
        radiobtn61 = Radiobutton(test6frame) #
        radiobtn61.config(text='Yellow ppt', variable=test6var, value=['Pb']) ###   
        radiobtn61.pack()#

        radiobtn62 = Radiobutton(test6frame)#
        radiobtn62.config(text='Nil', variable=test6var, value='nil') # # ##
        radiobtn62.pack()#
        
        #TEST 7
        test7frame=Frame(frameforscrollcation)#
        test7frame.pack()#
        
        test7label= Label(test7frame, text='\nGroup 2 Test', fg='blue',font= "applecherry 20")###
        test7label.pack()#
        pro7='To Original Solution add Dil Hcl and H2S\n'##
        test7proceduce= Label(test7frame,text=pro7)###
        test7proceduce.pack()#

        test7var = StringVar()#
    
        radiobtn71 = Radiobutton(test7frame) #
        radiobtn71.config(text='Black ppt', variable=test7var, value=['Cu']) ###   
        radiobtn71.pack()#

        radiobtn72 = Radiobutton(test7frame)#
        radiobtn72.config(text='Nil', variable=test7var, value='nil') #   ##
        radiobtn72.pack()#

        #TEST 8
        test8frame=Frame(frameforscrollcation)#
        test8frame.pack()#
        
        test8label= Label(test8frame, text='\nGroup 2 Test', fg='blue',font= "applecherry 20")###
        test8label.pack()#
        pro8='To Original Solution add NH3(aq)\n'##
        test8proceduce= Label(test8frame,text=pro8)###
        test8proceduce.pack()#

        test8var = StringVar()#
    
        radiobtn81 = Radiobutton(test8frame) #
        radiobtn81.config(text='Deep Blue Color', variable=test8var, value=['Cu']) ###  # 
        radiobtn81.pack()#

        radiobtn82 = Radiobutton(test8frame)#
        radiobtn82.config(text='Nil', variable=test8var, value='nil') #   ###
        radiobtn82.pack()#

        #TEST 9
        test9frame=Frame(frameforscrollcation)#
        test9frame.pack()#
        
        test9label= Label(test9frame, text='\nGroup 2 Test  *', fg='blue',font= "applecherry 20")###
        test9label.pack()#
        pro9='To Original Solution add Pottasium Ferrocyannide Solution\n'##
        test9proceduce= Label(test9frame,text=pro9)###
        test9proceduce.pack()#

        test9var = StringVar()#
    
        radiobtn91 = Radiobutton(test9frame) ##
        radiobtn91.config(text='Chocolate Brown ppt', variable=test9var, value=['Cu']) ###  # 
        radiobtn91.pack()#

        radiobtn92 = Radiobutton(test9frame)##
        radiobtn92.config(text='Nil', variable=test9var, value='nil') #   ###
        radiobtn92.pack()#

        #TEST 10
        test10frame=Frame(frameforscrollcation)#
        test10frame.pack()#
        
        test10label= Label(test10frame, text='\nGroup 3 Test  *', fg='blue',font= "applecherry 20")###
        test10label.pack()#
        pro10='To Original Solution add NH4Cl and NH4OH\n'##
        test10proceduce= Label(test10frame,text=pro10)###
        test10proceduce.pack()#

        test10var = StringVar()#
    
        radiobtn101 = Radiobutton(test10frame) ##
        radiobtn101.config(text='Gelatenous White PPT', variable=test10var, value=['Al']) ###  # 
        radiobtn101.pack(side=LEFT)#

        radiobtn102 = Radiobutton(test10frame)##
        radiobtn102.config(text='Brown ppt', variable=test10var, value=['Fe']) #   ###
        radiobtn102.pack(side=LEFT)#

        radiobtn103 = Radiobutton(test10frame)##
        radiobtn103.config(text='Nil', variable=test10var, value='nil') #   ###
        radiobtn103.pack(side=LEFT)#

        #TEST 11
        test11frame=Frame(frameforscrollcation)#
        test11frame.pack()#
        
        test11label= Label(test11frame, text='\nGroup 3 Test  *', fg='blue',font= "applecherry 20")###
        test11label.pack()#
        pro11='Only if white PPt obtained Above\nDissolve the ppt in Dil Hcl\n Add drops of blue litmus\nAdd NH4OH Solution\n'##
        test11proceduce= Label(test11frame,text=pro11)###
        test11proceduce.pack()#

        test11var = StringVar()#
    
        radiobtn111 = Radiobutton(test11frame) ##
        radiobtn111.config(text='Blue Lake Formed', variable=test11var, value=['Al']) ###  # 
        radiobtn111.pack()#

        radiobtn112 = Radiobutton(test11frame)##
        radiobtn112.config(text='nil', variable=test11var, value='nil') #   ###
        radiobtn112.pack()#

        #TEST 12
        test12frame=Frame(frameforscrollcation)#
        test12frame.pack()#
        
        test12label= Label(test12frame, text='\nGroup 3 Test  *', fg='blue',font= "applecherry 20")###
        test12label.pack()#
        pro12='Only if Brown PPt obtained Above\nDissolve the ppt in Dil Hcl\n Separate the solution in 2 parts\nTo one Part Add Pottasium Ferrocyanide\nTo other add Ammonium Thiocyanate\n'##
        test12proceduce= Label(test12frame,text=pro12)###
        test12proceduce.pack()#

        test12var = StringVar()#

        radiobtn121 = Radiobutton(test12frame) ##
        radiobtn121.config(text='Pursian Blue Color\nBlood Red Color', variable=test12var, value=['Fe']) ###  # 
        radiobtn121.pack()#

        radiobtn122 = Radiobutton(test12frame)##
        radiobtn122.config(text='nil', variable=test12var, value='nil') #   ###
        radiobtn122.pack()#

        #TEST 13
        test13frame=Frame(frameforscrollcation)#
        test13frame.pack()#
        
        test13label= Label(test13frame, text='\nGroup 4 Test  *', fg='blue',font= "applecherry 20")###
        test13label.pack()#
        pro13='To Original Solution Add NH4Cl and NH4OH and H2S\n'##
        test13proceduce= Label(test13frame,text=pro13)###
        test13proceduce.pack()#

        test13var = StringVar()#

        radiobtn131 = Radiobutton(test13frame) ##
        radiobtn131.config(text='Dirty White ppt', variable=test13var, value=['Zn']) ###  # 
        radiobtn131.pack(side=LEFT)#
        
        radiobtn132 = Radiobutton(test13frame) ##
        radiobtn132.config(text='Buff ppt', variable=test13var, value=['Mn']) ###  # 
        radiobtn132.pack(side=LEFT)#
        
        radiobtn133 = Radiobutton(test13frame) ##
        radiobtn133.config(text='Black', variable=test13var, value=['Ni']) ###  # 
        radiobtn133.pack(side=LEFT)#

        radiobtn134 = Radiobutton(test13frame)##
        radiobtn134.config(text='nil', variable=test13var, value='nil') #   ###
        radiobtn134.pack(side=LEFT)#


        #TEST 14
        test14frame=Frame(frameforscrollcation)#
        test14frame.pack()#
        
        test14label= Label(test14frame, text='\nGroup 4 Test', fg='blue',font= "applecherry 20")###
        test14label.pack()#
        pro14='Only if reslt was obtained in above test\nDissolve ppt in Dil Hcl\nboil off H2S\nadd Pottasium Ferrocyanide\n'##
        test14proceduce= Label(test14frame,text=pro14)###
        test14proceduce.pack()#

        test14var = StringVar()#

        radiobtn141 = Radiobutton(test14frame) ##
        radiobtn141.config(text='Bluish White ppt', variable=test14var, value=['Zn']) ###  # 
        radiobtn141.pack()#

        radiobtn142 = Radiobutton(test14frame)##
        radiobtn142.config(text='nil', variable=test14var, value='nil') #   ###
        radiobtn142.pack()#

        #TEST 15
        test15frame=Frame(frameforscrollcation)#
        test15frame.pack()#
        
        test15label= Label(test15frame, text='\nGroup 4 Test', fg='blue',font= "applecherry 20")###
        test15label.pack()#
        pro15='Only if reslt was obtained in above test\nDissolve ppt in Dil Hcl\nboil off H2S\nadd NaOH\n'##
        test15proceduce= Label(test15frame,text=pro15)###
        test15proceduce.pack()#

        test15var = StringVar()#

        radiobtn151 = Radiobutton(test15frame) ##
        radiobtn151.config(text='White ppt', variable=test15var, value=['Mn']) ###  # 
        radiobtn151.pack()#

        radiobtn152 = Radiobutton(test15frame)##
        radiobtn152.config(text='nil', variable=test15var, value='nil') #   ###
        radiobtn152.pack()#

        #TEST 16
        test16frame=Frame(frameforscrollcation)#
        test16frame.pack()#
        
        test16label= Label(test16frame, text='\nGroup 4 Test', fg='blue',font= "applecherry 20")###
        test16label.pack()#
        pro16='To Original Solution add DMG reagent\n'##
        test16proceduce= Label(test16frame,text=pro16)###
        test16proceduce.pack()#

        test16var = StringVar()#

        radiobtn161 = Radiobutton(test16frame) ##
        radiobtn161.config(text='Rosy red ppt', variable=test16var, value=['Ni']) ###  # 
        radiobtn161.pack()#

        radiobtn162 = Radiobutton(test16frame)##
        radiobtn162.config(text='nil', variable=test16var, value='nil') #   ###
        radiobtn162.pack()#

        #TEST 17
        test17frame=Frame(frameforscrollcation)#
        test17frame.pack()#
        
        test17label= Label(test17frame, text='\nGroup 5 Test  *', fg='blue',font= "applecherry 20")###
        test17label.pack()#
        pro17='To Original add Nh4Cl and NH4OH and (NH4)2CO3 \nif White ppt obtained, divide into 3 parts\nTo First Part add Pottasium Chromate\nTo Second Part add Ammonium Oxalate \n To Third Part add Ammonium Sulphate\n'##
        test17proceduce= Label(test17frame,text=pro17)###
        test17proceduce.pack()#

        test17var = StringVar()#

        radiobtn171 = Radiobutton(test17frame) ##
        radiobtn171.config(text='Yellow ppt in First Part', variable=test17var, value=['Ba']) ###  # 
        radiobtn171.pack(side=LEFT)#

        radiobtn172 = Radiobutton(test17frame) ##
        radiobtn172.config(text='White ppt in First Part', variable=test17var, value=['Ca']) ###  # 
        radiobtn172.pack(side=LEFT)#

        radiobtn173 = Radiobutton(test17frame) ##
        radiobtn173.config(text='Whitw ppt in First Part', variable=test17var, value=['Sr']) ###  # 
        radiobtn173.pack(side=LEFT)#

        radiobtn174 = Radiobutton(test17frame)##
        radiobtn174.config(text='Nil', variable=test17var, value='nil') #   ###
        radiobtn174.pack(side=LEFT)#
        
        submittestbtn = Button(frameforscrollcation, text="Submit", command=testy)
        submittestbtn.pack()
        
        canvas.create_window(0, 0, anchor='nw', window=frameforscrollcation)

        
        # make sure everything is displayed before configuring the scrollregion
        canvas.update_idletasks()

        canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scroll_y.set)
                 
        canvas.pack(fill='both', expand=True, side='left')
        scroll_y.pack(fill='y', side='right')


        
        
        root.mainloop()
            
    def possibleresults():
        def seeresults():
            def checkprocedures():
                global resultmessageframe
                try:
                    val=variablean.get()
                except:
                    val=variableca.get()
                try:
                    resultmessageframe.pack_forget()
                except:
                    pass
                resultmessageframe=Frame(possibleresultsframe)
                resultmessageframe.pack()
                #[,'NO3']
                if val == 'CO3':
                    
                    test1frame=Frame(resultmessageframe)
                    test1frame.pack()
                    test1label= Label(resultmessageframe, text='Solubility Test', fg='blue',font= "applecherry 20")
                    test1label.pack()
                    pro1='In a Testube add Salt and Water\nExpected Result: Insoluble Except Ammonium Carbonate'
                    test1proceduce= Label(resultmessageframe,text=pro1)
                    test1proceduce.pack()

                    #TEST2
                    test2frame=Frame(resultmessageframe)
                    test2frame.pack()
        
                    test2label= Label(resultmessageframe, text='Salt + Dil H2SO4', fg='blue',font= "applecherry 20")
                    test2label.pack()
                    pro2='In a Testube add Salt and Dilute H2SO4\nExpected Result: Brisk Effervescence of CO2'
                    test2proceduce= Label(resultmessageframe,text=pro2)
                    test2proceduce.pack()

                    #TEST
                    test3frame=Frame(resultmessageframe)
                    test3frame.pack()
        
                    test3label= Label(resultmessageframe, text='Confirmatory Test', fg='blue',font= "applecherry 20")
                    test3label.pack()
                    pro3='In a Testube add Salt and MgSO4\nExpected Result: White Precipitate of MgCO3'
                    test3proceduce= Label(resultmessageframe,text=pro3)
                    test3proceduce.pack()
                    
                elif val == 'SO4':
                    
                    test1frame=Frame(resultmessageframe)
                    test1frame.pack()
                    test1label= Label(resultmessageframe, text='Solubility Test', fg='blue',font= "applecherry 20")
                    test1label.pack()
                    pro1='In a Testube add Salt and Water\nExpected Result: Soluble'
                    test1proceduce= Label(resultmessageframe,text=pro1)
                    test1proceduce.pack()

                    #TEST2
                    test2frame=Frame(resultmessageframe)
                    test2frame.pack()
        
                    test2label= Label(resultmessageframe, text='Salt Solution + BaCl2 solution', fg='blue',font= "applecherry 20")
                    test2label.pack()
                    pro2='In a Testube add Salt Solutionand BaCl2 solution\nExpected Result: White Precipitate insoluble in Conc HCl'
                    test2proceduce= Label(resultmessageframe,text=pro2)
                    test2proceduce.pack()

                    #TEST
                    test3frame=Frame(resultmessageframe)
                    test3frame.pack()
        
                    test3label= Label(resultmessageframe, text='Salt Solution + Lead Accetate solution', fg='blue',font= "applecherry 20")
                    test3label.pack()
                    pro3='In a Testube add Salt Solution and Lead Accetate Solution\nExpected Result: White Precipitate'
                    test3proceduce= Label(resultmessageframe,text=pro3)
                    test3proceduce.pack()

                elif val == 'Cl':
                    
                    test1frame=Frame(resultmessageframe)
                    test1frame.pack()
                    test1label= Label(resultmessageframe, text='Solubility Test', fg='blue',font= "applecherry 20")
                    test1label.pack()
                    pro1='In a Testube add Salt and Water\nExpected Result: Soluble'
                    test1proceduce= Label(resultmessageframe,text=pro1)
                    test1proceduce.pack()

                    #TEST2
                    test2frame=Frame(resultmessageframe)
                    test2frame.pack()
        
                    test2label= Label(resultmessageframe, text='Salt + Conc H2SO4 and Heat', fg='blue',font= "applecherry 20")
                    test2label.pack()
                    pro2='In a Testube add Salt and Conc H2SO4 and Heat\nExpected Result: Colorless gas with pungent smell\nWhite Fumes with Glass rod\nDipped in NH3 solution'
                    test2proceduce= Label(resultmessageframe,text=pro2)
                    test2proceduce.pack()


                    #TEST 3 
                    test3frame=Frame(resultmessageframe)
                    test3frame.pack()
        
                    test3label= Label(resultmessageframe, text='Salt Solution + AgNO3 Solution', fg='blue',font= "applecherry 20")
                    test3label.pack()
                    pro3='In a Testube add Salt Solution and Silver Nitrate Solution\nExpected Result: Curdy white ppt soluble in excess of NH3 solution'
                    test3proceduce= Label(resultmessageframe,text=pro3)
                    test3proceduce.pack()

                    #TEST 4 
                    test4frame=Frame(resultmessageframe)
                    test4frame.pack()
        
                    test4label= Label(resultmessageframe, text='Chromyl Chloride Test', fg='blue',font= "applecherry 20")
                    test4label.pack()
                    pro4='In a Testube add Salt + Pottasium Dicromate + Conc H2SO4 and Heat\nExpected Result: Orange Red Fumes of chromyl Chloride\nYellow ppt when passed through\nalkaline solution of Lead Accetate'
                    test4proceduce= Label(resultmessageframe,text=pro4)
                    test4proceduce.pack()
                    
                elif val == 'Br':
                    
                    test1frame=Frame(resultmessageframe)
                    test1frame.pack()
                    test1label= Label(resultmessageframe, text='Solubility Test', fg='blue',font= "applecherry 20")
                    test1label.pack()
                    pro1='In a Testube add Salt and Water\nExpected Result: Soluble'
                    test1proceduce= Label(resultmessageframe,text=pro1)
                    test1proceduce.pack()

                    #TEST2
                    test2frame=Frame(resultmessageframe)
                    test2frame.pack()
                    test2label= Label(resultmessageframe, text='Salt + Conc H2SO4 and Heat', fg='blue',font= "applecherry 20")
                    test2label.pack()
                    pro2='In a Testube add Salt and Conc H2SO4 and Heat\nExpected Result: Brown Fumes'
                    test2proceduce= Label(resultmessageframe,text=pro2)
                    test2proceduce.pack()


                    #TEST 3 
                    test3frame=Frame(resultmessageframe)
                    test3frame.pack()
        
                    test3label= Label(resultmessageframe, text='Salt Solution + AgNO3 Solution', fg='blue',font= "applecherry 20")
                    test3label.pack()
                    pro3='In a Testube add Salt Solution and Silver Nitrate Solution\nExpected Result: Pale Yellow ppt'
                    test3proceduce= Label(resultmessageframe,text=pro3)
                    test3proceduce.pack()

                elif val == 'I':
                    
                    test1frame=Frame(resultmessageframe)
                    test1frame.pack()
                    test1label= Label(resultmessageframe, text='Solubility Test', fg='blue',font= "applecherry 20")
                    test1label.pack()
                    pro1='In a Testube add Salt and Water\nExpected Result: Soluble'
                    test1proceduce= Label(resultmessageframe,text=pro1)
                    test1proceduce.pack()

                    #TEST2
                    test2frame=Frame(resultmessageframe)
                    test2frame.pack()
                    test2label= Label(resultmessageframe, text='Salt + Conc H2SO4 and Heat', fg='blue',font= "applecherry 20")
                    test2label.pack()
                    pro2='In a Testube add Salt and Conc H2SO4 and Heat\nExpected Result: Violet Vapors'
                    test2proceduce= Label(resultmessageframe,text=pro2)
                    test2proceduce.pack()


                    #TEST 3 
                    test3frame=Frame(resultmessageframe)
                    test3frame.pack()
        
                    test3label= Label(resultmessageframe, text='Salt Solution + AgNO3 Solution', fg='blue',font= "applecherry 20")
                    test3label.pack()
                    pro3='In a Testube add Salt Solution and Silver Nitrate Solution\nExpected Result: Dark Yellow ppt'
                    test3proceduce= Label(resultmessageframe,text=pro3)
                    test3proceduce.pack()
                elif val == 'NO3':
                    
                    test1frame=Frame(resultmessageframe)
                    test1frame.pack()
                    test1label= Label(resultmessageframe, text='Solubility Test', fg='blue',font= "applecherry 20")
                    test1label.pack()
                    pro1='In a Testube add Salt and Water\nExpected Result: Soluble'
                    test1proceduce= Label(resultmessageframe,text=pro1)
                    test1proceduce.pack()

                    #TEST2
                    test2frame=Frame(resultmessageframe)
                    test2frame.pack()
                    test2label= Label(resultmessageframe, text='Salt + Conc H2SO4 and Heat', fg='blue',font= "applecherry 20")
                    test2label.pack()
                    pro2='In a Testube add Salt and Conc H2SO4 and Heat\nExpected Result: Brown Fumes'
                    test2proceduce= Label(resultmessageframe,text=pro2)
                    test2proceduce.pack()


                    #TEST 3 
                    test3frame=Frame(resultmessageframe)
                    test3frame.pack()
        
                    test3label= Label(resultmessageframe, text='Salt + Conc H2SO4 +Cu Turnings and Heat', fg='blue',font= "applecherry 20")
                    test3label.pack()
                    pro3='In a Testube add Salt Solution and Silver Nitrate Solution\nExpected Result: Intense Brown Fumes'
                    test3proceduce= Label(resultmessageframe,text=pro3)
                    test3proceduce.pack()

                    #TEST 4 
                    test4frame=Frame(resultmessageframe)
                    test4frame.pack()
        
                    test4label= Label(resultmessageframe, text='Confirmatory Test', fg='blue',font= "applecherry 20")
                    test4label.pack()
                    pro4='In a Testube add Salt + Pottasium Dicromate + Fresh FeSO4 solution and Conc H2SO4 through Sides of Test Tube\nExpected Result: Brown Ring at junction Between 2 Layers'
                    test4proceduce= Label(resultmessageframe,text=pro4)
                    test4proceduce.pack()

                    
                    '''
                    canvas = Canvas(resultmessageframe, width=650, height=600)
                    scroll_y = Scrollbar(resultmessageframe, orient="vertical", command=canvas.yview)
                    frameforscrollresult= Frame(canvas)
                    
                    canvas.create_window(0, 0, anchor='nw', window=frameforscrollresult)
                    # make sure everything is displayed before configuring the scrollregion
                    canvas.update_idletasks()
                    canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scroll_y.set)
                    canvas.pack(fill='both', expand=True, side='left')
                    scroll_y.pack(fill='y', side='right')'''

                

                elif val == 'NH4':
                    test1frame=Frame(resultmessageframe)
                    test1frame.pack()
                    test1label= Label(resultmessageframe, text='Ammonium Test I', fg='blue',font= "applecherry 20")
                    test1label.pack()
                    pro1='In a Testube add Salt and NaOH and Heat\nExpected Result: Pungent Smell of NH3 gives dense white fumes \nwith glass rod dipped in Conc HCl'
                    test1proceduce= Label(resultmessageframe,text=pro1)
                    test1proceduce.pack()

                    #TEST2
                    test2frame=Frame(resultmessageframe)
                    test2frame.pack()
                    test2label= Label(resultmessageframe, text='Ammonium Test II', fg='blue',font= "applecherry 20")
                    test2label.pack()
                    pro2='In a Testube add Salt Solution and Nesslers Reagent\nExpected Result: Brown Precipitate'
                    test2proceduce= Label(resultmessageframe,text=pro2)
                    test2proceduce.pack()

                elif val == 'Pb':
                    test1frame=Frame(resultmessageframe)
                    test1frame.pack()
                    test1label= Label(resultmessageframe, text='Flame Test', fg='blue',font= "applecherry 20")
                    test1label.pack()
                    pro1='Make a paste of sat in Conc HCl and show it to blue part of Flame\nExpected Result: White Flame'
                    test1proceduce= Label(resultmessageframe,text=pro1)
                    test1proceduce.pack()

                    #TEST2
                    test2frame=Frame(resultmessageframe)
                    test2frame.pack()
                    test2label= Label(resultmessageframe, text='Salt + Dil HCl', fg='blue',font= "applecherry 20")
                    test2label.pack()
                    pro2='In a Testube add Salt Solution and Dilute HCl\nExpected Result: White Precipitate'
                    test2proceduce= Label(resultmessageframe,text=pro2)
                    test2proceduce.pack()


                    #TEST 3 
                    test3frame=Frame(resultmessageframe)
                    test3frame.pack()
                    test3label= Label(resultmessageframe, text='Confirmatory Test I', fg='blue',font= "applecherry 20")
                    test3label.pack()
                    pro3='In a Testube add Salt Solution and KI Solution\nExpected Result: Yellow ppt'
                    test3proceduce= Label(resultmessageframe,text=pro3)
                    test3proceduce.pack()

                    #TEST 4 
                    test4frame=Frame(resultmessageframe)
                    test4frame.pack()
                    test4label= Label(resultmessageframe, text='Confirmatory Test II', fg='blue',font= "applecherry 20")
                    test4label.pack()
                    pro4='In a Testube add Salt Solution and Pottasium Chromate Solution\nExpected Result: Yellow ppt'
                    test4proceduce= Label(resultmessageframe,text=pro4)
                    test4proceduce.pack()

                elif val == 'Cu':
                    test1frame=Frame(resultmessageframe)
                    test1frame.pack()
                    test1label= Label(resultmessageframe, text='Color of Salt', fg='blue',font= "applecherry 20")
                    test1label.pack()
                    pro1='Observe Color of Salt\nExpected Result: Blue Color'
                    test1proceduce= Label(resultmessageframe,text=pro1)
                    test1proceduce.pack()

                    #TEST2
                    test2frame=Frame(resultmessageframe)
                    test2frame.pack()
                    test2label= Label(resultmessageframe, text='Salt Solution + Dil HCl + H2S', fg='blue',font= "applecherry 20")
                    test2label.pack()
                    pro2='In a Testube add Salt Solution and Dilute HCl and H2S\nExpected Result: Black Precipitate'
                    test2proceduce= Label(resultmessageframe,text=pro2)
                    test2proceduce.pack()


                    #TEST 3 
                    test3frame=Frame(resultmessageframe)
                    test3frame.pack()
                    test3label= Label(resultmessageframe, text='Salt Solution + NH3 Solution', fg='blue',font= "applecherry 20")
                    test3label.pack()
                    pro3='In a Testube add Salt Solution and NH3 Solution\nExpected Result: Deep Blue Color'
                    test3proceduce= Label(resultmessageframe,text=pro3)
                    test3proceduce.pack()

                    #TEST 4 
                    test4frame=Frame(resultmessageframe)
                    test4frame.pack()
                    test4label= Label(resultmessageframe, text='Confirmatory Test', fg='blue',font= "applecherry 20")
                    test4label.pack()
                    pro4='In a Testube add Salt Solution and Pottasium Ferrocyanide\nExpected Result: Chocolate Brown pptw ppt'
                    test4proceduce= Label(resultmessageframe,text=pro4)
                    test4proceduce.pack()

                elif val == 'Al':
                    test1frame=Frame(resultmessageframe)
                    test1frame.pack()
                    test1label= Label(resultmessageframe, text='Salt Solution + NH4Cl + NH4OH', fg='blue',font= "applecherry 20")
                    test1label.pack()
                    pro1='In a Testube add Salt Solution and NH4Cl and NH4OH\nExpected Result: Blue Color'
                    test1proceduce= Label(resultmessageframe,text=pro1)
                    test1proceduce.pack()

                    #TEST2
                    test2frame=Frame(resultmessageframe)
                    test2frame.pack()
                    test2label= Label(resultmessageframe, text='Confirmatory Test', fg='blue',font= "applecherry 20")
                    test2label.pack()
                    pro2='Dissolve Above precipitate in dilute Hcl\nAdd drop of Blue litmus solution\nAdd NH4OH Solution\nExpected Result: Blue Lake Formed'
                    test2proceduce= Label(resultmessageframe,text=pro2)
                    test2proceduce.pack()

                elif val == 'Fe':
                    test1frame=Frame(resultmessageframe)
                    test1frame.pack()
                    test1label= Label(resultmessageframe, text='Color of Salt', fg='blue',font= "applecherry 20")
                    test1label.pack()
                    pro1='Observe Color of Salt\nExpected Result: Yellow Color'
                    test1proceduce= Label(resultmessageframe,text=pro1)
                    test1proceduce.pack()

                    #TEST2
                    test2frame=Frame(resultmessageframe)
                    test2frame.pack()
                    test2label= Label(resultmessageframe, text='Salt Solution + NH4Cl + NH4OH', fg='blue',font= "applecherry 20")
                    test2label.pack()
                    pro2='In a Testube add Salt Solution and NH4Cl and NH4OH\nExpected Result: Brown Precipitate'
                    test2proceduce= Label(resultmessageframe,text=pro2)
                    test2proceduce.pack()

                    #TEST 3 
                    test3frame=Frame(resultmessageframe)
                    test3frame.pack()
                    test3label= Label(resultmessageframe, text='Confirmatory Test', fg='blue',font= "applecherry 20")
                    test3label.pack()
                    pro3='Dissolve Above precipitate in dilute Hcl and Divide into 2 Parts\nTo First one, Add Pottasium Ferrocyanide solution\nTo Second one, Add Ammonium thicocyanide\nExpected Result: Pursian Blue Color and Blood Red Color resp'
                    test3proceduce= Label(resultmessageframe,text=pro3)
                    test3proceduce.pack()
                elif val == 'Zn':
                    test1frame=Frame(resultmessageframe)
                    test1frame.pack()
                    test1label= Label(resultmessageframe, text='Salt Solution + NH4Cl + NH4OH + H2S', fg='blue',font= "applecherry 20")
                    test1label.pack()
                    pro1='In a Testube add Salt Solution and NH4Cl and NH4OH and H2S\nExpected Result: Dirty White Precipitate'
                    test1proceduce= Label(resultmessageframe,text=pro1)
                    test1proceduce.pack()

                    #TEST2
                    test2frame=Frame(resultmessageframe)
                    test2frame.pack()
                    test2label= Label(resultmessageframe, text='Confirmatory Test', fg='blue',font= "applecherry 20")
                    test2label.pack()
                    pro2='Dissolve Above precipitate in dilute Hcl and \nBoil off H2s and add Pottasium Ferrocyanide solution\nExpected Result: Bluish White ppt'
                    test2proceduce= Label(resultmessageframe,text=pro2)
                    test2proceduce.pack()

                elif val == 'Mn':
                    test0frame=Frame(resultmessageframe)
                    test0frame.pack()
                    test0label= Label(resultmessageframe, text='Color of Salt', fg='blue',font= "applecherry 20")
                    test0label.pack()
                    pro0='Observe Color of Salt\nExpected Result: Buff Color'
                    test0proceduce= Label(resultmessageframe,text=pro0)
                    test0proceduce.pack()

                    #TEST 1
                    test1frame=Frame(resultmessageframe)
                    test1frame.pack()
                    test1label= Label(resultmessageframe, text='Salt Solution + NH4Cl + NH4OH + H2S', fg='blue',font= "applecherry 20")
                    test1label.pack()
                    pro1='In a Testube add Salt Solution and NH4Cl and NH4OH and H2S\nExpected Result:Buff Precipitate'
                    test1proceduce= Label(resultmessageframe,text=pro1)
                    test1proceduce.pack()

                    #TEST2
                    test2frame=Frame(resultmessageframe)
                    test2frame.pack()
                    test2label= Label(resultmessageframe, text='Confirmatory Test', fg='blue',font= "applecherry 20")
                    test2label.pack()
                    pro2='Dissolve Above precipitate in dilute Hcl and \nBoil off H2s and add NaOH\nExpected Result: White ppt which turen brown or black with bromine water'
                    test2proceduce= Label(resultmessageframe,text=pro2)
                    test2proceduce.pack()

                elif val == 'Ni':
                    test0frame=Frame(resultmessageframe)
                    test0frame.pack()
                    test0label= Label(resultmessageframe, text='Color of Salt', fg='blue',font= "applecherry 20")
                    test0label.pack()
                    pro0='Observe Color of Salt\nExpected Result: Greenish Blue Color'
                    test0proceduce= Label(resultmessageframe,text=pro0)
                    test0proceduce.pack()

                    #TEST 1
                    test1frame=Frame(resultmessageframe)
                    test1frame.pack()
                    test1label= Label(resultmessageframe, text='Salt Solution + NH4Cl + NH4OH + H2S', fg='blue',font= "applecherry 20")
                    test1label.pack()
                    pro1='In a Testube add Salt Solution and NH4Cl and NH4OH and H2S\nExpected Result: Black Precipitate'
                    test1proceduce= Label(resultmessageframe,text=pro1)
                    test1proceduce.pack()

                    #TEST2
                    test2frame=Frame(resultmessageframe)
                    test2frame.pack()
                    test2label= Label(resultmessageframe, text='Confirmatory Test', fg='blue',font= "applecherry 20")
                    test2label.pack()
                    pro2='In a Testtube add DMG reagent\nExpected Result: rosy red precipitate'
                    test2proceduce= Label(resultmessageframe,text=pro2)
                    test2proceduce.pack()

                elif val == 'Ca':
                    test0frame=Frame(resultmessageframe)
                    test0frame.pack()
                    test0label= Label(resultmessageframe, text='Flame Test', fg='blue',font= "applecherry 20")
                    test0label.pack()
                    pro0='Make a paste of sat in Conc HCl and show it to blue part of Flame\nExpected Result: Brick Red Flame'
                    test0proceduce= Label(resultmessageframe,text=pro0)
                    test0proceduce.pack()

                    #TEST 1
                    test1frame=Frame(resultmessageframe)
                    test1frame.pack()
                    test1label= Label(resultmessageframe, text='Salt Solution + NH4Cl + NH4OH + (NH4)2CO3', fg='blue',font= "applecherry 20")
                    test1label.pack()
                    pro1='In a Testube add Salt Solution and NH4Cl and NH4OH and (NH4)2CO3\n and Add Pottasium Chromate Solution\nExpected Result: Yellow Precipitate'
                    test1proceduce= Label(resultmessageframe,text=pro1)
                    test1proceduce.pack()

                elif val == 'Ba':
                    test0frame=Frame(resultmessageframe)
                    test0frame.pack()
                    test0label= Label(resultmessageframe, text='Flame Test', fg='blue',font= "applecherry 20")
                    test0label.pack()
                    pro0='Make a paste of sat in Conc HCl and show it to blue part of Flame\nExpected Result: Apple Green Flame'
                    test0proceduce= Label(resultmessageframe,text=pro0)
                    test0proceduce.pack()

                    #TEST 1
                    test1frame=Frame(resultmessageframe)
                    test1frame.pack()
                    test1label= Label(resultmessageframe, text='Salt Solution + NH4Cl + NH4OH + (NH4)2CO3', fg='blue',font= "applecherry 20")
                    test1label.pack()
                    pro1='In a Testube add Salt Solution and NH4Cl and NH4OH and (NH4)2CO3\n and Add Ammonium Oxalate Solution\nExpected Result: White Precipitate'
                    test1proceduce= Label(resultmessageframe,text=pro1)
                    test1proceduce.pack()
                elif val == 'Sr':
                    test0frame=Frame(resultmessageframe)
                    test0frame.pack()
                    test0label= Label(resultmessageframe, text='Flame Test', fg='blue',font= "applecherry 20")
                    test0label.pack()
                    pro0='Make a paste of sat in Conc HCl and show it to blue part of Flame\nExpected Result: Crimson Red Flame'
                    test0proceduce= Label(resultmessageframe,text=pro0)
                    test0proceduce.pack()

                    #TEST 1
                    test1frame=Frame(resultmessageframe)
                    test1frame.pack()
                    test1label= Label(resultmessageframe, text='Salt Solution + NH4Cl + NH4OH + (NH4)2CO3', fg='blue',font= "applecherry 20")
                    test1label.pack()
                    pro1='In a Testube add Salt Solution and NH4Cl and NH4OH and (NH4)2CO3\n and Add Ammonium Sulphate Solution\nExpected Result: White Precipitate'
                    test1proceduce= Label(resultmessageframe,text=pro1)
                    test1proceduce.pack()



                  
                print(val)
                
            global possibleresultsframeoptions
            global possibleresultsframe
            possibleresultsframeoptions.pack_forget()
            possibleresultsframeoptions=Frame(possibleresultsframe)
            possibleresultsframeoptions.pack()
            typeresult=variable.get()
            if typeresult == 'Anion':
                OPTIONStypean = ['CO3','SO4','Cl','Br','I','NO3']
                variablean = StringVar()
                variablean.set(OPTIONStypean[0]) # default value
                w1 = OptionMenu(possibleresultsframe, variablean, *OPTIONStypean)
                w1.pack()
            else:
                OPTIONStypeca = ['NH4','Pb','Cu','Al','Fe','Zn','Mn','Ni','Ca','Ba','Sr']
                variableca = StringVar()
                variableca.set(OPTIONStypeca[0]) # default value
                w2 = OptionMenu(possibleresultsframe, variableca, *OPTIONStypeca)
                w2.pack()
            chkbtn=Button(possibleresultsframe,text='Check',command=checkprocedures)
            chkbtn.pack()


        
        global possibleresultsframe
        global possibleanionlist
        global resultframe
        global possibleresultsframeoptions
        global possibleresultsframe
        try:
            testforanionframe.pack_forget()
        except:
            pass
        try:
            testforcationframe.pack_forget()
        except:
            pass
        try:
            possibleresultsframe.pack_forget()
        except:
            pass
        
        possibleresultsframe=Frame(everythingframe)
        possibleresultsframe.pack()
        possibleresultsframeoptions=Frame(possibleresultsframe)
        possibleresultsframeoptions.pack()
        
        
        OPTIONStype = ["Anion","Cation"] #etc
        variable = StringVar()
        variable.set(OPTIONStype[0]) # default value
        w = OptionMenu(possibleresultsframeoptions, variable, *OPTIONStype)
        w.pack()

        
        seepossiblebtn = Button(possibleresultsframeoptions, text="See results", command=seeresults)
        seepossiblebtn.pack()
        
    possibleanionlist=['C03','SO4','Cl','Br','I','NO3'] #LIST OF ALL ANION
    possiblecationlist=['NH4','Pb','Cu','Al','Fe','Zn','Mn','Ni','Ca','Ba','Sr']
    headerlabel=Label(everythingframe, text='Salt Analysis', fg='blue',font= "applecherry 35" )
    headerlabel.pack()
    spacelbl=Label(everythingframe, text='\n\n')
    spacelbl.pack()
    
    btntestanion=Button(everythingframe,text='Test Anion',command=testforanion)
    btntestanion.pack()
    btntestcation=Button(everythingframe,text='Test Cation',command=testforcation)
    btntestcation.pack()
    btnpossibletest=Button(everythingframe,text='Tests and Results',command=possibleresults)
    btnpossibletest.pack()
    btnrestart=Button(everythingframe,text='restart',command=test)
    btnrestart.pack(side=BOTTOM)
    resultframe=Frame(everythingframe)
    resultframe.pack(side=BOTTOM)
    

test()
