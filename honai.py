def mov_disk(height,st ,nd,rd):
    global pacet_disk
    if height >= 1:
        mov_disk(height-1,st,rd,nd)
        pacet_disk(st,nd)
        mov_disk(height-1,rd,nd,st )
        return mov_disk
def pacet_disk(before,after):
    print('dvijen ot ',before, "k",after)
mov_disk(3,"1","2","3")