import os

from flask import Flask, render_template, request, send_from_directory
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

def generate_img(job_id, doc_name, doc_desc, show_desc):
    
    base_image_path = 'static/base.png'
    base_image = Image.open(base_image_path)
    draw = ImageDraw.Draw(base_image)
    
    width, height = base_image.size
    
    font_path = 'static/fonts/AntipastoPro-Bold_trial.ttf'
    custom_font = ImageFont.truetype(font_path, 280)
    
    text_width, text_height = draw.textsize(doc_name, custom_font)
    x = ((width - text_width) // 2)

    if show_desc is True:
        y = ((height - text_height) // 2)+730
        draw.text((x, y), doc_name, font=custom_font, fill=(0, 0, 0))
    elif show_desc is False:
        y = ((height - text_height) // 2)+730
        draw.text((x, y), doc_name, font=custom_font, fill=(0, 0, 0))
        
    job_folder = os.path.join('static', 'jobs')
    output_path = os.path.join(job_folder, f'{job_id}.png')
    base_image.save(output_path)
    
    return job_id

@app.route('/gen', methods=['GET', 'POST'])
def gen():
    try:
        job_id = request.form.get('job_id')
        doc_name = request.form.get('doc_name')
        doc_desc = request.form.get('doc_desc')
        if not job_id or not doc_name:
            raise ValueError("Missing parameters")
        
        show_desc = True
        if doc_desc is None:
            show_desc = False
        else:
            if not doc_desc:
                raise ValueError("Missing parameters")
        
        job_id = generate_img(job_id=job_id, doc_name=doc_name, doc_desc=doc_name, show_desc=show_desc)
        
        return send_from_directory('static', f'jobs/{job_id}.png', as_attachment=False)

    except Exception as e:
        return render_template('error.html', error=str(e))
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8090, debug=True)
    