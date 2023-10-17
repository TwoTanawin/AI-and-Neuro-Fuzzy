import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# Define the dataset
X = torch.tensor([
    [0, 0, 0],
    [0, 0, 1],
    [0, 1, 0],
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 1]
], dtype=torch.float32)

# Define the associated values (target labels)
y = torch.tensor([1, 0, 0, 1, 0, 1, 1, 0], dtype=torch.float32).view(-1, 1)

# Define the neural network model
class MLP(nn.Module):
    def __init__(self):
        super(MLP, self).__init__()
        self.fc1 = nn.Linear(3, 4)  # Input layer with 3 features and 4 hidden units
        self.fc2 = nn.Linear(4, 1)  # Output layer with 1 output neuron

    def forward(self, x):
        x = torch.sigmoid(self.fc1(x))
        x = torch.sigmoid(self.fc2(x))
        return x

# Create an instance of the MLP
mlp = MLP()

# Define the loss function and optimizer
criterion = nn.BCELoss()  # Binary Cross-Entropy Loss
optimizer = optim.SGD(mlp.parameters(), lr=0.1)

# Training loop
for epoch in range(10000):
    # Forward pass
    outputs = mlp(X)
    
    # Compute the loss
    loss = criterion(outputs, y)
    
    # Backpropagation and optimization
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# Print the trained weights and biases
for name, param in mlp.named_parameters():
    if 'weight' in name:
        print(f'{name}: {param}')
    elif 'bias' in name:
        print(f'{name}: {param}')
