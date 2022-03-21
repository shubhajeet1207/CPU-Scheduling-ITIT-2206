import numpy as np
import matplotlib.pyplot as plt;

plt.rcdefaults()
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
import matplotlib.patches as mpatches


def FCFS(n, at, bt):
    wt = [0] * n  # waiting time
    tat = [0] * n  # turn around time
    rt = [0] * n  # remaining time

    for i in range(n):
        rt[i] = bt[i]
    t = 0  # current time
    first = 0
    complete = 0
    check = False
    while (complete != n):
        for j in range(n):
            if ((at[j] <= t) and (rt[j] > 0)):
                first = j
                check = True
        if (check == False):
            t += 1
            continue
        rt[first] = 0
        plt.barh(y=1, left=t, width=bt[first], height=0.5, alpha=0.5)
        plt.text(t, 1, s=first, ha='left', va='center')

        t += bt[first]
        complete += 1

        wt[first] = (t - bt[first] - at[first])
        if wt[first] < 0:
            wt[first] = 0

    for i in range(n):
        tat[i] = bt[i] + wt[i]

    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt = 10 + total_wt + wt[i]
        total_tat = 10 + total_tat + tat[i]

    AWT = total_wt / n
    ATT = total_tat / n
    plt.show()
    return ATT, AWT


def SJF_nonpreem(n, bt, at):
    wt = [0] * n
    tat = [0] * n
    rt = [0] * n

    for i in range(n):
        rt[i] = bt[i]
    complete = 0
    t = 0
    minm = 999999999
    short = 0
    check = False

    while (complete != n):
        for j in range(n):
            if ((at[j] <= t) and
                    (rt[j] < minm) and rt[j] > 0):
                minm = rt[j]
                short = j
                check = True
        if (check == False):
            t += 1
            continue

        rt[short] = 0

        minm = 999999999

        plt.barh(y=1, left=t, width=bt[short], height=0.5, alpha=0.5)
        plt.text(t, 1, s=short, ha='left', va='center')

        complete += 1
        check = False
        t += bt[short]

        wt[short] = (t - bt[short] - at[short])

        if (wt[short] < 0):
            wt[short] = 0

    for i in range(n):
        tat[i] = bt[i] + wt[i]

    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]

    AwT = total_wt / n
    ATT = total_tat / n
    plt.show()
    return ATT, AwT


def SJFpreem(n, bt, at):
    wt = [0] * n
    tat = [0] * n
    rt = [0] * n

    for i in range(n):
        rt[i] = bt[i]
    complete = 0
    t = 0
    minm = 999999999
    short = 0
    check = False

    while (complete != n):
        for j in range(n):
            if ((at[j] <= t) and
                    (rt[j] < minm) and rt[j] > 0):
                minm = rt[j]
                short = j
                check = True
        if (check == False):
            t += 1
            continue
        plt.barh(y=1, left=t, width=1, height=0.5, alpha=0.5)
        plt.text(t, 1, s=short, ha='left', va='center')
        rt[short] -= 1

        minm = rt[short]
        if (minm == 0):
            minm = 999999999

        if (rt[short] == 0):
            complete += 1
            check = False
            fint = t + 1

            wt[short] = (fint - bt[short] - at[short])

            if (wt[short] < 0):
                wt[short] = 0

        t += 1

    for i in range(n):
        tat[i] = bt[i] + wt[i]

    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]

    AwT = total_wt / n
    ATT = total_tat / n
    plt.show()
    return ATT, AwT


def Prioritynon(n, bt, at, pr):
    wt = [0] * n
    tat = [0] * n

    complete = 0
    t = 0
    prior = 99999999
    first = 0
    check = False

    while (complete != n):
        for j in range(n):
            if ((at[j] <= t) and
                    (pr[j] <= prior)):

                if (pr[j] == prior):
                    if (at[j] > at[first]):
                        continue

                prior = pr[j]
                first = j
                check = True
        if (check == False):
            t += 1
            continue

        pr[first] = 999999999

        prior = 99999999

        plt.barh(y=1, left=t, width=bt[first], height=0.5, alpha=0.5)
        plt.text(t, 1, s=first, ha='left', va='center')

        complete += 1
        check = False
        t += bt[first]

        wt[first] = (t - bt[first] - at[first])

        if (wt[first] < 0):
            wt[first] = 0

    for i in range(n):
        tat[i] = bt[i] + wt[i]
    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]

    awt = total_wt / n
    att = total_tat / n
    plt.show()
    return att, awt


def RR(n, bt, at, quantum):
    wt = [0] * n
    tat = [0] * n
    rem_bt = [0] * n

    for i in range(n):
        rem_bt[i] = bt[i]
    t = 0  # Current time
    check = False
    complete = 0

    while (complete != n):

        for j in range(n):

            if (rem_bt[j] > 0 and at[j] <= t):

                check = True
                if (rem_bt[j] > quantum):

                    plt.barh(y=1, left=t, width=quantum, height=0.5, alpha=0.5)
                    plt.text(t, 1, s=j, ha='left', va='center')

                    t += quantum
                    rem_bt[j] -= quantum

                else:

                    plt.barh(y=1, left=t, width=rem_bt[j], height=0.5, alpha=0.5)
                    plt.text(t, 1, s=j, ha='left', va='center')

                    t = t + rem_bt[j]
                    wt[j] = t - bt[j] - at[j]
                    rem_bt[j] = 0
                    complete += 1
        if (check == False):
            t += 1
            continue
        check = False

    for i in range(n):
        tat[i] = bt[i] + wt[i]

    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]

    AWT = total_wt / n
    ATT = total_tat / n
    plt.show()
    return AWT, ATT


def priority_preem(n, bt, at, pr):
    wt = [0] * n
    tat = [0] * n
    rt = [0] * n

    for i in range(n):
        rt[i] = bt[i]
    complete = 0
    t = 0
    prior = 999999999
    first = 0
    check = False

    while (complete != n):
        for j in range(n):
            if ((at[j] <= t) and
                    (pr[j] <= prior) and rt[j] > 0):
                if (pr[j] == prior):
                    if (at[j] > at[first]):
                        continue
                prior = pr[j]
                first = j
                check = True

        if (check == False):
            t += 1
            continue
        plt.barh(y=1, left=t, width=1, height=0.5, alpha=0.5)
        plt.text(t, 1, s=first, ha='left', va='center')
        rt[first] -= 1  # remaining time ^_^

        if (rt[first] == 0):
            complete += 1
            pr[first] = 999999999
            prior = 99999999
            check = False
            fint = t + 1

            wt[first] = (fint - bt[first] - at[first])

            if (wt[first] < 0):
                wt[first] = 0

        t += 1

    for i in range(n):
        tat[i] = bt[i] + wt[i]

    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]

    AWT = total_wt / n
    ATT = total_tat / n
    plt.show()
    return AWT, ATT
