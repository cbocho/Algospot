su = input('su : ')
su = int(su)
lst = [0 for _ in range(su)]

for n in range(0, su):
    num = input('input : ')
    num = int(num)
    u_num = num & 0xFFFFFFFF
    result = ((u_num & 255)<<24) + ((u_num & (255 <<8))<<8) + ((u_num & (255 << 16))>>8) + ((u_num & (255 << 24))>>24)
    lst.pop(0)
    lst.append(result)

print( "\n".join(map(str, lst)))






