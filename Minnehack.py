#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
import speech_recognition as sr
def getListen(recognizer):
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return ":("
    except sr.RequestError:
        return ">:("
def fill(arr, num, val):
    for i in range(num):
        arr.append(val)
def stringMatch(string, list2):
    for stre in list2:
        if stre in string:
            return True
    return False 
def stringMatchAll(string, list2):
    DECISIONOFALIFETIMEPLEASEHELPME = False
    for stre in list2:
        if stre in string:
            DECISIONOFALIFETIMEPLEASEHELPME = True
        else:
            DECISIONOFALIFETIMEPLEASEHELPME = False        

    return DECISIONOFALIFETIMEPLEASEHELPME
def yesNoVerify(recognizer):
    result = getListen(recognizer)
    if stringMatch(result, ["yes", "yeah", "definitely", "totally"]):
        return True
    elif stringMatch(result, ["no", "nah", "nope"]):
        return False
    else:
        print("Invalid voice input, please try again!")
        yesNoVerify(recognizer)
def resultCheckOR(recognizer, keys, funcs, params):
    fill(params, len(funcs) - len(params), [])
    result = getListen(recognizer)
    for i, keylist in enumerate(keys):
        for key in keylist:
            if stringMatch(result, key):
                return funcs[i](*params[i])    
    print("Invalid voice input, please retry.")
    resultCheck(recognizer, keys, funcs, params)
def resultCheckAND(recognizer, keys, funcs, params):
    fill(params, len(funcs) - len(params), [])
    result = getListen(recognizer)
    for i, keylist in enumerate(keys):
        for key in keylist:
            if stringMatchAll(result, key):
                return funcs[i](*params[i])    
    print("Invalid voice input, please retry.")
    resultCheck(recognizer, keys, funcs, params)
    
def resultCheckANDOR(recognizer, keyANDList, keyOR, funcs, ANDParamList, ORParamaList):
    result = getListen(recognizer)
    for i, keylist in enumerate(keyANDList):
        for key in keylist:
            if stringMatchAll(result, keylist):
                return funcs[i](*ANDParamList[i])
            elif stringMatch(result, keyOR[i]):
                return funcs[i](*ORParamaList[i])
    print("Invalid voice input, please retry.")
    resultCheckANDOR(recognizer, keyANDList, keyOR, funcs, ANDParamList, ORParamaList)
def returningFalse():
    return False
def returningTrue():
    return True
def category1():
    print("From your responses, it can be concluded that you are experiencing a Category 1 Mild Traumatic Brain Injury")
    print("The best way to treat this sort of in jury is to simply rest and not rush back into the activity that caused the injury.")
    print("If any other vision impediment or mechanical problems occur, consult a physician immediately.")
def category2():
    print("From your responses, it can be concluded that you are experiencing a Category 2 Mild Traumatic Brain Injury")
    print("Once the effects have lingered past a half hour, aspirin or ibuprofen can be taken to reduce the pain of headaches.")
    print("If the condition worsens over time, medical attention is required immediately. ")

def category3():
    print("From your responses, it can be concluded that you are experiencing a Category 3 Mild Traumatic Brain Injury")
    print("Immediate medical attention is required.")
    print("If further medical attention is not met, early signs of brain damage could be seen.")

def migraine():
    print("From your responses, it can be concluded that you are experiencing a Migraine")
    print("Migraines are often undiagnosed and untreated. If you regularly experience signs and symptoms of migraine attacks, keep a record of your attacks and how you treated them. ")
    print("Make an appointment with your doctor to discuss your headaches.")

def blood_clot():
    print("From your responses, it can be concluded that you are experiencing a Thrombus in the Brain.")
    print("In the event of a blood clot, alarming emergency services is imperative in saving one's life.")
    print("There is a narroww time window during which clot-busting drugs may be used to dissolve the blood clot and reverse a stroke.")

r = sr.Recognizer()
print("What is the issue?")
check = resultCheckANDOR(r, 
    [["head", "hurts"]],
        [["head", "aches"]],
        [returningTrue],
        [[]],
        [[]]
    )
if check:
    print("Were you ever unconcious?")
    check = resultCheckOR(r, [
        ["yeah", "yes"],
        ["no", "nah", "nope"]
        ], [returningTrue, returningFalse], [
            [], 
            []
            ])
    if check:
        print("Approximately how many minutes were you unconcious for?")
        res = getListen(r)
        def fetchFirstInt(string):
            dlist = string.split()
            for stre in dlist:
                if stre.isdigit():
                    return int(stre)
            return False
        num = fetchFirstInt(res)
        if num < 6:
            category2()
        else:
            category3()
    else:
        print("Did you experience some form of head trauma?")
        check = resultCheckOR(r, [
        ["yeah", "yes"],
        ["no", "nah", "nope"]
        ], [returningTrue, returningFalse], [
            [], 
            []
            ])
        if check:
            category1()
        else:
            print("What are some of your symptoms?")
            check = resultCheckOR(r, [
                ["pain", "lightheadedness", "blurred vision", "sensitivity"],
                ["weakness", "sudden", "severe", "headaches", "confusion", "numbness", "difficulty"]
                ], [returningTrue, returningFalse], [
                    [], 
                    []
                    ])
            if check:
                migraine()
            else:
                blood_clot()
