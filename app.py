from flask import Flask, send_from_directory

app = Flask(__name__)

# Serve the main HTML page
@app.route('/')
def home():
    return send_from_directory('C:/Users/admin/OneDrive/Desktop/Python.class/Father', 'index.html')

# Serve the image
@app.route('/master.jpg')
def image():
    return send_from_directory('C:/Users/admin/OneDrive/Desktop/Python.class/Father', 'master.jpg')

if __name__ == '__main__':
    app.run(debug=True)
