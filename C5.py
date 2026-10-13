#C5
#star delta transformation
def star_to_delta(ra, rb, rc):
    total = ra * rb + rb * rc + rc * ra

    delta_ab = total / rc
    delta_bc = total / ra
    delta_ca = total / rb

    return round(delta_ab, 2), round(delta_bc, 2), round(delta_ca, 2)


print("Delta resistances =", star_to_delta(10, 20, 30))
