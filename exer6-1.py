

def m_table(*args):

    if 1>len(args) or len(args)>2:
        raise ValueError("Number of arguements should be <1 or >2")
    
    c=args[0]
    r=c
    
    if len(args) == 2:
        r=args[1]
 
    table = []
    for r in range(1,r+1):
        row=[]
        for c in range(1, c+1):
            row.append(r*c)
        table.append(row)
    
    for row in table:
        print(*row)


m_table(4,2)


