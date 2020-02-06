from src.ActivationFunction import *
from src.CostFunction import *
from src.ExampleTemplate import ExampleTemplate


class XorExample(ExampleTemplate):

    def get_data(self) -> np.array:
        return np.array(
            [[1, 1, 0],
             [0, 0, 0],
             [0, 1, 1],
             [1, 0, 1]]
        )

    def define_data(self):
        self.training_data = self.get_columns_between_a_and_b(self.get_data(), 0, 1)
        self.expected_output = self.get_column(self.get_data(), 2)

    def define_architecture(self):
        self.architecture = []
        self.input_neurons = 2
        self.output_neurons = 1

        layer_1 = (2, Relu())
        layer_2 = (2, Relu())
        layer_3 = (2, Relu())
        layer_4 = (2, Relu())

        self.architecture.append(layer_1)
        self.architecture.append(layer_2)
        self.architecture.append(layer_3)
        self.architecture.append(layer_4)

        self.cost_function = MeanSquaredError()

    def define_training_parameters(self):
        self.learning_rate = 0.1
        self.iterations = 10_000

    def run_tests(self):
        print(f" [0, 0] = {self.neuronal_net.forward(np.array([0, 0]).reshape(-1, 1))}")
        print(f" [0, 1] = {self.neuronal_net.forward(np.array([0, 1]).reshape(-1, 1))}")
        print(f" [1, 0] = {self.neuronal_net.forward(np.array([1, 0]).reshape(-1, 1))}")
        print(f" [1, 1] = {self.neuronal_net.forward(np.array([1, 1]).reshape(-1, 1))}")


if __name__ == '__main__':
    xor_example = XorExample("xor_example")
    xor_example.run()
