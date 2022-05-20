

from ga.population import Population


class MultiTaskGA() :


    def __init__(self, tasks, pop_size, p_mutation, time_reset):
        self.tasks = tasks
        self.time_reset = time_reset
        self.p_mutation = p_mutation
        self.population = Population(pop_size, tasks)