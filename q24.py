import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def get_user_input():
    print("Enter symptom features for the new patient:")
    symptom_features = []
    for i in range(num_features):
        feature = float(input(f"Feature {i + 1}: "))
        symptom_features.append(feature)
    return symptom_features

def main():
    dataset = np.array([
        [1.2, 2.3, 0],
        [2.1, 3.1, 0],
        [0.8, 4.9, 1],
        [3.5, 2.4, 1],
    ])

    X = dataset[:, :-1]
    y = dataset[:, -1]


    global num_features
    num_features = X.shape[1]

    new_patient_features = get_user_input()

    k = int(input("Enter the number of neighbors (k): "))

    knn_classifier = KNeighborsClassifier(n_neighbors=k)
    knn_classifier.fit(X, y)

    prediction = knn_classifier.predict([new_patient_features])

    if prediction[0] == 1:
        print("The patient likely has the medical condition.")
    else:
        print("The patient is unlikely to have the medical condition.")

if __name__ == "__main__":
    main()
