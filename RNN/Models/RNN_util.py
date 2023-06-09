import json
import numpy as np
from sklearn.model_selection import train_test_split
import time
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader, TensorDataset

def load_data(data_path):
    """
    Load data from JSON file and return features and labels 

    Parameters:
    - data_path: path to JSON file (string) 

    Return: 
    - X: features from data (numpy array)
    - y: labels for data (numpy array)

    Resource: 
        https://github.com/musikalkemist/DeepLearningForAudioWithPython/blob/master/19-%20How%20to%20implement%20an%20RNN-LSTM%20for%20music%20genre%20classification/code/19-%20How%20to%20implement%20an%20RNN-LSTM%20for%20music%20genre%20classification.py
    """

    # open file for reading 
    with open(data_path, "r") as fp:
        data = json.load(fp)

    # store features and labels as np arrays
    X = np.array(data["mfcc"])
    y = np.array(data["labels"])
    
    return X, y


def prepare_datasets(data_path, test_size, validation_size):
    """
    Loads data and splits it into train, validation and test sets.

    Parameters: 
    - test_size: percentage of data set to allocate for testing (float)
    - validation_size: percentages of training set to allocate for validation (float)

    Return: 
    - X_train: training set (numpy array)
    - X_validation: training validation set (numpy array)
    - X_test: testing set (numpy array)
    - y_train: labels for training set (numpy array)
    - y_validation: labels for training validation set (numpy array)
    - y_test: labels for testing set (numpy array)

    Resource:
        https://github.com/musikalkemist/DeepLearningForAudioWithPython/blob/master/19-%20How%20to%20implement%20an%20RNN-LSTM%20for%20music%20genre%20classification/code/19-%20How%20to%20implement%20an%20RNN-LSTM%20for%20music%20genre%20classification.py
    """
    # load data
    X, y = load_data(data_path)

    # create train, validation and test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)
    X_train, X_validation, y_train, y_validation = train_test_split(X_train, y_train, test_size=validation_size)

    return X_train, X_validation, X_test, y_train, y_validation, y_test


def get_data_loaders(data_path):
    """
    Create and return PyTorch DataLoader objects for the training, validation, and test data

    Parameters: 
    - data_path: Path to JSON file with data (string)

    Return: 
    - train_loader: training data (DataLoader)
    - val_loader: val data (DataLoader)
    - test_loader: test data (DataLoader)
    """
    batch_size = 32

    # get train, validation, test splits
    X_train, X_validation, X_test, y_train, y_validation, y_test = prepare_datasets(data_path, 0.2, 0.2)

    train_features = torch.Tensor(X_train)
    train_targets = torch.Tensor(y_train)
    val_features = torch.Tensor(X_validation)
    val_targets = torch.Tensor(y_validation)
    test_features = torch.Tensor(X_test)
    test_targets = torch.Tensor(y_test)

    train_dataset = TensorDataset(train_features, train_targets)
    val_dataset = TensorDataset(val_features, val_targets)
    test_dataset = TensorDataset(test_features, test_targets)

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=False, drop_last=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False, drop_last=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False, drop_last=True)

    return train_loader, val_loader, test_loader


def train(model, train_loader, val_loader, k_epochs, device):
    """
    Time and train model for k_epochs using the train_loader while regulating performance 
    using the val_loader 

    Parameters: 
    - model: model to train with 
    - train_loader: data to train on (DataLoader)
    - val_loader: data to validate and regulate performance (DataLoader)
    - k_epochs: number of epochs to run training on (int)
    - device: device to move to 

    Guidance from CS451 lecture notes
    """

    begin = time.time()

    loss_fn = nn.BCEWithLogitsLoss() # Loss function for binary classification
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # Printing purposes
    last_epoch = len(model.training_info['train_losses'])

    for epoch in range(k_epochs):

        # Training
        model.train() #Set model to training mode
        train_loss = 0
        correct = 0
        total = 0

        for i, data in enumerate(train_loader, 0):
            X, y = data
            X = X.to(device)
            y = y.to(device)

            optimizer.zero_grad()
            
            output = model(X)

            # Training Loss
            loss = loss_fn(output.squeeze(), y)
            loss.backward()
            optimizer.step()
            train_loss += loss.item()
            
            # Training Accuracy 
            predicted = (output.sigmoid() >= 0.5).float()
            predicted = predicted.view(-1) # modify dimensions
            total += y.size(0)
            correct += (predicted == y.float()).sum().item()

        # Calculate training loss and accuracy 
        train_loss /= len(train_loader)
        train_accuracy = 100. * (correct / total)

        # Add training loss and accuracy to model's history 
        model.training_info['train_losses'].append(train_loss)
        model.training_info['train_accuracies'].append(train_accuracy)


        # Validation
        model.eval() # Set model to evaluation mode
        val_loss = 0
        correct = 0
        total = 0

        # Do not store computational graph since we are simulating testing 
        with torch.no_grad():
            for i, data in enumerate(val_loader, 0):
                X, y = data
                X = X.to(device)
                y = y.to(device)

                output = model(X)

                # Validation Loss
                loss = loss_fn(output.squeeze(), y)
                val_loss += loss.item()

                # Validation Accuracy 
                predicted = (output.sigmoid() >= 0.5).float()
                predicted = predicted.view(-1) # modify dimensions
                total += y.size(0)
                correct += (predicted == y.float()).sum().item()

            # Calculate validation loss and accuracy
            val_loss /= len(val_loader)
            val_accuracy = 100. * (correct / total)

            # Add validation loss and accuracy to model's history 
            model.training_info['val_losses'].append(val_loss)
            model.training_info['val_accuracies'].append(val_accuracy)

        print(f'Epoch {last_epoch+epoch+1}:') 
        print(f'\tTrain Loss={train_loss:.4f} Train Accuracy={train_accuracy:.2f}%')
        print(f'\tVal Loss  ={val_loss:.4f} Val Accuracy  ={val_accuracy:.2f}%')

    end = time.time()
    print(f'Finished training in {round(end - begin)}s')


def test(model, test_loader, device):
    """
    Test performance of model based on test_loader 

    Parameters: 
    - model: model to test 
    - test_loader: test data to assess performance (DataLoader)
    - device: device to move to 

    Guidance from CS451 lecture notes
    """
    correct = 0
    total = 0
    
    # Do no store computational graph since we are testing 
    with torch.no_grad():
        for data in test_loader:
            X, y = data
            X = X.to(device)
            y = y.to(device)
            
            y_hat = model(X)

            predicted = (y_hat.sigmoid() >= 0.5).float()
            predicted = predicted.view(-1) # modify dimensions

            # compute the accuracy
            total += y.size(0)
            correct += (predicted == y).sum().item()

    print(f'Test accuracy: {100 * correct // total} %')


def plot_history(title, model, graph_path):
    """
    Plot the models history of training/validation accuracies and 
    training/validation losses on separate graphs based on what is 
    stored in its training info. Save the created graphs at graph_path. 

    Parameters: 
    - title: title to give graph (string)
    - model: model whose history to inspect
    - graph_path: path for storing images of graphs (string)
    """

    fig, axs = plt.subplots(2)

    fig.suptitle(title, fontweight='heavy')

    # create accuracy sublpot
    axs[0].plot(model.training_info["train_accuracies"], label="train accuracy")
    axs[0].plot(model.training_info["val_accuracies"], label="val accuracy")
    axs[0].set_ylabel("Accuracy")
    axs[0].set_xlabel("Epoch")
    axs[0].legend(loc="lower right")
    axs[0].set_title("Accuracy eval")

    # create error sublpot
    axs[1].plot(model.training_info["train_losses"], label="train error")
    axs[1].plot(model.training_info["val_losses"], label="val error")
    axs[1].set_ylabel("Error")
    axs[1].set_xlabel("Epoch")
    axs[1].legend(loc="upper right")
    axs[1].set_title("Error eval")

    fig.tight_layout()

    plt.savefig(graph_path)
    plt.show()
