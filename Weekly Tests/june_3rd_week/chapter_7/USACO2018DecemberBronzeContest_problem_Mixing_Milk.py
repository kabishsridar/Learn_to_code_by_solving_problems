c_lst = [] # capacity of each bucket list
m_lst = [] # milk in each bucket list
for i in range(3): # mentioned 3 buckets
    values = input().split() # prompt for the values of both capacity and milk
    c1 = values[0]
    m1 = values[1]
    c_lst.append(c1) # appending the values to the list
    m_lst.append(m1)

c1 = int(c_lst[0]) # storing each values seperately
c2 = int(c_lst[1])
c3 = int(c_lst[2])
m1 = int(m_lst[0])
m2 = int(m_lst[1])
m3 = int(m_lst[2])

# the m1 should be transferred to c2 only if c2 is greater than m1
""" # it can't pour milk from bucket 3 to bucket 1
    if c2 >= m1 + m2:
        m2 += m1
        m1 = 0
    else:
        m1 = (m1 + m2) - c2
        m2 = c2
    if c3 >= m2 + m3:
        m3 += m2
        m2 = 0
    else:
        m2 = (m2 +m3) - c2
        m3 = 0 """

step = 0
for i in range(100): # loops for 100 times
    if step == 0:
        # Bucket 1 to Bucket 2
        space = c2 - m2 # the remaining space
        if m1 <= space:
            m2 += m1 # pour all milk from m1
            m1 = 0 # no milk in m1
        else:
            m2 = c2
            m1 = m1 - space # pour only upto the available space
        step = 1

    elif step == 1:
        # Bucket 2 to Bucket 3
        space = c3 - m3
        if m2 <= space:
            m3 += m2
            m2 = 0
        else:
            m3 = c3
            m2 = m2 - space
        step = 2

    elif step == 2:
        # Bucket 3 to Bucket 1
        space = c1 - m1
        if m3 <= space:
            m1 += m3
            m3 = 0
        else:
            m1 = c1
            m3 = m3 - space
        step = 0
print(m1) # display the output
print(m2)
print(m3)