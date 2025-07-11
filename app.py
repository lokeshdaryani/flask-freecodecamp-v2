from flask import Flask, render_template, jsonify

app = Flask(__name__)

Jobs = [{
    'JOb_id': 1,
    'Job_title': 'Data Analyst',
    'Job_location': 'Bengaluru, India',
    'Salary': 'Rs. 10,00,000'
}, {
    'JOb_id': 2,
    'Job_title': 'Data Scientist',
    'Job_location': 'Delhi, India',
    'Salary': 'Rs.15,00,000'
}, {
    'JOb_id': 3,
    'Job_title': 'Frontend Engineer',
    'Job_location': 'Remote',
    'Salary': 'Rs.12,00,000'
}, {
    'JOb_id': 4,
    'Job_title': 'Backend Engineer',
    'Job_location': 'San Francisco, USA',
    'Salary': '$120,000'
}]


@app.route("/")
def index():
    return render_template('home.html', jobs=Jobs, company_name='Jovian')


@app.route("/api/jobs")
def list_jobs():
    return jsonify(Jobs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
