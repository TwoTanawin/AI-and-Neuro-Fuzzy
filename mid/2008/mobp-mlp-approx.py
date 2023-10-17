import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def error(t, a):
    return t - a

def cal_s_power_2(e):
    return -2 * e

def cal_a2(w2, a_layer1, b2):
    return np.dot(w2, a_layer1) + b2

def cal_s_power_1(a_layer1, w2, s_power2):
    diagonal_elements = (1 - a_layer1) * a_layer1
    return np.diag(diagonal_elements).dot(w2.T).dot(s_power2)

def cal_w_power_2(w2, learningRate, s_power2, a_layer1):
    return w2 - learningRate * np.outer(s_power2, a_layer1)

def cal_b_power_2(b2, learningRate, s_power2):
    return b2 - learningRate * s_power2

def cal_w_power_1(w1, learningRate, s_power1, a_layer0):
    return w1 - learningRate * np.outer(s_power1, a_layer0)

def cal_b_power_1(b1, learningRate, s_power1):
    return b1 - learningRate * s_power1

def cal_a1(p1, w1, b1):
    a1 = sigmoid(p1 * w1 + b1)
    return a1

p1 = 0
t1 = -30

p2 = 100
t2 = 0

w1 = np.array([0.1, 0.3, 0.5])
b1 = np.array([0.9, 0.6, 0.2])

w2 = np.array([1, 2, 3])
b2 = 4

learningRate = 0.01

a_layer0 = 0
a_layer1 = cal_a1(p1, w1, b1)
a_layer2 = cal_a2(w2, a_layer1, b2)

print("a Layer 1:")
print(a_layer1)

print("a Layer 2:")
print(a_layer2)

print("Error 1:")
print(error(t1, a_layer2))

s_power2 = cal_s_power_2(error(t1, a_layer2))
print("s^2:")
print(s_power2)

s_power1 = cal_s_power_1(a_layer1, w2, s_power2)
print("s^1:")
print(s_power1)

w_power2 = cal_w_power_2(w2, learningRate, s_power2, a_layer1)
print("w^2:")
print(w_power2)

b_power2 = cal_b_power_2(b2, learningRate, s_power2)
print("b^2:")
print(b_power2)

w_power1 = cal_w_power_1(w1, learningRate, s_power1, a_layer0)
print("w^1:")
print(w_power1)

b_power1 = cal_b_power_1(b1, learningRate, s_power1)
print("b^1:")
print(b_power1)
