import sys

class VirtualMachine:
    def __init__(self, name, ram=1, cpu=1.3, hdd=100, os='Debian'):
        self.name = name
        self.ram = ram
        self.cpu = cpu
        self.hdd = hdd
        self.os = os
        self.status = 0
        self.proc = list()

    def stop(self):
        self.status = 0
        self.proc = list()

    def start(self):
        self.status = 1

    def suspend(self):
        self.status = 2

    def reboot(self):
        self.stop()
        self.start()

    def run(self, pid, ram, cpu, hdd):
        print(f'Ejecutando proceso con PID {pid}...')
        self.proc.append({'pid': pid, 'ram': ram, 'cpu': cpu, 'hdd': hdd})

    def ram_usage(self):
        ram = 0
        for proccess in self.proc:
            ram += proccess['ram']
        return ram * 100 / self.ram

    def cpu_usage(self):
        cpu = 0
        for proccess in self.proc:
            cpu += proccess['cpu']
        return cpu * 100 / self.cpu

    def hdd_usage(self):
        hdd = 0
        for proccess in self.proc:
            hdd += proccess['hdd']
        return hdd * 100 / self.hdd

    def get_status(self):
        if self.status == 0:
            return 'Stopped'
        elif self.status == 1:
            return 'Running'
        else:
            return 'Suspended'

    def __str__(self):
        return f'''
{self.os} <{self.name}> [{self.get_status()}]
{self.ram_usage():.2f}% RAM used | {self.cpu_usage():.2f}% CPU used | {self.hdd_usage():.2f}% HDD used\n'''

if __name__ == '__main__':
    mv1 = VirtualMachine('Minas Tirith', 8, 2.3, 380, 'Ubuntu')
    print(mv1)
    mv1.start()
    print(mv1)
    mv1.run(1, 1.7, 0.3, 20)
    mv1.run(4, 4, 0.9, 100)
    mv1.run(7, 0.4, 1.1, 250)
    print(mv1)
    mv1.reboot()
    print(mv1)


    mv2 = VirtualMachine('Rohan', 6, 1.9, 250, 'Debian')
    print(mv2)
    mv2.start()
    print(mv2)
    mv2.run(2, 0.6, 0.7, 50)
    mv2.run(5, 2.1, 0.2, 75)
    mv2.run(8, 2.5, 0.4, 30)
    print(mv2)
    mv2.reboot()
    print(mv2)


    mv3 = VirtualMachine('Rivendel', 16, 3, 1000, 'OpenSuse')
    print(mv3)
    mv3.start()
    print(mv3)
    mv3.run(3, 2, 1, 25)
    mv3.run(6, 0.3, 0.5, 12)
    mv3.run(9, 1.4, 0.8, 65)
    print(mv3)
    mv3.reboot()
    print(mv3)
