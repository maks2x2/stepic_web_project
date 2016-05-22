def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    res = env['QUERY_STRING'].split('&')
    #res = [item+'\r\n' for item in res]
    res='\r\n'.join(res)
    return [bytes(res,encoding="utf8")]
