def find_duplicate_chara(characters):
    chara_count = {}
    duplicate = []

    for i in characters:
        if i in chara_count:
            chara_count[i] += 1
        else:
            chara_count[i] = 1

    for i, count in chara_count.items():
        if count > 1:
            duplicate.append(i)

    return duplicate

print("duplicated character are:",find_duplicate_chara("Ggwp hsskddt"))