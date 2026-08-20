class Polynomial:
    def __init__(self, coefficients):
        # Initialize the polynomial with a list of coefficients
        self.coefficients = coefficients

    # Add two polynomials
    def add(self, other):
        # Pad the smaller polynomial with zeros
        length = max(len(self.coefficients), len(other.coefficients))
        coeff1 = self.coefficients + [0] * (length - len(self.coefficients))
        coeff2 = other.coefficients + [0] * (length - len(other.coefficients))

        # Add corresponding coefficients
        result_coeffs = [coeff1[i] + coeff2[i] for i in range(length)]
        return Polynomial(result_coeffs)

    # Multiply two polynomials
    def multiply(self, other):
        # Initialize a result array of zeros with appropriate size
        result_coeffs = [0] * (len(self.coefficients) + len(other.coefficients) - 1)

        # Perform polynomial multiplication (distribute each term)
        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                result_coeffs[i + j] += self.coefficients[i] * other.coefficients[j]
        return Polynomial(result_coeffs)

    # Evaluate the polynomial for a given value of x
    def evaluate(self, x):
        result = 0
        for i in range(len(self.coefficients)):
            result += self.coefficients[i] * (x ** (len(self.coefficients) - i - 1))
        return result

    # Display the polynomial in a readable format
    def __str__(self):
        terms = []
        degree = len(self.coefficients) - 1
        for i, coeff in enumerate(self.coefficients):
            if coeff != 0:
                if degree - i > 0:
                    terms.append(f"{coeff}x^{degree - i}")
                else:
                    terms.append(f"{coeff}")
        return " + ".join(terms).replace(" + -", " - ").replace("x^1", "x")

# Driver Code
if __name__ == "__main__":
    # Polynomial 1: 4x^3 + 2x^2 + 3x + 1
    poly1 = Polynomial([4, 2, 3, 1])
    # Polynomial 2: 3x^2 + 5x + 2
    poly2 = Polynomial([3, 5, 2])
    print("Polynomial 1:", poly1)
    print("Polynomial 2:", poly2)
    # Add polynomials
    sum_poly = poly1.add(poly2)
    print("Sum of polynomials:", sum_poly)                                                                                                                
    product_poly = poly1.multiply(poly2)
    print("Product of polynomials:", product_poly)
    # Evaluate the first polynomial at x = 2
    value = poly1.evaluate(2)
    print("Evaluation of Polynomial 1 at x = 2:", value)