import sys
from flask import Flask , render_template, request
from pytrends.request import TrendReq



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
def logger_page():
    page = """
    <script>
    console.log('This is a front-end log');
    </script>
    
    <script>
    alert('Message in a text box');
    </script>
    """

    print('This is a back-end log')
    app.logger.error("An error message")
    app.logger.critical("A critical message")
    print('This is error output', file=sys.stderr)
    return page + "This page logs stuff"

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text

@app.route('/cookie', methods=["GET","POST"])
def mycookies():
    req = request.get("https://www.google.com/")
    return req.cookies.get_dict() 

@app.route('/cookieganalytics', methods=["GET","POST"])
def mycookieganalytics():
    req = request.get("https://analytics.google.com/analytics/web/#/report-home/a250385898w345179770p281245720")
    return req.text

pytrends = TrendReq(hl='en-US', tz=360)
# build list of keywords
kw_list = ["earth", "energy", "space"]
# build the payload
pytrends.build_payload(kw_list, timeframe='2016-01-01 2016-03-31', geo='US')
# store interest over time information in df
df = pytrends.interest_over_time()
print (df)
@app.route('/googletrend')
def googletrend():
    line_labels = df.index
    line_values = df['earth']
    return render_template('chart.html', title='Earth through time', labels=line_labels, values=line_values)

