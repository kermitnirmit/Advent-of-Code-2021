from functools import reduce
f = open("input.txt").read().strip()
binary_string = bin(int(f, 16))[2:]
while len(binary_string) % 4 != 0:
    binary_string = "0" + binary_string


def solve(curr):
    v = curr[:3]
    curr = curr[3:]
    v = int(v, base=2)
    t = curr[:3]
    curr = curr[3:]
    t = int(t, base=2)
    if t == 4:
        # print("it's a literal")
        parts = ''
        while True:
            p = curr[:5]
            curr = curr[5:]
            parts += p[1:]
            if p[0] == '0':
                break
        n = int(parts, base=2)
        packet = (v, t, n)
        return packet, curr
    lbit = curr[0]
    curr = curr[1:]
    if lbit == "0":
        l, curr = curr[:15], curr[15:]
        len_subpackets = int(l,2)
        extra, curr = curr[:len_subpackets], curr[len_subpackets:]
        packets = []
        while extra:
            p, extra = solve(extra)
            packets.append(p)
    else:
        l, curr = curr[:11], curr[11:]
        num_subpackets = int(l,2)
        packets = []
        while len(packets) != num_subpackets:
            p, curr = solve(curr)
            packets.append(p)

    p = (v, t, None, packets)
    return p, curr

# A packet has (version, typeID, number if literal, subPackets if not literal)
queue = [solve(binary_string)[0]]
answer = 0
while queue:
    p = queue.pop(0)
    answer += p[0]
    if p[1] == 4:
        continue
    queue.extend(p[3])
print("p1", answer)
"""
# Packets with type ID 0 are sum packets - their value is the sum of the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
# Packets with type ID 1 are product packets - their value is the result of multiplying together the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
# Packets with type ID 2 are minimum packets - their value is the minimum of the values of their sub-packets.
# Packets with type ID 3 are maximum packets - their value is the maximum of the values of their sub-packets.
# Packets with type ID 5 are greater than packets - their value is 1 if the value of the first sub-packet is greater than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
# Packets with type ID 6 are less than packets - their value is 1 if the value of the first sub-packet is less than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
# Packets with type ID 7 are equal to packets - their value is 1 if the value of the first sub-packet is equal to the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
"""
def evaluate_packet(p):
    # why the fuck are there so many rules
    answer = 0
    if p[1] == 0:
        answer += sum(evaluate_packet(x) for x in p[3])
    if p[1] == 1:
        answer += reduce(lambda a, b: a * b, [evaluate_packet(x) for x in p[3]], 1)
    if p[1] == 2:
        answer += min(evaluate_packet(x) for x in p[3])
    if p[1] == 4:
        answer += p[2]
    if p[1] == 3:
        answer += max(evaluate_packet(x) for x in p[3])
    if p[1] == 5:
        answer += evaluate_packet(p[3][0]) > evaluate_packet(p[3][1])
    if p[1] == 6:
        answer += evaluate_packet(p[3][1]) > evaluate_packet(p[3][0])
    if p[1] == 7:
        answer += evaluate_packet(p[3][0]) == evaluate_packet(p[3][1])
    return answer


answer = 0
queue = [solve(binary_string)[0]]
while queue:
    p = queue.pop(0)
    answer += evaluate_packet(p)
print("p2", answer)
