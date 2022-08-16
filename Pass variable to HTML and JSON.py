# (1) Json
 cloudHeaders={"Content-Type": "application/json","Connection":"keep-alive","Authorization": "Bearer %s" %servertoken}
    url='https://graph.microsoft.com/v1.0/me/microsoft.graph.sendMail'
    my_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(my_time)
    data = {
        "message": {
        "subject": "Meet for lunch?",
        "body": {
            "contentType": "Text",
            "content": "The new cafeteria is open at {}.".format(my_time)
        },
        "toRecipients": [
            {
                "emailAddress": {
                    "address": "cguo@oplaenergy.com"
                }
            }
        ]
    }
}
    requests.post(url,headers=cloudHeaders,json=data)
    
    
    
# (2) HTML
# message body
message = """
<html>
<body>

<h2>HTML Images</h2>
<p>HTML images are defined with the img tag:</p>

<img src="temp.jpg{}" alt="W3Schools.com" width="1000" height="1000">

</body>
</html>

"""

<2.1>
message=message.format('abcabcabcabcabcabcacbabcabcabcabcabcabcabcacbabc')
print(message)

<2.2>
base64='abcabcabcabcabcabcacbabcabcabcabcabcabcabcacbabc'
message = f"""
<html>
<body>

<h2>HTML Images</h2>
<p>HTML images are defined with the img tag:</p>

<img src="temp.jpg{base64}" alt="W3Schools.com" width="1000" height="1000">

</body>
</html>

"""
print(message)

