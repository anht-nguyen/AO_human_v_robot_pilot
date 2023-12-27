/******************************* 
 * Ao_Human_V_Robot_Pilot *
 *******************************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2023.2.3.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'AO_human_v_robot_pilot';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: false,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
const loopLoaderLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(loopLoaderLoopBegin(loopLoaderLoopScheduler));
flowScheduler.add(loopLoaderLoopScheduler);
flowScheduler.add(loopLoaderLoopEnd);


flowScheduler.add(stimShufflerRoutineBegin());
flowScheduler.add(stimShufflerRoutineEachFrame());
flowScheduler.add(stimShufflerRoutineEnd());
flowScheduler.add(welcomeScreenRoutineBegin());
flowScheduler.add(welcomeScreenRoutineEachFrame());
flowScheduler.add(welcomeScreenRoutineEnd());
const loopFuncRunLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(loopFuncRunLoopBegin(loopFuncRunLoopScheduler));
flowScheduler.add(loopFuncRunLoopScheduler);
flowScheduler.add(loopFuncRunLoopEnd);










flowScheduler.add(endTrialRoutineBegin());
flowScheduler.add(endTrialRoutineEachFrame());
flowScheduler.add(endTrialRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'stimuli_table.xlsx', 'path': 'stimuli_table.xlsx'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2023.2.3';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var stimLoaderClock;
var condition_list;
var action_list;
var stim_dir_list;
var N_rep;
var stimShufflerClock;
var counterBlock;
var cbBlockList;
var dictBlockList;
var condBlockList;
var welcomeScreenClock;
var textWelcome;
var keyWelcome;
var restPeriodClock;
var crossRest;
var counterStim;
var skipRest;
var beginBlockClock;
var beginInstruction;
var textCountDown;
var stimVidClock;
var stimActionClock;
var stimAction;
var endStimClock;
var endFuncRunClock;
var endTrialClock;
var textEnd;
var keyEnd;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "stimLoader"
  stimLoaderClock = new util.Clock();
  // Run 'Begin Experiment' code from codeLoader
  condition_list = [];
  action_list = [];
  stim_dir_list = [];
  N_rep = 4;
  
  // Initialize components for Routine "stimShuffler"
  stimShufflerClock = new util.Clock();
  // Run 'Begin Experiment' code from codeShuffler
  counterBlock = 0;
  cbBlockList = [];
  dictBlockList = [];
  condBlockList = [];
  
  // Initialize components for Routine "welcomeScreen"
  welcomeScreenClock = new util.Clock();
  textWelcome = new visual.TextStim({
    win: psychoJS.window,
    name: 'textWelcome',
    text: 'Welcome\n\nPress Space to start the experiment',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  keyWelcome = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "restPeriod"
  restPeriodClock = new util.Clock();
  crossRest = new visual.ShapeStim ({
    win: psychoJS.window, name: 'crossRest', 
    vertices: 'cross', size:[0.1, 0.1],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  // Run 'Begin Experiment' code from codeRest
  counterStim = 0;
  
  skipRest = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "beginBlock"
  beginBlockClock = new util.Clock();
  beginInstruction = new visual.TextStim({
    win: psychoJS.window,
    name: 'beginInstruction',
    text: 'Observe the actions presented in the following videos.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.25], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  textCountDown = new visual.TextStim({
    win: psychoJS.window,
    name: 'textCountDown',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "stimVid"
  stimVidClock = new util.Clock();
  stimActionClock = new util.Clock();
  stimAction = new visual.MovieStim({
    win: psychoJS.window,
    name: 'stimAction',
    units: psychoJS.window.units,
    movie: undefined,
    pos: [0, 0],
    anchor: 'center',
    size: [0.75, 0.42],
    ori: 0.0,
    opacity: undefined,
    loop: false,
    noAudio: true,
    depth: 0
    });
  // Initialize components for Routine "endStim"
  endStimClock = new util.Clock();
  // Initialize components for Routine "endFuncRun"
  endFuncRunClock = new util.Clock();
  // Initialize components for Routine "endTrial"
  endTrialClock = new util.Clock();
  textEnd = new visual.TextStim({
    win: psychoJS.window,
    name: 'textEnd',
    text: 'Thank you for your participation!\n\nPress Space to exit the experiment',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  keyEnd = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var loopLoader;
function loopLoaderLoopBegin(loopLoaderLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    loopLoader = new TrialHandler({
      psychoJS: psychoJS,
      nReps: N_rep, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'stimuli_table.xlsx',
      seed: undefined, name: 'loopLoader'
    });
    psychoJS.experiment.addLoop(loopLoader); // add the loop to the experiment
    currentLoop = loopLoader;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisLoopLoader of loopLoader) {
      snapshot = loopLoader.getSnapshot();
      loopLoaderLoopScheduler.add(importConditions(snapshot));
      loopLoaderLoopScheduler.add(stimLoaderRoutineBegin(snapshot));
      loopLoaderLoopScheduler.add(stimLoaderRoutineEachFrame());
      loopLoaderLoopScheduler.add(stimLoaderRoutineEnd(snapshot));
      loopLoaderLoopScheduler.add(loopLoaderLoopEndIteration(loopLoaderLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function loopLoaderLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(loopLoader);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function loopLoaderLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var loopFuncRun;
function loopFuncRunLoopBegin(loopFuncRunLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    loopFuncRun = new TrialHandler({
      psychoJS: psychoJS,
      nReps: N_block, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'loopFuncRun'
    });
    psychoJS.experiment.addLoop(loopFuncRun); // add the loop to the experiment
    currentLoop = loopFuncRun;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisLoopFuncRun of loopFuncRun) {
      snapshot = loopFuncRun.getSnapshot();
      loopFuncRunLoopScheduler.add(importConditions(snapshot));
      loopFuncRunLoopScheduler.add(restPeriodRoutineBegin(snapshot));
      loopFuncRunLoopScheduler.add(restPeriodRoutineEachFrame());
      loopFuncRunLoopScheduler.add(restPeriodRoutineEnd(snapshot));
      const loopCountDownLoopScheduler = new Scheduler(psychoJS);
      loopFuncRunLoopScheduler.add(loopCountDownLoopBegin(loopCountDownLoopScheduler, snapshot));
      loopFuncRunLoopScheduler.add(loopCountDownLoopScheduler);
      loopFuncRunLoopScheduler.add(loopCountDownLoopEnd);
      const loopBlockLoopScheduler = new Scheduler(psychoJS);
      loopFuncRunLoopScheduler.add(loopBlockLoopBegin(loopBlockLoopScheduler, snapshot));
      loopFuncRunLoopScheduler.add(loopBlockLoopScheduler);
      loopFuncRunLoopScheduler.add(loopBlockLoopEnd);
      loopFuncRunLoopScheduler.add(endFuncRunRoutineBegin(snapshot));
      loopFuncRunLoopScheduler.add(endFuncRunRoutineEachFrame());
      loopFuncRunLoopScheduler.add(endFuncRunRoutineEnd(snapshot));
      loopFuncRunLoopScheduler.add(loopFuncRunLoopEndIteration(loopFuncRunLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var loopCountDown;
function loopCountDownLoopBegin(loopCountDownLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    loopCountDown = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 4, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'loopCountDown'
    });
    psychoJS.experiment.addLoop(loopCountDown); // add the loop to the experiment
    currentLoop = loopCountDown;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisLoopCountDown of loopCountDown) {
      snapshot = loopCountDown.getSnapshot();
      loopCountDownLoopScheduler.add(importConditions(snapshot));
      loopCountDownLoopScheduler.add(beginBlockRoutineBegin(snapshot));
      loopCountDownLoopScheduler.add(beginBlockRoutineEachFrame());
      loopCountDownLoopScheduler.add(beginBlockRoutineEnd(snapshot));
      loopCountDownLoopScheduler.add(loopCountDownLoopEndIteration(loopCountDownLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function loopCountDownLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(loopCountDown);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function loopCountDownLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var loopBlock;
function loopBlockLoopBegin(loopBlockLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    loopBlock = new TrialHandler({
      psychoJS: psychoJS,
      nReps: N_stim, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'loopBlock'
    });
    psychoJS.experiment.addLoop(loopBlock); // add the loop to the experiment
    currentLoop = loopBlock;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisLoopBlock of loopBlock) {
      snapshot = loopBlock.getSnapshot();
      loopBlockLoopScheduler.add(importConditions(snapshot));
      loopBlockLoopScheduler.add(stimVidRoutineBegin(snapshot));
      loopBlockLoopScheduler.add(stimVidRoutineEachFrame());
      loopBlockLoopScheduler.add(stimVidRoutineEnd(snapshot));
      loopBlockLoopScheduler.add(endStimRoutineBegin(snapshot));
      loopBlockLoopScheduler.add(endStimRoutineEachFrame());
      loopBlockLoopScheduler.add(endStimRoutineEnd(snapshot));
      loopBlockLoopScheduler.add(loopBlockLoopEndIteration(loopBlockLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function loopBlockLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(loopBlock);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function loopBlockLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function loopFuncRunLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(loopFuncRun);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function loopFuncRunLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var t;
var frameN;
var continueRoutine;
var stimLoaderComponents;
function stimLoaderRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'stimLoader' ---
    t = 0;
    stimLoaderClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('stimLoader.started', globalClock.getTime());
    // Run 'Begin Routine' code from codeLoader
    action_list.push(actions);
    condition_list.push(conditions);
    stim_dir_list.push(stimDir);
    
    // keep track of which components have finished
    stimLoaderComponents = [];
    
    for (const thisComponent of stimLoaderComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function stimLoaderRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'stimLoader' ---
    // get current time
    t = stimLoaderClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of stimLoaderComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function stimLoaderRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'stimLoader' ---
    for (const thisComponent of stimLoaderComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('stimLoader.stopped', globalClock.getTime());
    // the Routine "stimLoader" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _pj;
var find_unique;
var unique_conditions;
var N_condition;
var N_stim;
var N_block;
var N_blockStim;
var block_list;
var actionCond;
var blockCond;
var reshaped_list;
var condIdxList;
var enumerated_list;
var idx;
var checkConditions;
var shuffled_indexes;
var shuffled_cond;
var ctShuffledCounter;
var dictBlock;
var condList;
var actionList;
var dirList;
var actionStr;
var stimShufflerComponents;
function stimShufflerRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'stimShuffler' ---
    t = 0;
    stimShufflerClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('stimShuffler.started', globalClock.getTime());
    // Run 'Begin Routine' code from codeShuffler
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    function find_unique_func(arr) {
        var unique_elements;
        unique_elements = [];
        for (var item, _pj_c = 0, _pj_a = arr, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
            item = _pj_a[_pj_c];
            if ((! _pj.in_es6(item, unique_elements))) {
                unique_elements.push(item);
            }
        }
        return unique_elements;
    }
    find_unique = find_unique_func;
    unique_conditions = find_unique(condition_list);
    N_condition = unique_conditions.length;
    N_stim = Number.parseInt((action_list.length / (N_rep * N_condition)));
    N_block = (N_rep * N_condition);
    N_blockStim = Number.parseInt((action_list.length / N_block));
    block_list = [];
    actionCond = [];
    blockCond = [];
    for (var cond, _pj_c = 0, _pj_a = unique_conditions, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        cond = _pj_a[_pj_c];
        actionCond = [];
        for (var idx, _pj_f = 0, _pj_d = util.range(condition_list.length), _pj_e = _pj_d.length; (_pj_f < _pj_e); _pj_f += 1) {
            idx = _pj_d[_pj_f];
            if ((condition_list[idx] === cond)) {
                actionCond.push(action_list[idx]);
            }
        }
        checkConditions = false;
        while ((! checkConditions)) {
            util.shuffle(actionCond);
            for (var i, _pj_f = 0, _pj_d = util.range((actionCond.length - 2)), _pj_e = _pj_d.length; (_pj_f < _pj_e); _pj_f += 1) {
                i = _pj_d[_pj_f];
                if (((actionCond[i] === actionCond[(i + 1)]) && (actionCond[(i + 1)] === actionCond[(i + 2)]))) {
                    break;
                } else {
                    checkConditions = true;
                }
            }
        }
        blockCond = function () {
        var _pj_d = [], _pj_e = util.range(0, actionCond.length, N_blockStim);
        for (var _pj_f = 0, _pj_g = _pj_e.length; (_pj_f < _pj_g); _pj_f += 1) {
            var i = _pj_e[_pj_f];
            _pj_d.push(actionCond.slice(i, (i + N_blockStim)));
        }
        return _pj_d;
    }
    .call(this);
        block_list.push(blockCond);
    }
    reshaped_list = [];
    for (var outer_list, _pj_c = 0, _pj_a = block_list, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        outer_list = _pj_a[_pj_c];
        for (var inner_list, _pj_f = 0, _pj_d = outer_list, _pj_e = _pj_d.length; (_pj_f < _pj_e); _pj_f += 1) {
            inner_list = _pj_d[_pj_f];
            reshaped_list.push(inner_list);
        }
    }
    block_list = reshaped_list;
    condIdxList = [];
    for (var num, _pj_c = 0, _pj_a = util.range(N_condition), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        num = _pj_a[_pj_c];
        for (var _, _pj_f = 0, _pj_d = util.range(N_rep), _pj_e = _pj_d.length; (_pj_f < _pj_e); _pj_f += 1) {
            _ = _pj_d[_pj_f];
            condIdxList.push(num);
        }
    }
    enumerated_list = [];
    idx = 0;
    for (var val, _pj_c = 0, _pj_a = condIdxList, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        val = _pj_a[_pj_c];
        enumerated_list.push([idx, val]);
        idx = (idx + 1);
    }
    checkConditions = false;
    shuffled_indexes = [];
    shuffled_cond = [];
    while ((! checkConditions)) {
        util.shuffle(enumerated_list);
        for (var row, _pj_c = 0, _pj_a = enumerated_list, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
            row = _pj_a[_pj_c];
            shuffled_indexes.push(row[0]);
            shuffled_cond.push(row[1]);
        }
        for (var i, _pj_c = 0, _pj_a = util.range((shuffled_cond.length - 2)), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
            i = _pj_a[_pj_c];
            if (((shuffled_cond[i] === shuffled_cond[(i + 1)]) && (shuffled_cond[(i + 1)] === shuffled_cond[(i + 2)]))) {
                break;
            } else {
                checkConditions = true;
            }
        }
    }
    for (var i, _pj_c = 0, _pj_a = shuffled_indexes, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        i = _pj_a[_pj_c];
        cbBlockList.push(block_list[i]);
    }
    ctShuffledCounter = 0;
    dictBlock = {};
    condList = [];
    actionList = [];
    dirList = [];
    actionStr = "";
    for (var block, _pj_c = 0, _pj_a = util.range(N_block), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        block = _pj_a[_pj_c];
        dictBlock = {};
        condList = [];
        actionList = [];
        dirList = [];
        for (var idx, _pj_f = 0, _pj_d = util.range(N_stim), _pj_e = _pj_d.length; (_pj_f < _pj_e); _pj_f += 1) {
            idx = _pj_d[_pj_f];
            actionStr = cbBlockList[block][idx];
            condList.push(actionStr.slice(0, (- 2)));
            actionList.push(actionStr);
            dirList.push((("./stimuli/" + actionStr) + ".mp4"));
        }
        dictBlock["conditions"] = condList;
        dictBlock["actions"] = actionList;
        dictBlock["stimDir"] = dirList;
        dictBlockList.push(dictBlock);
    }
    for (var i, _pj_c = 0, _pj_a = util.range(N_block), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        i = _pj_a[_pj_c];
        condBlockList.push(find_unique(dictBlockList[i]["conditions"]));
    }
    
    // keep track of which components have finished
    stimShufflerComponents = [];
    
    for (const thisComponent of stimShufflerComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function stimShufflerRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'stimShuffler' ---
    // get current time
    t = stimShufflerClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of stimShufflerComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function stimShufflerRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'stimShuffler' ---
    for (const thisComponent of stimShufflerComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('stimShuffler.stopped', globalClock.getTime());
    // the Routine "stimShuffler" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _keyWelcome_allKeys;
var welcomeScreenComponents;
function welcomeScreenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'welcomeScreen' ---
    t = 0;
    welcomeScreenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('welcomeScreen.started', globalClock.getTime());
    keyWelcome.keys = undefined;
    keyWelcome.rt = undefined;
    _keyWelcome_allKeys = [];
    // keep track of which components have finished
    welcomeScreenComponents = [];
    welcomeScreenComponents.push(textWelcome);
    welcomeScreenComponents.push(keyWelcome);
    
    for (const thisComponent of welcomeScreenComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function welcomeScreenRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'welcomeScreen' ---
    // get current time
    t = welcomeScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textWelcome* updates
    if (t >= 0.0 && textWelcome.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textWelcome.tStart = t;  // (not accounting for frame time here)
      textWelcome.frameNStart = frameN;  // exact frame index
      
      textWelcome.setAutoDraw(true);
    }
    
    
    // *keyWelcome* updates
    if (t >= 0.0 && keyWelcome.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyWelcome.tStart = t;  // (not accounting for frame time here)
      keyWelcome.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keyWelcome.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keyWelcome.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keyWelcome.clearEvents(); });
    }
    
    if (keyWelcome.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyWelcome.getKeys({keyList: ['space'], waitRelease: false});
      _keyWelcome_allKeys = _keyWelcome_allKeys.concat(theseKeys);
      if (_keyWelcome_allKeys.length > 0) {
        keyWelcome.keys = _keyWelcome_allKeys[_keyWelcome_allKeys.length - 1].name;  // just the last key pressed
        keyWelcome.rt = _keyWelcome_allKeys[_keyWelcome_allKeys.length - 1].rt;
        keyWelcome.duration = _keyWelcome_allKeys[_keyWelcome_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of welcomeScreenComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function welcomeScreenRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'welcomeScreen' ---
    for (const thisComponent of welcomeScreenComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('welcomeScreen.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(keyWelcome.corr, level);
    }
    psychoJS.experiment.addData('keyWelcome.keys', keyWelcome.keys);
    if (typeof keyWelcome.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('keyWelcome.rt', keyWelcome.rt);
        psychoJS.experiment.addData('keyWelcome.duration', keyWelcome.duration);
        routineTimer.reset();
        }
    
    keyWelcome.stop();
    // the Routine "welcomeScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _skipRest_allKeys;
var restPeriodComponents;
function restPeriodRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'restPeriod' ---
    t = 0;
    restPeriodClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(15.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('restPeriod.started', globalClock.getTime());
    skipRest.keys = undefined;
    skipRest.rt = undefined;
    _skipRest_allKeys = [];
    // keep track of which components have finished
    restPeriodComponents = [];
    restPeriodComponents.push(crossRest);
    restPeriodComponents.push(skipRest);
    
    for (const thisComponent of restPeriodComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function restPeriodRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'restPeriod' ---
    // get current time
    t = restPeriodClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *crossRest* updates
    if (t >= 0.0 && crossRest.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crossRest.tStart = t;  // (not accounting for frame time here)
      crossRest.frameNStart = frameN;  // exact frame index
      
      crossRest.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crossRest.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crossRest.setAutoDraw(false);
    }
    
    // *skipRest* updates
    if (t >= 0 && skipRest.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      skipRest.tStart = t;  // (not accounting for frame time here)
      skipRest.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { skipRest.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { skipRest.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { skipRest.clearEvents(); });
    }
    
    frameRemains = 0 + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (skipRest.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      skipRest.status = PsychoJS.Status.FINISHED;
        }
      
    if (skipRest.status === PsychoJS.Status.STARTED) {
      let theseKeys = skipRest.getKeys({keyList: ['space'], waitRelease: false});
      _skipRest_allKeys = _skipRest_allKeys.concat(theseKeys);
      if (_skipRest_allKeys.length > 0) {
        skipRest.keys = _skipRest_allKeys[_skipRest_allKeys.length - 1].name;  // just the last key pressed
        skipRest.rt = _skipRest_allKeys[_skipRest_allKeys.length - 1].rt;
        skipRest.duration = _skipRest_allKeys[_skipRest_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of restPeriodComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var countDownN;
function restPeriodRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'restPeriod' ---
    for (const thisComponent of restPeriodComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('restPeriod.stopped', globalClock.getTime());
    // Run 'End Routine' code from codeRest
    console.log(`======= counterBlock ${counterBlock} - condition: ${condBlockList[counterBlock]} =======`);
    counterStim = 0;
    countDownN = 3;
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(skipRest.corr, level);
    }
    psychoJS.experiment.addData('skipRest.keys', skipRest.keys);
    if (typeof skipRest.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('skipRest.rt', skipRest.rt);
        psychoJS.experiment.addData('skipRest.duration', skipRest.duration);
        routineTimer.reset();
        }
    
    skipRest.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var beginBlockComponents;
function beginBlockRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'beginBlock' ---
    t = 0;
    beginBlockClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('beginBlock.started', globalClock.getTime());
    textCountDown.setText(countDownN);
    // keep track of which components have finished
    beginBlockComponents = [];
    beginBlockComponents.push(beginInstruction);
    beginBlockComponents.push(textCountDown);
    
    for (const thisComponent of beginBlockComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function beginBlockRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'beginBlock' ---
    // get current time
    t = beginBlockClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *beginInstruction* updates
    if (t >= 0.0 && beginInstruction.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      beginInstruction.tStart = t;  // (not accounting for frame time here)
      beginInstruction.frameNStart = frameN;  // exact frame index
      
      beginInstruction.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (beginInstruction.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      beginInstruction.setAutoDraw(false);
    }
    
    // *textCountDown* updates
    if (t >= 0.0 && textCountDown.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textCountDown.tStart = t;  // (not accounting for frame time here)
      textCountDown.frameNStart = frameN;  // exact frame index
      
      textCountDown.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (textCountDown.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textCountDown.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of beginBlockComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function beginBlockRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'beginBlock' ---
    for (const thisComponent of beginBlockComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('beginBlock.stopped', globalClock.getTime());
    // Run 'End Routine' code from codeCountDown
    countDownN = (countDownN - 1);
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var stimVidComponents;
function stimVidRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'stimVid' ---
    t = 0;
    stimVidClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('stimVid.started', globalClock.getTime());
    stimAction.setMovie(dictBlockList[counterBlock]["stimDir"][counterStim]);
    // Run 'Begin Routine' code from codeStim
    console.log(`counterStim ${counterStim} - ${dictBlockList[counterBlock]["stimDir"][counterStim]}`);
    
    // keep track of which components have finished
    stimVidComponents = [];
    stimVidComponents.push(stimAction);
    
    for (const thisComponent of stimVidComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function stimVidRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'stimVid' ---
    // get current time
    t = stimVidClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *stimAction* updates
    if (t >= 0.0 && stimAction.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stimAction.tStart = t;  // (not accounting for frame time here)
      stimAction.frameNStart = frameN;  // exact frame index
      
      stimAction.setAutoDraw(true);
      stimAction.play();
    }
    
    if (stimAction.status === PsychoJS.Status.FINISHED) {  // force-end the Routine
        continueRoutine = false;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of stimVidComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function stimVidRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'stimVid' ---
    for (const thisComponent of stimVidComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('stimVid.stopped', globalClock.getTime());
    stimAction.stop();  // ensure movie has stopped at end of Routine
    // the Routine "stimVid" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var endStimComponents;
function endStimRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'endStim' ---
    t = 0;
    endStimClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('endStim.started', globalClock.getTime());
    // Run 'Begin Routine' code from codeEndStim
    counterStim += 1;
    
    // keep track of which components have finished
    endStimComponents = [];
    
    for (const thisComponent of endStimComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function endStimRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'endStim' ---
    // get current time
    t = endStimClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of endStimComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function endStimRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'endStim' ---
    for (const thisComponent of endStimComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('endStim.stopped', globalClock.getTime());
    // the Routine "endStim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var endFuncRunComponents;
function endFuncRunRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'endFuncRun' ---
    t = 0;
    endFuncRunClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('endFuncRun.started', globalClock.getTime());
    // Run 'Begin Routine' code from codeEndRun
    counterBlock += 1;
    
    // keep track of which components have finished
    endFuncRunComponents = [];
    
    for (const thisComponent of endFuncRunComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function endFuncRunRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'endFuncRun' ---
    // get current time
    t = endFuncRunClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of endFuncRunComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function endFuncRunRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'endFuncRun' ---
    for (const thisComponent of endFuncRunComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('endFuncRun.stopped', globalClock.getTime());
    // the Routine "endFuncRun" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _keyEnd_allKeys;
var endTrialComponents;
function endTrialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'endTrial' ---
    t = 0;
    endTrialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(20.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('endTrial.started', globalClock.getTime());
    keyEnd.keys = undefined;
    keyEnd.rt = undefined;
    _keyEnd_allKeys = [];
    // keep track of which components have finished
    endTrialComponents = [];
    endTrialComponents.push(textEnd);
    endTrialComponents.push(keyEnd);
    
    for (const thisComponent of endTrialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function endTrialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'endTrial' ---
    // get current time
    t = endTrialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textEnd* updates
    if (t >= 0.0 && textEnd.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textEnd.tStart = t;  // (not accounting for frame time here)
      textEnd.frameNStart = frameN;  // exact frame index
      
      textEnd.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 20 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (textEnd.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textEnd.setAutoDraw(false);
    }
    
    // *keyEnd* updates
    if (t >= 0.0 && keyEnd.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyEnd.tStart = t;  // (not accounting for frame time here)
      keyEnd.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keyEnd.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keyEnd.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keyEnd.clearEvents(); });
    }
    
    frameRemains = 0.0 + 20 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (keyEnd.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      keyEnd.status = PsychoJS.Status.FINISHED;
        }
      
    if (keyEnd.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyEnd.getKeys({keyList: ['space'], waitRelease: false});
      _keyEnd_allKeys = _keyEnd_allKeys.concat(theseKeys);
      if (_keyEnd_allKeys.length > 0) {
        keyEnd.keys = _keyEnd_allKeys[_keyEnd_allKeys.length - 1].name;  // just the last key pressed
        keyEnd.rt = _keyEnd_allKeys[_keyEnd_allKeys.length - 1].rt;
        keyEnd.duration = _keyEnd_allKeys[_keyEnd_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of endTrialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function endTrialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'endTrial' ---
    for (const thisComponent of endTrialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('endTrial.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(keyEnd.corr, level);
    }
    psychoJS.experiment.addData('keyEnd.keys', keyEnd.keys);
    if (typeof keyEnd.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('keyEnd.rt', keyEnd.rt);
        psychoJS.experiment.addData('keyEnd.duration', keyEnd.duration);
        routineTimer.reset();
        }
    
    keyEnd.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
