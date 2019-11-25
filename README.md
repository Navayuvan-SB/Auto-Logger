# Auto-Logger
This Application is for the developers and the programmers who wish to log what they do with the output in the console. This Application is currently developed for `debian based linux machines`. If you want for `MAC and Windows`, please let me know in the `issues` section of this repo.

**Feel free to Report any bugs or suggestions in `issues` section of this repo** :fire: :heart_eyes: 

## How should I Install it?

- This Application runs on python 3.x 
- Download this repo and run the setup.py file

```
$: python setup.py
$: python3 setup.py
```

## How should I use this Application?

    Usage: log [OPTIONS] [COMMAND]

        Options:
            Message log mode:
                [empty], -m, --message                  Type the log message and press 'Enter' to log 
                                                        into the file. Double tap 'Enter' to exit the 
                                                        Application
                        Eg: log <empty>
                                $ log
                            log -m <message>
                                $ log -m This is an example message
                            log --message <message>
                                $ log --message This is an example message
                        
            Command log mode:
                -c, --command                           Type the command and it will be logged with 
                                                        output in terminal_log.txt file
                        Eg: log -c <command>
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

## License
Auto Logger is licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for the full license text.
```
   Copyright © Cypher Source

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```