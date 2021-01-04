import numpy as np
# DO NOT add any library

def train_transformation(X, Y,R, train_steps=100, learning_rate=0.0003):
    #please write your code here
    # find best R using Gradient Descent
    #WRITE your code here
    m = len(Y)
    prediction = X.dot(R)
    for _ in range(train_steps):
        R = R - np.transpose((learning_rate / m * (np.transpose(prediction - Y))).dot(X))
    
    #END of your code
    return R
    
def nearest_neighbor(v, candidates, k=1):
    # find k best similar vectors index. please sort them in order max to min and return index
    # for your similarity function please use cosine similarity
    similarity_l = []
    #WRITE your code here
    for candidate in candidates:
        ss = v.dot(np.transpose(candidate)) / np.sqrt(v.dot(np.transpose(v)) * candidate.dot(np.transpose(candidate)))
        similarity_l = np.append(similarity_l, ss)
    #END of your code
    sorted_ids = np.argsort(similarity_l)

    k_idx = sorted_ids[-k:]
    return k_idx

# This is how this code is called
# X, y = np.load('X_train.npy'), np.load('Y_train.npy')
# print(train_transformation(X, y, np.random.randn(300,300)))