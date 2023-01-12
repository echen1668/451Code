#Eric Chen
# ID: LD19338

# FM's in Figure 1

def automatonM1(InputString): #function for M1
    EndState = 'q0' #start state
    for i in InputString:
        #Transition function
        if EndState == 'q0' and i == '0':
            EndState = 'q1'
        elif EndState == 'q0' and i == '1':
            EndState = 'q0'
        elif EndState == 'q1' and i == '0':
            EndState = 'q0'
        elif EndState == 'q1' and i == '1':
            EndState = 'q1'
    if EndState in ['q0']:
        AcceptFlag = True
    else:
        AcceptFlag = False
    return AcceptFlag, EndState

def automatonM2(InputString): #function for M2
    EndState = 'q0' #start state
    for i in InputString:
        #Transition function
        if EndState == 'q0' and i == '0':
            EndState = 'q1'
        elif EndState == 'q0' and i == '1':
            EndState = 'q0'
        elif EndState == 'q1' and i == '0':
            EndState = 'q0'
        elif EndState == 'q1' and i == '1':
            EndState = 'q1'
    if EndState in ['q1']:
        AcceptFlag = True
    else:
        AcceptFlag = False
    return AcceptFlag, EndState

def automatonM3(InputString): #function for M3
    EndState = 'q0' #start state
    for i in InputString:
        #Transition function
        if EndState == 'q0' and i == '0':
            EndState = 'q0'
        elif EndState == 'q0' and i == '1':
            EndState = 'q1'
        elif EndState == 'q1' and i == '0':
            EndState = 'q1'
        elif EndState == 'q1' and i == '1':
            EndState = 'q0'
    if EndState in ['q0']:
        AcceptFlag = True
    else:
        AcceptFlag = False
    return AcceptFlag, EndState

def automatonM4(InputString): #function for M4
    EndState = 'q0' #start state
    for i in InputString:
        #Transition function
        if EndState == 'q0' and i == '0':
            EndState = 'q0'
        elif EndState == 'q0' and i == '1':
            EndState = 'q1'
        elif EndState == 'q1' and i == '0':
            EndState = 'q1'
        elif EndState == 'q1' and i == '1':
            EndState = 'q0'
    if EndState in ['q1']:
        AcceptFlag = True
    else:
        AcceptFlag = False
    return AcceptFlag, EndState

#_______________________________________________________________________________________________________________________
# FM's in Figure 2

def transitionFunction(startState, InputString): #tranistion function for M5, M6, M7, and M8
    state = startState
    for i in InputString:
        #Transition function
        if state == 'q0' and i == '0':
            state = 'q1'
        elif state == 'q0' and i == '1':
            state = 'q3'
        elif state == 'q1' and i == '0':
            state = 'q0'
        elif state == 'q1' and i == '1':
            state = 'q2'
        elif state == 'q2' and i == '0':
            state = 'q3'
        elif state == 'q2' and i == '1':
            state = 'q1'
        elif state == 'q3' and i == '0':
            state = 'q2'
        elif state == 'q3' and i == '1':
            state = 'q0'
    return state


def automatonM5(InputString): #function for M5
    EndState = 'q0' #start state
    EndState = transitionFunction(EndState, InputString) #Transition function called
    if EndState in ['q0']:
        AcceptFlag = True
    else:
        AcceptFlag = False
    return AcceptFlag, EndState

def automatonM6(InputString): #function for M6
    EndState = 'q0' #start state
    EndState = transitionFunction(EndState, InputString) #Transition function called
    if EndState in ['q1']:
        AcceptFlag = True
    else:
        AcceptFlag = False
    return AcceptFlag, EndState

def automatonM7(InputString): #function for M7
    EndState = 'q0' #start state
    EndState = transitionFunction(EndState, InputString) #Transition function called
    if EndState in ['q3']:
        AcceptFlag = True
    else:
        AcceptFlag = False
    return AcceptFlag, EndState

def automatonM8(InputString): #function for M8
    EndState = 'q0' #start state
    EndState = transitionFunction(EndState, InputString) #Transition function called
    if EndState in ['q2']:
        AcceptFlag = True
    else:
        AcceptFlag = False
    return AcceptFlag, EndState

#_______________________________________________________________________________________________________________________
# FM's in Figure 3

def transitionFunction2(startState, InputString): #tranistion function for M9 and M10
    state = startState
    for i in InputString:
        #Transition function
        if state == 'q0' and i == '0':
            state = 'q1'
        elif state == 'q0' and i == '1':
            state = 'q3'
        elif state == 'q1' and i == '0':
            state = 'q1'
        elif state == 'q1' and i == '1':
            state = 'q2'
        elif state == 'q2' and i == '0':
            state = 'q1'
        elif state == 'q2' and i == '1':
            state = 'q2'
        elif state == 'q3' and i == '0':
            state = 'q3'
        elif state == 'q3' and i == '1':
            state = 'q3'
    return state

def automatonM9(InputString): #function for M9
    EndState = 'q0' #start state
    EndState = transitionFunction2(EndState, InputString) #Transition function called
    if EndState in ['q2']:
        AcceptFlag = True
    else:
        AcceptFlag = False
    return AcceptFlag, EndState

def automatonM10(InputString): #function for M10
    EndState = 'q0' #start state
    EndState = transitionFunction2(EndState, InputString) #Transition function called
    if EndState in ['q0', 'q1', 'q3']:
        AcceptFlag = True
    else:
        AcceptFlag = False
    return AcceptFlag, EndState

#_______________________________________________________________________________________________________________________
# FM's in Figure 4

def transistionFunctionNFA(state, InputString, possibleEndStates):
    if len(InputString) == 0:
        possibleEndStates.append(state)
        return state
    # Transition function
    if state == 'q0' and InputString[0] == '0':
        transistionFunctionNFA('q0', InputString[1:], possibleEndStates)
    elif state == 'q0' and InputString[0] == '1':
        transistionFunctionNFA('q0', InputString[1:], possibleEndStates)
        transistionFunctionNFA('q1', InputString[1:], possibleEndStates)
    elif state == 'q1' and InputString[0] == '0':
        transistionFunctionNFA('q2', InputString[1:], possibleEndStates)
    elif state == 'q1' and InputString[0] == '1':
        transistionFunctionNFA('q2', InputString[1:], possibleEndStates)
    elif state == 'q2':
        return 'dead'

def automatonN(InputString): #function for N
    EndState = 'q0' #start state
    possibleEndStates = []
    transistionFunctionNFA(EndState, InputString, possibleEndStates) #Transition function called
    EndState = possibleEndStates
    if 'q2' in EndState:
        AcceptFlag = True
    else:
        AcceptFlag = False
    return AcceptFlag, EndState

def automatonM(InputString): #function for M
    EndState = 'q0' #start state
    for i in InputString:
        #Transition function
        if EndState == 'q0' and i == '0':
            EndState = 'q0'
        elif EndState == 'q0' and i == '1':
            EndState = 'q1'
        elif EndState == 'q1' and i == '0':
            EndState = 'q2'
        elif EndState == 'q1' and i == '1':
            EndState = 'q3'
        elif EndState == 'q2' and i == '0':
            EndState = 'q0'
        elif EndState == 'q2' and i == '1':
            EndState = 'q1'
        elif EndState == 'q3' and i == '0':
            EndState = 'q2'
        elif EndState == 'q3' and i == '1':
            EndState = 'q3'
    if EndState in ['q2', 'q3']:
        AcceptFlag = True
    else:
        AcceptFlag = False
    return AcceptFlag, EndState

if __name__ == '__main__':
    print("Compare NFA N and DFA M")
    print("Output for 110")
    print("NFA N:", automatonN("110"))
    print("DFA M:", automatonM("110"))
    print("Output for 010")
    print("NFA N:", automatonN("010"))
    print("DFA M:", automatonM("010"))
    print("Output for 111")
    print("NFA N:", automatonN("111"))
    print("DFA M:", automatonM("111"))
    print("Output for 011")
    print("NFA N:", automatonN("011"))
    print("DFA M:", automatonM("011"))
    print("Output for 1011")
    print("NFA N:", automatonN("1011"))
    print("DFA M:", automatonM("1011"))
    print("Output for 100")
    print("NFA N:", automatonN("100"))
    print("DFA M:", automatonM("100"))
    print("Output for 000")
    print("NFA N:", automatonN("000"))
    print("DFA M:", automatonM("000"))
    print("Output for 001")
    print("NFA N:", automatonN("001"))
    print("DFA M:", automatonM("001"))
    print("Output for 101")
    print("NFA N:", automatonN("101"))
    print("DFA M:", automatonM("101"))
    print("Output for 0100")
    print("NFA N:", automatonN("0100"))
    print("DFA M:", automatonM("0100"))

