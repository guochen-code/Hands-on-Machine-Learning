For simplicity's sake, let's consider writing instead of reading for now.

So when you use open() like say:

with open("test.dat", "wb") as f:
    f.write(b"Hello World")
    f.write(b"Hello World")
    f.write(b"Hello World")
After executing that a file called test.dat will be created, containing 3x Hello World. 
The data wont be kept in memory after it's written to the file (unless being kept by a name).

Now when you consider io.BytesIO() instead:

with io.BytesIO() as f:
    f.write(b"Hello World")
    f.write(b"Hello World")
    f.write(b"Hello World")
Which instead of writing the contents to a file, it's written to an in memory buffer. In other words a chunk of RAM. 
Essentially writing the following would be the equivalent:

buffer = b""
buffer += b"Hello World"
buffer += b"Hello World"
buffer += b"Hello World"
In relation to the example with the with statement, then at the end there would also be a del buffer.

The key difference here is optimization and performance. 
io.BytesIO is able to do some optimizations that makes it faster than simply concatenating all the b"Hello World" one by one.

Just to prove it here's a small benchmark:

Concat: 1.3529 seconds
BytesIO: 0.0090 seconds
import io
import time

begin = time.time()
buffer = b""
for i in range(0, 50000):
    buffer += b"Hello World"
end = time.time()
seconds = end - begin
print("Concat:", seconds)

begin = time.time()
buffer = io.BytesIO()
for i in range(0, 50000):
    buffer.write(b"Hello World")
end = time.time()
seconds = end - begin
print("BytesIO:", seconds)
Besides the performance gain, using BytesIO instead of concatenating has the advantage that BytesIO can be used in place of a file object. 
So say you have a function that expects a file object to write to. Then you can give it that in-memory buffer instead of a file.

The difference is that open("myfile.jpg", "rb") simply loads and returns the contents of myfile.jpg; whereas, BytesIO again is just a buffer containing some data.

Since BytesIO is just a buffer - if you wanted to write the contents to a file later - you'd have to do:

buffer = io.BytesIO()
# ...
with open("test.dat", "wb") as f:
    f.write(buffer.getvalue())
Also, you didn't mention a version; I'm using Python 3. Related to the examples: I'm using the with statement instead of calling f.close()
  
*********************************************************************************************************************************************************************
*********************************************************************************************************************************************************************
*********************************************************************************************************************************************************************

matplotlib image to base64 without saving

No. You need to "save" the image, get that bytestream, and encode that to base64. 
You don't have to save the image to an actual file; you can actually use a buffer.

w = WordCloud().generate('Test')
buffer = io.BytesIO()
w.to_image().save(buffer, 'png')
b64 = base64.b64encode(buffer.getvalue())
And to convert that back and display the image

img = Image.open(io.BytesIO(base64.b64decode(b64)))
plt.imshow(img)
plt.show()
