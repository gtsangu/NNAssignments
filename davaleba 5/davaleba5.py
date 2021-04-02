X = [[2,  5,  6,  4],
     [57, 15, 31, 91],
     [12, 80, 57,  6],
     [53,  3, 31,  5],
     [81, 42, 67, 35]]

D = [[4, 4],
     [775, 5],
     [34, 1],
     [56, 4],
     [3, 7]]

W = [[[5, -9, -18, 4, 0], [23, 45, 32, 21, 2], [45, -4, 4, 2, 7]],
     [[-1, -16, 1], [23, 12, 1], [-5, -4, -7]],
     [[11, 2, -14], [51, 14, -13]]]


def relu(x):
    return max(0, x)


def neuro(x, w):
    v = 0
    for i in range(len(x)):
        v += w[i] * x[i]
    return relu(v + w[-1])


def loss(X, D, W):
    total_loss = 0
    for sample_index in range(len(X)):
        sample_x = X[sample_index]
        sample_expected_output = D[sample_index]
        inputs = sample_x
        for layer in W:
            print("input: " + str(inputs))
            print("layer: " + str(layer))
            outputs = []
            for neuron in layer:
                outputs.append(neuro(inputs, neuron))
            inputs = outputs
        print("output: " + str(inputs))
        print("expected output: " + str(sample_expected_output))
        sample_output = inputs
        sample_loss = 0
        for i in range(len(sample_expected_output)):
            sample_loss += (sample_expected_output[i] - sample_output[i])**2
        sample_loss /= 2
        total_loss += sample_loss
        print("loss: " + str(sample_loss))
        print()
    total_loss /= len(X)
    return total_loss


print(loss(X, D, W))
