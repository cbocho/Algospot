su = input('su : ')
su = int(su)
sentence_lst = [0 for _ in range(su)]

for i in range(0,su):
    munja = input('input : ')
    len_munja = len(munja)
    div_len_mun = len_munja/2
    div_len_mun = int(div_len_mun)
    character_lst = [0 for _ in range(div_len_mun)]
    for a in range(0,div_len_mun):
        result = munja[a*2] + munja[(a*2)+1]
        character_lst.pop(0)
        character_lst.append(result)
    character_lst.sort(key=str.lower)
    character="".join(character_lst)
    sentence_lst.pop(0)
    sentence_lst.append(character)

print( "\n".join(map(str, sentence_lst)))


