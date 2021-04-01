import urllib2

url = 'http://api.justin.tv/api/stream/list.json?channel=nicomf_'
contents = urllib2.urlopen(url)

print(contents.read())
