from typing import Tuple


def kendall_tau(seq : Tuple[int]) -> int:
    dist = 0
    for ii in seq:
        for jj in seq:
            if ii > jj and seq.index(ii) < seq.index(jj):
                dist += 1
    return dist