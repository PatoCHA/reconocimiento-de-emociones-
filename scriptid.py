import urllib2
import urllib
import time
http_url = 'https://api-us.faceplusplus.com/facepp/v3/detect'
key = "yWVme-oiYYTI_6qhb14MOmxQn2j5DGod"
secret = "GNcZpSkJsB_04hpx84xQYrGQue0e667c"
filepath = r"local-filename.jpg"
boundary = '----------%s' % hex(int(time.time() * 1000))
data = []
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
data.append(key)
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
data.append(secret)
data.append('--%s' % boundary)
fr=open(filepath,'rb')
data.append('Content-Disposition: form-data; name="%s"; filename="co33.jpg"' % 'image_file')
data.append('Content-Type: %s\r\n' % 'application/octet-stream')
data.append(fr.read())
fr.close()
data.append('--%s--\r\n' % boundary)
attributes = "gender,age"
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_attributes')
data.append(attributes)
data.append('--%s--\r\n' % boundary)

http_body='\r\n'.join(data)
#buld http request
req=urllib2.Request(http_url)
#header
req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
req.add_data(http_body)
try:
	#post data to server
	resp = urllib2.urlopen(req, timeout=5)
	#get response
	qrcont=resp.read()
	print qrcont

except urllib2.HTTPError as e:
    print e.read()
import pandas as pd
from sqlalchemy import create_engine
from pandas.io.json import json_normalize
import json
engine = create_engine("mysql+mysqldb://root:"+'pjcm64930'+"@localhost/parrot_db")
normalized=json_normalize(json_normalize(json.loads(qrcont)).faces[0])

Porline=normalized['face_token'].values.tolist()

for line in Porline:
    http_url = "https://api-us.faceplusplus.com/facepp/v3/face/analyze"
    key = "yWVme-oiYYTI_6qhb14MOmxQn2j5DGod"
    secret = "GNcZpSkJsB_04hpx84xQYrGQue0e667c"
    filepath = r"1488276307959.jpg"
    boundary = '----------%s' % hex(int(time.time() * 1000))
    data1 = []
    data1.append('--%s' % boundary)
    data1.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
    data1.append(key)
    data1.append('--%s' % boundary)
    data1.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
    data1.append(secret)
    data1.append('--%s' % boundary)
    return_landmark= '0'
    data1.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_landmark')
    data1.append(return_landmark)
    data1.append('--%s' % boundary)
    return_landmark1= 'gender,age,smiling,headpose,facequality,blur,eyestatus'
    data1.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_attributes')
    data1.append(return_landmark1)
    data1.append('--%s' % boundary)
    face_tokens= str(line)
    data1.append('Content-Disposition: form-data; name="%s"\r\n' % 'face_tokens')
    data1.append(face_tokens)
    data1.append('--%s--\r\n' % boundary)

    http_body='\r\n'.join(data1)
    #buld http request
    req=urllib2.Request(http_url)
    #header
    req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
    req.add_data(http_body)
    try:
        #post data to server
        resp = urllib2.urlopen(req, timeout=5)
        #get response
        qrcont=resp.read()
        print qrcont
        normalized=json_normalize(json_normalize(json.loads(qrcont)).faces[0])
        normalized['time']=pd.to_datetime('now')
        normalized.to_sql('veoveo1',engine,flavor='mysql', if_exists='append',index=True)

    except urllib2.HTTPError as e:
        print e.read()
