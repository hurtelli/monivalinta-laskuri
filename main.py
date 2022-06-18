from tkinter import *

"""
Otto Palmgren

Ohjelma auttaa hahmottamaan monivalintakysymksiä, joissa ei anneta palautetta valintakohtaisesti
Toisinsanoen ohjelman tarkoitus on pitää kirjaa, missä on todennäköisemmin oikea vastaus.

Versio 1.0.1

Ominaisuudet:
Vaihtoehtojen määrän valinta
Laskuri 1 tai 0 tilanteelle numerokohtaisesti
Summat kaikista yrityksistä
Yrityskertahavainnollistus, iteraatiokerran indexoinnilla
"""

# TODO implementoi todennäköisyydet 1 tai 0 tilalle
# jos valitsee 3, joista saa piteet 6/10 tod näk kaks on oikein
# tällöin todennäköisyys jokaiselle olla oikea on 2/3
# tämä 2/3 tulisi lisätä listaan ja summana voi tarkastella suurinta lukua=suurinta todennäköisyyttä

#Todo yrityskertojen määrä näkyviin

#TODO Parempi alotusteksti

# TODO vitusti bugfixejä, yksikkötestejä jne.

# TODO JOSKUS SITTEN

# algoritmi kertomaan mitä kannattaa valita


root = Tk()

#The sum of the results
ResultSum = StringVar()
ResultSum.set('')

#Wall of text sums on top of each other
Result = StringVar()
Result.set('')

#maximum amount of variables
MAXIMUM_VARIABLES=10



def SetError(error,errorcolor,Error):
    print(f"Setting Error....")
    print(f"Error color: {errorcolor}\nError name: {error}")
    Error[1].config(text=error)
    Error[1].config(bg=errorcolor)

def UpdateSumResults(sums):
    sumstr = ""
    for sum in sums:
        sumstr += str(sums[sum])
        sumstr += '      '
    ResultSum.set(sumstr)

#Todo include what iter it is atm

def UpdateResults(options_dic,iter):
    resultstr=""
    resultstr+=Result.get()
    if resultstr != "":
        resultstr+="\n"

    #Index number of iter
    resultstr+=str(iter) + '.' + '        '

    for option in options_dic:
        try:
            resultstr += str(options_dic[option][-1])
        except IndexError:
            resultstr+='0'
        resultstr+= '      '
    Result.set(resultstr)


def OptionStatusCheck(options_dic,iter):
    sums = {}
    i = 0
    print(f"len optionsdic on  {options_dic}")
    for option in options_dic:
        sums[i] = sum(options_dic[option])
        i += 1
    UpdateResults(options_dic,iter)
    UpdateSumResults(sums)



# Function check wether a box is ticked when the user HAS PRESSED 0
# SO IF THE BOX IS CHECKED IT GETS THE VALUE 0 TO ITS LIST
def StatusCheck0(variables_list, options_dic, checkbox_list,status_checks,Error):
    status_checks[0]+=1
    print(f"statuschecks on    {status_checks[0]}")
    if status_checks[0] <= 10:
        i = 0
        for variable in variables_list:
            if variable.get() == 1:
                options_dic[i].append(0)
            i += 1

        OptionStatusCheck(options_dic,status_checks[0])
    else:
        SetError("Can't display more tries",'red',Error)


def StatusCheck1(variables_list, options_dic, checkbox_list,status_checks,Error):
    status_checks[0]+=1
    print(f"statuschecks on    {status_checks[0]}")
    if status_checks[0] <= 10:
        i = 0
        for variable in variables_list:
            if variable.get() == 1:
                options_dic[i].append(1)
            i += 1
        OptionStatusCheck(options_dic,status_checks[0])
    else:
        SetError("Can't display more tries",'red',Error)


def MainWindow(entry_amount_str):

    entry_amount = int(entry_amount_str)

    MainRoot = root
    MainRoot.title('Algorithm')

    main_width=(entry_amount * 90)


    scrwdth = root.winfo_screenwidth()
    scrhgt = root.winfo_screenheight()

    xLeft = (scrwdth / 2) - (main_width / 2)
    yTop = (scrhgt / 2) - (550 / 2)


    MainRoot.geometry(str(main_width)+"x"+"450"+ "+" + str(int(xLeft)) + "+" + str(int(yTop)))
    MainRoot.attributes('-alpha',1)
    MainRoot.attributes("-topmost",1)
    MainRoot.update()

    MainRoot.iconbitmap("icon.ico")

    BGFrame = Frame(MainRoot, bg='dark grey')
    BGFrame.place(relwidth=1, relheight=1)

# For printing errors
    ErrorFrame = Frame(BGFrame, bg='gray')
    ErrorFrame.place(relwidth=0.3, relheight=0.3, relx=0.65, rely=0.45)

    ErrorLabel = Label(ErrorFrame, bg='light gray', text='')
    ErrorLabel.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    Error = [ErrorFrame, ErrorLabel]


#Top textlabel
    TextFrame = Frame(BGFrame, bg='grey')
    TextFrame.place(relheight=0.2, relwidth=0.9, rely=0.05, relx=0.05)


    TutoLabel = Label(TextFrame, text=f"Choose {entry_amount // 2 + 1} from the options:\n", bg='light grey', )
    TutoLabel.place(relheight=0.9, relwidth=0.9, rely=0.05, relx=0.05)


#ChecBoxes
    BoxFrame = Frame(BGFrame, bg='grey')
    BoxFrame.place(relheight=0.1, relwidth=0.55, rely=0.3, relx=0.05)

    CheckFrame = Frame(BoxFrame, bg='grey')
    CheckFrame.place(relheight=0.8, relwidth=0.8, rely=0.15, relx=0.1)
    i = 0
    variables_list = []
    checkbox_list = []
    options_dic = {}
    for i in range(entry_amount):
        var = IntVar()
        CheckBox = Checkbutton(CheckFrame, text=f'{i + 1}', variable=var, onvalue=1, offvalue=0, bg='grey', bd=0,
                               padx=5, relief='groove')
        CheckBox.grid(row=0, column=i)
        CheckBox.deselect()
        options_dic[i] = []
        variables_list.append(var)
        checkbox_list.append(CheckBox)
    status_checks=[0]

    print(f"variablet:    {variables_list}")
    print(f"checkboxit:      {checkbox_list}")
    print(f"optioni dictin len:    {len(options_dic)}")


#Status Check
    StatusCheckFrame = Frame(BGFrame, bg='gray')
    StatusCheckFrame.place(relwidth=0.3, relheight=0.1, relx=0.65, rely=0.3)


    Status0Button = Button(StatusCheckFrame, text='0',
                           command=lambda: StatusCheck0(variables_list, options_dic, checkbox_list,status_checks,Error), bg='light gray',
                           bd=1)
    Status0Button.place(relwidth=0.3, relheight=0.6, relx=0.1, rely=0.2)

    Status1Button = Button(StatusCheckFrame, text='1',
                           command=lambda: StatusCheck1(variables_list, options_dic, checkbox_list,status_checks,Error), bg='light gray',
                           bd=1)
    Status1Button.place(relwidth=0.3, relheight=0.6, relx=0.6, rely=0.2)




#Results
    ResultFrame = Frame(BGFrame, bg='grey')
    ResultFrame.place(relwidth=0.55, relheight=0.6, relx=0.05, rely=0.45)

    ResultLabel = Label(ResultFrame, bg='light gray', textvariable=Result)
    ResultLabel.place(relwidth=0.9, relheight=0.8, relx=0.05, rely=0.05)

    ResultSumLabel = Label(ResultFrame, bg='white',textvariable=ResultSum)
    ResultSumLabel.place(relwidth=0.9,relheight=0.05, relx=0.05,rely=0.75)


#TODO Reset Button
    #
    #
    #



#Exit Button
    # TODO implement automatic app shutdown on pressing cross
    ExitFrame = Frame(BGFrame, bg='grey')
    ExitFrame.place(relwidth=0.1, relheight=0.2, rely=0.8, relx=0.85)
    ExitButton = Button(ExitFrame, text="EXIT", command=lambda: root.destroy(), bd=1, bg='red')
    ExitButton.place(relwidth=0.8, relheight=0.8, rely=0.1, relx=0.1)


# has false check for values under 1
def DestroyEntry(entry_amount, EntryRoot):
    try:
        int(entry_amount)

        if 1 / int(entry_amount) < 1 and int(entry_amount) <= MAXIMUM_VARIABLES:
            MainWindow(entry_amount)
            EntryRoot.destroy()

        else:
            ErrorLabel = Label(EntryRoot, bg='light gray', fg='red', text="ERROR: False input type")
            ErrorLabel.place(relheight=0.15, relwidth=0.8, relx=0.1, rely=0.22)
    except ValueError:
        ErrorLabel = Label(EntryRoot, bg='light gray', fg='red', text="ERROR: False input type")
        ErrorLabel.place(relheight=0.15, relwidth=0.8, relx=0.1, rely=0.22)


def EntryWindow():
    # Creates a greeting window with input choice
    EntryRoot = Toplevel(root)
    EntryRoot.attributes("-topmost",True)
    EntryRoot.title("Algorithm")
    EntryRoot.iconbitmap("icon.ico")

    # Minimizes the base root of the software
    root.title("Algorithm")
    root.iconbitmap("icon.ico")
    root.attributes('-alpha',0)

    entryframe = Frame(EntryRoot, bg="dark grey")
    entryframe.place(relwidth=1, relheight=1)

    InputLabel = Label(entryframe, text='Input the Amount of options', bg='grey', borderwidth=2)
    InputLabel.place(relx=0.1, rely=0.1, relwidth=0.80, relheight=0.10)

    InputEntry = Entry(entryframe, bg='grey', borderwidth=2)
    InputEntry.place(relx=0.35, rely=0.40, relwidth=0.30, relheight=0.10)

    OkButton = Button(entryframe, text='OK', bg='grey', command=lambda: DestroyEntry(InputEntry.get(), EntryRoot))
    OkButton.place(relx=0.40, rely=0.60, relwidth=0.20, relheight=0.20)

    EntryRoot.mainloop()


EntryWindow()
