
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