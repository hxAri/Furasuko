
from flask import Flask, request, render_template as render
from furasuko import Furasuko

app = Flask( __name__, template_folder="/root/coding/Py/Furasuko/furasuko/template" )

@app.route( "/" )
def index():
	url = request.args.get( "url" )  
	pages = request.args.get( "max" )
	try:
		if url != None:
			if pages == None:
				pages = 5
			crawler = Furasuko( url, pages )
			crawler.crawl_website()
			return render( "index.html", results=crawler.results )
		else:
			return render( "input.html" )
	except Exception as e:
		return type( e ).__name__ + ": " + str( e )

if __name__ == "__main__":
	app.run( debug=True )