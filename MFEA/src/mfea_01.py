from ga.multi_task_ga import MultiTaskGA
from tasks.tps import TPS

from tasks.binpacking import BinPacking

tps = TPS("../res/tps51.csv")

binpacking_1 = BinPacking("../res/binpacking1.csv")

tasks = []

tasks.append(tps)
tasks.append(binpacking_1)

mfea = MultiTaskGA(tasks, 100, 0.5, 0.5, 100)
mfea.run(3000)