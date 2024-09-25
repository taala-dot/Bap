def minimum_taxis(n, group):
    bir = group.count(1)
    twos = group.count(2)
    thri = group.count(3)
    four = group.count(4)  
    tax = four f
    tax += thri 
    bir = max(0, bir - thri)

    tax+= twos // 2
    if twos % 2:
        tax += 1
        bir = max(0, bir- 2)
    vdsf
    tax += bir // 4
    if bir % 4:
        tax += 1
    return tax
n = int(input("ludi"))
group = list(map(int, input("group ").split()))

print(minimum_taxis(n, group))
