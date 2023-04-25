
def r_sort(lst,sorted_lst):

    if len(lst)==0:
        return sorted_lst
    else:
        a = min(lst)
        lst.remove(a)
        sorted_lst.append(a)
        return r_sort(lst,sorted_lst)


lst = [6,7,4,9,0,2,1]
sorted_lst = []
print(r_sort(lst,sorted_lst))