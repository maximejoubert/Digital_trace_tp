from flask import Flask , render_template, request

# https://lfco2p.deta.dev

app = Flask(__name__)
@app.route('/', methods=["GET"])
def hello_world():
    prefix_google = """
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-250385898-2"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-250385898-2');
</script>
"""
    return prefix_google + render_template('first.html')+"Hello World"

@app.route('/logger',methods=["GET"])
def log():
    
    return render_template("log.html") + "test"

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text