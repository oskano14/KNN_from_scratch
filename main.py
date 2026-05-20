from knn_models import KNN
from data_loader import load_normalized_data


if __name__ == '__main__':
	X_normalized, Y, standard_scaler_object = load_normalized_data(file_path="bienetre.csv")
	knn_object = KNN()
	best_k, best_score, results = knn_object.grid_search(
		X_normalized[:400],
		Y.iloc[:400],
		X_normalized[400:500],
		Y.iloc[400:500],
		range(1, 12, 2),
	)
	print(f"Meilleur k: {best_k}")
	print(f"Meilleur score: {best_score}")
	print(results)