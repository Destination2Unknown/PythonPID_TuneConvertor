import tkinter as tk
from tkinter import ttk

class gui(object):
    def __init__(self):        
        self.root = tk.Tk()
        self.root.title("PID Tune Convertor")
        self.root.configure(bg='light grey')

        #Frames
        self.menuframe = tk.Frame(self.root,height=120, width=550)
        self.menuframe.pack(expand=True, fill="both")
        self.menuframe.grid_propagate(False)
        self.lowerframe = tk.Frame(self.root,height=200, width=550)
        #Button
        ttk.Label(self.menuframe, text="     ").grid(row=1,column=4,padx=4,pady=4,sticky="W")             
        self.buttonConvert = ttk.Button(self.menuframe, text="Convert", command=lambda :[self.convert()])
        self.buttonConvert.grid(row=1,column=5,columnspan=1,padx=4,rowspan=3,pady=4,sticky="NESW")      
        ttk.Label(self.menuframe, text="         ").grid(row=1,column=6,padx=4,pady=4,sticky="W")

        self.fromP = ttk.Entry(self.menuframe,width=8)
        self.fromI = ttk.Entry(self.menuframe,width=8)
        self.fromD = ttk.Entry(self.menuframe,width=8)
        self.fromP.bind('<FocusOut>', self.convert)
        self.fromI.bind('<FocusOut>', self.convert)
        self.fromD.bind('<FocusOut>', self.convert)
        self.fromPunit = tk.StringVar()
        self.fromIunit = tk.StringVar()
        self.fromDunit = tk.StringVar()
        self.toP = tk.StringVar()
        self.toI = tk.StringVar()
        self.toD = tk.StringVar()
        self.toPunit = tk.StringVar()
        self.toIunit = tk.StringVar()
        self.toDunit = tk.StringVar()
        self.radioFromType=tk.StringVar()
        self.radioFromTime=tk.StringVar()
        self.radioToType=tk.StringVar()
        self.radioToTime=tk.StringVar()
        self.statustext = tk.StringVar()

        #Load Defaults
        self.reset()        
       
        #Convert From
        ttk.Label(self.menuframe, text="Convert From:").grid(row=0,column=0,columnspan=2,padx=4,pady=4,sticky="NESW") 
        ttk.Label(self.menuframe, text="P:").grid(row=1,column=0,padx=4,pady=4,sticky="E") 
        ttk.Label(self.menuframe, text="I:").grid(row=2,column=0,padx=4,pady=4,sticky="E") 
        ttk.Label(self.menuframe, text="D:").grid(row=3,column=0,padx=4,pady=4,sticky="E")        
        self.fromP.grid(row=1,column=1,padx=4,pady=4,sticky="W")
        self.fromI.grid(row=2,column=1,padx=4,pady=4,sticky="W")
        self.fromD.grid(row=3,column=1,padx=4,pady=4,sticky="W")
        ttk.Label(self.menuframe, text="                           ").grid(row=0,column=3,padx=4,pady=4,sticky="W")
        ttk.Label(self.menuframe, textvariable=self.fromPunit).grid(row=1,column=3,padx=4,pady=4,sticky="W") 
        ttk.Label(self.menuframe, textvariable=self.fromIunit).grid(row=2,column=3,padx=4,pady=4,sticky="W") 
        ttk.Label(self.menuframe, textvariable=self.fromDunit).grid(row=3,column=3,padx=4,pady=4,sticky="W")  

        #Convert to
        ttk.Label(self.menuframe, text="Convert To:").grid(row=0,column=7,columnspan=2,padx=4,pady=4,sticky="NESW") 
        ttk.Label(self.menuframe, text="P:").grid(row=1,column=7,padx=4,pady=4,sticky="E") 
        ttk.Label(self.menuframe, text="I:").grid(row=2,column=7,padx=4,pady=4,sticky="E") 
        ttk.Label(self.menuframe, text="D:").grid(row=3,column=7,padx=4,pady=4,sticky="E")         
        ttk.Label(self.menuframe, textvariable=self.toP).grid(row=1,column=8,padx=4,pady=4,sticky="W") 
        ttk.Label(self.menuframe, textvariable=self.toI).grid(row=2,column=8,padx=4,pady=4,sticky="W") 
        ttk.Label(self.menuframe, textvariable=self.toD).grid(row=3,column=8,padx=4,pady=4,sticky="W")        
        ttk.Label(self.menuframe, textvariable=self.toPunit).grid(row=1,column=9,padx=4,pady=4,sticky="W") 
        ttk.Label(self.menuframe, textvariable=self.toIunit).grid(row=2,column=9,padx=4,pady=4,sticky="W") 
        ttk.Label(self.menuframe, textvariable=self.toDunit).grid(row=3,column=9,padx=4,pady=4,sticky="W") 
        ttk.Label(self.menuframe, text="              ").grid(row=4,column=8,padx=4,pady=4,sticky="W")

        #lower frame
        ttk.Radiobutton(self.lowerframe, text = "Seconds", variable=self.radioFromTime, value = "Seconds",command=self.fromUnitConvert).grid(row=0,column=1, sticky="NESW")
        ttk.Radiobutton(self.lowerframe, text = "Minutes", variable=self.radioFromTime, value = "Minutes",command=self.fromUnitConvert).grid(row=0,column=2,columnspan=2, sticky="NESW")         
        ttk.Radiobutton(self.lowerframe, text = "Independent", variable=self.radioFromType, value = "Independent",command=self.fromUnitConvert).grid(row=1,column=1, sticky="NESW")
        ttk.Radiobutton(self.lowerframe, text = "Dependent", variable=self.radioFromType, value = "Dependent",command=self.fromUnitConvert).grid(row=1,column=2,columnspan=2, sticky="NESW")        
        ttk.Label(self.lowerframe, text="                        ").grid(row=0,column=4,padx=4,pady=4,sticky="W")
        ttk.Label(self.lowerframe, text="                        ").grid(row=0,column=5,padx=4,pady=4,sticky="W")
        ttk.Radiobutton(self.lowerframe, text = "Seconds", variable=self.radioToTime, value = "Seconds",command=self.toUnitConvert).grid(row=0,column=6, sticky="NESW")
        ttk.Radiobutton(self.lowerframe, text = "Minutes", variable=self.radioToTime, value = "Minutes",command=self.toUnitConvert).grid(row=0,column=7,columnspan=2, sticky="NESW")         
        ttk.Radiobutton(self.lowerframe, text = "Independent", variable=self.radioToType, value = "Independent",command=self.toUnitConvert).grid(row=1,column=6, sticky="NESW")
        ttk.Radiobutton(self.lowerframe, text = "Dependent", variable=self.radioToType, value = "Dependent",command=self.toUnitConvert).grid(row=1,column=7,columnspan=2, sticky="NESW")

        #status bar        
        self.status_frame = tk.Frame(self.root)
        self.status = tk.Label(self.status_frame, textvariable=self.statustext,bg='light grey')
        self.status.pack(fill="both", expand=True)
        self.menuframe.grid(row=0, column=0, rowspan=1, sticky="NESW")
        self.lowerframe.grid(row=1, column=0, columnspan=1, sticky="NESW")
        self.status_frame.grid(row=2, column=0, columnspan=1, sticky="NESW")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def reset(self):
        self.fromP.insert(0, "1.7701")
        self.fromI.insert(0, "2.7706")
        self.fromD.insert(0, "0.1283")
        self.fromPunit.set("Kp")
        self.fromIunit.set("Ki (1/s)")
        self.fromDunit.set("Kd (s)")
        self.toPunit.set("Kc")
        self.toIunit.set("Ti (min/repeat)")
        self.toDunit.set("Td (min)")
        self.radioFromType.set("Independent")
        self.radioFromTime.set("Seconds")
        self.radioToType.set("Dependent")
        self.radioToTime.set("Minutes")
        self.statustext.set("Ready...                 ")
    
    def fromUnitConvert(self):
        if str(self.radioFromType.get())=="Independent" and str(self.radioFromTime.get())=="Seconds":
            self.fromPunit.set("Kp")
            self.fromIunit.set("Ki (1/s)")
            self.fromDunit.set("Kd (s)")
        elif str(self.radioFromType.get())=="Independent" and str(self.radioFromTime.get())=="Minutes":
            self.fromPunit.set("Kp")
            self.fromIunit.set("Ki (1/min)")
            self.fromDunit.set("Kd (min)")
        elif str(self.radioFromType.get())=="Dependent" and str(self.radioFromTime.get())=="Seconds":
            self.fromPunit.set("Kc")
            self.fromIunit.set("Ti (sec/repeat)")
            self.fromDunit.set("Td (sec)")
        elif str(self.radioFromType.get())=="Dependent" and str(self.radioFromTime.get())=="Minutes":
            self.fromPunit.set("Kc")
            self.fromIunit.set("Ti (min/repeat)")
            self.fromDunit.set("Td (min)")
        self.toP.set("")
        self.toI.set("")
        self.toD.set("")
        self.statustext.set("Ready...                 ")

    def toUnitConvert(self):
        if str(self.radioToType.get())=="Independent" and str(self.radioToTime.get())=="Seconds":
            self.toPunit.set("Kp")
            self.toIunit.set("Ki (1/s)")
            self.toDunit.set("Kd (s)")
        elif str(self.radioToType.get())=="Independent" and str(self.radioToTime.get())=="Minutes":
            self.toPunit.set("Kp")
            self.toIunit.set("Ki (1/min)")
            self.toDunit.set("Kd (min)")
        elif str(self.radioToType.get())=="Dependent" and str(self.radioToTime.get())=="Seconds":
            self.toPunit.set("Kc")
            self.toIunit.set("Ti (sec/repeat)")
            self.toDunit.set("Td (sec)")
        elif str(self.radioToType.get())=="Dependent" and str(self.radioToTime.get())=="Minutes":
            self.toPunit.set("Kc")
            self.toIunit.set("Ti (min/repeat)")
            self.toDunit.set("Td (min)")
        self.toP.set("")
        self.toI.set("")
        self.toD.set("")
        self.statustext.set("Ready...                 ")

    def convert(self,entry=0):     
        try:
            self.thisP=float(self.fromP.get()) 
            self.thisI=float(self.fromI.get()) 
            self.thisD=float(self.fromD.get()) 
            self.statustext.set("Converted                 ")
            #From Independent Seconds
            if str(self.radioFromType.get())=="Independent" and str(self.radioFromTime.get())=="Seconds":
                if str(self.radioToType.get())=="Independent" and str(self.radioToTime.get())=="Seconds":
                    self.toP.set(self.thisP)
                    self.toI.set(self.thisI)
                    self.toD.set(self.thisD)
                elif str(self.radioToType.get())=="Independent" and str(self.radioToTime.get())=="Minutes":
                    self.toP.set(self.thisP)
                    self.toI.set(round(self.thisI*60,5))
                    self.toD.set(round(self.thisD/60,5))
                elif str(self.radioToType.get())=="Dependent" and str(self.radioToTime.get())=="Seconds":
                    self.toP.set(self.thisP)
                    self.toI.set(round(self.thisP/self.thisI,5))
                    self.toD.set(round(self.thisD/self.thisP,5))
                elif str(self.radioToType.get())=="Dependent" and str(self.radioToTime.get())=="Minutes":
                    self.toP.set(self.thisP)
                    self.toI.set(round(self.thisP/(self.thisI*60),5))
                    self.toD.set(round(self.thisD/(self.thisP*60),5))
            
            #From Independent Minutes
            elif str(self.radioFromType.get())=="Independent" and str(self.radioFromTime.get())=="Minutes":
                if str(self.radioToType.get())=="Independent" and str(self.radioToTime.get())=="Seconds":
                    self.toP.set(self.thisP)
                    self.toI.set(round(self.thisI/60,5))
                    self.toD.set(round(self.thisD*60,5))
                elif str(self.radioToType.get())=="Independent" and str(self.radioToTime.get())=="Minutes":
                    self.toP.set(self.thisP)
                    self.toI.set(self.thisI)
                    self.toD.set(self.thisD)
                elif str(self.radioToType.get())=="Dependent" and str(self.radioToTime.get())=="Seconds":
                    self.toP.set(self.thisP)
                    self.toI.set(round(self.thisP/(self.thisI/60),5))
                    self.toD.set(round((self.thisD/self.thisP)*60,5))
                elif str(self.radioToType.get())=="Dependent" and str(self.radioToTime.get())=="Minutes":
                    self.toP.set(self.thisP)
                    self.toI.set(round(self.thisP/self.thisI,5))
                    self.toD.set(round(self.thisD/self.thisP,5))

            #From Dependent Seconds 
            if str(self.radioFromType.get())=="Dependent" and str(self.radioFromTime.get())=="Seconds":
                if str(self.radioToType.get())=="Dependent" and str(self.radioToTime.get())=="Seconds":
                    self.toP.set(self.thisP)
                    self.toI.set(self.thisI)
                    self.toD.set(self.thisD)
                elif str(self.radioToType.get())=="Dependent" and str(self.radioToTime.get())=="Minutes":
                    self.toP.set(self.thisP)
                    self.toI.set(round(self.thisI/60,5))
                    self.toD.set(round(self.thisD/60,5))
                elif str(self.radioToType.get())=="Independent" and str(self.radioToTime.get())=="Seconds":
                    self.toP.set(self.thisP)
                    self.toI.set(round(self.thisP/self.thisI,5))
                    self.toD.set(round(self.thisP*self.thisD,5))
                elif str(self.radioToType.get())=="Independent" and str(self.radioToTime.get())=="Minutes":
                    self.toP.set(self.thisP)
                    self.toI.set(round(60*(self.thisP/self.thisI),5))
                    self.toD.set(round(self.thisP*self.thisD/60,5))
            
            #From Dependent Minutes
            if str(self.radioFromType.get())=="Dependent" and str(self.radioFromTime.get())=="Minutes":
                if str(self.radioToType.get())=="Dependent" and str(self.radioToTime.get())=="Seconds":
                    self.toP.set(self.thisP)
                    self.toI.set(self.thisI*60)
                    self.toD.set(self.thisD*60)
                elif str(self.radioToType.get())=="Dependent" and str(self.radioToTime.get())=="Minutes":
                    self.toP.set(self.thisP)
                    self.toI.set(self.thisI)
                    self.toD.set(self.thisD)
                elif str(self.radioToType.get())=="Independent" and str(self.radioToTime.get())=="Seconds":
                    self.toP.set(self.thisP)
                    self.toI.set(round(self.thisP/(self.thisI*60),5))
                    self.toD.set(round(self.thisP*self.thisD*60,5))
                elif str(self.radioToType.get())=="Independent" and str(self.radioToTime.get())=="Minutes":
                    self.toP.set(self.thisP)
                    self.toI.set(round(self.thisP/self.thisI,5))
                    self.toD.set(round(self.thisP*self.thisD,5))

        except Exception as e:
            self.statustext.set('Error: ' + str(e))
        
home=gui()
home.root.mainloop()