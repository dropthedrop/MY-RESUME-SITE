from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/professional_experience')
def professional_experience():
    return render_template('professional_experience.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/about_me')
def about_me():
    return render_template('about_me.html')

if __name__ == '__main__':
    app.run(debug=True)
