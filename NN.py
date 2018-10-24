import tensorflow as tf
import pandas as pd

data = pd.read_csv("dataset.csv")


#TODO: READ ACTUAL CSV FILE
n_x = 4 #number of input features per training example
# Currently = MAGNITUDE, DISTANCE, DEPTH
#TODO: SET ACTUAL TRAIN/TEST/DEV SET SIZES #EXPECTED FOR SMALL DATASET 60/20/20
train = data[0:93647]  #80%
dev = data[93648:105353] #10%
test = data[105353:]    #10%


#TODO: NORMALIZE TRAINING AND TEST SET FIRST IF NECESSARY BY SUBTRACTING FROM MEAN AND THEN DIVIDING BY VARIANCE
#TODO: SET TO ACTUAL INDICES
X_train = train['Depth', 'Magnitude', 'Distance']
Y_train = train['Threat Level']

print(X_train.shape)
print(Y_train.shape)

X_dev = dev['Depth', 'Magnitude', 'Distance']
Y_dev = dev['Threat Level']
print(X_dev.shape)
print(Y_dev.shape)
#ASSUMING OUR CLASSIFIER RETURNS A VALUE FROM 0 to 4 -> FIVE DIFFERENT CLASSIFICATIONS
#TODO: SET TO ACTUAL INDICES
X_test = test['Depth', 'Magnitude', 'Distance']
Y_test = test['Threat Level']

print(X_test.shape)
print(Y_test.shape)
#DEFINING DIFFERENT MODELS

model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation=tf.nn.relu),
    tf.keras.layers.Dense(8, activation=tf.nn.relu),
    tf.keras.layers.Dense(5, activation=tf.nn.relu),
    tf.keras.layers.Dense(3, activation=tf.nn.relu),#TODO: ITERATE THROUGH DIFFERENT NUMBER OF LAYERS
    tf.keras.layers.Dense(3, activation=tf.nn.softmax)  # since no of classifications = 3

])
full_deep_model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation= tf.nn.relu),
    tf.keras.layers.Dense(128, activation= tf.nn.relu),
    tf.keras.layers.Dense(128, activation= tf.nn.relu),
    tf.keras.layers.Dense(128, activation= tf.nn.relu),
    tf.keras.layers.Dense(128, activation= tf.nn.relu),
    tf.keras.layers.Dense(128, activation= tf.nn.relu),
    tf.keras.layers.Dense(128, activation= tf.nn.relu),
    tf.keras.layers.Dense(128, activation= tf.nn.relu),
    tf.keras.layers.Dense(128, activation= tf.nn.relu),
    tf.keras.layers.Dense(128, activation= tf.nn.relu),
    tf.keras.layers.Dense(3, activation=tf.nn.softmax)  # since no of classifications = 3

])
#DECIDING LOSS FUNCTIONS AND OPTIMIZATION ALGORITHM

model.compile(optimizer=tf.train.AdamOptimizer(), loss='sparse_categorical_crossentropy', metrics=['accuracy']) #TODO: CHECK IF BETTER LOSS FUNCTION EXISTS

#full_deep_model.compile(optimizer=tf.train.AdamOptimizer(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])


#FITTING ON TRAINING DATA

model.fit(X_train, Y_train, epochs=5) #TODO: TEST DIFFERENT EPOCH CYCLES FOR BETTER ACCURACY

test_loss, test_accuracy = model.evaluate(X_dev, Y_dev)
print("Dev Set Accuracy: " + test_accuracy)

#FINALLY TESTING ON TEST SET

test_loss, test_accuracy = model.evaluate(X_test, Y_test)

print('Test Set Accuracy:    ', test_accuracy)






