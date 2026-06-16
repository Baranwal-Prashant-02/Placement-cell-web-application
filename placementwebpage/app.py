import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

app = Flask(__name__)


# Configure the databases
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
ALLOWED_EXTENSIONS = {'pdf'}
MAX_FILE_SIZE = 5 * 1024 * 1024

app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Directory to save uploaded resumes
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')  # Ensures the directory is correctly set
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

db = SQLAlchemy(app)

# Job model to store job postings
class JobPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    requirements = db.Column(db.Text, nullable=False)
    salary = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<JobPost {self.title}>'

# Registration model to store student registrations
class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    degree = db.Column(db.String(50), nullable=False)
    resume_filename = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Registration {self.name}>'

class JobApplicantDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    job_id = db.Column(db.Integer, db.ForeignKey('job_post.id'))

    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)

    course = db.Column(db.String(50), nullable=False)
    branch = db.Column(db.String(100), nullable=False)

    yop = db.Column(db.Integer, nullable=False)

    organisation_name = db.Column(db.String(200), nullable=False)

    permanent_address = db.Column(db.Text, nullable=False)

    email = db.Column(db.String(120), nullable=False)

    contact = db.Column(db.String(15), nullable=False)

    resume_filename = db.Column(db.String(255), nullable=False)        

# Home page displaying all job postings
@app.route('/')
def index():
    jobs = JobPost.query.all()
    return render_template('index.html', jobs=jobs)

# Page for companies to post job openings
@app.route('/post-job', methods=['GET', 'POST'])
def post_job():
    if request.method == 'POST':
        # Get data from the form
        title = request.form['title']
        company = request.form['company']
        location = request.form['location']
        description = request.form['description']
        requirements = request.form['requirements']
        salary = request.form['salary']

        # Create a new job post and add it to the database
        new_job = JobPost(title=title, company=company, location=location,
                          description=description, requirements=requirements, salary=salary)
        db.session.add(new_job)
        db.session.commit()

        return """
        <script>
            alert("Job Posted Successfully!");
            window.location.href = "/post-job";
        </script>
        """

    return render_template('post_job.html')

@app.route('/registration', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Extract form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        degree = request.form.get('degree')
        resume = request.files.get('resume')
        print(f"Received file: {resume}")

        # Validate required fields
        if not all([name, email, phone, degree, resume]):
            return jsonify({"error": "All fields are required!"}), 400

        # Validate file type
        #if not allowed_file(resume.filename):
        #    return jsonify({"error": "Invalid file type. Only PDF and DOCX are allowed!"}), 400

        # Secure filename and save file
        resume_filename = secure_filename(resume.filename)
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], resume_filename)
        try:
            resume.save(save_path)
        except Exception as e:
            return jsonify({"error": f"File could not be saved: {str(e)}"}), 500

        # Save registration details (mock database logic here)
        try:
            # Simulating database save
            new_registration = Registration(
                name= name,
                email= email,
                phone= phone,
                degree= degree,
                resume_filename= resume_filename,
            )
            db.session.add(new_registration)
            db.session.commit()
            return jsonify({"message": "Registration successful!"}), 200
        except Exception as e:
            return jsonify({"error": f"Database error: {str(e)}"}), 500

    return render_template('registration.html')

@app.route('/students')
def students():
    jobs = JobPost.query.all()
    return render_template('student-resources.html', jobs=jobs)

@app.route('/apply/<int:job_id>', methods=['GET', 'POST'])
def apply(job_id):

    job = JobPost.query.get_or_404(job_id)

    if request.method == 'POST':

        first_name = request.form['first_name']
        last_name = request.form['last_name']
        course = request.form['course']
        branch = request.form['branch']
        yop = request.form['yop']
        organisation_name = request.form['organisation_name']
        permanent_address = request.form['permanent_address']
        email = request.form['email']
        contact = request.form['contact']

        resume = request.files['resume']

        if not resume:
            return "Resume Required"

        if not allowed_file(resume.filename):
            return "Only PDF files allowed"

        filename = secure_filename(resume.filename)

        resume.save(
            os.path.join(
                app.config['UPLOAD_FOLDER'],
                filename
            )
        )

        existing = JobApplicantDetails.query.filter_by(
            email=email,
            job_id=job.id
        ).first()

        if existing:
            return '''
            <script>
            alert("You already applied for this job!");
            window.history.back();
            </script>
            '''

        applicant = JobApplicantDetails(
            job_id=job.id,
            first_name=first_name,
            last_name=last_name,
            course=course,
            branch=branch,
            yop=yop,
            organisation_name=organisation_name,
            permanent_address=permanent_address,
            email=email,
            contact=contact,
            resume_filename=filename
        )

        db.session.add(applicant)
        db.session.commit()

        return '''
        <script>
        alert("Application Submitted Successfully!");
        window.location="/students";
        </script>
        '''

    return render_template(
        'apply_job.html',
        job=job
    )

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/placements')
def placements():
    return render_template('placement.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('login.html')

  

if __name__ == '__main__':
    # Initialize the database
    with app.app_context():
        db.create_all()
    app.run(debug=True)



    
