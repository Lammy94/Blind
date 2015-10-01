import urllib2  # the lib that handles the url stuff

data = urllib2.urlopen("https://pheonix.worcestercomputing.com:2083/cpsess6949684798/frontend/x3/filemanager/showfile.html?file=Blind.txt&fileop=&dir=%2Fhome%2Fiwzxeyes%2Fpublic_html%2FUpdate&dirop=&charset=&file_charset=&baseurl=&basedir=") # it's a file like object and works just like a file
for line in data: # files are iterable
    print (line)
