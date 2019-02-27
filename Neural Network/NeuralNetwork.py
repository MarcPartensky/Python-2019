import numpy as np

picture=np.random.randn(28,28)

class NeuralNetwork:
    def __init__(self,sizes=[784,784,28,10]):
        """Create a neural network using list of sizes."""
        self.sizes=sizes
        self.biases=[np.random.randn(y) for y in sizes[1:]]
        self.weights=[np.random.randn(x,y) for x,y in zip(sizes[:-1],sizes[1:])]
        #self.function=lamba x:1/(1+np.exp(-x))

    def evaluate(self,test_data):
        """Return number of successful predictions using test_datas list."""
        results=[(np.argmax(self.predict(x)),y]) for (x,y) in test_data]
        return sum(int(x==y) for (x,y) in results])

    def predict(self,input):
        """Return predictions for given input."""
        input=np.reshape(input,(1,self.sizes[0]))[0]
        for weight,bias in zip(self.weights,self.biases):
            input=self.sigmoid(np.dot(input,weight)+bias)
        return input

    def train(self,training_data,learning_rate=0.1,mini_batch_size=10,epochs=10,test_data=None):
        """Train neural network using training_data and optionnal parameters such as learning rate,
         mini_batch_size, epochs and test_data."""
        for epoch in range(epochs):
            random.shuffle(training_data)
            mini_batches=[training_data[k:k+10] for k in range(0,len(training_data)//10,mini_batch_size)]
            for mini_batch in mini_batches:
                self.learn(mini_batch,learning_rate)
            print("Epochs completed:",epoch,"/",epochs)
            if test_data:
                print("Results:",self.evaluate(test_data),"/",len(test_data))

    def learn(self,mini_batch,learning_rate):
        """Train neural network using minibatch and learning_rate."""
        l=learning_rate
        weights_errors = [np.zeros(weight.shape) for weight in self.weights]
        biases_error  = [np.zeros(bias.shape) for bias in self.biases]
        for input,output in mini_batch:
            biases_columns,weights_columns=self.backpropagation(input,output)
            weights_errors = [error+column for (error,column) in zip(weights_errors,weights_columns)]
            biases_errors  = [error+column for (error,column) in zip(biases_errors,biases_columns)]
            self.weights=[w-l*e for (w,e) in zip(self.weights,weights_errors)]
            self.weights=[b-l*e for (b,e) in zip(self.biases,biases_errors)]


    def backpropagation(self,x,y):
        """Return tuple of weights_errors and biases in columns."""
        weights_errors = [np.zeros(weight.shape) for weight in self.weights]
        biases_error  = [np.zeros(bias.shape) for bias in self.biases]

        activations=[x]
        weighted=[]
        for (w,b) in zip(self.weights,self.biases):
            z=np.dot(x,w)+b
            weighted.append(z)
            x=sigmoid(z)
            activations.append(x)
        


        return dB,dW

    def opposite_sigmoid(self,x): #overly complicated
        return -np.log(abs((x-1)/x))

    def sigmoid(self,x):
        return 1/(1+np.exp(-x))

    def derivative_sigmoid(self,x):
        a=self.sigmoid(x)
        return a(1-a)

    def cost(self,input,output):
        prediction=self.predict(input)
        l=len(predictions)
        return sum([(output[i]-prediction[i])**2] for i in range(l))

if __name__=="__main__":
    nn=NeuralNetwork()
    print(nn.__dict__)
    print(nn.run(picture))
