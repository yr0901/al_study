#다솔이의 다이아몬드 장식
tcase=int(input())
for tc in range(tcase):
    string = input()
    if len(string)==1:
        print('..#..')
        print('.#.#.')
        print('#.{}.#'.format(string))
        print('.#.#.')
        print('..#..')

    else:
        le=len(string)
        print('..#.'*le + '.')
        print('.#'*le*2+'.')
        for n in string:
            print('#.{}.'.format(n) , end='')
        print('#')
        print('.#'*le*2+'.')
        print('..#.'*le + '.')
