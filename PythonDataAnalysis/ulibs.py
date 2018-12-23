
import scipy.misc
import matplotlib.pyplot as plt
import numpy as np
import pkgutil as pu
import pydoc

def show_img_with_x(img):
    '''from Python Data Analysis p41'''
    xmax = img.shape[0]
    ymax = img.shape[1]
    img[range(xmax), range(ymax)] = 0
    img[range(xmax - 1, -1, -1), range(ymax)] = 0
    plt.imshow(img)
    plt.show()

def _test_show_img_with_x():
    show_img_with_x(scipy.misc.ascent())

def shuffle_indices(size):
    ''' from Python Data Analysis p43'''
    arr = np.arange(size)
    np.random.shuffle(arr)
    return arr

def _clean(astr):
    s = astr
    #remove multiple spaces
    s = " ".join(s.split())
    s = s.replace("=","")

    return s

def print_desc(prefix, pkg_path):
    '''from Python Data Analysis p51'''
    for pkg in pu.iter_modules(path = pkg_path):
        name = prefix + "." + pkg[1]
        
        if pkg[2] == True:
            try:
                docstr = pydoc.plain(pydoc.render_doc(name))
                docstr = _clean(docstr)
                start = docstr.find("DESCRIPTION")
                docstr = docstr[start: start + 140]
                print(name, docstr)
            except:
                continue

def print_t(y = 1, x = 1):
    i = int(y)
    while i <= 9:
        s = int(x)
        while s <= i:
            p = i * s
            print(str(i) + "*" + str(s) + "=" + str(p), end="\t")
            s += 1
        print("")
        i += 1

def pkg_check(model):
    for pkg in pu.iter_modules(path = model.__path__):
        name = pkg[1]
        if pkg[2] == True:
            print(name)


if __name__ == "__main__":
    #_test_show_img_with_x()
    print_t()