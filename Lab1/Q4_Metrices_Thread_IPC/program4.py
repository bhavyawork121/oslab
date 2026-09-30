processes = [
    {"pid": "P1", "arrival": 0, "burst": 7},
    {"pid": "P2", "arrival": 2, "burst": 4},
    {"pid": "P3", "arrival": 4, "burst": 1},
    {"pid": "P4", "arrival": 5, "burst": 4},
]

from threading import Thread, current_thread
from multiprocessing import Process, Pipe, Value

# --- Part A: Data and Metrics (From Image) ---
processes = [
    {"pid": "P1", "arrival": 0, "burst": 7},
    {"pid": "P2", "arrival": 2, "burst": 4},
    {"pid": "P3", "arrival": 4, "burst": 1},
    {"pid": "P4", "arrival": 5, "burst": 4},
]

intervals = [
    ("P1", 0, 2), ("P2", 2, 4), ("P1", 4, 6),
    ("P3", 6, 7), ("P2", 7, 9), ("P4", 9, 11),
    ("P1", 11, 13), ("P4", 13, 15), ("P1", 15, 16)
]


def calculate_metrics():
    print("\n--- SCHEDULING METRICS ---")
    print("PID AT BT CT TAT WT RT")

    tat_total = wt_total = rt_total = 0

    for p in processes:
        runs = [x for x in intervals if x[0] == p["pid"]]
        first_start = runs[0][1]
        completion = runs[-1][2]

        tat = completion - p["arrival"]
        wt = tat - p["burst"]
        rt = first_start - p["arrival"]

        tat_total += tat
        wt_total += wt
        rt_total += rt

        print(p["pid"], p["arrival"], p["burst"],
              completion, tat, wt, rt)

    n = len(processes)
    print("Average TAT =", round(tat_total/n,2))
    print("Average WT =", round(wt_total/n,2))
    print("Average RT =", round(rt_total/n,2))

def show_gantt_chart():
    print("\n--- ROUND ROBIN GANTT CHART ---")
    print(" | ".join(pid for pid, _, _ in intervals))
    times = [intervals[0][1]] + [end for _, _, end in intervals]
    print("    ".join(str(t) for t in times))

calculate_metrics()
show_gantt_chart()