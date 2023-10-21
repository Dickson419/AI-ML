import numpy as np

def k_means_step(data, cluster_centers):
    # Assign each point to the nearest cluster
    assigned_clusters = np.argmin(np.linalg.norm(data - cluster_centers[:, np.newaxis], axis=2), axis=0)

    # Update cluster centers
    new_cluster_centers = np.array([np.mean(data[assigned_clusters == k], axis=0) for k in range(len(cluster_centers))])

    return new_cluster_centers

# Example usage:
if __name__ == "__main__":
    # Initial cluster centers
    initial_centers = np.array([[2, 1], [3, 3]]) #UPDATE with cluster centres

    # Data points --> UPDATE this with all x and y co-ords
    data = np.array([
        [3, 1],
        [4, 3],
        [4, 4],
        [5, 3],
        [5, 4],
    ])

    # Perform one step of k-means
    new_centers = k_means_step(data, initial_centers)

    print("Initial Cluster Centers:")
    print(initial_centers)

    print("\nData Points:")
    print(data)

    print("\nUpdated Cluster Centers (top C1, bottom C2:")
    print(new_centers)
