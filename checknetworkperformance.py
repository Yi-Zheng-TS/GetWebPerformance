import sys, os
import time
import pycurl

# set the URL
url = 'https://www.cardiff.ac.uk/'
# set the curl object
curl = pycurl.Curl()
# define the requesting URL
curl.setopt(pycurl.URL, url)
# define the waiting time for requesting a connection
curl.setopt(pycurl.CONNECTTIMEOUT, 5)
# define the time for timeout
curl.setopt(pycurl.TIMEOUT, 5)
# not block download progress bar
curl.setopt(pycurl.NOPROGRESS, 1)
curl.setopt(pycurl.FORBID_REUSE, 1)
curl.setopt(pycurl.MAXREDIRS, 1)
curl.setopt(pycurl.DNS_CACHE_TIMEOUT, 60)
# create a file object, open it by web method, used to store the return content including http header and web
indexfile = open(os.path.dirname(os.path.realpath(__file__)) + '/content.txt', 'wb')
curl.setopt(pycurl.WRITEHEADER, indexfile)
curl.setopt(pycurl.WRITEDATA, indexfile)

# if failed to conntect direction url, close file and url object, terminate python program
try:
    curl.perform()
except Exception as e:
    print('Connection error:' + str(e))
    indexfile.close()
    curl.close()
    sys.exit() # sys.exit() and os._exit()

# Get DNS resolution time
NAMELOOKUP_TIME = curl.getinfo(curl.NAMELOOKUP_TIME)
# Get connection establishment time
CONNECT_TIME = curl.getinfo(curl.CONNECT_TIME)
# Get the time elapsed from establishment of connection to preparation of transfer
PRETRANSFER_TIME = curl.getinfo(curl.PRETRANSFER_TIME)
# Get the time elapsed from establishment of connection to start of transmission
STARTTRANSFER_TIME = curl.getinfo(curl.STARTTRANSFER_TIME)
# Get the total time of transfer
TOTAL_TIME = curl.getinfo(curl.TOTAL_TIME)
# Get HTTP status code
HTTP_CODE = curl.getinfo(curl.HTTP_CODE)
# Get the size of the uploaded packet
SIZE_UPLOAD = curl.getinfo(curl.SIZE_UPLOAD)
# Get download packet size
SIZE_DOWNLOAD = curl.getinfo(curl.SIZE_DOWNLOAD)
# Get the size of HTTP header
HEADER_SIZE = curl.getinfo(curl.HEADER_SIZE)
# Get average upload sepeed
SPEED_UPLOAD = curl.getinfo(curl.SPEED_UPLOAD)
# Get average download sepeed
SPEED_DOWNLOAD = curl.getinfo(curl.SPEED_DOWNLOAD)

print ("HTTP status code：%s" % (HTTP_CODE))
print ("DNS resolution time：%.2f ms" % (NAMELOOKUP_TIME*1000))
print ("Connection establishment time：%.2f ms" % (CONNECT_TIME*1000))
print ("Preparation transmission time：%.2f ms" % (PRETRANSFER_TIME*1000))
print ("The time of the start of the transmission：%.2f ms" % (STARTTRANSFER_TIME*1000))
print ("The time of the end of the transmission：%.2f ms" % (TOTAL_TIME*1000))
print ("Upload packet size：%d bytes/s" % (SIZE_DOWNLOAD))
print ("Download packet size：%d bytes/s" % (SIZE_DOWNLOAD))
print ("The size of HTTP header：%d bytes/s" % (HEADER_SIZE))
print ("Average upload sepeed：%d bytes/s" % (SPEED_DOWNLOAD))
print ("Average download sepeed：%d bytes/s" % (SPEED_DOWNLOAD))

indexfile.close()
curl.close()