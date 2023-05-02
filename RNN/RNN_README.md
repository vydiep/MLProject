# RNN

## PT-RNN-DataPrep
1. Took first 45 seconds of each song 
2. Broken it up into 15 segments (3 second long clips)
3. Extracted MFCCs from segments for training 
4. Stored data and labels in a JSON file, which are pulled out later 

## PT-RNN-A 
- Model 
    - 1 LSTM Layer 
- Loss: BCEWithLogitsLoss
- Optimizer: Adam 

## PT-RNN-B 
- Model 
    - 1 LSTM Layer 
    - Dropout Layer with 0.2 dropout rate 
- Loss: BCEWithLogitsLoss
- Optimizer: Adam 

## TO-DO
- 2 LSTM layers 
- 2 LSTM layers with Dropout 
- Add JSON file of data to repo 
- Add graph images to repo 
- Clean up notebooks and move some code into .py files