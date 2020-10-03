def encrypt_sentence(sentence):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    main_list = []
    word = sentence.split()
    for i in range(0, len(word)):
        if (i % 2 == 0):
            main_list.append(word[i][::-1])
        else:
            vow = []
            con = []
            for j in word[i]:
                if (j in vowel_list):
                    vow.append(j)
                else:
                    con.append(j)
            new_string = "".join(con) + "".join(vow)
            main_list.append(new_string)
    return " ".join(main_list)


sentence = "The sun rises in the east"
encrypted_sentence = encrypt_sentence(sentence)
print(encrypted_sentence)
