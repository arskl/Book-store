def parser():
    file = open("debug.log", "r")
    log_list = []
    for line in file:
        log_list.append(str(line))

    for line in log_list:
        check = 'HTTP/1.1" 302 0'
        if check in line:
            Logger(log=line).save()
            CrudLogger(crud_log=line).save()
        else:
            Logger(log=line).save()
