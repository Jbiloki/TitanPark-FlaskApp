## TitanPark

Using a web interface trained on years of past sensor data at the CSUF parking structures an algorithm was trained to predict future parking habits.

Titan park was create to support students to find better parking as well as a project to practice machine learning techniques on real world data and problems.

The current MSE for the eastside structure is ~27 spots. This error can be reduced as I continue my work over time.

# Current algorithms implemented:

# Gradient Boosting

This dataset is connected and can be used, on the server I have implemented an GBR with Sklearn.

Pre-processing: The data directly from the repository has error values, to compensate for this the values were removed before training. After testing I have finalized my preprocessing using faeture engineering to use timeseries as the main feature affecting the data, thoughout time latent features such as weather are planned to be implemented.

Training is done on this data using 33% as validation/testing data.

Next Steps:

The implementation of all parking structures and latent vairables to improve predicitons as well as testing with deep learning and other machine learning models.
