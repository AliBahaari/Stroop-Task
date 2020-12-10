#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.6),
    on May 12, 2019, at 21:35
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.0.6'
expName = 'Main'  # from the Builder filename that created this script
expInfo = {'participant': 'John Doe', 'session': 'Test'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='F:\\Stroop\\Main.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1366, 768], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "praInstruction"
praInstructionClock = core.Clock()
praText = visual.TextStim(win=win, name='praText',
    text='در این آزمون ما در پی سنجش سرعت پاسخگویی شما به رنگها هستیم.\nشما باید با سریعترین حالت ممکن به رنگها پاسخ و دکمه\u200cی مناسب آن را را فشار بدهید.\nاز چهار رنگ زرد، قرمز، آبی و سبز در این آزمون استفاده شده است.\nابتدا کمی تمرین کنیم. \nلطفا به رنگ اشکال پاسخ بدهید.\n',
    font='IRANSans',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=0.0);

# Initialize components for Routine "practice"
practiceClock = core.Clock()
praShape = visual.Rect(
    win=win, name='praShape',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "praAgain"
praAgainClock = core.Clock()

praAgainText = visual.TextStim(win=win, name='praAgainText',
    text='آیا نیاز به تمرین بیشتر دارید؟',
    font='IRANSans',
    pos=(0, 0), height=0.065, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=-1.0);

# Initialize components for Routine "instruction"
instructionClock = core.Clock()
instructionText = visual.TextStim(win=win, name='instructionText',
    text='در این قسمت به جای اشکال از کلمات استفاده شده است.\nکلمات را نادیده بگیرید و فقط به رنگ پاسخ بدهید.\n',
    font='IRANSans',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
targetText = visual.TextStim(win=win, name='targetText',
    text='default text',
    font='IRANSans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=0.0);

# Initialize components for Routine "trialEnd"
trialEndClock = core.Clock()
trialEndText = visual.TextStim(win=win, name='trialEndText',
    text=' از همکاری شما در این پژوهش صمیمانه متشکریم.',
    font='IRANSans',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "praInstruction"-------
t = 0
praInstructionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
praInsKeboard = event.BuilderKeyResponse()
# keep track of which components have finished
praInstructionComponents = [praText, praInsKeboard]
for thisComponent in praInstructionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "praInstruction"-------
while continueRoutine:
    # get current time
    t = praInstructionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *praText* updates
    if t >= 0.0 and praText.status == NOT_STARTED:
        # keep track of start time/frame for later
        praText.tStart = t
        praText.frameNStart = frameN  # exact frame index
        praText.setAutoDraw(True)
    
    # *praInsKeboard* updates
    if t >= 0.0 and praInsKeboard.status == NOT_STARTED:
        # keep track of start time/frame for later
        praInsKeboard.tStart = t
        praInsKeboard.frameNStart = frameN  # exact frame index
        praInsKeboard.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if praInsKeboard.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in praInstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "praInstruction"-------
for thisComponent in praInstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "praInstruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
praAgainLoop = data.TrialHandler(nReps=3, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='praAgainLoop')
thisExp.addLoop(praAgainLoop)  # add the loop to the experiment
thisPraAgainLoop = praAgainLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPraAgainLoop.rgb)
if thisPraAgainLoop != None:
    for paramName in thisPraAgainLoop:
        exec('{} = thisPraAgainLoop[paramName]'.format(paramName))

for thisPraAgainLoop in praAgainLoop:
    currentLoop = praAgainLoop
    # abbreviate parameter names if possible (e.g. rgb = thisPraAgainLoop.rgb)
    if thisPraAgainLoop != None:
        for paramName in thisPraAgainLoop:
            exec('{} = thisPraAgainLoop[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    practices = data.TrialHandler(nReps=5, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('ShapesColors.xlsx'),
        seed=None, name='practices')
    thisExp.addLoop(practices)  # add the loop to the experiment
    thisPractice = practices.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
    if thisPractice != None:
        for paramName in thisPractice:
            exec('{} = thisPractice[paramName]'.format(paramName))
    
    for thisPractice in practices:
        currentLoop = practices
        # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
        if thisPractice != None:
            for paramName in thisPractice:
                exec('{} = thisPractice[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "practice"-------
        t = 0
        practiceClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        praKeyboard = event.BuilderKeyResponse()
        praShape.setFillColor(stimShapeColor)
        praShape.setLineColor(stimShapeColor)
        # keep track of which components have finished
        practiceComponents = [praKeyboard, praShape]
        for thisComponent in practiceComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "practice"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = practiceClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *praKeyboard* updates
            if t >= 0.5 and praKeyboard.status == NOT_STARTED:
                # keep track of start time/frame for later
                praKeyboard.tStart = t
                praKeyboard.frameNStart = frameN  # exact frame index
                praKeyboard.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(praKeyboard.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 0.5 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if praKeyboard.status == STARTED and t >= frameRemains:
                praKeyboard.status = FINISHED
            if praKeyboard.status == STARTED:
                theseKeys = event.getKeys(keyList=['a', 's', 'k', 'l'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if praKeyboard.keys == []:  # then this was the first keypress
                        praKeyboard.keys = theseKeys[0]  # just the first key pressed
                        praKeyboard.rt = praKeyboard.clock.getTime()
                        # a response ends the routine
                        continueRoutine = False
            
            # *praShape* updates
            if t >= 0.5 and praShape.status == NOT_STARTED:
                # keep track of start time/frame for later
                praShape.tStart = t
                praShape.frameNStart = frameN  # exact frame index
                praShape.setAutoDraw(True)
            frameRemains = 0.5 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if praShape.status == STARTED and t >= frameRemains:
                praShape.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practiceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "practice"-------
        for thisComponent in practiceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if praKeyboard.keys in ['', [], None]:  # No response was made
            praKeyboard.keys=None
        practices.addData('praKeyboard.keys',praKeyboard.keys)
        if praKeyboard.keys != None:  # we had a response
            practices.addData('praKeyboard.rt', praKeyboard.rt)
    # completed 5 repeats of 'practices'
    
    
    # ------Prepare to start Routine "praAgain"-------
    t = 0
    praAgainClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    
    praAgainKeyboard = event.BuilderKeyResponse()
    # keep track of which components have finished
    praAgainComponents = [praAgainText, praAgainKeyboard]
    for thisComponent in praAgainComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "praAgain"-------
    while continueRoutine:
        # get current time
        t = praAgainClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *praAgainText* updates
        if t >= 0.0 and praAgainText.status == NOT_STARTED:
            # keep track of start time/frame for later
            praAgainText.tStart = t
            praAgainText.frameNStart = frameN  # exact frame index
            praAgainText.setAutoDraw(True)
        
        # *praAgainKeyboard* updates
        if t >= 0.0 and praAgainKeyboard.status == NOT_STARTED:
            # keep track of start time/frame for later
            praAgainKeyboard.tStart = t
            praAgainKeyboard.frameNStart = frameN  # exact frame index
            praAgainKeyboard.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(praAgainKeyboard.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if praAgainKeyboard.status == STARTED:
            theseKeys = event.getKeys(keyList=['y', 'n'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if praAgainKeyboard.keys == []:  # then this was the first keypress
                    praAgainKeyboard.keys = theseKeys[0]  # just the first key pressed
                    praAgainKeyboard.rt = praAgainKeyboard.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in praAgainComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "praAgain"-------
    for thisComponent in praAgainComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if praAgainKeyboard.keys == 'n' :
        praAgainLoop.finished = True
    else :
        pass
    # check responses
    if praAgainKeyboard.keys in ['', [], None]:  # No response was made
        praAgainKeyboard.keys=None
    praAgainLoop.addData('praAgainKeyboard.keys',praAgainKeyboard.keys)
    if praAgainKeyboard.keys != None:  # we had a response
        praAgainLoop.addData('praAgainKeyboard.rt', praAgainKeyboard.rt)
    # the Routine "praAgain" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 3 repeats of 'praAgainLoop'


# ------Prepare to start Routine "instruction"-------
t = 0
instructionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
instructionKeyboard = event.BuilderKeyResponse()
# keep track of which components have finished
instructionComponents = [instructionText, instructionKeyboard]
for thisComponent in instructionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instruction"-------
while continueRoutine:
    # get current time
    t = instructionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructionText* updates
    if t >= 0.0 and instructionText.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructionText.tStart = t
        instructionText.frameNStart = frameN  # exact frame index
        instructionText.setAutoDraw(True)
    
    # *instructionKeyboard* updates
    if t >= 0.0 and instructionKeyboard.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructionKeyboard.tStart = t
        instructionKeyboard.frameNStart = frameN  # exact frame index
        instructionKeyboard.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if instructionKeyboard.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction"-------
for thisComponent in instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=10, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('WordsColors.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    targetText.setColor(stimColor, colorSpace='rgb')
    targetText.setText(stimText)
    respKeyboard = event.BuilderKeyResponse()
    # keep track of which components have finished
    trialComponents = [targetText, respKeyboard]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *targetText* updates
        if t >= 0.50 and targetText.status == NOT_STARTED:
            # keep track of start time/frame for later
            targetText.tStart = t
            targetText.frameNStart = frameN  # exact frame index
            targetText.setAutoDraw(True)
        frameRemains = 0.50 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if targetText.status == STARTED and t >= frameRemains:
            targetText.setAutoDraw(False)
        
        # *respKeyboard* updates
        if t >= 0.50 and respKeyboard.status == NOT_STARTED:
            # keep track of start time/frame for later
            respKeyboard.tStart = t
            respKeyboard.frameNStart = frameN  # exact frame index
            respKeyboard.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(respKeyboard.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.50 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if respKeyboard.status == STARTED and t >= frameRemains:
            respKeyboard.status = FINISHED
        if respKeyboard.status == STARTED:
            theseKeys = event.getKeys(keyList=['a', 's', 'k', 'l'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if respKeyboard.keys == []:  # then this was the first keypress
                    respKeyboard.keys = theseKeys[0]  # just the first key pressed
                    respKeyboard.rt = respKeyboard.clock.getTime()
                    # was this 'correct'?
                    if (respKeyboard.keys == str(corrAns)) or (respKeyboard.keys == corrAns):
                        respKeyboard.corr = 1
                    else:
                        respKeyboard.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if respKeyboard.keys in ['', [], None]:  # No response was made
        respKeyboard.keys=None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           respKeyboard.corr = 1;  # correct non-response
        else:
           respKeyboard.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('respKeyboard.keys',respKeyboard.keys)
    trials.addData('respKeyboard.corr', respKeyboard.corr)
    if respKeyboard.keys != None:  # we had a response
        trials.addData('respKeyboard.rt', respKeyboard.rt)
    thisExp.nextEntry()
    
# completed 10 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "trialEnd"-------
t = 0
trialEndClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
trialEndKeyboard = event.BuilderKeyResponse()
# keep track of which components have finished
trialEndComponents = [trialEndText, trialEndKeyboard]
for thisComponent in trialEndComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "trialEnd"-------
while continueRoutine:
    # get current time
    t = trialEndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *trialEndText* updates
    if t >= 0.0 and trialEndText.status == NOT_STARTED:
        # keep track of start time/frame for later
        trialEndText.tStart = t
        trialEndText.frameNStart = frameN  # exact frame index
        trialEndText.setAutoDraw(True)
    
    # *trialEndKeyboard* updates
    if t >= 0.0 and trialEndKeyboard.status == NOT_STARTED:
        # keep track of start time/frame for later
        trialEndKeyboard.tStart = t
        trialEndKeyboard.frameNStart = frameN  # exact frame index
        trialEndKeyboard.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if trialEndKeyboard.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialEndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trialEnd"-------
for thisComponent in trialEndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "trialEnd" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
