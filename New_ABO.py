# modules
# from faulthandler import disable
# from turtle import clear
# from unittest import result
# from docx import Document
# from docx.opc.coreprops import CoreProperties
# from docx.enum.style import WD_STYLE_TYPE
# from docx.enum.text import WD_ALIGN_PARAGRAPH
# from docx.shared import Inches, Pt
from tkinter import *
def abo_main():
    ws = Tk()
    ws.title('American Board of Orthodontic Analysis')
    ws.geometry('700x700+700+200')
    ws.config(bg='#456')

    f = ('sans-serif', 13)
    btn_font = ('sans-serif', 10)
    bgcolor = '#5BB1D4'

    # Parameters
    parvar = StringVar()
    paropt = ['SNA', 'SNB', 'ANB', 'SN-GoGn', 'NPo-FH', 'IMPA', 
                'FMA', 'Li-APo', 'Ui-NA', 'Ui-NA(mm.)', 'Li-NB',
                'Li-NB(mm.)', 'Ui-Li', 'Wits', 'L lip-E-line']
    parvar.set('---Select Parameters -')

    # Function here
    def analysis():
        result1 = ""
        result2 = ""
        result3 = ""
        result4 = ""
        result5 = ""
        result6 = ""
        result7 = ""
        result8 = ""
        result9 = ""
        result10 = ""
        result11 = ""
        result12 = ""
        result13 = ""
        result14 = ""
        result15 = ""
        for i in range(1,len(paropt)+1,1):
            
            ## set stage to normal ##
            einterp1.config(state='normal')
            einterp1.delete(0, 'end')
            einterp2.config(state='normal')
            einterp2.delete(0, 'end')
            einterp3.config(state='normal')
            einterp3.delete(0, 'end')
            einterp4.config(state='normal')
            einterp4.delete(0, 'end')
            einterp5.config(state='normal')
            einterp5.delete(0, 'end')
            einterp6.config(state='normal')
            einterp6.delete(0, 'end')
            einterp7.config(state='normal')
            einterp7.delete(0, 'end')
            einterp8.config(state='normal')
            einterp8.delete(0, 'end')
            einterp9.config(state='normal')
            einterp9.delete(0, 'end')
            einterp10.config(state='normal')
            einterp10.delete(0, 'end')
            einterp11.config(state='normal')
            einterp11.delete(0, 'end')
            einterp12.config(state='normal')
            einterp12.delete(0, 'end')
            einterp13.config(state='normal')
            einterp13.delete(0, 'end')
            einterp14.config(state='normal')
            einterp14.delete(0, 'end')
            einterp15.config(state='normal')
            einterp15.delete(0, 'end')
            ### get input ###
            #input_value = int(evalue1.get())
            #input_para = epar1.get()
            #### testing ####
            #print(input_value)
            #print(input_para)
            #### data for analysis ####

            #SNA range 87-79
            if epar1.get() == paropt[0]:
                if int(evalue1.get()) < 79:
                    result1 = "Retrognathic Maxilla"
                elif int(evalue1.get()) > 87:
                    result1 = "Prognathic maxilla"
                else:
                    result1 = "Orthognathic maxilla"
            #SNB range 82-76
            if epar2.get() == paropt[1]:
                if int(evalue2.get()) < 76:
                    result2 = "Retrognathic Mandible"
                elif int(evalue2.get()) > 82:
                    result2 = "Prognathic mandible"
                else:
                    result2 = 'Orthognathic mandible'
            #ANB = SNA - SNB range 6-2
            if epar3.get() == paropt[2]:
                if int(evalue3.get()) < 2:
                    result3 = "Skeletal class III"
                elif int(evalue3.get()) > 6:
                    result3 = "Skeletal class II"
                else:
                    result3 = "Skeletal Class I"
            #SN-GoGn range 40-28
            if epar4.get() == paropt[3]:
                if int(evalue4.get()) < 28:
                    result4 = "Skeletal deep bite"
                elif int(evalue4.get()) > 40:
                    result4 = "Skeletal open bite"
                else:
                    result4 = "Skeletal normal bite"

            #NPo-FH range 87-83
            if epar5.get() == paropt[4]:
                if int(evalue5.get()) < 83:
                    result5 = "Retrognathic mandible"
                elif int(evalue5.get()) > 87:
                    result5 = "Prognathic mandible"
                else:
                    result5 = "Orthognathic mandible"

            #IMPA range 103-95
            if epar6.get() == paropt[5]:
                if int(evalue6.get()) < 95:
                    result6 = "Lower incisor retroclination"
                elif int(evalue6.get()) > 103:
                    result6 = "Lower incisor proclination"
                else:
                    result6 = "Lower incisor normal inclination"

            #FMA range 29-21
            if epar7.get() == paropt[6]:
                if int(evalue7.get()) < 21:
                    result7 = "Skeletal deep bite"
                elif int(evalue7.get()) > 29:
                    result7 = "Skeletal open bite"
                else:
                    result7 = "Skeletal normal bite"
                
            #Li-APo range 7-3    
            if epar8.get() == paropt[7]:
                if int(evalue8.get()) < 3:
                    result8 = "Lower incisor retrusion"
                elif int(evalue8.get()) > 7:
                    result8 = "Lower incisor protrusion"
                else:
                    result8 = "Lower incisor normal position"
            
            #Ui-NA range 32-34
            if epar9.get() == paropt[8]:
                if int(evalue9.get()) < 24:
                    result9 = "Upper incisor retroclination"
                elif int(evalue9.get()) > 32:
                    result9 = "Upper incisor proclination"
                else:
                    result9 = "Upper incisor normal inclination"

            #Ui-NA(mm.) range 8-4
            if epar10.get() == paropt[9]:
                if int(evalue10.get()) < 4:
                    result10 = "Upper incisor retrusion"
                elif int(evalue10.get()) > 8:
                    result10 = "Upper incisor protrusion"
                else:
                    result10 = "Upper incisor normal position"

            #Li-NB range 38-26
            if epar11.get() == paropt[10]:
                if int(evalue11.get()) < 26:
                    result11 = "Lower incisor retroclination"
                elif int(evalue11.get()) > 38:
                    result11 = "Lower incisor proclination"
                else:
                    result11 = "Lower incisor normal inclination"

            #Li-NA(mm.) range 8-4
            if epar12.get() == paropt[11]:
                if int(evalue12.get()) < 4:
                    result12 = "Lower incisor retrusion"
                elif int(evalue12.get()) > 8:
                    result12 = "Lower incisor protrusion"
                else:
                    result12 = "Lower incisor normal position"

            #Ui-Li range 120-110
            if epar13.get() == paropt[12]:
                if int(evalue13.get()) < 110:
                    result13 = "Acute interincisal angle"
                elif int(evalue13.get()) > 126:
                    result13 = "Obtuse interincisal angle"
                else:
                    result13 = "Normal interincisal angle"

            #Wits range (-1)-(-5)
            if epar14.get() == paropt[13]:
                if int(evalue14.get()) < -5:
                    result14 = "Dental base class III"
                elif int(evalue14.get()) > -1:
                    result14 = "Dental base class II"
                else:
                    result14 = "Dental base class I"

            #L lip-E-line range 5.5-0.5
            if epar15.get() == paropt[14]:
                if float(evalue15.get()) < 0.5:
                    result15 = "Lower lip retrusion"
                elif float(evalue15.get()) > 5.5:
                    result15 = "Lower lip protrusion"
                else:
                    result15 = "Lower lip normal position"

            ## set stage disabled ##
                einterp1.insert('end',result1)
                einterp1.config(state='disabled')
                einterp2.insert('end',result2)
                einterp2.config(state='disabled')
                einterp3.insert('end',result3)
                einterp3.config(state='disabled')
                einterp4.insert('end',result4)
                einterp4.config(state='disabled')
                einterp5.insert('end',result5)
                einterp5.config(state='disabled')
                einterp6.insert('end',result6)
                einterp6.config(state='disabled')
                einterp7.insert('end',result7)
                einterp7.config(state='disabled')
                einterp8.insert('end',result8)
                einterp8.config(state='disabled')
                einterp9.insert('end',result9)
                einterp9.config(state='disabled')
                einterp10.insert('end',result10)
                einterp10.config(state='disabled')
                einterp11.insert('end',result11)
                einterp11.config(state='disabled')
                einterp12.insert('end',result12)
                einterp12.config(state='disabled')
                einterp13.insert('end',result13)
                einterp13.config(state='disabled')
                einterp14.insert('end',result14)
                einterp14.config(state='disabled')
                einterp15.insert('end',result15)
                einterp15.config(state='disabled')
                
    def clear_inputs():
        #cleaning box1#
        evalue1.delete(0, 'end')
        einterp1.config(state='normal')
        einterp1.delete(0, 'end')
        einterp1.insert('end', "-- Please insert value --")
        einterp1.config(state='disabled')
        #cleaning box2#
        evalue2.delete(0, 'end')
        einterp2.config(state='normal')
        einterp2.delete(0, 'end')
        einterp2.insert('end', "-- Please insert value --")
        einterp2.config(state='disabled')
        #cleaning box2#
        evalue3.delete(0, 'end')
        einterp3.config(state='normal')
        einterp3.delete(0, 'end')
        einterp3.insert('end', "-- Please insert value --")
        einterp3.config(state='disabled')
        #cleaning box2#
        evalue4.delete(0, 'end')
        einterp4.config(state='normal')
        einterp4.delete(0, 'end')
        einterp4.insert('end', "-- Please insert value --")
        einterp4.config(state='disabled')
        #cleaning box2#
        evalue5.delete(0, 'end')
        einterp5.config(state='normal')
        einterp5.delete(0, 'end')
        einterp5.insert('end', "-- Please insert value --")
        einterp5.config(state='disabled')
        #cleaning box2#
        evalue6.delete(0, 'end')
        einterp6.config(state='normal')
        einterp6.delete(0, 'end')
        einterp6.insert('end', "-- Please insert value --")
        einterp6.config(state='disabled')
        #cleaning box2#
        evalue7.delete(0, 'end')
        einterp7.config(state='normal')
        einterp7.delete(0, 'end')
        einterp7.insert('end', "-- Please insert value --")
        einterp7.config(state='disabled')
        #cleaning box2#
        evalue8.delete(0, 'end')
        einterp8.config(state='normal')
        einterp8.delete(0, 'end')
        einterp8.insert('end', "-- Please insert value --")
        einterp8.config(state='disabled')
        #cleaning box2#
        evalue9.delete(0, 'end')
        einterp9.config(state='normal')
        einterp9.delete(0, 'end')
        einterp9.insert('end', "-- Please insert value --")
        einterp9.config(state='disabled')
        #cleaning box2#
        evalue10.delete(0, 'end')
        einterp10.config(state='normal')
        einterp10.delete(0, 'end')
        einterp10.insert('end', "-- Please insert value --")
        einterp10.config(state='disabled')
        #cleaning box2#
        evalue11.delete(0, 'end')
        einterp11.config(state='normal')
        einterp11.delete(0, 'end')
        einterp11.insert('end', "-- Please insert value --")
        einterp11.config(state='disabled')
        #cleaning box2#
        evalue12.delete(0, 'end')
        einterp12.config(state='normal')
        einterp12.delete(0, 'end')
        einterp12.insert('end', "-- Please insert value --")
        einterp12.config(state='disabled')
        #cleaning box2#
        evalue13.delete(0, 'end')
        einterp13.config(state='normal')
        einterp13.delete(0, 'end')
        einterp13.insert('end', "-- Please insert value --")
        einterp13.config(state='disabled')
        #cleaning box14#
        evalue14.delete(0, 'end')
        einterp14.config(state='normal')
        einterp14.delete(0, 'end')
        einterp14.insert('end', "-- Please insert value --")
        einterp14.config(state='disabled')
        #cleaning box15#
        evalue15.delete(0, 'end')
        einterp15.config(state='normal')
        einterp15.delete(0, 'end')
        einterp15.insert('end', "-- Please insert value --")
        einterp15.config(state='disabled')


    # Frames
    frame = Frame(ws, padx=20, pady=20, bg=bgcolor)
    frame.pack(expand=True, fill=BOTH)

    # Label widgets
    Label(
        frame, 
        text="Parameter",
        font=f,
        bg=bgcolor
    ).grid(row=0, column=0, sticky='w')
    Label(
        frame, 
        text="Value",
        font=f,
        bg=bgcolor
    ).grid(row=0, column=1, sticky='w')
    Label(
        frame, 
        text="Interpretation",
        font=f,
        bg=bgcolor
    ).grid(row=0, column=2, sticky='w')
    # entry widgets
    # parameter = OptionMenu(
    #     frame, 
    #     parvar,
    #     *paropt
    # )
    # parameter.grid(row=i, column=0, pady=(5,0))
    # parameter.config(width=15, font=f)
    #entry box
    #for i in range(1,16,1):
        #message = ["test1", "test2"]


    #insert 1
    epar1 = Entry(frame, width=20, font=f)
    epar1.grid(row=1, column=0, pady=(5,0)) #position
    epar1.insert('end', paropt[0]) #Parameter index
    epar1.config(state='disabled')

    evalue1 = Entry(frame, width=20, font=f)
    evalue1.grid(row=1, column=1, pady=(5,0)) #position
    evalue1.config(width=15)

    einterp1 = Entry(frame, width=27, font=f)
    einterp1.grid(row=1, column=2, pady=(5,0)) #position
    einterp1.insert('end', "-- Please insert value --")
    einterp1.config(state='disabled')

    #insert 2

    epar2 = Entry(frame, width=20, font=f)
    epar2.grid(row=2, column=0, pady=(5,0)) #position
    epar2.insert('end', paropt[1]) #Parameter index
    epar2.config(state='disabled')

    evalue2 = Entry(frame, width=20, font=f)
    evalue2.grid(row=2, column=1, pady=(5,0)) #position
    evalue2.config(width=15)

    einterp2 = Entry(frame, width=27, font=f)
    einterp2.grid(row=2, column=2, pady=(5,0)) #position
    einterp2.insert('end', "-- Please insert value --")
    einterp2.config(state='disabled')

    #insert 3

    epar3 = Entry(frame, width=20, font=f)
    epar3.grid(row=3, column=0, pady=(5,0)) #position
    epar3.insert('end', paropt[2]) #Parameter index
    epar3.config(state='disabled')

    evalue3 = Entry(frame, width=20, font=f)
    evalue3.grid(row=3, column=1, pady=(5,0)) #position
    evalue3.config(width=15)

    einterp3 = Entry(frame, width=27, font=f)
    einterp3.grid(row=3, column=2, pady=(5,0)) # position
    einterp3.insert('end', "-- Please insert value --")
    einterp3.config(state='disabled')

    #insert 4

    epar4 = Entry(frame, width=20, font=f)
    epar4.grid(row=4, column=0, pady=(5,0)) #position
    epar4.insert('end', paropt[3]) #Parameter index
    epar4.config(state='disabled')

    evalue4 = Entry(frame, width=20, font=f)
    evalue4.grid(row=4, column=1, pady=(5,0)) #position
    evalue4.config(width=15)

    einterp4 = Entry(frame, width=27, font=f)
    einterp4.grid(row=4, column=2, pady=(5,0)) # position
    einterp4.insert('end', "-- Please insert value --")
    einterp4.config(state='disabled')

    #insert 5

    epar5 = Entry(frame, width=20, font=f)
    epar5.grid(row=5, column=0, pady=(5,0)) #position
    epar5.insert('end', paropt[4]) #Parameter index
    epar5.config(state='disabled')

    evalue5 = Entry(frame, width=20, font=f)
    evalue5.grid(row=5, column=1, pady=(5,0)) #position
    evalue5.config(width=15)

    einterp5 = Entry(frame, width=27, font=f)
    einterp5.grid(row=5, column=2, pady=(5,0)) # position
    einterp5.insert('end', "-- Please insert value --")
    einterp5.config(state='disabled')

    #insert 6

    epar6 = Entry(frame, width=20, font=f)
    epar6.grid(row=6, column=0, pady=(5,0)) #position
    epar6.insert('end', paropt[5]) #Parameter index
    epar6.config(state='disabled')

    evalue6 = Entry(frame, width=20, font=f)
    evalue6.grid(row=6, column=1, pady=(5,0)) #position
    evalue6.config(width=15)

    einterp6 = Entry(frame, width=27, font=f)
    einterp6.grid(row=6, column=2, pady=(5,0)) # position
    einterp6.insert('end', "-- Please insert value --")
    einterp6.config(state='disabled')

    #insert 7

    epar7 = Entry(frame, width=20, font=f)
    epar7.grid(row=7, column=0, pady=(5,0)) #position
    epar7.insert('end', paropt[6]) #Parameter index
    epar7.config(state='disabled')

    evalue7 = Entry(frame, width=20, font=f)
    evalue7.grid(row=7, column=1, pady=(5,0)) #position
    evalue7.config(width=15)

    einterp7 = Entry(frame, width=27, font=f)
    einterp7.grid(row=7, column=2, pady=(5,0)) # position
    einterp7.insert('end', "-- Please insert value --")
    einterp7.config(state='disabled')

    #insert 8

    epar8 = Entry(frame, width=20, font=f)
    epar8.grid(row=8, column=0, pady=(5,0)) #position
    epar8.insert('end', paropt[7]) #Parameter index
    epar8.config(state='disabled')

    evalue8 = Entry(frame, width=20, font=f)
    evalue8.grid(row=8, column=1, pady=(5,0)) #positionw
    evalue8.config(width=15)

    einterp8 = Entry(frame, width=27, font=f)
    einterp8.grid(row=8, column=2, pady=(5,0)) # position
    einterp8.insert('end', "-- Please insert value --")
    einterp8.config(state='disabled')

    #insert 9

    epar9 = Entry(frame, width=20, font=f)
    epar9.grid(row=9, column=0, pady=(5,0)) #position
    epar9.insert('end', paropt[8]) #Parameter index
    epar9.config(state='disabled')

    evalue9 = Entry(frame, width=20, font=f)
    evalue9.grid(row=9, column=1, pady=(5,0)) #position
    evalue9.config(width=15)

    einterp9 = Entry(frame, width=27, font=f)
    einterp9.grid(row=9, column=2, pady=(5,0)) # position
    einterp9.insert('end', "-- Please insert value --")
    einterp9.config(state='disabled')

    #insert 10

    epar10 = Entry(frame, width=20, font=f)
    epar10.grid(row=10, column=0, pady=(5,0)) #position
    epar10.insert('end', paropt[9]) #Parameter index
    epar10.config(state='disabled')

    evalue10 = Entry(frame, width=20, font=f)
    evalue10.grid(row=10, column=1, pady=(5,0)) #position
    evalue10.config(width=15)

    einterp10 = Entry(frame, width=27, font=f)
    einterp10.grid(row=10, column=2, pady=(5,0)) # position
    einterp10.insert('end', "-- Please insert value --")
    einterp10.config(state='disabled')

    #insert 11

    epar11 = Entry(frame, width=20, font=f)
    epar11.grid(row=11, column=0, pady=(5,0)) #position
    epar11.insert('end', paropt[10]) #Parameter index
    epar11.config(state='disabled')

    evalue11 = Entry(frame, width=20, font=f)
    evalue11.grid(row=11, column=1, pady=(5,0)) #position
    evalue11.config(width=15)

    einterp11 = Entry(frame, width=27, font=f)
    einterp11.grid(row=11, column=2, pady=(5,0)) # position
    einterp11.insert('end', "-- Please insert value --")
    einterp11.config(state='disabled')

    #insert 12

    epar12 = Entry(frame, width=20, font=f)
    epar12.grid(row=12, column=0, pady=(5,0)) #position
    epar12.insert('end', paropt[11]) #Parameter index
    epar12.config(state='disabled')

    evalue12 = Entry(frame, width=20, font=f)
    evalue12.grid(row=12, column=1, pady=(5,0)) #position
    evalue12.config(width=15)

    einterp12 = Entry(frame, width=27, font=f)
    einterp12.grid(row=12, column=2, pady=(5,0)) # position
    einterp12.insert('end', "-- Please insert value --")
    einterp12.config(state='disabled')

    #insert 13

    epar13 = Entry(frame, width=20, font=f)
    epar13.grid(row=13, column=0, pady=(5,0)) #position
    epar13.insert('end', paropt[12]) #Parameter index
    epar13.config(state='disabled')

    evalue13 = Entry(frame, width=20, font=f)
    evalue13.grid(row=13, column=1, pady=(5,0)) #position
    evalue13.config(width=15)

    einterp13 = Entry(frame, width=27, font=f)
    einterp13.grid(row=13, column=2, pady=(5,0)) # position
    einterp13.insert('end', "-- Please insert value --")
    einterp13.config(state='disabled')

    #insert 14

    epar14 = Entry(frame, width=20, font=f)
    epar14.grid(row=14, column=0, pady=(5,0)) #position
    epar14.insert('end', paropt[13]) #Parameter index
    epar14.config(state='disabled')

    evalue14 = Entry(frame, width=20, font=f)
    evalue14.grid(row=14, column=1, pady=(5,0)) #position
    evalue14.config(width=15)

    einterp14 = Entry(frame, width=27, font=f)
    einterp14.grid(row=14, column=2, pady=(5,0)) # position
    einterp14.insert('end', "-- Please insert value --")
    einterp14.config(state='disabled')

    #insert 15

    epar15 = Entry(frame, width=20, font=f)
    epar15.grid(row=15, column=0, pady=(5,0)) #position
    epar15.insert('end', paropt[14]) #Parameter index
    epar15.config(state='disabled')

    evalue15 = Entry(frame, width=20, font=f)
    evalue15.grid(row=15, column=1, pady=(5,0)) #position
    evalue15.config(width=15)

    einterp15 = Entry(frame, width=27, font=f)
    einterp15.grid(row=15, column=2, pady=(5,0)) # position
    einterp15.insert('end', "-- Please insert value --")
    einterp15.config(state='disabled')

    #####

    btn_frame = Frame(frame, bg=bgcolor)
    btn_frame.grid(columnspan=2, pady=(50, 0))
    #button
    result_btn = Button(
        btn_frame,
        text='Submit',
        command=analysis,
        font=btn_font,
        padx=10,
        pady=5
    )

    clear_btn = Button(
        btn_frame,
        text='Clear',
        command=clear_inputs,
        font=btn_font,
        padx=10, 
        pady=5,
        width=7
    )

    result_btn.pack(side=LEFT, expand=True, padx=(15, 0))
    clear_btn.pack(side=LEFT, expand=True, padx=15)
    # mainloop
    ws.mainloop()
if __name__ == '__main__':
    # test1.py executed as script
    # do something
    abo_main()