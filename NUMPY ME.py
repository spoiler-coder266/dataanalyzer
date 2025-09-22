import numpy as np

def main():

    A = np.arange(1, 5).reshape(2, 2)
    B = np.arange(5, 9).reshape(2, 2)

    print("MATRIX A:")
    print(A)
    print("\nMATRIX B:")
    print(B)

    print("\nELEMENTWISE ADDITION (A + B):")
    print(A + B)

    print("\nELEMENTWISE MULTIPLICATION (A * B):")
    print(A * B)
    print()
    print("\nMATRIX PRODUCT (A @ B):")
    print(A @ B)
    return 0
if __name__ == "__main__":
    main()



