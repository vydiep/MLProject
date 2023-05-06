# RNN Notes

## PT-RNN-DataPrep
1. Took first 45 seconds of each song 
2. Broken it up into 15 segments (3 second long clips)
3. Extracted MFCCs from segments for training 
4. Stored data and labels in a JSON file, which are pulled out later 

## Models 
- Loss: BCEWithLogitsLoss
- Optimizer: Adam 

### 1 LSTM Layer 
- Testing Accuracy: 74%
### 2 LSTM Layers 
- Testing Accuracy: 78% 
### 1 LSTM Layer with Dropout 
- Testing Accuracy: 76%
### 2 LSTMs Layer with Dropout 
- Testing Accuracy: 76% 