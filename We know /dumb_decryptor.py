def cipher_decrypt(ciphertext, key):
    decrypted = ""
    for c in ciphertext:
        if c.isupper():
            c_index = ord(c) - ord('A')
            c_og_pos = (c_index - key) % 26 + ord('A')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.islower():
            c_index = ord(c) - ord('a')
            c_og_pos = (c_index - key) % 26 + ord('a')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.isdigit():
            c_og = (int(c) - key) % 10
            decrypted += str(c_og)
        else:
            decrypted += c
    return decrypted
ciphertext = "Terrgvatf, arjpbzre! Jr ner tynq gb frr, gung lbh unir fhpprffshyyl cnffrq bhe vavgvny grfg. Qba'g or fb cebhq bs lbhefrys - vg'f whfg n grfg gb svygre zbfg hfryrff crbcyr, gung pna qb abguvat sbe bhe pbzzhavgl. Orsber jr jvyy cnff lbh fbzr erny gnfxf gb qb - chg lbhe rapelcgvba penpxre gb lbhe ercbfvgbel. Anzr sbyqre Jr xabj, naq chg vafvqr qhzo_qrpelcgbe.cl. Nyfb, va beqre gb cnff guvf gnfx - lbh fubhyq jevgr Dhvf phfgbqvrg vcfbf phfgbqrf? nf n pbzzrag. Guvf zrffntr va pbzzrag frpgvba vf lbhe npprcgnapr sbe gur fbzr arj wbo gb qb. Jr ner jnvgvat..."
decrypted_msg = cipher_decrypt(ciphertext, 13)
print("The cipher text:\n", ciphertext)
print("The decrypted message is:\n",decrypted_msg)