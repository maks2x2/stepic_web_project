#from cgi import parse_qs

def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    #qs=parse_qs(env['QUERY_STRING'])
    res = env['QUERY_STRING'].split('&')
    #res = ['%s=%s<br>' % (k, qs[k][0]) for k in qs]
    res = [item+'\r\n' for item in res]
    return res
