import numpy as np
import pandas as pd
import tensorflow as tf
import keras

def reshape_for_conv(arr, channels, length):
	print("Reshaping input for convolution...")
	# Reshape the input data to (1, 100, 6)
	new_X = np.zeros([1, length, channels])

	for x in np.array(arr):
		t = np.array(np.split(np.array(x), channels)) # (6, 100)
		t = t.transpose() # (100, 6)
		t = t.reshape((1, length, channels))
		new_X = np.append(new_X, t, axis=0)

	new_X = new_X[1:]
	return new_X

def get_data(data_type, datapoints, extra=""):
	print("Loading training data (type=", data_type, "datapoints=", datapoints, ")...")
	file_str = "./data/" + data_type + "/" + data_type + "_" + str(datapoints) + ".csv"

	if extra != "":
		file_str = "./data/" + data_type + "/" + data_type + "_" + extra + "_" + str(datapoints) + ".csv"
	
	df = pd.read_csv(file_str)
	X = df.iloc[:, 0:-3]
	y = df.iloc[:, -1]

	return (df, X, y)

def get_data_conv(data_type, datapoints, channels, extra=""):
	(df, X, y) = get_data(data_type=data_type, datapoints=datapoints, extra=extra)
	X = reshape_for_conv(X, channels, datapoints)
	return (df, X, y)

def create_conv_model(channels, length):
	input_shape = (length, channels)
	num_classes = 1

	input_layer = keras.layers.Input(input_shape)

	conv1 = keras.layers.Conv1D(filters=64, kernel_size=6, padding="same")(input_layer)
	conv1 = keras.layers.BatchNormalization()(conv1)
	conv1 = keras.layers.ReLU()(conv1)

	conv2 = keras.layers.Conv1D(filters=64, kernel_size=6, padding="same")(conv1)
	conv2 = keras.layers.BatchNormalization()(conv2)
	conv2 = keras.layers.ReLU()(conv2)

	conv3 = keras.layers.Conv1D(filters=64, kernel_size=6, padding="same")(conv2)
	conv3 = keras.layers.BatchNormalization()(conv3)
	conv3 = keras.layers.ReLU()(conv3)

	gap = keras.layers.GlobalAveragePooling1D()(conv3)

	output_layer = keras.layers.Dense(num_classes, activation="sigmoid")(gap)

	model = keras.models.Model(inputs=input_layer, outputs=output_layer)

	model.compile(
		optimizer="adam",
		loss="binary_crossentropy",
		metrics=["accuracy"],
	)

	return model

def create_simple_model(channels, length):
	num_classes = 1
 
	model = tf.keras.models.Sequential([
		tf.keras.layers.Dense(256, activation='relu', input_dim=channels*length),
		tf.keras.layers.Dense(128, activation='relu'),
		tf.keras.layers.Dense(64, activation='relu'),
		tf.keras.layers.Dense(num_classes, activation='sigmoid')
	])
	
	model.compile(loss=tf.keras.losses.BinaryCrossentropy(),
		optimizer=tf.keras.optimizers.Adam(), # use Adam instead of SGD
		metrics=['accuracy']
	)

	return model