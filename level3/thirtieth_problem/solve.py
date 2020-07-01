# 01234567890123456789012345678901

# Breakpoint *0x565563d0
# pwndbg> x/32bx $ebx+0x214
# 0x565581c0:	0xd5	0x2b	0x5c	0xbf	0x7c	0x15	0xea	0xa5
# 0x565581c8:	0xa0	0xc9	0x8b	0x38	0x80	0xd5	0xa3	0xcd
# 0x565581d0:	0xb7	0xeb	0xa0	0xc9	0x8b	0x38	0x80	0xd5
# 0x565581d8:	0xa3	0xcd	0xb7	0xeb	0xa0	0xc9	0xcd	0xfe

from z3 import *

def bits_to_val(word_bits):
    bits = word_bits[:]
    if len(bits) < 16:
        bits.extend([0] * (16 - len(bits)))

    print(bits)
    val = 0
    for bit in bits:
        val |= bit
        val *= 2
    
    # val &= 0xffff
    val /= 2
    return val

def bits_to_hex(bits):
    target = []
    while True:
        word_bits = bits[:16]
        bits = bits[16:]
        val = bits_to_val(word_bits)
        # words.append(val)
        target.append(val >> 8)
        target.append(val & 0xff)
        if len(word_bits) < 16:
            break

    return target

def get_all_bits(s, limit = 0xff, reverse_bit_in_byte = False):
    all_bits = []
    for c in s:
        if type(c) == str:
            n = ord(c)
        else:
            n = c
        for i in range(8):
            if not reverse_bit_in_byte:
                bit_test = n & (1 << i)
            else:
                bit_test = n & (1 << (7 - i))
            all_bits.append(1 if bit_test else 0)

    all_bits = all_bits[: limit]
    # print(all_bits)
    return all_bits

def generate(all_bits, rounds = 0x40):

    l = len(all_bits)
    for i in range(rounds):
        new_bits = []
        for j in range(l):
            prev_idx = (j - 1) % l
            prev_bit = all_bits[prev_idx]
            next_idx = (j + 1) % l
            next_bit = all_bits[next_idx]
            curr_bit = all_bits[j]

            new_bit = (curr_bit | next_bit) ^ prev_bit
            new_bits.append(new_bit)
        
        # if i == 0x40 - 2:
        #     print(new_bits)

        all_bits = new_bits[:]

    # print(new_bits)
    target = bits_to_hex(new_bits)
    print(target)
    # for b in target:
    #     print(hex(b))
        

def z3_solve_one_round(bits):

    l = len(bits)
    s = [ BitVec('x%s' % i, 1) for i in range(l)]
    solver = Solver()

    for i in range(l):

            prev_idx = (i - 1) % l
            prev_bit = s[prev_idx]
            next_idx = (i + 1) % l
            next_bit = s[next_idx]
            curr_bit = s[i]

            # print(curr_bit, next_bit, prev_bit)
            solver.add((curr_bit | next_bit) ^ prev_bit == bits[i])

    # print(solver)

    ret = []
    if solver.check() == sat:

        m = solver.model()
        for i in range(l):
            c = m[s[i]].as_long()
            ret.append(c)
    else:
        print('failed!!!')

    return ret

def z3_solve(bits):
    for i in range(0x40):
        print(i)
        bits = z3_solve_one_round(bits)

    return bits

def bits_to_solution(bits):
    s = ''
    while True:
        this_char_bits = bits[:8]
        bits_str = [str(n) for n in this_char_bits]
        bits_str = bits_str[::-1]
        bin_str = ''.join(bits_str)
        n = int(bin_str, 2)
        s += chr(n)
        bits = bits[8:]
        if len(this_char_bits) < 8:
            break

    return s


def main():
    # s = '01234567890123456789012345678901'
    # all_bits = get_all_bits(s, 0xff)
    # generate(all_bits)

    # target = [213, 43, 92, 191, 124, 21, 234, 165, 160, 201, 139, 56, 128, 213, 163, 205, 183, 235, 160, 201, 139, 56, 128, 213, 163, 205, 183, 235, 160, 201, 205, 254]

    target = [
	0xd7, 0x76, 0x88, 0x8e, 0xb3, 0xa6, 0x30, 0xcd, 0xbb, 0x9b, 0x1f, 0x7f, 0x85, 0x2a, 0x6a, 0xcb,
	0xd6, 0xf3, 0x2a, 0xd3, 0xec, 0x82, 0xf9, 0x02, 0xef, 0xce, 0xb4, 0x71, 0x61, 0x6e, 0x8d, 0xb4
    ]


    target_bits =  get_all_bits(target, 0xff, True)
    # print('targe: ')
    # print(target_bits)
    # bits = z3_solve_one_round(target_bits)
    bits = z3_solve(target_bits)
    print(bits)

    s = bits_to_solution(bits)
    print(s)

    # generate(bits, rounds = 0x40)

if __name__ == '__main__':
    main()

# FLAG{1_h4rdw4r3_f0r_my_256_vms!}