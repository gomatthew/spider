from pyquery import PyQuery as pq


doc = pq(filename='detected_simple.html')

button = doc('#geetVerifyBtn.btn').text()
print(button)