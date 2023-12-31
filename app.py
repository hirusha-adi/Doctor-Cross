import os
from flask import Flask, render_template, request
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)
app_name = "Doctor Cross" 

job_folder = os.path.join('static', 'jobs')

def init():
    os.makedirs(job_folder, exist_ok=True)


def generate_img(job_id, doc_name, doc_desc, show_desc, transparency):

    if transparency:
        base_image_path = 'static/base-transparent.png'
    else:
        base_image_path = 'static/base.png'
        
    base_image = Image.open(base_image_path)
    draw = ImageDraw.Draw(base_image)
    width, height = base_image.size
    
    font_bold_path = 'static/fonts/AntipastoPro-Bold_trial.ttf'
    font_med_path = 'static/fonts/AntipastoPro-Medium_trial.ttf'

    if show_desc is True:
        font_bold = ImageFont.truetype(font_bold_path, 290)
        text_width, text_height = draw.textsize(doc_name, font_bold)
        x = ((width - text_width) // 2)
        y = ((height - text_height) // 2)+730
        draw.text((x, y), doc_name, font=font_bold, fill=(0, 0, 0))
        
        font_med = ImageFont.truetype(font_med_path, 200)
        text_width, text_height = draw.textsize(doc_desc, font_med)
        x = ((width - text_width) // 2)
        y = ((height - text_height) // 2)+1025
        draw.text((x, y), doc_desc, font=font_med, fill=(0, 0, 0))
        
    elif show_desc is False:
        font_bold = ImageFont.truetype(font_bold_path, 320)
        text_width, text_height = draw.textsize(doc_name, font_bold)
        x = ((width - text_width) // 2)
        y = ((height - text_height) // 2)+750
        draw.text((x, y), doc_name, font=font_bold, fill=(0, 0, 0))
        
    output_path = os.path.join(job_folder, f'{job_id}.png')
    base_image.save(output_path)
    
    return job_id


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', app_name=app_name)


@app.route('/gen', methods=['GET', 'POST'])
def gen():
    try:
        job_id = request.form.get('job_id')
        doc_name = request.form.get('doc_name')
        doc_desc = request.form.get('doc_desc')
        enable_transparency = request.form.get('enable_transparency')
        is_trans = enable_transparency is not None
        
        if not job_id or not doc_name:
            raise ValueError("Missing parameters")
        
        show_desc = True
        if (doc_desc is None) or (doc_desc == ""):
            show_desc = False
        else:
            if not doc_desc:
                raise ValueError("Missing parameters")
        
        job_id = generate_img(job_id=job_id, doc_name=doc_name, doc_desc=doc_desc, show_desc=show_desc, transparency=is_trans)
        
        return render_template('image.html', job_id=job_id, app_name=app_name)

    except Exception as e:
        return render_template('error.html', app_name=app_name, error=str(e), show_desc=show_desc)

if __name__ == "__main__":
    init()
    app.run(host='0.0.0.0', port=8090, debug=False)
    