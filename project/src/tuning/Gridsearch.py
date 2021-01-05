class Gridsearch():

    def __init__(self, executor, domain):
        self.executor = executor
        self.domain = domain

    def run(self):

        hyperparams = {
                "alpha":[0.001],
                "gamma":[0.999, 0.9999, 0.99999,1.],
                "entropy":[1000, 500, 250, 125, 75]
            }

        for i in hyperparams["alpha"]:
            for j in hyperparams["gamma"]:
                for k in hyperparams["entropy"]:
                    individual = [i,j,k]
                    self.executor.submit_task(params=self.unwrap_params(individual))


    def unwrap_params(self, individual):
        params = {}
        for index, value in enumerate(individual):
            params[self.domain.param_dict()[index][0]] = value
        return params