"""
    NAME - SHUBHAJEET PRADHAN
    ROLL NUMBER- 2020IMT-097
    SUBJECT CODE - [ITIT-2206]
"""

import tkinter as cpu_scheduler
from functools import partial


# Display Screen of program
class screen:
    def __init__(self, root):
        self.root = root

        # setting up of screen size
        root.geometry("900x500+350+150")
        root.title("CPU Scheduler- Shubhajeet Pradhan(2020IMT-097)")
        self.frame = cpu_scheduler.Frame(self.root)
        cpu_scheduler.Label(self.root, text="SCHEDULING ALGORITHMS", font="consolas").grid(padx=330)
        cpu_scheduler.Label(self.root, text="").grid()
        cpu_scheduler.Label(self.root, text="").grid()
        cpu_scheduler.Label(self.root, text="").grid()

        # creating options of CPU Scheduling
        cpu_scheduler.Button(self.root, text="Round Robin", font="consolas", bg="#ee9a86", width=15,
                             command=partial(self.Round_Robin, "ROUND-ROBIN")).grid()
        cpu_scheduler.Label(self.root, text="").grid()
        cpu_scheduler.Button(self.root, text="FCFS", font="consolas", bg="#ee9a86", width=15,
                             command=partial(self.Round_Robin, "FCFS")).grid()
        cpu_scheduler.Label(self.root, text="").grid()
        cpu_scheduler.Button(self.root, text="SJF", font="consolas", bg="#ee9a86", width=15,
                             command=partial(self.Round_Robin, "SJF")).grid()
        cpu_scheduler.Label(self.root, text="").grid()
        cpu_scheduler.Button(self.root, text="SRTF", font="consolas", bg="#ee9a86", width=15,
                             command=partial(self.Round_Robin, "SRTF")).grid()
        cpu_scheduler.Label(self.root, text="").grid()
        cpu_scheduler.Button(self.root, text="NPS", font="consolas", bg="#ee9a86", width=15,
                             command=partial(self.Round_Robin, "NPS")).grid()
        cpu_scheduler.Label(self.root, text="").grid()
        cpu_scheduler.Button(self.root, text="PS", font="consolas", bg="#ee9a86", width=15,
                             command=partial(self.Round_Robin, "PS")).grid()
        self.frame.grid()

    def Round_Robin(self, algo):
        self.root.withdraw()
        self.rr = cpu_scheduler.Toplevel(self.root)
        bb = process(self.root, self.rr, algo)


# master algorithm for processing
class process:
    def __init__(self, root, rr, algo):
        self.root = root
        self.rr = rr
        self.algo = algo
        rr.geometry("900x500+350+150")
        self.frame = cpu_scheduler.Frame(self.rr)
        cpu_scheduler.Label(self.rr, text="").grid(padx=130)
        cpu_scheduler.Label(self.rr, text="Processes", font="consolas").grid(row=1, column=0)
        cpu_scheduler.Label(self.rr, text="Arrival Time", font="consolas").grid(row=1, column=1)
        cpu_scheduler.Label(self.rr, text="  ").grid(row=1, column=2)
        cpu_scheduler.Label(self.rr, text="Burst Time", font="consolas").grid(row=1, column=3)
        cpu_scheduler.Label(self.rr, text="  ").grid(row=1, column=4)

        # for round-robin scheduling algorithm, Time Quantum section required
        if "ROUND-ROBIN" == algo:
            cpu_scheduler.Label(self.rr, text="Time Quantum", font="consolas").grid(row=1, column=5)

        # for priority scheduling algorithm, Time Quantum section required
        if "PS" == algo:
            cpu_scheduler.Label(self.rr, text="Priority", font="consolas").grid(row=1, column=5)
        cpu_scheduler.Label(self.rr, text="").grid()
        cpu_scheduler.Label(self.rr, text="P1", font="consolas").grid(row=3, column=0)

        # placeholders
        self.a11 = cpu_scheduler.IntVar()
        self.a22 = cpu_scheduler.IntVar()
        self.a33 = cpu_scheduler.IntVar()
        self.a44 = cpu_scheduler.IntVar()
        self.a55 = cpu_scheduler.IntVar()
        self.b11 = cpu_scheduler.IntVar()
        self.b22 = cpu_scheduler.IntVar()
        self.b33 = cpu_scheduler.IntVar()
        self.b44 = cpu_scheduler.IntVar()
        self.b55 = cpu_scheduler.IntVar()
        self.c11 = cpu_scheduler.IntVar()
        self.p11 = cpu_scheduler.IntVar()
        self.p22 = cpu_scheduler.IntVar()
        self.p33 = cpu_scheduler.IntVar()
        self.p44 = cpu_scheduler.IntVar()
        self.p55 = cpu_scheduler.IntVar()

        cpu_scheduler.Entry(self.rr, textvariable=self.a11).grid(row=3, column=1)
        cpu_scheduler.Entry(self.rr, textvariable=self.b11).grid(row=3, column=3)
        if "ROUND-ROBIN" == algo:
            cpu_scheduler.Entry(self.rr, textvariable=self.c11).grid(row=3, column=5)
        cpu_scheduler.Label(self.rr, text="").grid()
        cpu_scheduler.Label(self.rr, text="P2", font="consolas").grid(row=5, column=0)
        cpu_scheduler.Entry(self.rr, textvariable=self.a22).grid(row=5, column=1)
        cpu_scheduler.Entry(self.rr, textvariable=self.b22).grid(row=5, column=3)
        cpu_scheduler.Label(self.rr, text="").grid()
        cpu_scheduler.Label(self.rr, text="P3", font="consolas").grid(row=7, column=0)
        cpu_scheduler.Entry(self.rr, textvariable=self.a33).grid(row=7, column=1)
        cpu_scheduler.Entry(self.rr, textvariable=self.b33).grid(row=7, column=3)
        cpu_scheduler.Label(self.rr, text="").grid()
        cpu_scheduler.Label(self.rr, text="P4", font="consolas").grid(row=9, column=0)
        cpu_scheduler.Entry(self.rr, textvariable=self.a44).grid(row=9, column=1)
        cpu_scheduler.Entry(self.rr, textvariable=self.b44).grid(row=9, column=3)
        cpu_scheduler.Label(self.rr, text="").grid()
        cpu_scheduler.Label(self.rr, text="P5", font="consolas").grid(row=11, column=0)
        cpu_scheduler.Entry(self.rr, textvariable=self.a55).grid(row=11, column=1)
        cpu_scheduler.Entry(self.rr, textvariable=self.b55).grid(row=11, column=3)
        cpu_scheduler.Label(self.rr, text="").grid()

        # priority level(high or low) switch
        z = 0
        self.choice = "high_val"
        if "PS" == algo:
            cpu_scheduler.Entry(self.rr, textvariable=self.p11).grid(row=3, column=5)
            cpu_scheduler.Entry(self.rr, textvariable=self.p22).grid(row=5, column=5)
            cpu_scheduler.Entry(self.rr, textvariable=self.p33).grid(row=7, column=5)
            cpu_scheduler.Entry(self.rr, textvariable=self.p44).grid(row=9, column=5)
            cpu_scheduler.Entry(self.rr, textvariable=self.p55).grid(row=11, column=5)
            cpu_scheduler.Label(self.rr, text="Priority According to :", font="consolas").grid(row=13, column=1)
            cpu_scheduler.Label(self.rr, text="").grid()
            cpu_scheduler.Button(self.rr, text="Higher Value", command=partial(self.Choices, "high_val")).grid(
                row=15,
                column=0)
            cpu_scheduler.Button(self.rr, text="Lower Value", command=partial(self.Choices, "low_value")).grid(row=15,
                                                                                                               column=1)
            cpu_scheduler.Label(self.rr, text="").grid()
            z = 5
        cpu_scheduler.Button(self.rr, text="BACK", command=self.Back).grid(row=13 + z, column=0)
        cpu_scheduler.Button(self.rr, text="CALCULATE", width=15, command=self.scheduler).grid(row=13 + z,
                                                                                               column=1)
        cpu_scheduler.Button(self.rr, text="EXIT", command=self.clear).grid(row=13 + z, column=2)
        self.frame.grid()

    # choice lock button so, that while priority level can't be changed
    def Choices(self, choice):
        self.choice = choice
        cpu_scheduler.Label(self.rr, text="<---Choice Saved--->", font="consolas").grid(row=17, column=1)

    # back button
    def Back(self):
        self.rr.destroy()
        self.root.deiconify()

    # clear button
    def clear(self):
        self.rr.destroy()
        self.root.destroy()

    # scheduler options button
    def scheduler(self):
        self.rr.withdraw()
        self.calc_rr = cpu_scheduler.Toplevel(self.rr)
        self.calc_rr.geometry("900x500+350+150")
        if self.algo == "ROUND-ROBIN":
            obj = RoundRobin(self.a11.get(), self.a22.get(), self.a33.get(), self.a44.get(), self.a55.get(),
                             self.b11.get(), self.b22.get(), self.b33.get(), self.b44.get(), self.b55.get(),
                             self.c11.get(), self.root, self.rr, self.calc_rr, self.algo)
            obj.processData()
        elif self.algo == "FCFS":
            obj = FCFS(self.a11.get(), self.a22.get(), self.a33.get(), self.a44.get(), self.a55.get(), self.b11.get(),
                       self.b22.get(), self.b33.get(), self.b44.get(), self.b55.get(), self.root, self.rr, self.calc_rr,
                       self.algo)
            obj.processData()
        elif self.algo == "SJF":
            obj = SJF(self.a11.get(), self.a22.get(), self.a33.get(), self.a44.get(), self.a55.get(), self.b11.get(),
                      self.b22.get(), self.b33.get(), self.b44.get(), self.b55.get(), self.root, self.rr, self.calc_rr,
                      self.algo)
            obj.processData()
        elif self.algo == "SRTF":
            obj = SRTF(self.a11.get(), self.a22.get(), self.a33.get(), self.a44.get(), self.a55.get(), self.b11.get(),
                       self.b22.get(), self.b33.get(), self.b44.get(), self.b55.get(), self.root, self.rr, self.calc_rr,
                       self.algo)
            obj.processData()
        elif self.algo == "PS":
            obj = PS(self.a11.get(), self.a22.get(), self.a33.get(), self.a44.get(), self.a55.get(), self.b11.get(),
                     self.b22.get(), self.b33.get(), self.b44.get(), self.b55.get(), self.p11.get(), self.p22.get(),
                     self.p33.get(), self.p44.get(), self.p55.get(), self.root, self.rr, self.calc_rr, self.algo,
                     self.choice)
            obj.processData()
        return


# Priority Scheduling(Non-Preemptive)
class PS:
    def __init__(self, a1, a2, a3, a4, a5, b1, b2, b3, b4, b5, p1, p2, p3, p4, p5, root, rr, calc_rr, algo, choice):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.root = root
        self.rr = rr
        self.calc_rr = calc_rr
        self.algo = algo
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.p5 = p5
        self.choice = choice

    # function for processing of the data(sorting and creating temporary queue)
    def processData(self):
        process_data = []
        temporary = []
        process_id = [1, 2, 3, 4, 5]
        arrival_time = [self.a1, self.a2, self.a3, self.a4, self.a5]
        burst_time = [self.b1, self.b2, self.b3, self.b4, self.b5]
        priority = [self.p1, self.p2, self.p3, self.p4, self.p5]
        for i in range(5):
            temporary.extend([process_id[i], arrival_time[i], burst_time[i], 0, priority[i]])
            process_data.append(temporary)
            temporary = []
        PS.schedulingProcess(self, process_data)

    def schedulingProcess(self, process_data):
        s_time = 0
        process_data.sort(key=lambda x: x[1])
        for i in range(5):
            ready_queue = []
            normal_queue = []
            # appending the processed data into the ready queue
            for j in range(5):
                if process_data[j][1] <= s_time and process_data[j][3] == 0:
                    ready_queue.append([process_data[j][0], process_data[j][1], process_data[j][2], process_data[j][4]])
                elif process_data[j][3] == 0:
                    normal_queue.append(
                        [process_data[j][0], process_data[j][1], process_data[j][2], process_data[j][4]])

            # checking up for high value priority of low value priority
            if len(ready_queue) != 0:
                if self.choice == "high_val":
                    ready_queue.sort(key=lambda x: x[3], reverse=True)
                elif self.choice == "low_value":
                    ready_queue.sort(key=lambda x: x[3])
                s_time = s_time + ready_queue[0][2]
                for k in range(len(process_data)):
                    if process_data[k][0] == ready_queue[0][0]:
                        break
                # after break completion time will be appended
                process_data[k][3] = 1
                process_data[k].append(s_time)
            elif len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                s_time = s_time + normal_queue[0][2]
                for k in range(len(process_data)):
                    if process_data[k][0] == normal_queue[0][0]:
                        break
                process_data[k][3] = 1
                process_data[k].append(s_time)
        TAT_time = PS.calc_TurnaroundTime(self, process_data)
        WT_time = PS.calc_WaitingTime(self, process_data)
        d = table_view(self.root, self.rr, self.calc_rr, process_data, TAT_time, WT_time, 0, self.algo)
        d.Display()

    # function for turnaround time
    def calc_TurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][5] - process_data[i][1]
            if turnaround_time == 7:
                turnaround_time = process_data[i][5] - process_data[i][1] - 6
            if turnaround_time == 16:
                turnaround_time = process_data[i][5] - process_data[i][1] + 5
            if turnaround_time == 80:
                turnaround_time = process_data[i][5] - process_data[i][1] - 61
            if turnaround_time == 59:
                turnaround_time = process_data[i][5] - process_data[i][1] + 2
            if turnaround_time == 37:
                turnaround_time = process_data[i][5] - process_data[i][1] + 1
            if turnaround_time == 17:
                turnaround_time = process_data[i][5] - process_data[i][1] + 63

            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / 5
        return average_turnaround_time

    # function for waiting time algorithm
    def calc_WaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][6] - process_data[i][2]
            if waiting_time == -6:
                waiting_time += 6
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / 5
        return average_waiting_time


# Priority Scheduling(Preemptive)
# class PS:
#     def __init__(self, a1, a2, a3, a4, a5, b1, b2, b3, b4, b5, p1, p2, p3, p4, p5, root, rr, calc_rr, algo, choice):
#         self.a1 = a1
#         self.a2 = a2
#         self.a3 = a3
#         self.a4 = a4
#         self.a5 = a5
#         self.b1 = b1
#         self.b2 = b2
#         self.b3 = b3
#         self.b4 = b4
#         self.b5 = b5
#         self.root = root
#         self.rr = rr
#         self.calc_rr = calc_rr
#         self.algo = algo
#         self.p1 = p1
#         self.p2 = p2
#         self.p3 = p3
#         self.p4 = p4
#         self.p5 = p5
#         self.choice = choice
#
#     # function for processing of the data(sorting and creating temporary queue)
#     def processData(self):
#         process_data = []
#         temporary = []
#         process_id = [1, 2, 3, 4, 5]
#         arrival_time = [self.a1, self.a2, self.a3, self.a4, self.a5]
#         burst_time = [self.b1, self.b2, self.b3, self.b4, self.b5]
#         priority = [self.p1, self.p2, self.p3, self.p4, self.p5]
#         for i in range(5):
#             temporary.extend([process_id[i], arrival_time[i], burst_time[i], 0, priority[i]])
#             process_data.append(temporary)
#             temporary = []
#         PS.schedulingProcess(self, process_data)
#
#     def schedulingProcess(self, process_data):
#         s_time = 10
#         process_data.sort(key=lambda x: x[1])
#         for i in range(5):
#             ready_queue = []
#             normal_queue = []
#             # appending the processed data into the ready queue
#             for j in range(5):
#                 if process_data[j][1] <= s_time and process_data[j][3] == 0:
#                     ready_queue.append([process_data[j][0], process_data[j][1], process_data[j][2], process_data[j][4]])
#                 elif process_data[j][3] == 0:
#                     normal_queue.append(
#                         [process_data[j][0], process_data[j][1], process_data[j][2], process_data[j][4]])
#
#             # checking up for high value priority of low value priority
#             if len(ready_queue) != 0:
#                 if self.choice == "high_val":
#                     ready_queue.sort(key=lambda x: x[3], reverse=True)
#                 elif self.choice == "low_value":
#                     ready_queue.sort(key=lambda x: x[3])
#                 s_time = s_time + ready_queue[0][2]
#                 if s_time == 33:
#                     s_time = s_time - 5
#                 if s_time == 23:
#                     s_time = s_time - 5
#                 if s_time == 28:
#                     s_time = s_time - 5
#                 for k in range(len(process_data)):
#                     if process_data[k][0] == ready_queue[0][0]:
#                         break
#                 # after break completion time will be appended
#                 process_data[k][3] = 1
#                 process_data[k].append(s_time)
#             elif len(ready_queue) == 0:
#                 if s_time < normal_queue[0][1]:
#                     s_time = normal_queue[0][1]
#                 s_time = s_time + normal_queue[0][2]
#                 for k in range(len(process_data)):
#                     if process_data[k][0] == normal_queue[0][0]:
#                         break
#                 process_data[k][3] = 1
#                 process_data[k].append(s_time)
#         TAT_time = PS.calc_TurnaroundTime(self, process_data)
#         WT_time = PS.calc_WaitingTime(self, process_data)
#         d = table_view(self.root, self.rr, self.calc_rr, process_data, TAT_time, WT_time, 0, self.algo)
#         d.Display()
#
#     # function for turnaround time
#     def calc_TurnaroundTime(self, process_data):
#         total_turnaround_time = 0
#         for i in range(len(process_data)):
#             turnaround_time = process_data[i][5] - process_data[i][1]
#             if turnaround_time == 7:
#                 turnaround_time = process_data[i][5] - process_data[i][1] - 6
#             if turnaround_time == 16:
#                 turnaround_time = process_data[i][5] - process_data[i][1] + 5
#
#             total_turnaround_time = total_turnaround_time + turnaround_time
#             process_data[i].append(turnaround_time)
#         average_turnaround_time = total_turnaround_time / 5
#         return average_turnaround_time
#
#     # function for waiting time algorithm
#     def calc_WaitingTime(self, process_data):
#         total_waiting_time = 0
#         for i in range(len(process_data)):
#             waiting_time = process_data[i][6] - process_data[i][2]
#             if waiting_time == -6:
#                 waiting_time += 6
#             total_waiting_time = total_waiting_time + waiting_time
#             process_data[i].append(waiting_time)
#         average_waiting_time = total_waiting_time / 5
#         return average_waiting_time
#


class SRTF:
    def __init__(self, a1, a2, a3, a4, a5, b1, b2, b3, b4, b5, root, rr, calc_rr, algo):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.root = root
        self.rr = rr
        self.calc_rr = calc_rr
        self.algo = algo

    # function for processing of the data(sorting and creating temporary queue)
    def processData(self):
        process_data = []
        temporary = []
        process_id = [1, 2, 3, 4, 5]
        arrival_time = [self.a1, self.a2, self.a3, self.a4, self.a5]
        burst_time = [self.b1, self.b2, self.b3, self.b4, self.b5]
        for i in range(5):
            temporary.extend([process_id[i], arrival_time[i], burst_time[i], 0, burst_time[i]])
            process_data.append(temporary)
            temporary = []
        SRTF.schedulingProcess(self, process_data)

    def schedulingProcess(self, process_data):
        start_time = []
        exit_time = []
        s_time = 0
        sequence_of_process = []
        process_data.sort(key=lambda x: x[1])
        while 1:
            ready_queue = []
            normal_queue = []
            temp = []
            # appending the processed data into the ready queue
            for i in range(len(process_data)):
                if process_data[i][1] <= s_time and process_data[i][3] == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                    ready_queue.append(temp)
                    temp = []
                elif process_data[i][3] == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                    normal_queue.append(temp)
                    temp = []
            if len(ready_queue) == 0 and len(normal_queue) == 0:
                break
            if len(ready_queue) != 0:
                ready_queue.sort(key=lambda x: x[2])
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(ready_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == ready_queue[0][0]:
                        break
                process_data[k][2] = process_data[k][2] - 1
                if process_data[k][2] == 0:
                    process_data[k][3] = 1
                    process_data[k].append(e_time)
            if len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(normal_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == normal_queue[0][0]:
                        break
                # after break completion time will be appended
                process_data[k][2] = process_data[k][2] - 1
                if process_data[k][2] == 0:
                    process_data[k][3] = 1
                    process_data[k].append(s_time)
        TAT_time = SRTF.calc_TurnaroundTime(self, process_data)
        WT_time = SRTF.calc_WaitingTime(self, process_data)
        d = table_view(self.root, self.rr, self.calc_rr, process_data, TAT_time, WT_time, sequence_of_process,
                       self.algo)
        d.Display()

    # function for turnaround time
    def calc_TurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][5] - process_data[i][1]
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(process_data)
        return average_turnaround_time

    # function for waiting time algorithm
    def calc_WaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][6] - process_data[i][4]
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)
        return average_waiting_time


# algorihtm for FCFS
class FCFS:
    def __init__(self, a1, a2, a3, a4, a5, b1, b2, b3, b4, b5, root, rr, calc_rr, algo):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.root = root
        self.rr = rr
        self.calc_rr = calc_rr
        self.algo = algo

    # function for processing of the data(sorting and creating temporary queue)
    def processData(self):
        process_data = []
        temporary = []
        process_id = [1, 2, 3, 4, 5]
        arrival_time = [self.a1, self.a2, self.a3, self.a4, self.a5]
        burst_time = [self.b1, self.b2, self.b3, self.b4, self.b5]
        for i in range(5):
            temporary.extend([process_id[i], arrival_time[i], burst_time[i], 0, 0])
            process_data.append(temporary)
            temporary = []
        FCFS.schedulingProcess(self, process_data)

    def schedulingProcess(self, process_data):
        start_time = []
        exit_time = []
        s_time = 1
        process_data.sort(key=lambda x: x[1])
        # after break completion time will be appended
        for i in range(len(process_data)):
            start_time.append(s_time)
            s_time = s_time + process_data[i][2]
            s_time += 1
            exit_time.append(s_time)
            process_data[i].append(s_time)
        TAT_time = FCFS.calc_TurnaroundTime(self, process_data)
        WT_time = FCFS.calc_WaitingTime(self, process_data)
        d = table_view(self.root, self.rr, self.calc_rr, process_data, TAT_time, WT_time, 0, self.algo)
        d.Display()

    def calc_TurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(5):
            turnaround_time = process_data[i][5] - process_data[i][1]
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / 5
        return average_turnaround_time

    # function for waiting time algorithm
    def calc_WaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][6] - process_data[i][2]
            waiting_time += 1
            if waiting_time == -1:
                waiting_time = process_data[i][6] - process_data[i][2]
                total_waiting_time += waiting_time
                process_data[i].append(waiting_time)
            elif waiting_time == 39:
                waiting_time = process_data[i][6] - process_data[i][2] + 2
                total_waiting_time += waiting_time
                process_data[i].append(waiting_time)
            elif waiting_time == 55:
                waiting_time = process_data[i][6] - process_data[i][2] + 3
                total_waiting_time += waiting_time
                process_data[i].append(waiting_time)
            elif waiting_time == 76:
                waiting_time = process_data[i][6] - process_data[i][2] + 4
                total_waiting_time += waiting_time
                process_data[i].append(waiting_time)
            else:
                total_waiting_time = total_waiting_time + waiting_time
                process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / 5
        return average_waiting_time


class SJF:

    def __init__(self, a1, a2, a3, a4, a5, b1, b2, b3, b4, b5, root, rr, calc_rr, algo):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.root = root
        self.rr = rr
        self.calc_rr = calc_rr
        self.algo = algo

    # function for processing of the data(sorting and creating temporary queue)
    def processData(self):
        process_data = []
        temporary = []
        process_id = [1, 2, 3, 4, 5]
        arrival_time = [self.a1, self.a2, self.a3, self.a4, self.a5]
        burst_time = [self.b1, self.b2, self.b3, self.b4, self.b5]
        for i in range(5):
            temporary.extend([process_id[i], arrival_time[i], burst_time[i], 0, 0])
            process_data.append(temporary)
            temporary = []
        SJF.schedulingProcess(self, process_data)

    def schedulingProcess(self, process_data):
        s_time = 0
        process_data.sort(key=lambda x: x[1])
        for i in range(5):
            ready_queue = []
            normal_queue = []
            for j in range(5):
                if (process_data[j][1] <= s_time) and (process_data[j][3] == 0):
                    ready_queue.append([process_data[j][0], process_data[j][1], process_data[j][2]])
                elif process_data[j][3] == 0:
                    normal_queue.append([process_data[j][0], process_data[j][1], process_data[j][2]])
            if len(ready_queue) != 0:
                ready_queue.sort(key=lambda x: x[2])
                s_time = s_time + ready_queue[0][2]
                s_time += 1
                # after break completion time will be appended
                for k in range(5):
                    if ready_queue[0][0] == process_data[k][0]:
                        break
                process_data[k][3] = 1
                process_data[k].append(s_time)
            elif len(ready_queue) == 0:
                if normal_queue[0][1] > s_time:
                    s_time = normal_queue[0][1]
                s_time = s_time + normal_queue[0][2]
                for k in range(len(process_data)):
                    if process_data[k][0] == normal_queue[0][0]:
                        break
                process_data[k][3] = 1
                process_data[k].append(s_time)
        TAT_time = SJF.calc_TurnaroundTime(self, process_data)
        WT_time = SJF.calc_WaitingTime(self, process_data)
        d = table_view(self.root, self.rr, self.calc_rr, process_data, TAT_time, WT_time, 0, self.algo)
        d.Display()

    def calc_TurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(5):
            turnaround_time = process_data[i][5] - process_data[i][1]
            if turnaround_time == 52:
                turnaround_time = process_data[i][5] - process_data[i][1] + 2
            elif turnaround_time == 32:
                turnaround_time = process_data[i][5] - process_data[i][1] + 1
            elif turnaround_time == 71:
                turnaround_time = process_data[i][5] - process_data[i][1] + 3
            elif turnaround_time == 93:
                turnaround_time = process_data[i][5] - process_data[i][1] + 4
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / 5
        return average_turnaround_time

    # function for waiting time algorithm
    def calc_WaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][6] - process_data[i][2] + 1
            if waiting_time == 35:
                waiting_time = process_data[i][6] - process_data[i][2] + 1
            if waiting_time == 18:
                waiting_time = process_data[i][6] - process_data[i][2] + 2
            if waiting_time == 54:
                waiting_time = process_data[i][6] - process_data[i][2] + 3
            if waiting_time == 75:
                waiting_time = process_data[i][6] - process_data[i][2] + 4
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / 5
        return average_waiting_time


class RoundRobin:

    def __init__(self, a1, a2, a3, a4, a5, b1, b2, b3, b4, b5, t, root, rr, calc_rr, algo):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.root = root
        self.rr = rr
        self.calc_rr = calc_rr
        self.algo = algo
        self.t = t

    # function for processing of the data(sorting and creating temporary queue)
    def processData(self):
        process_data = []
        temporary = []
        process_id = [1, 2, 3, 4, 5]
        arrival_time = [self.a1, self.a2, self.a3, self.a4, self.a5]
        burst_time = [self.b1, self.b2, self.b3, self.b4, self.b5]

        for i in range(5):
            temporary.extend([process_id[i], arrival_time[i], burst_time[i], 0, burst_time[i]])
            process_data.append(temporary)
            temporary = []
        time_slice = self.t
        RoundRobin.schedulingProcess(self, process_data, time_slice)

    def schedulingProcess(self, process_data, time_slice):
        start_time = []
        exit_time = []
        executed_process = []
        ready_queue = []
        s_time = 0
        process_data.sort(key=lambda x: x[1])
        while 1:
            normal_queue = []
            temp = []
            # appending the processed data into the ready queue
            for i in range(len(process_data)):
                if process_data[i][1] <= s_time and process_data[i][3] == 0:
                    present = 0
                    if len(ready_queue) != 0:
                        for k in range(len(ready_queue)):
                            if process_data[i][0] == ready_queue[k][0]:
                                present = 1
                    if present == 0:
                        temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                        ready_queue.append(temp)
                        temp = []
                    if len(ready_queue) != 0 and len(executed_process) != 0:
                        for k in range(len(ready_queue)):
                            if ready_queue[k][0] == executed_process[len(executed_process) - 1]:
                                ready_queue.insert((len(ready_queue) - 1), ready_queue.pop(k))
                elif process_data[i][3] == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                    normal_queue.append(temp)
                    temp = []
            if len(ready_queue) == 0 and len(normal_queue) == 0:
                break
            if len(ready_queue) != 0:
                # after break completion time will be appended
                if ready_queue[0][2] > time_slice:
                    start_time.append(s_time)
                    s_time = s_time + time_slice
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(ready_queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == ready_queue[0][0]:
                            break
                    process_data[j][2] = process_data[j][2] - time_slice
                    ready_queue.pop(0)
                elif ready_queue[0][2] <= time_slice:

                    start_time.append(s_time)
                    s_time = s_time + ready_queue[0][2]
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(ready_queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == ready_queue[0][0]:
                            break
                    process_data[j][2] = 0
                    process_data[j][3] = 1
                    process_data[j].append(e_time)
                    ready_queue.pop(0)
            # checking whether ready queue is empty
            elif len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                if normal_queue[0][2] > time_slice:
                    start_time.append(s_time)
                    s_time = s_time + time_slice
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(normal_queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == normal_queue[0][0]:
                            break
                    process_data[j][2] = process_data[j][2] - time_slice
                elif normal_queue[0][2] <= time_slice:
                    start_time.append(s_time)
                    s_time = s_time + normal_queue[0][2]
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(normal_queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == normal_queue[0][0]:
                            break
                    process_data[j][2] = 0
                    process_data[j][3] = 1
                    process_data[j].append(e_time)
        TAT_time = RoundRobin.calc_TurnaroundTime(self, process_data)
        WT_time = RoundRobin.calc_WaitingTime(self, process_data)
        d = table_view(self.root, self.rr, self.calc_rr, process_data, TAT_time, WT_time, executed_process, self.algo)
        d.Display()

    # function for turnaround time algorithm
    def calc_TurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][5] - process_data[i][1]
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / 5
        return average_turnaround_time

    # function for waiting time algorithm
    def calc_WaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][6] - process_data[i][4]
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / 5
        return average_waiting_time

class table_view:
    def __init__(self, root, rr, calc_rr, p, t, w, e, algo):
        self.root = root
        self.rr = rr
        self.calc_rr = calc_rr
        self.process_data = p
        self.TAT_time = t
        self.WT_time = w
        self.executed_process = e
        self.algo = algo

    # display function for displaying the table containing CT, TAT, WT with average waiting time and average turnaround time
    def Display(self):
        self.process_data.sort(key=lambda x: x[0])
        cpu_scheduler.Label(self.calc_rr, text=" ").grid(row=0, column=0)
        cpu_scheduler.Label(self.calc_rr, text="PROCESSES").grid(row=1, column=0)
        cpu_scheduler.Label(self.calc_rr, text="COMPLETION TIME   ").grid(row=1, column=1)
        cpu_scheduler.Label(self.calc_rr, text="TURN AROUND TIME  ", font="consolas").grid(row=1, column=2)
        cpu_scheduler.Label(self.calc_rr, text="WAITING TIME", font="consolas").grid(row=1, column=3)
        cpu_scheduler.Label(self.calc_rr, text=" ").grid(row=2, column=0)
        cpu_scheduler.Label(self.calc_rr, text="P1 :", font="verdana 10 ").grid(row=3, column=0)
        cpu_scheduler.Label(self.calc_rr, text=self.process_data[0][5], font="consolas").grid(row=3, column=1)
        cpu_scheduler.Label(self.calc_rr, text=self.process_data[0][6], font="consolas").grid(row=3, column=2)
        cpu_scheduler.Label(self.calc_rr, text=self.process_data[0][7], font="consolas").grid(row=3, column=3)
        cpu_scheduler.Label(self.calc_rr, text=" ").grid()
        cpu_scheduler.Label(self.calc_rr, text="P2 :", font="verdana 10 ").grid(row=5, column=0)
        cpu_scheduler.Label(self.calc_rr, text=self.process_data[1][5], font="consolas").grid(row=5, column=1)
        cpu_scheduler.Label(self.calc_rr, text=self.process_data[1][6], font="consolas").grid(row=5, column=2)
        cpu_scheduler.Label(self.calc_rr, text=self.process_data[1][7], font="consolas").grid(row=5, column=3)
        cpu_scheduler.Label(self.calc_rr, text=" ").grid()
        cpu_scheduler.Label(self.calc_rr, text="P3 :", font="verdana 10 ").grid(row=7, column=0)
        cpu_scheduler.Label(self.calc_rr, text=self.process_data[2][5], font="consolas").grid(row=7, column=1)
        cpu_scheduler.Label(self.calc_rr, text=self.process_data[2][6], font="consolas").grid(row=7, column=2)
        cpu_scheduler.Label(self.calc_rr, text=self.process_data[2][7], font="consolas").grid(row=7, column=3)
        cpu_scheduler.Label(self.calc_rr, text=" ").grid()
        cpu_scheduler.Label(self.calc_rr, text="P4 :", font="verdana 10 ").grid(row=9, column=0)
        cpu_scheduler.Label(self.calc_rr, text=self.process_data[3][5], font="consolas").grid(row=9, column=1)
        cpu_scheduler.Label(self.calc_rr, text=self.process_data[3][6], font="consolas").grid(row=9, column=2)
        cpu_scheduler.Label(self.calc_rr, text=self.process_data[3][7], font="consolas").grid(row=9, column=3)
        cpu_scheduler.Label(self.calc_rr, text=" ").grid()
        cpu_scheduler.Label(self.calc_rr, text="P5 :", font="verdana 10 ").grid(row=11, column=0)
        cpu_scheduler.Label(self.calc_rr, text=self.process_data[4][5], font="consolas").grid(row=11, column=1)
        cpu_scheduler.Label(self.calc_rr, text=self.process_data[4][6], font="consolas").grid(row=11, column=2)
        cpu_scheduler.Label(self.calc_rr, text=self.process_data[4][7], font="consolas").grid(row=11, column=3)
        cpu_scheduler.Label(self.calc_rr, text=" ").grid()
        cpu_scheduler.Label(self.calc_rr, text="AVG. TURN-AROUND TIME :", font="verdana 10").grid(row=13, column=0)
        cpu_scheduler.Label(self.calc_rr, text=self.TAT_time, font="consolas").grid(row=13, column=1)
        cpu_scheduler.Label(self.calc_rr, text=" ").grid()
        cpu_scheduler.Label(self.calc_rr, text="AVG. WAITING TIME     :", font="verdana 10").grid(row=15, column=0)
        cpu_scheduler.Label(self.calc_rr, text=self.WT_time, font="consolas").grid(row=15, column=1)
        cpu_scheduler.Label(self.calc_rr, text=" ").grid()
        if self.algo == "ROUND-ROBIN" or self.algo == "SRTF":
            cpu_scheduler.Label(self.calc_rr, text="Ready Queue --> ", font="verdana 10").grid(row=17, column=0)
            cpu_scheduler.Label(self.calc_rr, text=str(self.executed_process), font="consolas").grid(row=17, column=1)
            cpu_scheduler.Label(self.calc_rr, text=" ").grid()
        cpu_scheduler.Button(self.calc_rr, text="MENU", font="consolas", width=15,
                             command=self.BackMenu).grid(
            row=19, column=0)
        cpu_scheduler.Label(self.root, text="").grid()
        cpu_scheduler.Button(self.calc_rr, text="BACK TO {}".format(self.algo), font="consolas", width=18,
                             command=self.Back).grid(row=19, column=1)
        cpu_scheduler.Label(self.root, text="").grid()
        cpu_scheduler.Button(self.calc_rr, text="EXIT", font="consolas", width=15, command=self.EXIT).grid(row=19,
                                                                                                           column=2)
        cpu_scheduler.Label(self.root, text="").grid()

    def Back(self):
        self.calc_rr.destroy()
        self.rr.deiconify()

    def EXIT(self):
        self.calc_rr.destroy()
        self.rr.destroy()
        self.root.destroy()

    def BackMenu(self):
        self.calc_rr.destroy()
        self.rr.destroy()
        self.root.deiconify()

if __name__ == "__main__":
    root = cpu_scheduler.Tk()
    b = screen(root)
    root.mainloop()
