import numpy as np
import matplotlib.pyplot as plt

X = np.array(([-20], [-19], [-18],[-17],[20],[-10],[30]), dtype=float)
y = np.array(([10], [5], [-1],[5],[20],[-10],[30]), dtype=float)

# scale units
#X = X/np.amax(X, axis=0) # maximum of X array
#y = y/100

class Neural_Network(object):
  def __init__(self):
    #parameters
    self.inputSize = 1
    self.outputSize = 1
    self.hiddenSize = 40
    #weights
    self.W1 = np.random.randn(self.inputSize, self.hiddenSize) # weight matrix from input to hidden layer
    self.W2 = np.random.randn(self.hiddenSize, self.outputSize) # weight matrix from hidden to output layer

  def forward(self, X):
    #forward propagation through our network
    self.z = np.dot(X, self.W1) # dot product of X (input) and first set of 3x2 weights
    self.z2 = self.sigmoid(self.z) # activation function
    self.z3 = np.dot(self.z2, self.W2) # dot product of hidden layer (z2) and second set of 3x1 weights
    #o = self.sigmoid(self.z3) # final activation function
    #o = self.z3
    return self.z3

  def sigmoid(self, s):
    # activation function
    #return 1/(1+np.exp(-s))
    return np.tanh(s)

  def sigmoidPrime(self, s):
    #derivative of sigmoid
    #return s * (1 - s)
    return (1 - (np.tanh(s)**2))

  def backward(self, X, y, o):
    # backward propgate through the network
    self.o_error = y - o # error in output
    self.o_delta = self.o_error*self.sigmoidPrime(o) # applying derivative of sigmoid to error

    self.z2_error = self.o_delta.dot(self.W2.T) # z2 error: how much our hidden layer weights contributed to output error
    self.z2_delta = self.z2_error*self.sigmoidPrime(self.z2) # applying derivative of sigmoid to z2 error

    self.W1 += X.T.dot(self.z2_delta) # adjusting first set (input --> hidden) weights
    self.W2 += self.z2.T.dot(self.o_delta) # adjusting second set (hidden --> output) weights

  def train (self, X, y):
    o = self.forward(X)
    self.backward(X, y, o)

NN = Neural_Network()
for i in range(1000): # trains the NN 1,000 times
  print ("Input: \n" + str(X))
  print ("Actual Output: \n" + str(y))
  print ("Predicted Output: \n" + str(NN.forward(X)))
  print ("Loss: \n" + str(np.mean(np.square(y - NN.forward(X))))) # mean sum squared loss
  print ("\n")
  NN.train(X, y)

  result_array = np.array(([-20],[-19],[-18],[-17],[-16],[-15],[-14],[-13],[-12],[-11],[-10],[-9],[-8],[-7],[-6],[-5],[-4],[-3]
  ,[-2],[-1],[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[11],[12],[13],[14],[15],[16],[17],[18],[19],
  [20]),dtype=float)
  #X_final_pred = np.array((), dtype=float)
  print ("Predicted Output: \n" + str(NN.forward(result_array)))

plt.plot(result_array, NN.forward(result_array))
plt.xlabel('Input (X)')
plt.ylabel('Prediction(Y_)')
plt.title('Prediction on given data')
plt.grid(True)
plt.savefig("test.png")
plt.show()
