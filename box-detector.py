from keras.models import Sequential
from keras.layers import Dense, Activation, Input

def buildModel() {
    model = Sequential([
        # Input Layer
        Input(shape=(270, 180, 3), name="image"),

        # Layer 1
        Convolution2D(8, 3, 3),
        Activation('relu'),
        MaxPooling2D(pool_size=(2,2)),

        # Layer 2
        Convolution2D(16, 3, 3),
        Activation('relu'),
        MaxPooling2D(pool_size=(2,2)),

        # Flatten
        Flatten(),

        # Layer 3
        Dense(32),
        Activation('linear'),
        Dropout(.4),

        # Output Layer
        Dense(4, name="output")
    ])

    model.compile(optimizer='adam',
                loss='mean_squared_error',
                metrics=['accuracy'])

    return model
}

def trainModel(model, images, labels) {
    model.fit(images, labels, epochs=30, batch_size=2, verbose=2, callbacks=None, validation_split=0.2, shuffle=True, initial_epoch=0)
    model.save("box-detector.h5")
    return model
}