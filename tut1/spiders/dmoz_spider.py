from scrapy.spider import BaseSpider 
from scrapy.selector import HtmlXPathSelector 
import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from items  import DmozItem

class DmozSpider(BaseSpider): 
   name = "dmoz" 
   allowed_domains = ["dmoz.org"] 
   start_urls = [ 
       "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/", 
       "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/" 
   ] 
  
   def parse(self, response): 
       hxs = HtmlXPathSelector(response) 
       sites = hxs.select('//fieldset/ul/li') 
       #sites = hxs.select('//ul/li') 
       items = [] 
       for site in sites:
           print "=================================================="
           item = DmozItem() 
           item['title'] = site.select('a/text()').extract() 
           item['link'] = site.select('a/@href').extract() 
           item['desc'] = site.select('text()').extract() 
           items.append(item) 
       return items  
