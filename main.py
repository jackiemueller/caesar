
import webapp2
from caesar import encrypt

page_header = """
<!DOCTYPE html>
<html>
<head>
    <style>
        form {
            background-color: #eee;
            padding: 20px;
            margin: 0 auto;
            width: 540px;
            font: 16px sans-serif;
            border-radius: 10px;
        }
        textarea {
            margin: 10px 0;
            width: 540px;
            height: 120px;
        }
        p.error {
            color: red;
        }
    </style>
</head>
<body>
"""

form = """
<form action="/" method="post">
    <div>
        <label for="rot">Rotate by this amount:</label>
        <input type="text" name="rot" value="0">
        <p class="error"></p>
    </div>
    <textarea type="text" name="text"></textarea>
    <br>
    <input type="submit" value="Encrypt it!"/>
</form>
"""

page_footer = """
</body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(page_header + form + page_footer)

    def post(self):
        answer = self.request.get("answer")
        answer = encrypt()
        print(answer)
        self.response.write(page_header + form + page_footer)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
