from flask import Flask, request, send_file, render_template

app = Flask(__name__)

# Homepage with links to File 1 and File 2
@app.route('/')
def index():
    return render_template('index.html')

# Serve files based on file_id
@app.route('/file/<int:file_id>')
def view_file(file_id):
    file_path = f"files/{file_id}.txt"
    try:
        return send_file(file_path, as_attachment=False)
    except FileNotFoundError:
        return "File not found!", 404

if __name__ == '__main__':
    app.run(debug=True)