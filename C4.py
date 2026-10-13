#C4
#loaded voltage divider
def loaded_divider(vs, r1, r2, rl):
    unloaded = vs * r2 / (r1 + r2)

    parallel = (r2 * rl) / (r2 + rl)

    loaded = vs * parallel / (r1 + parallel)

    return unloaded, loaded


print("Unloaded and loaded voltage =", loaded_divider(12, 1000, 1000, 500))
