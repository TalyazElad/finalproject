from brisque import BRISQUE

def print_hi():
    brisq = BRISQUE()
    print('yaelbit_before image: %s' % brisq.score("yaelbit_before.jpg"))
    #print('yaelbit_afterblurr image: %s' % brisq.get_score("yaelbit_afterblurr.png"))
    #print('yaelbit image: %s' % brisq.get_score("yaelbit.png"))


if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
