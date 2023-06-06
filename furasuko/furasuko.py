
from bs4 import BeautifulSoup
import requests

class Furasuko:
	
	def __init__( self, url, max_pages ):
		self.url = url
		self.max_pages = max_pages
		self.results = []
	
	def crawl_website( self ):
		response = requests.get( self.url )
		content = response.content
		soup = BeautifulSoup( content, "html.parser" )
		self.crawl_page( self.url, soup, 0 )
	
	def crawl_page( self, url, soup, count ):
		if count >= self.max_pages:
			return
		for link in soup.find_all( "a" ):
			title = link.text
			href = link.get( "href" )
			if href.startswith( "/" ):
				href = url + href
			elif href.startswith( "http" ):
				pass
			else:
				href = url + "/" + href
			self.results.append({
				"title": title,
				"href": href
			})
		for link in soup.find_all( "a" ):
			if count >= self.max_pages:
				return
			href = link.get( "href" )
			if href.startswith( "http" ):
				response = requests.get( href )
				content = response.content
				soup = BeautifulSoup( content, "html.parser" )
				count += 1
				self.crawl_page( href, soup, count )
	
