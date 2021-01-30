import tkinter as tk
from tkinter import Entry, Grid, ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os


main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.title('text editor')
#############################main menu############################
navbar_menu = tk.Menu()
# nav bar 
file = tk.Menu(navbar_menu,tearoff=0)
edit = tk.Menu(navbar_menu,tearoff=0)
view = tk.Menu(navbar_menu,tearoff=0)
color_theme = tk.Menu(navbar_menu,tearoff=0)


# file icons 
new_icon = tk.PhotoImage(file='icons/new_file.png')
open_icon = tk.PhotoImage(file='icons/open.png')
save_icon = tk.PhotoImage(file='icons/save.png')
saveas_icon = tk.PhotoImage(file='icons/save_as.png')
exit_icon = tk.PhotoImage(file='icons/exit.png')


#edit icons#################
copy_icon = tk.PhotoImage(file='icons/copy.png')
cut_icon = tk.PhotoImage(file='icons/cut.png')
paste_icon = tk.PhotoImage(file='icons/paste.png')
clear_all_icon = tk.PhotoImage(file='icons/clear.png')
find_icon = tk.PhotoImage(file='icons/find.png')


#view icons########
tool_bar_icon = tk.PhotoImage(file='icons/tools.png')
status_bar_icon = tk.PhotoImage(file='icons/open.png')


# theme icons
light_default_icon = tk.PhotoImage(file="")
green_icon = tk.PhotoImage(file="")
black_icon = tk.PhotoImage(file="")
gray_icon = tk.PhotoImage(file="")



#cascade

navbar_menu.add_cascade(label="File", menu=file)
navbar_menu.add_cascade(label="Edit", menu=edit)
navbar_menu.add_cascade(label="View", menu=view)
navbar_menu.add_cascade(label="Theme", menu=color_theme)
# -------------------------------&&&&&&& End main menu&&&&&&---------------------

#############################toolbar bar###################################################################
tool_bar = ttk.Label(main_application,background='skyblue')
tool_bar.pack(side=tk.TOP,fill=tk.X)
font_family_var = tk.StringVar()
font_tuple = tk.font.families() #get all font families
#create select option for font family
font_box = ttk.Combobox(tool_bar, width=30,textvariable=font_family_var,state='readonly')
font_box['values'] = font_tuple
# font_box.current(1)
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0,column=0, padx=5,pady=25)



#size box

size_var =tk.IntVar()
#create select option for font size
font_size = ttk.Combobox(tool_bar,width=16,textvariable=size_var,state='readonly')
font_size['values'] = tuple(range(7,150))
font_size.current(4)
font_size.grid(row=0,column=1,padx=5)


#bold button

bold_icon = tk.PhotoImage(file='icons/bold.png')
italic_icon = tk.PhotoImage(file='icons/italic.png')
underline_icon = tk.PhotoImage(file='icons/underline.png')

boldbtn = ttk.Button(tool_bar,image=bold_icon)
boldbtn.grid(row=0,column=2,padx=5)
italicbtn = ttk.Button(tool_bar,image=italic_icon)
italicbtn.grid(row=0,column=3,padx=5)
underlinebtn = ttk.Button(tool_bar,image=underline_icon)
underlinebtn.grid(row=0,column=5,padx=5)


# font_color button 
font_color_icon = tk.PhotoImage(file='./icons/color_picker.png')
font_color_btn = ttk.Button(tool_bar,image=font_color_icon)
font_color_btn.grid(row=0,column=6,padx=5)


align_left_icon = tk.PhotoImage(file='icons/text-left.png')
align_center_icon = tk.PhotoImage(file='icons/text-center.png')
align_right_icon = tk.PhotoImage(file='icons/text-right.png')


align_left_btn = ttk.Button(tool_bar,image=align_left_icon)
align_left_btn.grid(row=0,column=7,padx=5)
align_center_btn = ttk.Button(tool_bar,image=align_center_icon)
align_center_btn.grid(row=0,column=8,padx=5)

align_right_btn = ttk.Button(tool_bar,image=align_right_icon)
align_right_btn.grid(row=0,column=9,padx=5)
# -------------------------------&&&&&&& End tools bar menu&&&&&&----------------------------------------------


#############################text editor#############################################################################
text_editor = tk.Text(main_application)
text_editor.config(wrap='word',relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)

text_editor.focus_set()
text_editor.pack(fill=tk.BOTH, expand=True)

scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)


## font family and font size functionality

current_font_family = "Arial"
current_font_size = 11
def change_font(event=None):
    global current_font_family
    current_font_family = font_family_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))

def change_font_size(event=None):
    global current_font_size
    current_font_size = font_size.get()
    text_editor.configure(font=(current_font_family,current_font_size))

font_box.bind("<<ComboboxSelected>>",change_font)
font_size.bind("<<ComboboxSelected>>", change_font_size)

#button functionality

#bold button fnctionality\
def bold_change():

    text_property = tk.font.Font(font=text_editor['font']).actual()
    print(text_property)
    if text_property['weight'] == 'normal':
        text_editor.configure(font=(current_font_family,current_font_size,'bold'))
    if text_property['weight'] == 'bold':
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

boldbtn.configure(command=bold_change)

def italic_change():
    text_property = tk.font.Font(font=text_editor['font']).actual()
    if text_property['slant'] == 'roman':
        text_editor.configure(font=(current_font_family,current_font_size,'italic'))
    if text_property['slant'] == 'italic':
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))
italicbtn.configure(command=italic_change)

def underline_change():
    text_property = tk.font.Font(font=text_editor['font']).actual()
    if text_property['underline'] == 0:
        text_editor.configure(font=(current_font_family,current_font_size,'underline'))
    if text_property['underline'] == 1:
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

underlinebtn.configure(command=underline_change)

#change font color functionallity

def  font_color_change():
    color_var = tk.colorchooser.askcolor()
    print(color_var)
    text_editor.configure(fg=color_var[1])

font_color_btn.configure(command=font_color_change)



#text align buttons

def left_align():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')
    
align_left_btn.configure(command=left_align)
def center_align():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT,text_content,'center')
    
align_center_btn.configure(command=center_align)
def right_align():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT,text_content,'right')
    
align_right_btn.configure(command=right_align)

text_editor.configure(font=('Arial',12))


# -------------------------------&&&&&&& End Text editor&&&&&&--------------------------------------------------















#############################main status bar #####################################################################

status_bar = ttk.Label(main_application,text='Status Bar')
status_bar.pack(side=tk.BOTTOM)
text_change = False
def count_change(event=None):
    global text_change
    if text_editor.edit_modified(): #check the editor modified or not
       text_change = True
       len_of_word=  len(text_editor.get(1.0,'end-1c').split())
       len_of_characters = len(text_editor.get(1.0,'end-1c'))
       status_bar.config(text=f"Characters : {len_of_characters} Words: {len_of_word}")
    text_editor.edit_modified(False)

text_editor.bind("<<Modified>>", count_change)    

# -------------------------------&&&&&&& End Status bar &&&&&&---------------------------------------------------------------














#############################main menu functinality############################3###################################################


url = ''
def new_file_func():
    global url
    url = ''
    text_editor.delete(1.0,tk.END)
#open functionality
def open_file_func(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('Text File','*.txt'),('All File', '*.*')))
    try:
        with open(url,'r') as rf:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,rf.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))


#save functionality
def save_file_func(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0,tk.END))
            with open(url,'w', encoding='utf-8') as wf:
                wf.write(content)
        else:
            url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text File', '.txt'),('All file','*.*')))
            content2 = text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()
    except:
        return

# save as functionality 
def save_as_func(event=None):
    global url
    try:
        content = text_editor.get(1.0,tk.END)
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text file', '.txt'),('All File','*.*')))
        url.write(content)
        url.close()
    except:
        return
    
    
# exit functionaity
def exit_func(event=None):
    global url, text_change
    try:
        if text_change:
            mbox = messagebox.askyesnocancel('warning','Do yu want to save file ?' )
            if mbox is True:
                if url:
                    content = text_editor.get(1.0,tk.END)
                    with open(url,'w', encoding='utf-8') as wf:
                        wf.write(content)
                        main_application.destroy()
                else:
                    content2 = str(text_editor.get(1.0,tk.END))
                    url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text file', '.txt'),('All File','*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
                    
            elif mbox is False:
                main_application.destroy()
            else:
                main_application.destroy()
    except:
        return
#--------------------------------------------------------------------------------------------
    
# file_content
file.add_command(label="New", image=new_icon, compound=tk.LEFT, accelerator='Ctrl+N', command=new_file_func)
file.add_command(label="Open", image=open_icon, compound=tk.LEFT, accelerator='Ctrl+O', command=open_file_func)
file.add_command(label="Save", image=save_icon, compound=tk.LEFT, accelerator='Ctrl+S',command=save_file_func)
file.add_command(label="Save As", image=saveas_icon, compound=tk.LEFT, accelerator='Ctrl+Shift+S',command=save_as_func)
file.add_command(label="Exit", image=exit_icon, compound=tk.LEFT, accelerator='Ctrl+Q', command=exit_func)


def text_find(event=None):
    def find_func():
        search_word = find_input.get()
        text_editor.tag_remove('match','1.0',tk.END)
        matches = 0
        if search_word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(search_word, start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f"{start_pos} + {len(search_word)}c"
                text_editor.tag_add('match',start_pos,end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match',foreground='green', background='yellow')
    def replace_func():
        search_word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0,tk.END)
        new_content = content.replace(search_word,replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)
        
        
        
    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0,0)
    
    #frame
    find_frame_box = ttk.LabelFrame(find_dialogue, text="Find/Replace")
    find_frame_box.pack(pady=20)
    
    #labels
    text_find_label = ttk.Label(find_frame_box, text="Find")
    text_replae_label = ttk.Label(find_frame_box, text='Replace:')
    
    #entry
    find_input = ttk.Entry(find_frame_box, width=16)
    replace_input = ttk.Entry(find_frame_box, width=16)
    
    #button
    find_btn = ttk.Button(find_frame_box, text='Find',command=find_func)
    replace_btn = ttk.Button(find_frame_box, text='Replace',command=replace_func)
    
    #label grid
    text_find_label.grid(row=0,column=0,padx=4,pady=4)
    text_replae_label.grid(row=1,column=0,padx=4,pady=4)
    
    #entruy gridd
    find_input.grid(row=0,column=1,padx=4,pady=4)
    replace_input.grid(row=1,column=1,padx=4,pady=4)
    
    #button grid
    find_btn.grid(row=2,column=0,padx=8,pady=4)
    replace_btn.grid(row=2,column=1,padx=8,pady=4)
    
    
    
    find_dialogue.mainloop()
# edit content#####

edit.add_command(label="Copy", image=copy_icon, compound=tk.LEFT, accelerator="Ctrl + C",command=lambda: text_editor.event_generate("<Control c>"))
edit.add_command(label="Cut", image=cut_icon, compound=tk.LEFT, accelerator="Ctrl + X",command=lambda:text_editor.event_generate('<Control x>'))
edit.add_command(label="Paste", image=paste_icon, compound=tk.LEFT, accelerator="Ctrl + V",command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label="Clear all", image=clear_all_icon, compound=tk.LEFT, accelerator="Ctrl + Space",command=lambda:text_editor.delete(1.0,tk.END))
edit.add_command(label="Find", image=find_icon, compound=tk.LEFT, accelerator="Ctrl + F" ,command=text_find)


#view check button
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
def hide_tools():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True
def hide_status():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True

#view content
# view.add_command(label="Tools", image=tool_bar_icon,compound=tk.LEFT, accelerator="Ctrl + C")
# view.add_command(label="Status", image=status_bar_icon,compound=tk.LEFT, accelerator="Ctrl + X")
view.add_checkbutton(label='Tools', onvalue=True,offvalue=0,variable=show_toolbar,image=tool_bar_icon,compound=tk.LEFT,command=hide_tools)
view.add_checkbutton(label='Status Bar',onvalue=1,offvalue=False,variable=show_statusbar, image=tool_bar_icon,compound=tk.LEFT,command=hide_status)





#content theme
theme_var = tk.StringVar()
theme_color_icon = (light_default_icon,green_icon,black_icon,green_icon)

color_dict = {
    'Light Default' : ('#000000','#ffffff'),
    'Green ' : ('green','black'),
    'Red' : ('red','black'),
    'Gray': ('gray', 'black')
}
# color theme
count = 0

for i in color_dict:
    color_theme.add_radiobutton(label=i,image=theme_color_icon[count],variable=theme_var,compound=tk.LEFT)
    count += 1



# -------------------------------&&&&&&& End main menu&&&&&&---------------------


main_application.config(menu=navbar_menu)
main_application.mainloop()