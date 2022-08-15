(1) save the image in memory

<1.1> save in disk
import matplotlib.pyplot as plt
from PIL import Image
import base64
import io

# save a plot as a jpg
plt.plot([1,2,3],[1,2,3])
plt.savefig('temp.jpg')

# encode the saved image
im = Image.open("temp.jpg")
data = io.BytesIO()
im.save(data, "JPEG")
encoded_img_data = base64.b64encode(data.getvalue())


img_link="data:image/gif;base64,"+str(encoded_img_data)[2:-1]

# start to write HTML
f = open('image passing to html.html','w')

message = """
<html>
<body>
<h2>HTML Images</h2>
<p>HTML images are defined with the img tag:</p>
<img src={img_link:} alt="Base64 encoded image" width="150" height="150"/>
</body>
</html>
"""
f.write(message)
f.close()

# rewrite HTML
f = open('image passing to html.html').read().format(img_link_2=img_link_2)
f_old = open('image passing to html.html','w')
f_old.write(f)

# view HTML
import codecs
file = codecs.open("image passing to html.html", 'r', "utf-8")
print(file.read())

# view in browser
import webbrowser
webbrowser.open('image passing to html.html') 

<1.2> save in buffer
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
#############################################################################################################################################
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

###########################################################################################################################################
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

###########################################################################################################################################
###########################################################################################################################################
###########################################################################################################################################
# decode base64 image to normal image
import io
import base64

img_data= base64.b64decode(encoded_img_data.decode("utf-8"))
Image.open(io.BytesIO(img_data)) # open to display # Image.open("temp_10.jpg")


import base64
imgdata = base64.b64decode(imgstring)
filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
with open(filename, 'wb') as f:
    f.write(imgdata) # save as a jpg file
