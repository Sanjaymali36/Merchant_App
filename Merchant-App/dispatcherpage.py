#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.14
# In conjunction with Tcl version 8.6
#    Jun 13, 2018 07:07:24 PM

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import dispatcherpage_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = dispatcherpage (root)
    dispatcherpage_support.init(root, top)
    root.mainloop()

w = None
def create_dispatcherpage(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = dispatcherpage (w)
    dispatcherpage_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_dispatcherpage():
    global w
    w.destroy()
    w = None


class dispatcherpage:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font9 = "-family {DejaVu Sans} -size 15 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("661x316+427+148")
        top.title("dispatcherpage")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.93, relwidth=0.49)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="5")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#beadd8")
        self.Frame1.configure(width=325)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.06, rely=0.05, height=28, width=276)
        self.Label1.configure(background="#beadd8")
        self.Label1.configure(font=font9)
        self.Label1.configure(text='''DispatcherRegistration''')
        self.Label1.configure(width=276)

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.03, rely=0.2, height=28, width=126)
        self.Label2.configure(background="#beadd8")
        self.Label2.configure(font=font9)
        self.Label2.configure(text='''Id no''')
        self.Label2.configure(width=126)

        self.Label2_1 = Label(self.Frame1)
        self.Label2_1.place(relx=0.03, rely=0.34, height=28, width=126)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(background="#beadd8")
        self.Label2_1.configure(font=font9)
        self.Label2_1.configure(text='''Name''')

        self.Label2_2 = Label(self.Frame1)
        self.Label2_2.place(relx=0.03, rely=0.47, height=28, width=126)
        self.Label2_2.configure(activebackground="#f9f9f9")
        self.Label2_2.configure(background="#beadd8")
        self.Label2_2.configure(font=font9)
        self.Label2_2.configure(text='''Contact''')

        self.Label2_3 = Label(self.Frame1)
        self.Label2_3.place(relx=0.03, rely=0.61, height=28, width=126)
        self.Label2_3.configure(activebackground="#f9f9f9")
        self.Label2_3.configure(background="#beadd8")
        self.Label2_3.configure(font=font9)
        self.Label2_3.configure(text='''Password''')

        self.admin_dispatcher_id = Entry(self.Frame1)
        self.admin_dispatcher_id.place(relx=0.48, rely=0.21, height=20
                , relwidth=0.45)
        self.admin_dispatcher_id.configure(background="white")
        self.admin_dispatcher_id.configure(font="TkFixedFont")

        self.admin_dispatcher_name = Entry(self.Frame1)
        self.admin_dispatcher_name.place(relx=0.48, rely=0.35, height=20
                , relwidth=0.45)
        self.admin_dispatcher_name.configure(background="white")
        self.admin_dispatcher_name.configure(font="TkFixedFont")
        self.admin_dispatcher_name.configure(selectbackground="#c4c4c4")

        self.admin_dispatcher_contact = Entry(self.Frame1)
        self.admin_dispatcher_contact.place(relx=0.49, rely=0.48, height=20
                , relwidth=0.45)
        self.admin_dispatcher_contact.configure(background="white")
        self.admin_dispatcher_contact.configure(font="TkFixedFont")
        self.admin_dispatcher_contact.configure(selectbackground="#c4c4c4")

        self.admin_dispatcher_password = Entry(self.Frame1)
        self.admin_dispatcher_password.place(relx=0.49, rely=0.61, height=20
                , relwidth=0.45)
        self.admin_dispatcher_password.configure(background="white")
        self.admin_dispatcher_password.configure(font="TkFixedFont")
        self.admin_dispatcher_password.configure(selectbackground="#c4c4c4")
        self.admin_dispatcher_password.configure(show="*")

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.34, rely=0.78, height=36, width=107)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(background="#beadd8")
        self.Button1.configure(command=dispatcherpage_support.RegisterDispatcher)
        self.Button1.configure(font=font9)
        self.Button1.configure(text='''Save''')
        self.Button1.configure(width=107)

        self.Frame2 = Frame(top)
        self.Frame2.place(relx=0.51, rely=0.03, relheight=0.93, relwidth=0.48)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="5")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#beadd8")
        self.Frame2.configure(highlightbackground="#beadd8")
        self.Frame2.configure(width=315)

        self.Label3 = Label(self.Frame2)
        self.Label3.place(relx=0.13, rely=0.07, height=18, width=256)
        self.Label3.configure(background="#beadd8")
        self.Label3.configure(font=font9)
        self.Label3.configure(text='''DispatcherView''')
        self.Label3.configure(width=256)

        self.Label4 = Label(self.Frame2)
        self.Label4.place(relx=0.03, rely=0.21, height=28, width=126)
        self.Label4.configure(background="#beadd8")
        self.Label4.configure(font=font9)
        self.Label4.configure(text='''Id no''')
        self.Label4.configure(width=126)

        self.Label5 = Label(self.Frame2)
        self.Label5.place(relx=0.02, rely=0.33, height=28, width=136)
        self.Label5.configure(background="#beadd8")
        self.Label5.configure(font=font9)
        self.Label5.configure(text='''Name''')
        self.Label5.configure(width=136)

        self.Label6 = Label(self.Frame2)
        self.Label6.place(relx=0.06, rely=0.46, height=18, width=103)
        self.Label6.configure(background="#beadd8")
        self.Label6.configure(font=font9)
        self.Label6.configure(text='''Contact''')

        self.Label7 = Label(self.Frame2)
        self.Label7.place(relx=0.06, rely=0.59, height=18, width=110)
        self.Label7.configure(background="#beadd8")
        self.Label7.configure(font=font9)
        self.Label7.configure(text='''Password''')

        self.dispatcher_view_id = Entry(self.Frame2)
        self.dispatcher_view_id.place(relx=0.48, rely=0.2, height=20
                , relwidth=0.46)
        self.dispatcher_view_id.configure(background="white")
        self.dispatcher_view_id.configure(font="TkFixedFont")

        self.dispatcher_view_name = Entry(self.Frame2)
        self.dispatcher_view_name.place(relx=0.48, rely=0.33, height=20
                , relwidth=0.46)
        self.dispatcher_view_name.configure(background="white")
        self.dispatcher_view_name.configure(font="TkFixedFont")

        self.dispatcher_view_contact = Entry(self.Frame2)
        self.dispatcher_view_contact.place(relx=0.48, rely=0.45, height=20
                , relwidth=0.46)
        self.dispatcher_view_contact.configure(background="white")
        self.dispatcher_view_contact.configure(font="TkFixedFont")

        self.dispatcher_view_password = Entry(self.Frame2)
        self.dispatcher_view_password.place(relx=0.48, rely=0.58, height=20
                , relwidth=0.46)
        self.dispatcher_view_password.configure(background="white")
        self.dispatcher_view_password.configure(font="TkFixedFont")
        self.dispatcher_view_password.configure(show="*")

        self.Button2 = Button(self.Frame2)
        self.Button2.place(relx=0.32, rely=0.75, height=36, width=107)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(background="#beadd8")
        self.Button2.configure(font=font9)
        self.Button2.configure(text='''Show''')
        self.Button2.configure(width=107)






if __name__ == '__main__':
    vp_start_gui()



