
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
        <label>Rotate by this amount:</label>
        <input type="text" name="amount" value="0">
        <p class="error"></p>
    </div>
    <textarea input type="text" name="text">%(text)s
    </textarea>
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
        response = page_header + form + page_footer
        self.response.write(response)

    def post(self):
        rotate_amount = self.request.get("amount")
        user_text = self.request.get("text")
        if user_text:
            result = encrypt(user_text, int(rotate_amount))

        response = page_header + (form % {"text": result}) + page_footer
        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
