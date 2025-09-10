def Calculate_Z(X_list):
    """Calculate the product Z based on the given list of X values.
    
    Z = (3*1*X1) * (3*2*X2) * (3*4*X3) * (3*8*X4)
    """
    product = 1
    for j in range(4):
        coefficient = 3 * pow(2, j)
        term = coefficient * X_list[j]
        product *= term
    return product

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 5:
        print("Usage: python calc_product_z.py X1 X2 X3 X4")
        sys.exit(1)
    
    try:
        X_values = [float(arg) for arg in sys.argv[1:5]]
    except ValueError:
        print("All inputs must be numbers.")
        sys.exit(1)
    
    result = Calculate_Z(X_values)
    print(f"Z = {result}")