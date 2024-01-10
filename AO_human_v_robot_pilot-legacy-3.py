#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on January 10, 2024, at 11:03
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard
from psychopy.hardware import emotiv

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'AO_human_v_robot_pilot'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\anhtn\\OneDrive - PennO365\\Documents\\GitHub\\AO_human_v_robot_pilot\\AO_human_v_robot_pilot.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1600, 900], fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    # This is generated by the writeStartCode
    # This is generated by the writeStartCode
    # This is generated by the writeStartCode
    
    # --- Initialize components for Routine "stimLoader" ---
    # Run 'Begin Experiment' code from codeLoader
    condition_list = [];
    action_list = [];
    stim_dir_list=[];
    
    N_rep = 3
    
    
    # --- Initialize components for Routine "stimShuffler" ---
    # Run 'Begin Experiment' code from codeShuffler
    from numpy.random import choice
    import csv
    import datetime
    
    counterBlock = 0
    progVal = 0
    
    cbBlockList = [] # List of blocks in counterbalanced manner
    dictBlockList = [] # List of block dictionaries, each contains 
    condBlockList = [] # LIST OF CONDITION FOR EACH BLOCK
    #markerStimValList = []
    
    # --- Initialize components for Routine "welcomeScreen" ---
    textWelcome = visual.TextStim(win=win, name='textWelcome',
        text='Welcome\n\nPress Space to start the experiment',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    keyWelcome = keyboard.Keyboard()
    cortex_rec = visual.BaseVisualStim(win=win, name="cortex_rec")
    cortex_obj = emotiv.Cortex(subject=expInfo['participant'])
    
    # --- Initialize components for Routine "breakPeriod" ---
    textBreak = visual.TextStim(win=win, name='textBreak',
        text="Let's have 10-second break.\n\nAfter this break, focus on the white cross at the center.",
        font='Open Sans',
        pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    textBreakCountdown = visual.TextStim(win=win, name='textBreakCountdown',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    prog = visual.Progress(
        win, name='prog',
        progress=0.0,
        pos=(-0.3, -0.25), size=(0.6, 0.1), anchor='center left', units='height',
        barColor='white', backColor=None, borderColor='white', colorSpace='rgb',
        lineWidth=4.0, opacity=1.0, ori=0.0,
        depth=-3
    )
    textProg = visual.TextStim(win=win, name='textProg',
        text='Your progress',
        font='Open Sans',
        pos=(0, -0.35), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    keySkipBreak = keyboard.Keyboard()
    
    # --- Initialize components for Routine "restPeriod" ---
    crossRest = visual.ShapeStim(
        win=win, name='crossRest', vertices='cross',
        size=(0.1, 0.1),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    # Run 'Begin Experiment' code from codeRest
    counterStim = 0
    keySkipRest = keyboard.Keyboard()
    # This is generated by writeInitCode
    eegBaseline_marker = visual.BaseVisualStim(win=win, name="eegBaseline_marker")
    
    # --- Initialize components for Routine "beginBlock" ---
    beginInstruction = visual.TextStim(win=win, name='beginInstruction',
        text='Observe the actions presented in the following video.',
        font='Open Sans',
        pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    textCountDown = visual.TextStim(win=win, name='textCountDown',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    keySkipCD = keyboard.Keyboard()
    
    # --- Initialize components for Routine "stimVid" ---
    stimAction = visual.MovieStim(
        win, name='stimAction',
        filename=None, movieLib='ffpyplayer',
        loop=False, volume=1.0, noAudio=True,
        pos=(0, 0), size=(1.777, 1), units='height',
        ori=0.0, anchor='center',opacity=None, contrast=1.0,
        depth=-1
    )
    keySkipStim = keyboard.Keyboard()
    # This is generated by writeInitCode
    eegStim_marker = visual.BaseVisualStim(win=win, name="eegStim_marker")
    
    # --- Initialize components for Routine "executionPlaceholder" ---
    circleExecution = visual.ShapeStim(
        win=win, name='circleExecution',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    keySkipExe = keyboard.Keyboard()
    # This is generated by writeInitCode
    markerExecution = visual.BaseVisualStim(win=win, name="markerExecution")
    
    # --- Initialize components for Routine "endFuncRun" ---
    
    # --- Initialize components for Routine "endTrial" ---
    textEnd = visual.TextStim(win=win, name='textEnd',
        text='Thank you for your participation!\n\nPress Space to exit the experiment',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    keyEnd = keyboard.Keyboard()
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # set up handler to look after randomisation of conditions etc
    loopLoader = data.TrialHandler(nReps=N_rep, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('stimuli_table.xlsx'),
        seed=None, name='loopLoader')
    thisExp.addLoop(loopLoader)  # add the loop to the experiment
    thisLoopLoader = loopLoader.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoopLoader.rgb)
    if thisLoopLoader != None:
        for paramName in thisLoopLoader:
            globals()[paramName] = thisLoopLoader[paramName]
    
    for thisLoopLoader in loopLoader:
        currentLoop = loopLoader
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisLoopLoader.rgb)
        if thisLoopLoader != None:
            for paramName in thisLoopLoader:
                globals()[paramName] = thisLoopLoader[paramName]
        
        # --- Prepare to start Routine "stimLoader" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('stimLoader.started', globalClock.getTime())
        # Run 'Begin Routine' code from codeLoader
        action_list.append(actions);
        condition_list.append(conditions);
        stim_dir_list.append(stimDir);
        
        # keep track of which components have finished
        stimLoaderComponents = []
        for thisComponent in stimLoaderComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "stimLoader" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stimLoaderComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "stimLoader" ---
        for thisComponent in stimLoaderComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('stimLoader.stopped', globalClock.getTime())
        # the Routine "stimLoader" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed N_rep repeats of 'loopLoader'
    
    
    # --- Prepare to start Routine "stimShuffler" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('stimShuffler.started', globalClock.getTime())
    # Run 'Begin Routine' code from codeShuffler
    N_condition = len(np.unique(condition_list)) # number of conditions: human and robot, left and right arm
    N_stim = int(len(action_list)/(N_rep*N_condition)) # number of action stimuli: 8
    
    N_block = N_rep * N_condition # number of blocks = 4x4 = 16
    N_blockStim = int(len(action_list) / N_block) # number of stimuli per block: 8
    
    # ASSIGN ITEMS INTO BLOCKS AND SHUFFLE THEM WITHIN EACH BLOCK (Errante et al 2020)
    block_list = []
    for cond in np.unique(condition_list):
        actionCond = []
        for idx in range(len(condition_list)):
            if condition_list[idx] == cond:
                actionCond.append(action_list[idx])
        checkConditions = False
        while not checkConditions:
            shuffle(actionCond)
            for i in range(len(actionCond)-2):
                if actionCond[i] == actionCond[i+1] == actionCond[i+2]:
                    break
                else:
                    checkConditions = True
        blockCond = [actionCond[i:i+N_blockStim] for i in range(0, len(actionCond), N_blockStim)]
        block_list.append(blockCond)
    block_list = np.array(block_list).reshape(N_block, N_stim)
    #print('## block list', block_list)
    
    # SHUFFLE BLOCKS' ORDER IN COUNTERBALANCED MANNER
    condIdxList = [num for i in range(N_condition) for num in [i] * N_rep] # a list looking like [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
    indexed_list = list(enumerate(condIdxList))
    checkConditions = False
    while not checkConditions:
        shuffle(indexed_list)
        shuffled_indexes, shuffled_cond = zip(*indexed_list)
        count = 0
        for i in range(len(shuffled_cond)-2):
            if shuffled_cond[i] == shuffled_cond[i+1] == shuffled_cond[i+2]:
                break
            else:
                checkConditions = True
    for i in shuffled_indexes:
        cbBlockList.append(block_list[i,:])
    #print('cbBlockList:', cbBlockList)
    #print(cbBlockList[0])
    #print(cbBlockList[0][1])
        
    
    # LIST OF BLOCK DICTIONARY
    # Each dictionary is a block with N_stim stimuli
    ctShuffledCounter = 0
    for block in range(N_block):
        dictBlock = {}
        condList = []
        actionList = []
        dirList = []
        for idx in range(N_stim):
            actionStr = cbBlockList[block][idx]
            condList.append(actionStr[:-2])
            actionList.append(actionStr)
            dirList.append("./stimuli/" + actionStr + ".mp4")
        dictBlock['conditions'] = condList
        dictBlock['actions'] = actionList
        dictBlock['stimDir'] = dirList
        dictBlockList.append(dictBlock)
        
    print('dictBlockList:', dictBlockList)
    print(np.shape(dictBlockList))
    
    # EXPORT DICTIONARY dictBlockList
    current_datetime = datetime.datetime.now()
    filepath = f"./output/dictBlockList_{current_datetime.strftime('%Y-%m-%d_%H-%M-%S')}.csv"
    with open(filepath, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = list(dictBlockList[0].keys()))
        writer.writeheader()
        for entry in dictBlockList:
            rows = zip(entry['conditions'],entry['actions'], entry['stimDir'])
            for row in rows:
                writer.writerow({'conditions':row[0], 'actions':row[1], 'stimDir':row[2]})
            
    # LIST OF CONDITION FOR EACH BLOCK
    for i in range(N_block):
        condBlockList.append(np.unique(dictBlockList[i]['conditions']).tolist())
    print("Order of condition blocks: ", condBlockList)
    # keep track of which components have finished
    stimShufflerComponents = []
    for thisComponent in stimShufflerComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "stimShuffler" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimShufflerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "stimShuffler" ---
    for thisComponent in stimShufflerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('stimShuffler.stopped', globalClock.getTime())
    # Run 'End Routine' code from codeShuffler
    CDBreakN = 10
    # the Routine "stimShuffler" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "welcomeScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('welcomeScreen.started', globalClock.getTime())
    keyWelcome.keys = []
    keyWelcome.rt = []
    _keyWelcome_allKeys = []
    # keep track of which components have finished
    welcomeScreenComponents = [textWelcome, keyWelcome, cortex_rec]
    for thisComponent in welcomeScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "welcomeScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textWelcome* updates
        
        # if textWelcome is starting this frame...
        if textWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textWelcome.frameNStart = frameN  # exact frame index
            textWelcome.tStart = t  # local t and not account for scr refresh
            textWelcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textWelcome, 'tStartRefresh')  # time at next scr refresh
            # update status
            textWelcome.status = STARTED
            textWelcome.setAutoDraw(True)
        
        # if textWelcome is active this frame...
        if textWelcome.status == STARTED:
            # update params
            pass
        
        # *keyWelcome* updates
        waitOnFlip = False
        
        # if keyWelcome is starting this frame...
        if keyWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyWelcome.frameNStart = frameN  # exact frame index
            keyWelcome.tStart = t  # local t and not account for scr refresh
            keyWelcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyWelcome, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'keyWelcome.started')
            # update status
            keyWelcome.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyWelcome.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyWelcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyWelcome.status == STARTED and not waitOnFlip:
            theseKeys = keyWelcome.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _keyWelcome_allKeys.extend(theseKeys)
            if len(_keyWelcome_allKeys):
                keyWelcome.keys = _keyWelcome_allKeys[-1].name  # just the last key pressed
                keyWelcome.rt = _keyWelcome_allKeys[-1].rt
                keyWelcome.duration = _keyWelcome_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in welcomeScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "welcomeScreen" ---
    for thisComponent in welcomeScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('welcomeScreen.stopped', globalClock.getTime())
    # check responses
    if keyWelcome.keys in ['', [], None]:  # No response was made
        keyWelcome.keys = None
    thisExp.addData('keyWelcome.keys',keyWelcome.keys)
    if keyWelcome.keys != None:  # we had a response
        thisExp.addData('keyWelcome.rt', keyWelcome.rt)
        thisExp.addData('keyWelcome.duration', keyWelcome.duration)
    thisExp.nextEntry()
    # the Routine "welcomeScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    loopFuncRun = data.TrialHandler(nReps=N_block, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='loopFuncRun')
    thisExp.addLoop(loopFuncRun)  # add the loop to the experiment
    thisLoopFuncRun = loopFuncRun.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoopFuncRun.rgb)
    if thisLoopFuncRun != None:
        for paramName in thisLoopFuncRun:
            globals()[paramName] = thisLoopFuncRun[paramName]
    
    for thisLoopFuncRun in loopFuncRun:
        currentLoop = loopFuncRun
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisLoopFuncRun.rgb)
        if thisLoopFuncRun != None:
            for paramName in thisLoopFuncRun:
                globals()[paramName] = thisLoopFuncRun[paramName]
        
        # set up handler to look after randomisation of conditions etc
        loopBreakCD = data.TrialHandler(nReps=10.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='loopBreakCD')
        thisExp.addLoop(loopBreakCD)  # add the loop to the experiment
        thisLoopBreakCD = loopBreakCD.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLoopBreakCD.rgb)
        if thisLoopBreakCD != None:
            for paramName in thisLoopBreakCD:
                globals()[paramName] = thisLoopBreakCD[paramName]
        
        for thisLoopBreakCD in loopBreakCD:
            currentLoop = loopBreakCD
            thisExp.timestampOnFlip(win, 'thisRow.t')
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    inputs=inputs, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisLoopBreakCD.rgb)
            if thisLoopBreakCD != None:
                for paramName in thisLoopBreakCD:
                    globals()[paramName] = thisLoopBreakCD[paramName]
            
            # --- Prepare to start Routine "breakPeriod" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('breakPeriod.started', globalClock.getTime())
            textBreakCountdown.setText(CDBreakN)
            # Run 'Begin Routine' code from codeBreakCD
            progVal = counterBlock / N_block
            prog.setProgress(progVal)
            keySkipBreak.keys = []
            keySkipBreak.rt = []
            _keySkipBreak_allKeys = []
            # keep track of which components have finished
            breakPeriodComponents = [textBreak, textBreakCountdown, prog, textProg, keySkipBreak]
            for thisComponent in breakPeriodComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "breakPeriod" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *textBreak* updates
                
                # if textBreak is starting this frame...
                if textBreak.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    textBreak.frameNStart = frameN  # exact frame index
                    textBreak.tStart = t  # local t and not account for scr refresh
                    textBreak.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(textBreak, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    textBreak.status = STARTED
                    textBreak.setAutoDraw(True)
                
                # if textBreak is active this frame...
                if textBreak.status == STARTED:
                    # update params
                    pass
                
                # if textBreak is stopping this frame...
                if textBreak.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > textBreak.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        textBreak.tStop = t  # not accounting for scr refresh
                        textBreak.frameNStop = frameN  # exact frame index
                        # update status
                        textBreak.status = FINISHED
                        textBreak.setAutoDraw(False)
                
                # *textBreakCountdown* updates
                
                # if textBreakCountdown is starting this frame...
                if textBreakCountdown.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    textBreakCountdown.frameNStart = frameN  # exact frame index
                    textBreakCountdown.tStart = t  # local t and not account for scr refresh
                    textBreakCountdown.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(textBreakCountdown, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    textBreakCountdown.status = STARTED
                    textBreakCountdown.setAutoDraw(True)
                
                # if textBreakCountdown is active this frame...
                if textBreakCountdown.status == STARTED:
                    # update params
                    pass
                
                # if textBreakCountdown is stopping this frame...
                if textBreakCountdown.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > textBreakCountdown.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        textBreakCountdown.tStop = t  # not accounting for scr refresh
                        textBreakCountdown.frameNStop = frameN  # exact frame index
                        # update status
                        textBreakCountdown.status = FINISHED
                        textBreakCountdown.setAutoDraw(False)
                
                # *prog* updates
                
                # if prog is starting this frame...
                if prog.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    prog.frameNStart = frameN  # exact frame index
                    prog.tStart = t  # local t and not account for scr refresh
                    prog.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(prog, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    prog.status = STARTED
                    prog.setAutoDraw(True)
                
                # if prog is active this frame...
                if prog.status == STARTED:
                    # update params
                    pass
                
                # if prog is stopping this frame...
                if prog.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > prog.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        prog.tStop = t  # not accounting for scr refresh
                        prog.frameNStop = frameN  # exact frame index
                        # update status
                        prog.status = FINISHED
                        prog.setAutoDraw(False)
                
                # *textProg* updates
                
                # if textProg is starting this frame...
                if textProg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    textProg.frameNStart = frameN  # exact frame index
                    textProg.tStart = t  # local t and not account for scr refresh
                    textProg.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(textProg, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    textProg.status = STARTED
                    textProg.setAutoDraw(True)
                
                # if textProg is active this frame...
                if textProg.status == STARTED:
                    # update params
                    pass
                
                # if textProg is stopping this frame...
                if textProg.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > textProg.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        textProg.tStop = t  # not accounting for scr refresh
                        textProg.frameNStop = frameN  # exact frame index
                        # update status
                        textProg.status = FINISHED
                        textProg.setAutoDraw(False)

                # *keySkipBreak* updates
                waitOnFlip = False
                
                # if keySkipBreak is starting this frame...
                if keySkipBreak.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    keySkipBreak.frameNStart = frameN  # exact frame index
                    keySkipBreak.tStart = t  # local t and not account for scr refresh
                    keySkipBreak.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(keySkipBreak, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    keySkipBreak.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(keySkipBreak.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(keySkipBreak.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if keySkipBreak is stopping this frame...
                if keySkipBreak.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > keySkipBreak.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        keySkipBreak.tStop = t  # not accounting for scr refresh
                        keySkipBreak.frameNStop = frameN  # exact frame index
                        # update status
                        keySkipBreak.status = FINISHED
                        keySkipBreak.status = FINISHED
                if keySkipBreak.status == STARTED and not waitOnFlip:
                    theseKeys = keySkipBreak.getKeys(keyList=['s'], ignoreKeys=["escape"], waitRelease=False)
                    _keySkipBreak_allKeys.extend(theseKeys)
                    if len(_keySkipBreak_allKeys):
                        keySkipBreak.keys = _keySkipBreak_allKeys[-1].name  # just the last key pressed
                        keySkipBreak.rt = _keySkipBreak_allKeys[-1].rt
                        keySkipBreak.duration = _keySkipBreak_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in breakPeriodComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "breakPeriod" ---
            for thisComponent in breakPeriodComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('breakPeriod.stopped', globalClock.getTime())
            # Run 'End Routine' code from codeBreakCD
            CDBreakN = CDBreakN -1
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
        # completed 10.0 repeats of 'loopBreakCD'
        
        
        # --- Prepare to start Routine "restPeriod" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('restPeriod.started', globalClock.getTime())
        keySkipRest.keys = []
        keySkipRest.rt = []
        _keySkipRest_allKeys = []
        # This is generated by the writeRoutineStartCode
        # keep track of which components have finished
        restPeriodComponents = [crossRest, keySkipRest, eegBaseline_marker ]
        for thisComponent in restPeriodComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "restPeriod" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 8.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *crossRest* updates
            
            # if crossRest is starting this frame...
            if crossRest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crossRest.frameNStart = frameN  # exact frame index
                crossRest.tStart = t  # local t and not account for scr refresh
                crossRest.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crossRest, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'crossRest.started')
                # update status
                crossRest.status = STARTED
                crossRest.setAutoDraw(True)
            
            # if crossRest is active this frame...
            if crossRest.status == STARTED:
                # update params
                pass
            
            # if crossRest is stopping this frame...
            if crossRest.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crossRest.tStartRefresh + 8-frameTolerance:
                    # keep track of stop time/frame for later
                    crossRest.tStop = t  # not accounting for scr refresh
                    crossRest.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'crossRest.stopped')
                    # update status
                    crossRest.status = FINISHED
                    crossRest.setAutoDraw(False)
            
            # *keySkipRest* updates
            waitOnFlip = False
            
            # if keySkipRest is starting this frame...
            if keySkipRest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                keySkipRest.frameNStart = frameN  # exact frame index
                keySkipRest.tStart = t  # local t and not account for scr refresh
                keySkipRest.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(keySkipRest, 'tStartRefresh')  # time at next scr refresh
                # update status
                keySkipRest.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(keySkipRest.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(keySkipRest.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if keySkipRest is stopping this frame...
            if keySkipRest.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > keySkipRest.tStartRefresh + 8-frameTolerance:
                    # keep track of stop time/frame for later
                    keySkipRest.tStop = t  # not accounting for scr refresh
                    keySkipRest.frameNStop = frameN  # exact frame index
                    # update status
                    keySkipRest.status = FINISHED
                    keySkipRest.status = FINISHED
            if keySkipRest.status == STARTED and not waitOnFlip:
                theseKeys = keySkipRest.getKeys(keyList=['s'], ignoreKeys=["escape"], waitRelease=False)
                _keySkipRest_allKeys.extend(theseKeys)
                if len(_keySkipRest_allKeys):
                    keySkipRest.keys = _keySkipRest_allKeys[-1].name  # just the last key pressed
                    keySkipRest.rt = _keySkipRest_allKeys[-1].rt
                    keySkipRest.duration = _keySkipRest_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False

            # if eegBaseline_marker is starting this frame...
            if eegBaseline_marker.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                eegBaseline_marker.frameNStart = frameN  # exact frame index
                eegBaseline_marker.tStart = t  # local t and not account for scr refresh
                eegBaseline_marker.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(eegBaseline_marker, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('eegBaseline_marker.started', t)
                # update status
                eegBaseline_marker.status = STARTED
                eegBaseline_marker.status = STARTED
                delta_time = tThisFlip-t  # Adding the extra time between now and the next screen flip
                cortex_obj.inject_marker(value=str('1000'), label='"baseline"', delta_time=delta_time)
                eegBaseline_marker.start_sent = True
            
            # if eegBaseline_marker is stopping this frame...
            if eegBaseline_marker.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > eegBaseline_marker.tStartRefresh + 8-frameTolerance:
                    # keep track of stop time/frame for later
                    eegBaseline_marker.tStop = t  # not accounting for scr refresh
                    eegBaseline_marker.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.addData('eegBaseline_marker.stopped', t)
                    # update status
                    eegBaseline_marker.status = FINISHED
                    eegBaseline_marker.status = FINISHED
                    delta_time = tThisFlip-t  # Adding the extra time between now and the next screen flip
                    cortex_obj.update_marker(label='"baseline"', delta_time=delta_time)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in restPeriodComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "restPeriod" ---
        for thisComponent in restPeriodComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('restPeriod.stopped', globalClock.getTime())
        # Run 'End Routine' code from codeRest
        print(f"======= counterBlock {counterBlock} - condition: {condBlockList[counterBlock]} =======")
        #print('Condition: ', dictBlockList[counterBlock]['conditions'])
        
        counterStim = 0
        countDownN = 3
        # This is generated by the writeRoutineEndCode
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-8.000000)
        
        # set up handler to look after randomisation of conditions etc
        loopBlock = data.TrialHandler(nReps=N_stim, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='loopBlock')
        thisExp.addLoop(loopBlock)  # add the loop to the experiment
        thisLoopBlock = loopBlock.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLoopBlock.rgb)
        if thisLoopBlock != None:
            for paramName in thisLoopBlock:
                globals()[paramName] = thisLoopBlock[paramName]
        
        for thisLoopBlock in loopBlock:
            currentLoop = loopBlock
            thisExp.timestampOnFlip(win, 'thisRow.t')
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    inputs=inputs, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisLoopBlock.rgb)
            if thisLoopBlock != None:
                for paramName in thisLoopBlock:
                    globals()[paramName] = thisLoopBlock[paramName]
            
            # set up handler to look after randomisation of conditions etc
            loopCountDown = data.TrialHandler(nReps=4.0, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='loopCountDown')
            thisExp.addLoop(loopCountDown)  # add the loop to the experiment
            thisLoopCountDown = loopCountDown.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisLoopCountDown.rgb)
            if thisLoopCountDown != None:
                for paramName in thisLoopCountDown:
                    globals()[paramName] = thisLoopCountDown[paramName]
            
            for thisLoopCountDown in loopCountDown:
                currentLoop = loopCountDown
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisLoopCountDown.rgb)
                if thisLoopCountDown != None:
                    for paramName in thisLoopCountDown:
                        globals()[paramName] = thisLoopCountDown[paramName]
                
                # --- Prepare to start Routine "beginBlock" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('beginBlock.started', globalClock.getTime())
                textCountDown.setText(countDownN)              
                keySkipCD.keys = []
                keySkipCD.rt = []
                _keySkipCD_allKeys = []
                # keep track of which components have finished
                beginBlockComponents = [beginInstruction, textCountDown, keySkipCD]
                for thisComponent in beginBlockComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "beginBlock" ---
                routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 1.0:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *beginInstruction* updates
                    
                    # if beginInstruction is starting this frame...
                    if beginInstruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        beginInstruction.frameNStart = frameN  # exact frame index
                        beginInstruction.tStart = t  # local t and not account for scr refresh
                        beginInstruction.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(beginInstruction, 'tStartRefresh')  # time at next scr refresh
                        # update status
                        beginInstruction.status = STARTED
                        beginInstruction.setAutoDraw(True)
                    
                    # if beginInstruction is active this frame...
                    if beginInstruction.status == STARTED:
                        # update params
                        pass
                    
                    # if beginInstruction is stopping this frame...
                    if beginInstruction.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > beginInstruction.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            beginInstruction.tStop = t  # not accounting for scr refresh
                            beginInstruction.frameNStop = frameN  # exact frame index
                            # update status
                            beginInstruction.status = FINISHED
                            beginInstruction.setAutoDraw(False)
                    
                    # *textCountDown* updates
                    
                    # if textCountDown is starting this frame...
                    if textCountDown.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        textCountDown.frameNStart = frameN  # exact frame index
                        textCountDown.tStart = t  # local t and not account for scr refresh
                        textCountDown.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(textCountDown, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'textCountDown.started')
                        # update status
                        textCountDown.status = STARTED
                        textCountDown.setAutoDraw(True)
                    
                    # if textCountDown is active this frame...
                    if textCountDown.status == STARTED:
                        # update params
                        pass
                    
                    # if textCountDown is stopping this frame...
                    if textCountDown.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > textCountDown.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            textCountDown.tStop = t  # not accounting for scr refresh
                            textCountDown.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'textCountDown.stopped')
                            # update status
                            textCountDown.status = FINISHED
                            textCountDown.setAutoDraw(False)
                    
                    # *keySkipCD* updates
                    waitOnFlip = False
                    
                    # if keySkipCD is starting this frame...
                    if keySkipCD.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        keySkipCD.frameNStart = frameN  # exact frame index
                        keySkipCD.tStart = t  # local t and not account for scr refresh
                        keySkipCD.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(keySkipCD, 'tStartRefresh')  # time at next scr refresh
                        # update status
                        keySkipCD.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(keySkipCD.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(keySkipCD.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    
                    # if keySkipCD is stopping this frame...
                    if keySkipCD.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > keySkipCD.tStartRefresh + 1-frameTolerance:
                            # keep track of stop time/frame for later
                            keySkipCD.tStop = t  # not accounting for scr refresh
                            keySkipCD.frameNStop = frameN  # exact frame index
                            # update status
                            keySkipCD.status = FINISHED
                            keySkipCD.status = FINISHED
                    if keySkipCD.status == STARTED and not waitOnFlip:
                        theseKeys = keySkipCD.getKeys(keyList=['s'], ignoreKeys=["escape"], waitRelease=False)
                        _keySkipCD_allKeys.extend(theseKeys)
                        if len(_keySkipCD_allKeys):
                            keySkipCD.keys = _keySkipCD_allKeys[-1].name  # just the last key pressed
                            keySkipCD.rt = _keySkipCD_allKeys[-1].rt
                            keySkipCD.duration = _keySkipCD_allKeys[-1].duration
                            # a response ends the routine
                            continueRoutine = False
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in beginBlockComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "beginBlock" ---
                for thisComponent in beginBlockComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('beginBlock.stopped', globalClock.getTime())
                # Run 'End Routine' code from codeCountDown
                countDownN = countDownN -1
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if routineForceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-1.000000)
            # completed 4.0 repeats of 'loopCountDown'
            
            
            # --- Prepare to start Routine "stimVid" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('stimVid.started', globalClock.getTime())
            # Run 'Begin Routine' code from codeStim
            print(f"counterStim {counterStim} - {dictBlockList[counterBlock]['stimDir'][counterStim]}")
            
            
            # ASSIGN MARKER LABELS AND MARKER VALUES FOR DIFFERENT CONDITIONS AND ACTION STIMULI
            markerStimLabel = dictBlockList[counterBlock]['actions'][counterStim]
            print("markerStimLabel: ", markerStimLabel)
            
            actionN = int(dictBlockList[counterBlock]['actions'][counterStim][-1])
            if dictBlockList[counterBlock]['conditions'][counterStim] == "human_left":
                markerStimVal = 1 
            elif dictBlockList[counterBlock]['conditions'][counterStim] == "human_right":
                markerStimVal = 2
            elif dictBlockList[counterBlock]['conditions'][counterStim] == "robot_left":
                markerStimVal = 3 
            elif dictBlockList[counterBlock]['conditions'][counterStim] == "robot_right":
                markerStimVal = 4 
            markerStimVal = markerStimVal * 10 + actionN
            print("markerStimVal: ", markerStimVal)
            stimAction.setMovie(dictBlockList[counterBlock]['stimDir'][counterStim])
            keySkipStim.keys = []
            keySkipStim.rt = []
            _keySkipStim_allKeys = []
            # This is generated by the writeRoutineStartCode
            # keep track of which components have finished
            stimVidComponents = [stimAction, keySkipStim, eegStim_marker]
            for thisComponent in stimVidComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "stimVid" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *stimAction* updates
                
                # if stimAction is starting this frame...
                if stimAction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    stimAction.frameNStart = frameN  # exact frame index
                    stimAction.tStart = t  # local t and not account for scr refresh
                    stimAction.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(stimAction, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stimAction.started')
                    # update status
                    stimAction.status = STARTED
                    stimAction.setAutoDraw(True)
                    stimAction.play()
                if stimAction.isFinished:  # force-end the Routine
                    continueRoutine = False
                
                # *keySkipStim* updates
                waitOnFlip = False
                
                # if keySkipStim is starting this frame...
                if keySkipStim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    keySkipStim.frameNStart = frameN  # exact frame index
                    keySkipStim.tStart = t  # local t and not account for scr refresh
                    keySkipStim.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(keySkipStim, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    keySkipStim.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(keySkipStim.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(keySkipStim.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if keySkipStim is stopping this frame...
                if keySkipStim.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > keySkipStim.tStartRefresh + 5-frameTolerance:
                        # keep track of stop time/frame for later
                        keySkipStim.tStop = t  # not accounting for scr refresh
                        keySkipStim.frameNStop = frameN  # exact frame index
                        # update status
                        keySkipStim.status = FINISHED
                        keySkipStim.status = FINISHED
                if keySkipStim.status == STARTED and not waitOnFlip:
                    theseKeys = keySkipStim.getKeys(keyList=['s'], ignoreKeys=["escape"], waitRelease=False)
                    _keySkipStim_allKeys.extend(theseKeys)
                    if len(_keySkipStim_allKeys):
                        keySkipStim.keys = _keySkipStim_allKeys[-1].name  # just the last key pressed
                        keySkipStim.rt = _keySkipStim_allKeys[-1].rt
                        keySkipStim.duration = _keySkipStim_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False

                # if eegStim_marker is starting this frame...
                if eegStim_marker.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    eegStim_marker.frameNStart = frameN  # exact frame index
                    eegStim_marker.tStart = t  # local t and not account for scr refresh
                    eegStim_marker.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(eegStim_marker, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('eegStim_marker.started', t)
                    # update status
                    eegStim_marker.status = STARTED
                    eegStim_marker.status = STARTED
                    delta_time = tThisFlip-t  # Adding the extra time between now and the next screen flip
                    cortex_obj.inject_marker(value=str(markerStimVal), label=markerStimLabel, delta_time=delta_time)
                    eegStim_marker.start_sent = True
                
                # if eegStim_marker is stopping this frame...
                if eegStim_marker.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > eegStim_marker.tStartRefresh + 5-frameTolerance:
                        # keep track of stop time/frame for later
                        eegStim_marker.tStop = t  # not accounting for scr refresh
                        eegStim_marker.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.addData('eegStim_marker.stopped', t)
                        # update status
                        eegStim_marker.status = FINISHED
                        eegStim_marker.status = FINISHED
                        delta_time = tThisFlip-t  # Adding the extra time between now and the next screen flip
                        cortex_obj.update_marker(label=markerStimLabel, delta_time=delta_time)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in stimVidComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "stimVid" ---
            for thisComponent in stimVidComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('stimVid.stopped', globalClock.getTime())
            stimAction.stop()  # ensure movie has stopped at end of Routine
            # This is generated by the writeRoutineEndCode
            # the Routine "stimVid" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "executionPlaceholder" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('executionPlaceholder.started', globalClock.getTime())
            # Run 'Begin Routine' code from codeEndStim
            counterStim += 1
            
            markerExeLabel = 'exe_' + markerStimLabel
            markerExeVal = 100 + markerStimVal
            
            print("markerExeLabel: ", markerExeLabel)
            print("markerExeVal: ", markerExeVal)
            keySkipExe.keys = []
            keySkipExe.rt = []
            _keySkipExe_allKeys = []
            # This is generated by the writeRoutineStartCode
            # keep track of which components have finished
            executionPlaceholderComponents = [circleExecution, keySkipExe, markerExecution]
            for thisComponent in executionPlaceholderComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "executionPlaceholder" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 8.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *circleExecution* updates
                
                # if circleExecution is starting this frame...
                if circleExecution.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    circleExecution.frameNStart = frameN  # exact frame index
                    circleExecution.tStart = t  # local t and not account for scr refresh
                    circleExecution.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(circleExecution, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'circleExecution.started')
                    # update status
                    circleExecution.status = STARTED
                    circleExecution.setAutoDraw(True)
                
                # if circleExecution is active this frame...
                if circleExecution.status == STARTED:
                    # update params
                    pass
                
                # if circleExecution is stopping this frame...
                if circleExecution.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > circleExecution.tStartRefresh + 8-frameTolerance:
                        # keep track of stop time/frame for later
                        circleExecution.tStop = t  # not accounting for scr refresh
                        circleExecution.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'circleExecution.stopped')
                        # update status
                        circleExecution.status = FINISHED
                        circleExecution.setAutoDraw(False)
                
                # *keySkipExe* updates
                waitOnFlip = False
                
                # if keySkipExe is starting this frame...
                if keySkipExe.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    keySkipExe.frameNStart = frameN  # exact frame index
                    keySkipExe.tStart = t  # local t and not account for scr refresh
                    keySkipExe.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(keySkipExe, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    keySkipExe.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(keySkipExe.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(keySkipExe.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if keySkipExe is stopping this frame...
                if keySkipExe.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > keySkipExe.tStartRefresh + 8-frameTolerance:
                        # keep track of stop time/frame for later
                        keySkipExe.tStop = t  # not accounting for scr refresh
                        keySkipExe.frameNStop = frameN  # exact frame index
                        # update status
                        keySkipExe.status = FINISHED
                        keySkipExe.status = FINISHED
                if keySkipExe.status == STARTED and not waitOnFlip:
                    theseKeys = keySkipExe.getKeys(keyList=['s'], ignoreKeys=["escape"], waitRelease=False)
                    _keySkipExe_allKeys.extend(theseKeys)
                    if len(_keySkipExe_allKeys):
                        keySkipExe.keys = _keySkipExe_allKeys[-1].name  # just the last key pressed
                        keySkipExe.rt = _keySkipExe_allKeys[-1].rt
                        keySkipExe.duration = _keySkipExe_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # if markerExecution is starting this frame...
                if markerExecution.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    markerExecution.frameNStart = frameN  # exact frame index
                    markerExecution.tStart = t  # local t and not account for scr refresh
                    markerExecution.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(markerExecution, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('markerExecution.started', t)
                    # update status
                    markerExecution.status = STARTED
                    markerExecution.status = STARTED
                    delta_time = tThisFlip-t  # Adding the extra time between now and the next screen flip
                    cortex_obj.inject_marker(value=str(markerExeVal), label=markerExeLabel, delta_time=delta_time)
                    markerExecution.start_sent = True
                
                # if markerExecution is stopping this frame...
                if markerExecution.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > markerExecution.tStartRefresh + 8-frameTolerance:
                        # keep track of stop time/frame for later
                        markerExecution.tStop = t  # not accounting for scr refresh
                        markerExecution.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.addData('markerExecution.stopped', t)
                        # update status
                        markerExecution.status = FINISHED
                        markerExecution.status = FINISHED
                        delta_time = tThisFlip-t  # Adding the extra time between now and the next screen flip
                        cortex_obj.update_marker(label=markerExeLabel, delta_time=delta_time)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in executionPlaceholderComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "executionPlaceholder" ---
            for thisComponent in executionPlaceholderComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('executionPlaceholder.stopped', globalClock.getTime())
            # Run 'End Routine' code from codeEndStim
            countDownN = 3
            # This is generated by the writeRoutineEndCode
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-8.000000)
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed N_stim repeats of 'loopBlock'
        
        
        # --- Prepare to start Routine "endFuncRun" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('endFuncRun.started', globalClock.getTime())
        # Run 'Begin Routine' code from codeEndRun
        counterBlock += 1
        # keep track of which components have finished
        endFuncRunComponents = []
        for thisComponent in endFuncRunComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "endFuncRun" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in endFuncRunComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "endFuncRun" ---
        for thisComponent in endFuncRunComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('endFuncRun.stopped', globalClock.getTime())
        # Run 'End Routine' code from codeEndRun
        CDBreakN = 10
        # the Routine "endFuncRun" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed N_block repeats of 'loopFuncRun'
    
    
    # --- Prepare to start Routine "endTrial" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('endTrial.started', globalClock.getTime())
    keyEnd.keys = []
    keyEnd.rt = []
    _keyEnd_allKeys = []
    # keep track of which components have finished
    endTrialComponents = [textEnd, keyEnd]
    for thisComponent in endTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "endTrial" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textEnd* updates
        
        # if textEnd is starting this frame...
        if textEnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textEnd.frameNStart = frameN  # exact frame index
            textEnd.tStart = t  # local t and not account for scr refresh
            textEnd.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textEnd, 'tStartRefresh')  # time at next scr refresh
            # update status
            textEnd.status = STARTED
            textEnd.setAutoDraw(True)
        
        # if textEnd is active this frame...
        if textEnd.status == STARTED:
            # update params
            pass
        
        # *keyEnd* updates
        waitOnFlip = False
        
        # if keyEnd is starting this frame...
        if keyEnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyEnd.frameNStart = frameN  # exact frame index
            keyEnd.tStart = t  # local t and not account for scr refresh
            keyEnd.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyEnd, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'keyEnd.started')
            # update status
            keyEnd.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyEnd.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyEnd.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyEnd.status == STARTED and not waitOnFlip:
            theseKeys = keyEnd.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _keyEnd_allKeys.extend(theseKeys)
            if len(_keyEnd_allKeys):
                keyEnd.keys = _keyEnd_allKeys[-1].name  # just the last key pressed
                keyEnd.rt = _keyEnd_allKeys[-1].rt
                keyEnd.duration = _keyEnd_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in endTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "endTrial" ---
    for thisComponent in endTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('endTrial.stopped', globalClock.getTime())
    # check responses
    if keyEnd.keys in ['', [], None]:  # No response was made
        keyEnd.keys = None
    thisExp.addData('keyEnd.keys',keyEnd.keys)
    if keyEnd.keys != None:  # we had a response
        thisExp.addData('keyEnd.rt', keyEnd.rt)
        thisExp.addData('keyEnd.duration', keyEnd.duration)
    thisExp.nextEntry()
    # the Routine "endTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
