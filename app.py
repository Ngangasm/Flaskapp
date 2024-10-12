from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('bmi_form.html')

@app.route('/calculate_bmi', methods=['POST'])
def calculate_bmi():
    try:
        height = float(request.form['height']) / 100  # Convert cm to meters
        weight = float(request.form['weight'])
        bmi = weight / (height ** 2)
        return render_template('bmi_result.html', bmi=bmi)
    except ValueError:
        return "Invalid input. Please enter valid numbers for height and weight."

if __name__ == '__main__':
    app.run(debug=True)