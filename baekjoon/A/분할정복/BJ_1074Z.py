#Z

def CHECK(length, starty, startx):
    global cnt, r, c

    if length == 2:
        count = 0
        for y in range(2):
            for x in range(2):
                if starty+y == r and startx+x == c:
                    cnt += count
                count += 1
        return

    if starty <= r < starty+length//2 and startx<= c < startx+length//2:
        CHECK(length//2, starty, startx)

    elif starty <= r < starty+length//2 and startx+length//2 <= c < startx+length:
        cnt += length**2 // 4
        CHECK(length//2, starty, startx+length//2)

    elif starty+length//2<= r < starty+length and startx<= c < startx+length//2:
        cnt += length**2 // 4 * 2
        CHECK(length//2, starty+length//2, startx)

    else:
        cnt += length**2 // 4 * 3
        CHECK(length//2, starty+length//2, startx+length//2)



N, r, c = map(int, input().split())
cnt = 0
CHECK(2**N, 0, 0)
print(cnt)