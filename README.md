# Auto-Logger
This program is for the developers and the programmers who wish to log what they do with the output in the console. This program is specially developed for `debian based linux machines`. If you want for `MAC and Windows`, please let me know in the `issues` section of this repo.

**Feel free to Report any bugs or suggestions in `issues` section of this repo** :fire: :heart_eyes: 

## How should I Install it?

- Download this repo and run the setup.py file

```
/$: python setup.py
```

## How should I use this program?

    Usage: log [OPTIONS] [COMMAND]

        Options:
            Message log mode:
                [empty], -m, --message                  Type the log message and press 'Enter' to log 
                                                        into the file. Double tap 'Enter' to exit the 
                                                        program
                        Eg: log <empty>
                                $ log
                            log -m <message>
                                $ log -m This is an example message
                            log --message <message>
                                $ log --message This is an example message
                        
            Command log mode:
                [command], -c, --command                Type the command and it will be logged with 
                                                        output in terminal_log.txt file
                        Eg: log <command>
                                $ log npm install firebase
                            log -c <command>
                                $ log -c npm install firebase
                            log --command <command>
                                $ log --command npm install firebase

            Terminal mode:
                -t, --terminal                          Enter into terminal mode. The commands which you  
                                                        run will be logged with the output into 
                                                        terminal_log.txt file
                        Eg: $ log -t
                            $ log --terminal

                lm <message>                            If you want to log a message when you are in 
                                                        'Terminal mode', you can use this option
                        Eg: Assume you are in terminal mode 
                            $: lm This is the message to log
                    
        Additional Informations:
            ~ The output of the logs will be stored in 'AutoLogger' directory of your Home directory
            ~ Use 'exit()' in 'Terminal mode' to exit 'Terminal mode'

## Where to view my logs?

- The logs which you have created are stored in the file **log.txt** and **terminal_log.txt** inside the folder **AutoLogger** in your **Home** directory.
