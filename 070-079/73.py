def counting_fractions_in_a_range(limit):
    limit += 1
    in_a_range = [0, 0] + [(x - 1) for x in range(2, limit)]

    for d in range(2, limit):
        too_small  = int(1 * (d / 3))
        too_large = ((d - (int(1 * (d / 2)) + 1))
                     if d % 2 != 0 else (d - int(1 * (d / 2))))
        in_a_range[d] -= too_small + too_large

        for f in range((d * 2), limit, d):
            in_a_range[f] -= in_a_range[d]
            
    return sum(in_a_range)


