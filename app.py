from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample jobs data (no DB needed)
jobs = [
    {"id": 178456, "title": "Python Developer", "description": "Work with clean, simple code in a friendly environment.", 'Salary': 'Rs. 11,00,000', 'location': 'Remote'},
    {"id": 178784, "title": "Backend Developer", "description": "Work with clean, simple code in a friendly environment.", 'Salary': 'Rs. 15,00,000', 'location': 'Jaipur, India'},
    {"id": 244651, "title": "Automation Tester", "description": "A place to learn and grow while testing Python applications.", 'Salary': 'Rs. 13,00,000', 'location': 'Pune, India'},
    {"id": 348514, "title": "Flask API Developer", "description": "Build lightweight APIs with guidance and support.", 'Salary': 'Rs. 16,00,000', 'location': 'Bengaluru, India'},
]

@app.route('/')
def home():
    quote = "Start where you are. Use what you have. Do what you can."
    return render_template('home.html', quote=quote)

@app.route('/jobs')
def jobs_page():
    return render_template('jobs.html', jobs=jobs)

@app.route('/apply/<int:job_id>', methods=['GET', 'POST'])
def apply(job_id):
    job = next((job for job in jobs if job['id'] == job_id), None)
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        why = request.form.get('why')
        print(f"Application Received:\nJob: {job['title']}\nName: {name}\nEmail: {email}\nWhy: {why}\n")
        return redirect(url_for('thank_you'))
    return render_template('apply.html', job=job)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    cover_letter = request.form.get('cover')
    resume = request.files.get('resume')

    # For debugging and capture, print to console
    # print(f"Name: {name}")
    # print(f"Email: {email}")
    # print(f"Cover Letter: {cover_letter}")

    # If you want to save the uploaded resume file
    if resume:
        resume.save(f"uploads/{resume.filename}")
        print(f"Resume saved as: uploads/{resume.filename}")

    # Optionally, redirect to a thank you page
    return f"""
    <h2>Thank you, {name}!</h2>
    <p>We have received your application.</p>
    <a href='/'>Back to Home</a>
    """

@app.route('/about')
def thank_you():
    return render_template('about.html')

if __name__ == '__main__':
     app.run(host="0.0.0.0", port=8080)
