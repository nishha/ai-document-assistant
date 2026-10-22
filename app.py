from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify({"status": "healthy"}), 200




@app.post("/ask") #endpoint created
def ask():
    data = request.get_json(silent=True) or {} #reads the json data sent to your app
    question = data.get("question", "").strip()

    if not question:
        return jsonify({"error": "Please provide a question"}), 400

    return jsonify({
        "question": question,
        "answer": "Your question was received successfully!"
    }), 200



if __name__ == "__main__":
    app.run(debug=True)