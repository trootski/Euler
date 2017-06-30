#suppose we'll start with the brute force method

current_num_to_check = 1

is_current_num_ok = True

while True:
    
    is_current_num_ok = True

    for lp in range(1, 20):
        #print "Checking num %s (%s modulo %s)" % ((current_num_to_check % lp), current_num_to_check, lp)
        if (current_num_to_check % lp) != 0:
            is_current_num_ok = False
            break
    
    if is_current_num_ok:
        break
    else:
        current_num_to_check = current_num_to_check + 1

print "Smallest number is %s" % current_num_to_check
