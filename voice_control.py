import recorder
import os

def control():
    apps = {
        "browser": 'YOUR_BROWSER_PATH',
        "code": 'CODE_EDITOR_PATH',
        "terminal": 'TERMINAL_PATH',
        "file explorer": 'FILE_EXPLORER_PATH',
        "Audio": 'AUDIO_PLAYER_PATH'
    }
    create = {
    	"folder":'mkdir',
    	"file":'touch'
    }
    command = recorder.record_audio("command.wav", 5, 44100)
    print("Command: " + command.lower())
    
    if "open" in command.lower():
        extract = command.split(" ")
        app = extract[-1].lower()
        print(f"app : {app}")
        
        if app in apps:
            os.system(apps[app])
            print(apps[app])
        elif app not in apps:
        	print(f"App {app} not found !")

    elif "create" in command.lower():
    	extract_func = command.split(" ")
    	func = extract_func[1]
    	name = extract_func[-1]
    	if func in create:
    		os.system(create[func]+f" {name}")
    		print(func+f" {name} created successfully")
control()
#you can add more commands
