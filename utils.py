import numpy as np
import pandas as pd

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

def get_data(data_type, datapoints):
	print("Loading training data (type=", data_type, "datapoints=", datapoints, ")...")
	df = pd.read_csv("./data/" + data_type + "/" + data_type + "_" + str(datapoints) + ".csv")
	X = df.iloc[:, 0:-3]
	y = df.iloc[:, -1]

	return (df, X, y)

def get_data_conv(data_type, datapoints, channels):
	(df, X, y) = get_data()
	X = reshape_for_conv(X, channels, datapoints)
	return (df, X, y)