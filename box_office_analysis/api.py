from flask import Flask, jsonify,request
from analysis import DataLoader, DataAnalyzer


app = Flask(__name__)
loader = DataLoader("data/enhanced_box_office_data(2000-2024)u.csv")
data = loader.load_data()
analyzer = DataAnalyzer(data)

@app.route("/api/statistics", methods=["GET"])
def statistics():
    return jsonify(analyzer.get_statistics())

@app.route("/api/record/<int:id_>", methods=["GET"])
def record(id_):
    return jsonify(analyzer.get_record_by_id(id_))

@app.route("/api/data", methods=["GET"])
def data():
    year_min = request.args.get('year_min', type=int)
    year_max = request.args.get('year_max', type=int)
    genre = request.args.get('genre', type=str)
    min_rating = request.args.get('min_rating', type=float)
    max_rating = request.args.get('max_rating', type=float)

    result = analyzer.get_data(
        year_min=year_min,
        year_max=year_max,
        genre=genre,
        min_rating=min_rating,
        max_rating=max_rating
    )
    return jsonify(result)

@app.route('/api/categories', methods=["GET"])
def category():
    return jsonify(analyzer.get_all_category())

if __name__ == "__main__":
    app.run(debug=True, port=5000)