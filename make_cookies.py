for i in range(10):
    open('cookies%02d.dat' % i, 'w').write('This contains cookies #%d' % i)