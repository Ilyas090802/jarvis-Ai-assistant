def address_of_command(command,command1):
    list_command = {"web": 
                    {"youtube":                 "youtube.com",
                    "google":                   "google.com",
                    "hd movies 2":              "https://hdmovie2.media/"
                    },


                    "app"  :  
                    {"task manager":            "C:\Windows\System32\Taskmgr.exe",
                     "free_fire_bluestack":     "C:\Other data\Short cut to free fire\Free Fire MAX.lnk",
                     "cmd":                     "C:\Windows\System32\cmd.exe",
                     "control panel":           "C:\Windows\System32\control.exe",
                     "sys info":                "C:\Windows\System32\msinfo32.exe",
                     "screen saver":            "C:\Windows\System32\PhotoScreensaver.scr",
                     "reg edit":                "C:\Windows\System32\regedt32.exe",
                     "ribbon screen saver":     "C:\Windows\System32\Ribbons.scr",
                     "volume mixer":            "C:\Windows\System32\SndVol.exe",
                     "explorer":                "C:\Windows\explorer.exe",
                     "chrome":                  "C:\Program Files\Google\Chrome\Application\chrome.exe",
                     "opera":                   "G:\Programe files\Opera\opera.exe"
                    
                     },


                    "search in web":  
                    {"youtube":       "https://www.youtube.com/results?search_query=",
                    "google":         "https://www.google.com/search?q=",
                    }
                }
    address = list_command[command][command1]
    return f"{address}"