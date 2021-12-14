
import psutil
import threading
import time
import matplotlib.pyplot as plt
import numpy as np


class SystemUtilizationInfo(object):

    def display(self):
        _p = lambda text, param : '{}: {}\n'.format(text, param)
        print(
            _p("CPU percent", self.cpu_usage_percent) +
            _p("RAM usage", self.ram_usage_percent) +
            _p("Disk Usage", self.disk_usage_percent) +
            _p("PID count", self.pdis_count)
        )

    @property
    def disk_usage_percent(self):
        return psutil.disk_usage('/').percent

    @property
    def pdis_count(self):
        return len(psutil.pids())

    @property
    def ram_usage_percent(self):
        return psutil.virtual_memory().percent

    @property
    def ram_usage_mb(self):
        v = psutil.virtual_memory()
        return int(v.total - v.available) / 1024 / 1024
    
    @property
    def cpu_usage_percent(self):
        return psutil.cpu_percent(interval=0.5)


class Subplotter(object):

    def __init__(self, axs, x,color):
        self.color = color
        self.axs = axs
        self.y = np.array([0])
        self.lines, = self.axs.plot(x, self.y,color=color)

    def append_new_value(self, val):
        self.y = np.append(self.y, val)

    def draw(self, x):
        self.lines.set_xdata(x)
        self.lines.set_ydata(self.y)
        self.axs.relim()
        self.axs.autoscale_view()


class Plotter(object):

    def __init__(self):
        self.iterator = 0
        self.x_time = np.array([0])

        self.figure, all_subplots = plt.subplots(6)
        self.figure.tight_layout()

        self.cpu_usage = Subplotter(all_subplots[0], self.x_time,'r')
        self.cpu_usage.axs.set_ylabel("cpu % use")
        self.cpu_usage.axs.set_title("CPU usage")

        self.ram_usage = Subplotter(all_subplots[1], self.x_time,'b')
        self.ram_usage.axs.set_title("ram MB use")
        self.ram_usage.axs.set_ylabel("RAM usage")

        self.ram_usage_percent = Subplotter(all_subplots[2], self.x_time,'g')
        self.ram_usage_percent.axs.set_title("ram % use")
        self.ram_usage_percent.axs.set_ylabel("RAM usage")

        self.pdis_count = Subplotter(all_subplots[3], self.x_time,'r')
        self.pdis_count.axs.set_title("pdis count")
        self.pdis_count.axs.set_ylabel("PDIs Count")

        self.disk_usage_percent = Subplotter(all_subplots[4], self.x_time,'b')
        self.disk_usage_percent.axs.set_title("Disk % usage")
        self.disk_usage_percent.axs.set_ylabel("Disk usage")

        plt.show(block=False)

    def push_data(self, system_info):
        self.cpu_usage.append_new_value(system_info.cpu_usage_percent)
        self.ram_usage.append_new_value(system_info.ram_usage_mb)
        self.ram_usage_percent.append_new_value(system_info.ram_usage_percent)
        self.pdis_count.append_new_value(system_info.pdis_count)
        self.disk_usage_percent.append_new_value(system_info.disk_usage_percent)

    def draw(self):
        try:
            self.x_time = np.append(self.x_time, self.iterator)
            self.iterator += 1

            self.cpu_usage.draw(self.x_time)
            self.ram_usage.draw(self.x_time)
            self.ram_usage_percent.draw(self.x_time)
            self.pdis_count.draw(self.x_time)
            self.disk_usage_percent.draw(self.x_time)

            self.figure.canvas.draw()
            self.figure.canvas.flush_events()
        except ValueError:
            print("ValueError: shape mismatch: objects cannot be broadcast to a single shape")


var = False
def f():
    counter = 0
    p = Plotter()
    while var:
        time.sleep(0.1)
        s = SystemUtilizationInfo()
        s.display()
        p.push_data(s)
        p.draw()
        print("Function {} run!".format(counter))
        counter += 1


if __name__ == "__main__":
    t1 = threading.Thread(target=f)
    print("Starting thread")
    var = True
    t1.start()
    time.sleep(10)
    print("Something done")
    var = False
    t1.join()
    print("Thread Done")