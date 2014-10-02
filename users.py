# The following is an example from the Mandrillapp.com API Docs
import mandrill

try:
    mandrill_client = mandrill.Mandrill('hdsUHK9sxGH4Tzn6IiLNmw')
    result = mandrill_client.users.info()
    print mandrill_client.users.info()

except mandrill.Error, e:
    # Mandrill errors are thrown as exceptions
    print 'A mandrill error occurred: %s - %s' % (e.__class__, e)
    # A mandrill error occurred: <class 'mandrill.InvalidKeyError'> - Invalid API key    
    raise