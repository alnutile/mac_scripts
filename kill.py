#!/usr/bin/env python3
import psutil
from time import sleep


class Kill:

    def handle(self):
        checking_count = {}
        for proc in psutil.process_iter():
            if any(procstr in proc.name() for procstr in ["CommCenter"]):
                if proc.name() not in checking_count:
                    cpu_info = proc.cpu_percent()
                    # https://psutil.readthedocs.io/en/latest/#psutil.cpu_percent
                    sleep(0.1)
                    cpu_info = proc.cpu_percent()
                    if cpu_info > 50:
                        print(f'Killing {proc.name()}')
                        proc.kill()


if __name__ == "__main__":
    client = Kill()
    client.handle()
