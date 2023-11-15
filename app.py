from flask import Flask
from flask import render_template
from flask import request
from flask import send_from_directory
from PIL import Image, ImageDraw, ImageFont
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/gen', methods=['GET', 'POST'])
def gen():
    try:
        job_id = request.form.get('job_id')
        doc_name = request.form.get('doc_name')
        doc_desc = request.form.get('doc_desc')
        
        if not job_id or not doc_name or not doc_desc:
            raise ValueError("Missing parameters")
        
        base_image_path = 'static/base.png'
        base_image = Image.open(base_image_path)
        draw = ImageDraw.Draw(base_image)
        
        # get center
        width, height = base_image.size
        text = "Hello World"
        font = ImageFont.load_default()
        text_width, text_height = draw.textsize(text, font)
        x = (width - text_width) // 2
        y = (height - text_height) // 2
        
        draw.text((x, y), text, font=font, fill=(0, 0, 0))

        job_folder = os.path.join('static', 'jobs')
        output_path = os.path.join(job_folder, f'{job_id}.png')
        base_image.save(output_path)
        
        return send_from_directory('static', f'jobs/{job_id}.png', as_attachment=False)

    except Exception as e:
        return render_template('error.html', error=str(e))
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8090, debug=True)
    