cypher = [ 0xf7, 0xf8, 0xf1, 0xf4, 0xf1, 0xf8, 0xb3, 0xfc, 0xfc ]

key = 0b10010000 # 0x90

comb = [ 0b10010000, 0b00010000, 0b00000000, 0b10000000 ]


def get_code(idx, combidx):
	return ( cypher[idx] & ~ key ) | comb[combidx]

def print_state(state):
	plain = [u""] * len(cypher)
	for i in range(0, len(cypher)):
		
		code = get_code(i, state[i])
		plain[i] = chr(code)

	print u"".join(plain)


def produce_key(state, idx):
	if idx >= len(cypher):
		return True

	while state[idx] < 3:
		state[idx] += 1

		for c in range(idx+1, len(cypher)):
			state[c] = -1

		if get_code(idx, state[idx]) > 127:
			"""
			to avoid compatibility issues, discard all
			combinations that produce chars outside the
			ascii/utf8 common range
			"""
			continue

		if produce_key(state, idx + 1):
			print_state(state)


	return False


def produce_keys():
	
	current = [-1] * len(cypher)
	produce_key(current, 0)


if __name__ == "__main__":
	produce_keys()
	


