from flask import Flask, request, jsonify, render_template
from agent.travel_agent import create_travel_agent

app = Flask(
    __name__,
    template_folder="web/templates",
    static_folder="web/static"
)

# Initialize agent once
agent = create_travel_agent()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/plan", methods=["POST"])
def plan_trip():
    data = request.json
    query = data.get("query")

    if not query:
        return jsonify({"error": "Query is required"}), 400

    try:
        result = agent.invoke({"input": query})
        return jsonify({"result": result.content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)



