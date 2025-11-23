lol = input().split()

LHS = float(lol[0])
RHS = float(lol[2])


match lol[1]:
    case "*":
        print(f"{(LHS * RHS):.3f}")
    case "/":
        if RHS == 0:
            print("ze")
        else:
            print(f"{(LHS / RHS):.3f}")
    case "-":
        print(f"{(LHS - RHS):.3f}")
    case "+":
        print(f"{(LHS + RHS):.3f}")
