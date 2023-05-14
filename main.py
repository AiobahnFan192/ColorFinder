from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def get_color():
    x = request.form['x']
    y = request.form['y']
    color = get_pixel_color(x, y)  # Replace with your own function to get pixel color
    html_code = rgb_to_html(color)  # Replace with your own function to convert RGB to HTML code
    return html_code

if __name__ == '__main__':
    app.run()
