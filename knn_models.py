class KNN:
    def __init__(self, k=5):
        self.k = k  # nombre de voisins
        self.X_train = None  # données d'entraînement
        self.y_train = None  # labels d'entraînement

    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train
        return self

    def predict(self, X_test):
        # 1. Calculer la distance à chaque point d'entraînement
        predictions = []
        for x_test_point in X_test:
            distances_point = []
            for x_train_point in self.X_train:
                distance = sum((point1 - point2) ** 2 for point1, point2 in zip(x_test_point, x_train_point)) ** 0.5
                distances_point.append(distance)
            # 2. Trouver les indices des k plus proches voisins
            k_indices = sorted(range(len(distances_point)), key=lambda index: distances_point[index])[:self.k]
            # 3. Récupérer les labels des k plus proches voisins
            k_labels = [self.y_train[index] for index in k_indices]
            # 4. Prendre la majorité des labels
            label_counts = {}
            for label in k_labels:
                label_counts[label] = label_counts.get(label, 0) + 1
            majority_label = max(label_counts, key=label_counts.get)
            predictions.append(majority_label)
        return predictions
        

    

    def evaluate(self, X_test, y_test):
        predicted_labels = self.predict(X_test)
        correct_predictions = sum(
            predicted_label == true_label
            for predicted_label, true_label in zip(predicted_labels, y_test)
        )
        return correct_predictions / len(y_test)
        

    def grid_search(self, X_train, y_train, X_val, y_val, k_values):
        best_k = None
        best_score = -1
        Results
        for k in k_values:
            self.k = k
            self.fit(X_train, y_train)
            score = self.evaluate(X_val, y_val)
            results[k] = score
            if score > best_score:
                best_score = score
                best_k = k
        self.k = best_k  # Mettre à jour le modèle avec le meilleur k trouvé
        return best_k, best_score, results
