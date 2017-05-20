import urllib
import urllib2
#takes a picture from a local ip camera
urllib.urlretrieve("http://192.168.43.1:8080/photo.jpg", "local-filename.jpg")
