(1) save the image in memory

You need to "save" the image, get that bytestream, and encode that to base64. You don't have to save the image to an actual file; you can actually use a buffer.

w = WordCloud().generate('Test')
buffer = io.BytesIO()
w.to_image().save(buffer, 'png')
b64 = base64.b64encode(buffer.getvalue())
And to convert that back and display the image

img = Image.open(io.BytesIO(base64.b64decode(b64)))
plt.imshow(img)
plt.show()



(2) Finally, we use base64encode to transfer the image we saved as in-memory to html.
###############################################
from flask import Flask, render_template
from PIL import Image
import base64
import io

app = Flask(__name__)

@app.route('/')
def hello_world():

    # Full Script.
    im = Image.open("test.jpg")
    data = io.BytesIO()
    im.save(data, "JPEG")
    encoded_img_data = base64.b64encode(data.getvalue())

    return render_template("index.html", img_data=encoded_img_data.decode('utf-8'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')

#############################################    
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test Image</title>
</head>
<body>
    <img id="picture" src="data:image/jpeg;base64,{{ img_data }}">
</body>
</html>
