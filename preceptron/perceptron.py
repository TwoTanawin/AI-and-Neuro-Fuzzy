import numpy as np

p = np.array([[[2], [2]],
              [[1], [-2]],
              [[-2], [2]],
              [[-1], [1]]])

t = np.array([0, 1, 0, 1])

weight = np.array([[0, 0]])
bias = np.array([0])
error = [0]

re_check = np.array([])

def cal_a(w0, p, bias):
    a = np.dot(w0, p) + bias
    return a

def hardlim(a):
    if a >= 0:
        return 1
    else:
        return 0

def cal_error(t, a):
    e = t - a
    return e

def new_weight(w0, e, p0):
    n_w = w0 + (e * p0.ravel())
    return n_w

def new_bias(b0, e):
    return b0 + e

def backpropagation(h, weight, p, bias, i):
    err = cal_error(t[i], h)
    nw = new_weight(weight, err, p)
    nb = new_bias(bias, err)
    return err, nw, nb

iteration = 0

# for i in range(len(p)):
#     a = cal_a(weight[-1], p[i], bias[-1])
#     h = hardlim(a)
#     re_check = np.append(re_check, [h])
#     if h != t[i]: 
#         print("error")
#         iteration += 1
#         print(f"Iteration {iteration}")
#         err, nw, nb = backpropagation(h, weight[-1], p[i], bias[-1], i)
#         error.append(err)
#         weight = np.vstack([weight, nw])
#         bias = np.append(bias, [nb])

#     print(f"Last Weight {weight[-1]}, Last bias : {bias[-1]}")
#     print(f"a : {a}, h : {h}")
#     print("--------------------------------------------------")
    
# # print(re_check)    


# if np.all(re_check == t):
#     print('Done!')
#     loop = False
# else:
#     print('Train agin')
#     for i in range(len(p)):
#         a = cal_a(weight[-1], p[i], bias[-1])
#         h = hardlim(a)
#         re_check = np.append(re_check, [h])
#         if h != t[i]: 
#             print("error")
#             iteration += 1
#             print(f"Iteration {iteration}")
#             err, nw, nb = backpropagation(h, weight[-1], p[i], bias[-1], i)
#             error.append(err)
#             weight = np.vstack([weight, nw])
#             bias = np.append(bias, [nb])

#         print(f"Last Weight {weight[-1]}, Last bias : {bias[-1]}")
#         print(f"a : {a}, h : {h}")
#         print("--------------------------------------------------")

# Your code up to the while loop remains the same

while True:
    re_check = np.array([])  # Reset re_check for each iteration
    for i in range(len(p)):
        a = cal_a(weight[-1], p[i], bias[-1])
        h = hardlim(a)
        re_check = np.append(re_check, [h])  # Append the current prediction to re_check
        if h != t[i]: 
            print("error")
            iteration += 1
            print(f"Iteration {iteration}")
            err, nw, nb = backpropagation(h, weight[-1], p[i], bias[-1], i)
            error.append(err)
            weight = np.vstack([weight, nw])
            bias = np.append(bias, [nb])

        print(f"Last Weight {weight[-1]}, Last bias : {bias[-1]}")
        print(f"a : {a}, h : {h}")
        print("--------------------------------------------------")
    
    if np.all(re_check == t):
        print('Done!')
        break
    else:
        print("Train again!")


print(f"Iteration {iteration}")
print(f"Best Weight {weight[-1]}, Best bias : {bias[-1]}")