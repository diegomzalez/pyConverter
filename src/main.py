from converter import converter
from selection import selection
from menu import menu
from welcome import welcome
def space():
    print('-'*40)
def main():
    welcome()
    space()
    a,b=menu()
    c,d=selection(a,b)
    space()
    converter(c,d)    



if __name__ == '__main__':
    main()
