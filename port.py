def even_or_odd(var1):

    if pol%2==0:
        print(f"The Number {var1} is EVEN number.")
    else:
        print(f"The Number {var1} is ODD number.")


def compute(v1,v2,v3):

    t=v1+v2+v3
    if v1==v2 or v2==v1 or v1==v3 or v2==v3 or v3==v1:
        print(f"{v1} {v2} {v3} = 0")
    else:
        print(f"{v1} + {v2} + {v3} = {t}")

