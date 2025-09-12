def find_machine_epsilon():
    epsilon = 1.0
    while (1.0 + epsilon) != 1.0:
        epsilon /= 2.0
    return epsilon * 2.0   # The last valid epsilon before it became 0
if __name__ == "__main__":
    result = find_machine_epsilon()
    print("Machine Epsilon =", result)
