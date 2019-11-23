# Auto-Logger
This program is for the developers and the programmers who wish to log what they do with the output in the console.

**Feel free to Report any bugs or suggestions in `issues` section of this repo** :fire: :heart_eyes: 

## How should I Install it?

- Download this repo and run the setup.py file

```
/$: python setup.py
```

## How should I use this program?

    Usage: log [OPTIONS] [COMMAND]

    Options:
        [empty], -m, --message                  Type the log message and press 'Enter' to log into the 
                                                file. Double tap 'Enter' to exit the program
                Eg: log <empty>
                        $ log
                    log -m <message>
                        $ log -m This is an example message
                    log --message <message>
                        $ log --message This is an example message
                
        
        [command], -c, --command                Type the command and it will be logged with the output in
                                                my_terminal_log.txt file
                Eg: log <command>
                        $ log npm install firebase
                    log -c <command>
                        $ log -c npm install firebase
                    log --command <command>
                        $ log --command npm install firebase

        -t, --terminal                          Enter into terminal mode. The commands which you run will 
                                                be logged with the output into my_terminal_log.txt file
                Eg: $ log -t
                    $ log --terminal

    Additional Informations:
        ~ The output of the logs will be stored in 'AutoLogger' directory of your Home directory
        ~ Use 'exit()' in 'Terminal mode' to exit 'Terminal mode'

## Where to view my logs?

- The logs which you have created are stored in the file **my_log.txt** inside the folder **AutoLogger** in your **Home** directory.
