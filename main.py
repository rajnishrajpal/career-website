from flask import Flask, render_template, jsonify
app = Flask(__name__)

JOBS=[
  {
    "jobid":1,
    "designation": "backend engineer",
    "salary": "Rs 12,00,000",
    "location": "Bangalore"
  },
    {
    "jobid":2,
    "designation": "frontend engineer",
    "salary": "Rs 10,00,000",
    "location": "Delhi"
  },
  {
    "jobid":3,
    "designation": "Data Engineer",
    "salary": "Rs 15,00,000",
    "location": "Remote"
  },
  {
    "jobid":4,
    "designation": "Data Scientist",
    "salary": "Rs 20,00,000",
    "location": "San Francisco"
  }
]

@app.route("/")
def Hello_apex():
  return render_template("home.html", jobs=JOBS)

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)



if __name__ == "__main__":
  app.run(host = "0.0.0.0", debug=True)




