from flask import Flask, request, jsonify
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# Load the Iris dataset and train the model
iris = load_iris()
X, y = iris.data, iris.target

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# Create Flask application
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Iris prediction API is running"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if not data or "input" not in data:
        return jsonify({"error": "Send JSON with an 'input' field"}), 400

    values = data["input"]

    if not isinstance(values, list) or len(values) != 4:
        return jsonify({
            "error": "Input must contain 4 values: sepal length, sepal width, petal length, petal width"
        }), 400

    try:
        values = [float(value) for value in values]
        prediction = model.predict([values])[0]
        return jsonify({"prediction": iris.target_names[prediction]})
    except (TypeError, ValueError):
        return jsonify({"error": "All input values must be numbers"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
