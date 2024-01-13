 - combine data to get 3 things:
	- rotational data
		- determine where down is (using the gravity + rotation to shift coordinate system into x,y,z relative to earth)
		- calibrate rotation with that
	- get acceleration without gravity (accelerometer - gravity)
	- timestamps annotated with lift or piste, to get initial data


 - create ai training data:
	- combine the rotation + accel + gps to get training input data
	- try out different model types to predict skiing
	- try out different time intervals

 - create a visualisation
	- use the skiing data to annotate gps data with color

improve the model:
 - augment training data (not too helpful +/-0.01)
 - use more data from the available sources 
 - change model architecture
	- try to use classification model (https://keras.io/examples/timeseries/timeseries_classification_from_scratch/)
 - generate datasets with different context sizes
 - try hyperparameter tuning (https://keras.io/guides/keras_tuner/getting_started/)