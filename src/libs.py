try:
	import requests
	import sys, urlparse, hashlib
	from Queue import Queue, Empty as QueueEmpty
	from time import sleep
	from bs4 import BeautifulSoup as BS
	import threading as Thread
	import socket as soc
	import re as re

except:
	from Colors import TextColor
	raise SystemExit, TextColor.RED + \
					  str("We have problem in libreries please check it and then try latter") \
					  + TextColor.WHITE
