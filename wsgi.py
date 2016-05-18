from cgi import parse_qs

def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/plan')])
    qs=parse_qs(env['QUERY_STRING'])
    #return ['Hello World!']
    res = ['%s=%s<br>' % (k, qs[k][0]) for k in qs]
    #print (res)
    return res
