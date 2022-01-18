with open('nginx_logs.txt','r',encoding="utf-8") as f:
    request_list=[]
    for line in f:
        remote_addr=line[:line.find(' ')]
        request_type=line[line.find('"')+1:line.find('"')+4]
        requested_resourse=line[line.find('/d'):line.find('HTTP')-1]
        tuple_requests=(remote_addr,request_type,requested_resourse)
        request_list.append(tuple_requests)
        print(tuple_requests)