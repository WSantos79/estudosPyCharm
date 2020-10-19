'''import pydf

pdf = pydf.generate_pdf('<h1>Wellington e Tarcia</h1>')

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
'''

from __future__ import print_function

from pip._vendor.distlib.compat import raw_input

if __name__ == '__main__':
    n = int(raw_input())


for i in range(n):
    print(i+1, end='')

