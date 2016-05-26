

def start(results2,maxTime2):
    for row in results2:
        id=row[0]
        fnames=row[1]
        fd=fnames.split("|")
        fname=fd[0].strip()
        if fname==maxTime2:
            return id
        else:
            continue

