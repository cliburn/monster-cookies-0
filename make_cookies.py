if __name__ == '__main__':
    for i in range(10):
        open('f%02d.dat' % i, 'w').write('This contains intermediate results #%d' % i)