
TODO: replace old router functionality into 
TODO: get: command recog, face recog , automouse Inits.
TODO: create a global command manager(for commands to UI on stage status)
TODO: >>> get commands module: simple hand for ok / Cancel and double hand for Mode change / Log out


>>> App cycle [{'R1': 'DIGITS', 'R2': 'CMDS',
                       'R3': 'FACE-REC', 'R4': 'AUTO-MOUSE',
                       'R5': 'SLEEP','R6': 'OFFLINE'}]

> CMDS > {[LH Open: 'Y'], [LH Closed: 'N'], 
> (combo): [LH-RH Open: 'CHANGE_MODE?'], [LH-RH Closed: 'LOGOUT'], 
> [LH-RH Pointer: 'Auto-mouse']}

> 6 modes :: 3 types of commands DIGITS, SINGLE, COMBO, 

> 0: LogIn == ClockIn { this happens on face recognition in cold}
> 1: once data fetch to API call, offers clock in => CMDS (Y/N)
>   N: auto-Face-mode, Y: Clock-in: Select from menu opt [Ready, lunch, break, logout]

> one hnd alone dots on LH RH respective color and change when both hands on screen, change color when command is accepted type animation to green
> auto perceive both hands change mode command and change color of dots when 2 hands on screen!
> sleep mode shows tutorial page

> # //> COMMAND DICTIONARY GUIDE

# //> <<< LOGIC FLOW RULES >>> [HINTS BASIS] PLUS [ROUTER SCHEMA]
# //> ** [ 0 ] FACE_RECOGNITION ] FROM START UP DEFAULT
# //> ** [ 1 ] LEFT HAND ] DIGITS COMMANDS FOR MENU SELECTION[ONE OF MAX 6 OPTS]**
# //> ** [ 2 ] LEFT HAND ] OPEN / CLOSE > UP / DOWN FROM MULTI-SELECTION
# //> ** [ 3 ] LEFT HAND ] CLOSE 5 SECS(4 ROUNDS ON PHASE) GETS LOG_OUT ACTION BACK TO FACE_RECOGNITION MODE
# //> ** [ 4 ] LEFT HAND ] OPEN 5 SECS(4 ROUNDS ON PHASE) GETS MODE_CHANGE ACTION
# //> ** [ 5 ] LEFT HAND ] POINTER 5 SECS(4 ROUNDS ON PHASE) GETS BACK_SELECTION ACTION
# //> ** [ 6 ] RIGHT HAND ] OK / CLOSE > Y / N RESPECTIVELY
# //> ** [ 7 ] RIGHT HAND ] POINTER 5 SECS(4 ROUNDS ON PHASE) GETS AUTO_MOUSE MODE
# //> ** [ 8 ] RIGHT HAND ] AUTO_MOSE MODE OK 5 SECS(4 ROUNDS ON PHASE) GETS [GENERAL_MENU] MODE(LEFT HAND DIGITS)
# //> ** [ 9 ] RIGHT HAND ]