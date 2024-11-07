from flask import Flask, render_template, request
app = Flask(__name__)

# route 1 (page 1) #landing page
@app.route('/')
def home():
    return "Hello World"

if __name__ == "__main__": app.run(debug=True)