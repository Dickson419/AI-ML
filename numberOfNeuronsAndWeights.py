"""Program to calculate CNN number of neurons, weights and output volume"""
def calculate_neurons_and_weights(input_dim, num_filters, filter_dim):
    # Calculate number of neurons
    neurons_width = (input_dim[0] - filter_dim[0] + 2 * 0) // 1 + 1
    neurons_height = (input_dim[1] - filter_dim[1] + 2 * 0) // 1 + 1
    neurons_channels = num_filters
    num_neurons = neurons_width * neurons_height * neurons_channels

    # Calculate total number of weights
    total_weights_per_filter = filter_dim[0] * filter_dim[1] * filter_dim[2] + 1
    total_weights = num_filters * total_weights_per_filter

    return num_neurons, total_weights

def calculate_output_dimensions(input_dims, filter_dims, num_filters, stride=1, padding=0):
    output_width = ((input_dims[0] - filter_dims[0] + 2 * padding) // stride) + 1
    output_height = ((input_dims[1] - filter_dims[1] + 2 * padding) // stride) + 1
    output_channels = num_filters
    return output_width, output_height, output_channels

# Given values - CHANGE THESES!
input_dimension = (9, 9, 3)
num_filters = 10
filter_dimension = (4, 4, 3)

# Calculate neurons and weights
num_neurons, total_weights = calculate_neurons_and_weights(input_dimension, num_filters, filter_dimension)

#calculate output volume
output_dimensions = calculate_output_dimensions(input_dimension, filter_dimension, num_filters)

# Print the results
print("Number of Neurons:", num_neurons)
print("Total Number of Weights:", total_weights)
print("Output volume: ", output_dimensions)












