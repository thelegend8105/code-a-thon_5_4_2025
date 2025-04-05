from flask import Flask, render_template
import matplotlib as plt
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Make sure the static folder exists
    os.makedirs('static', exist_ok=True)

    # Generate a graph
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 1, 8, 7]

    plt.figure()
    plt.plot(x, y, marker='o')
    plt.title('Sample Graph')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.grid(True)

    # Save it to static folder
    plt.savefig('static/graph.png')
    plt.close()

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
