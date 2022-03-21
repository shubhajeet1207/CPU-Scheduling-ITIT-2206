# CPU Scheduler[ITIT-2206] in *Python*
## _Lab Assignment-4_

CPU Scheduling Algorithms implemented using python and GUI using pyqt5 and tkinter. 

**Time Quantum: 4Msec**

### - Types of schedulers supported: 

1. [FCFS](/FCFS.py)  
2. [SJF](/SJF.py)  
3. [SRTF](/SJF_non.py)  
4. [PRIORITY](/priority.py) 
5. [PRIORITY (NON-PREEMPTIVE)](/priority_non.py) 
6. [Round Robin](/RR.py)  


### - Package Required

For viewing gantt chart & table, following dependencies wil be required-

```sh
pip install matplotlib --user
pip install PyQt5 --user
```

## Table-1


| PROCESS | ARRIVAL TIME | EST. BURST TIME | 
| ------ | ------ | ------ |
| P1 | 0 | 7 |
| P2 | 1 | 19 |
| P3 | 2 | 16 |
| P4 | 3 | 8 |
| P5 | 4 | 5 |

## Table-2

**Context Switching time - 1mSec**

| PROCESS | ARRIVAL TIME | EST. BURST TIME | PRIORITY | 
| ------ | ------ | ------ | ------ |
| P1 | 1 | 17 | 7 |
| P2 | 1 | 19 | 5 |
| P3 | 2 | 16 | 10 |
| P4 | 3 | 21 | 3 |
| P5 | 5 | 23 | 1 |

> [Gantt Chart](/gantt_chart.py) for generating gantt chart.

> [For Scheduling Algorithms](/algorithm.py) for generating table with Avg. TurnAroundTime & Avg.Waiting Time.

## Instructions
```shell

```
## ScreenShots
[Click Here](/screenshots)

