import PySimpleGUI as sg
import subprocess
import os.path
import _thread
import time

    
class AppWindow:    
    # init function
    def __init__(self,theme,font,image_dir,delaytime,testex='testing'):
        self.theme = theme
        self.font = font
        self.image = image_dir
        self.delaytime = delaytime
        self.test = testex
    
    # custom functions
    def getFile(self,file_list):
        extension = ".CR2"
        self.list_of_names = [
                        f
                        for f in file_list
                        if os.path.isfile(os.path.join(self.folderin, f))
                        and f.endswith((extension))
                    ]
        self.list_of_fnames = ['{0}/{1}'.format(self.folderin,name) for name in self.list_of_names]
    
    def showFiles(self):
        print(">>>>>>>>>>>>>>>>>>>>>>>>>")
        print("\nLIST OF FILES TO CONVERT:")
        for file in self.list_of_names:
            print(file)
        print("\n--------------------------------")
            
    def runTestCmd(self):
        test_exit=subprocess.call(['./test.sh',self.test])
        return test_exit
    
    def runShellScript(self):
        exitval=subprocess.call(['./CR2toX',self.folderin,self.list_of_fnames,self.folderout,self.form])
        return exitval
    
    def justwait(self):
        time.sleep(self.delaytime)
        
    # main function (gui window)
    def main(self):
        sg.theme(self.theme)
        
        layout_help=[
            [
                sg.Image(source=self.image)
            ],
            [
                sg.Text('''How to use
                        
                1) select Input directory where CR2 raw images are stored.
                
                2) select Output directory where 'target format' images will be saved.
                        
                3) select 'target format' for images.
                
                4) hit the Run button at the bottom.
                    You should be able to see the progress on the right panel.
                    
                    
                Note: hit the Stop button to abort run or Exit button to quit program.
                
                Write to ale.lagreca@gmail.com for any questions. Cheers''')
            ]
        ]
        
        layout_file_col=[
            [
                sg.Text("Input directory"),sg.In(size=(25, 1), 
                enable_events=True, key="-FOLDERIN-"),sg.FolderBrowse()
            ],
            [
                sg.Button('Deselect',key="-DESESELCT-"),sg.Button('Clear',key="-CLR-")
            ],
            [
                sg.Listbox(values=[], enable_events=True, size=(40, 20), 
                key="-FILELIST-",select_mode=sg.SELECT_MODE_MULTIPLE,
                horizontal_scroll = False)
            ],
            [
                sg.Text("Output directory"),sg.In(size=(25, 1), 
                enable_events=True,key="-FOLDEROUT-"),sg.FolderBrowse()
            ],
            [
                sg.Button('Clear',key="-CLR1-")  
            ],
            [
                sg.Text("Target format:"),sg.Combo(values=["jpeg","tiff","png","gif","jp2","pict","bmp","qtif","psd","sgi","tga"],
                default_value="jpeg",key="-FORMAT-",enable_events=True)
            ],
            [
                sg.Button('Run', size=(4, 1), button_color='white on green', key='-PROC-'),sg.Button('Exit')
            ],
            [
                sg.Sizer(h_pixels=0,v_pixels=0)
            ]
            ]
        
        layout_run_proc=[
            [sg.Output(size=(40,30), background_color="black")],
            
        ]
        
        layout_full=[
            [
                sg.Column(layout_help),
                sg.VSeparator(),
                sg.Column(layout_file_col),
                sg.VSeparator(),
                sg.Column(layout_run_proc)
            ]
        ]
        
        window=sg.Window(title="CR2 converter",layout=layout_full)
        
        run = False
        while True:
            event, values = window.read()
                
            if event in ("Exit",sg.WIN_CLOSED):  # close gui with these events
                break

            if event == "-FOLDERIN-":           # read input directory
                self.folderin = values["-FOLDERIN-"]
                try:
                    file_list = os.listdir(self.folderin)    # list files in input directory
                except:
                    file_list = []
                self.getFile(file_list)   # keep CR2 files only and append path
                window["-FILELIST-"].update(self.list_of_names)      # display file names in listbox
            
            elif event == "-FILELIST-":     # selection inside listbox (multiple enabled)
                try:
                    selected = window["-FILELIST-"].get()       # get selected names
                except:
                    selected = []
                self.getFile(selected)
            
            elif event == "-DESESELCT-":        # clear selection in listbox
                try:
                    self.getFile(file_list)
                    window["-FILELIST-"].update(self.list_of_names)
                except:
                    pass
                
            elif event == "-CLR-":      # clear input directory and listbox
                try:
                    window["-FOLDERIN-"].update([])
                    window["-FILELIST-"].update([])
                    del (file_list,self.folderin,self.list_of_names,self.list_of_fnames)
                except:
                    pass
            
            elif event == "-FOLDEROUT-":      # read output directory
                self.folderout = values["-FOLDEROUT-"]
            
            elif event == "-CLR1-":
                try:
                    window["-FOLDEROUT-"].update([])
                    del self.folderout
                except:
                    pass
            
            elif event == "-FORMAT-":
                self.form = values["-FORMAT-"] # get new value if changed
            
            if event == "-PROC-":       # start run (initial run = False)
                run = not run           # change run status
                if run == True:         # execute command
                    window["-PROC-"].update(text="Stop",button_color="white on red")
                    try:
                        self.folderin
                        self.folderout
                        # --------------- Next block runs command with list of files ---------------
                        print("\nrunning...")
                        self.showFiles()
                        self.form=window["-FORMAT-"].get()
                        print("FORMAT: "+self.form)
                        try:
                            exitval=self.runTestCmd()   # uncomment to run test script (comment next line)
                            #self.runShellScript()   # actual bash script with sips cmd
                            if exitval == 0:
                                print("\n<<<<<<<<<<<<<<<<<<<<<<<<")
                                print("finished...")
                                self.justwait()
                                window['-PROC-'].update(text='Run', button_color='white on green')
                            else:
                                print('error...')
                                sg.popup('''Something is wrong with your files.
Please, check file properties.''',
                                keep_on_top=True,font=self.font,title="Error message",no_titlebar=False,button_color=("sienna1"))
                                window['-PROC-'].update(text='Run', button_color='white on green')
                                run = not run
                        except:
                            print('error...')
                            sg.popup('''Something is wrong with your files.
Please, check file properties.''',
                            keep_on_top=True,font=self.font,title="Error message",no_titlebar=False,button_color=("sienna1"))
                            window['-PROC-'].update(text='Run', button_color='white on green')
                            run = not run
                            
                    except:
                        sg.popup('''Select both input and output directories before running''',
                        keep_on_top=True,font=self.font,title="Missing directory",no_titlebar=False,button_color=("sienna2"))     # if input or output directories are not provided
                        window['-PROC-'].update(text='Run', button_color='white on green')
                        run = not run
                    # --------------- ------------------------------------------ ---------------
        window.close()
    
    
if __name__ == '__main__':
    
    # variables
    window_appearence='Dark'
    font_and_size=('Helvetica 12')
    path_to_image='images/cr2icon_256x256x32.png'
    button_change_delay=2

    # launch gui
    win = AppWindow(window_appearence,font_and_size,path_to_image,button_change_delay)
    win.main()