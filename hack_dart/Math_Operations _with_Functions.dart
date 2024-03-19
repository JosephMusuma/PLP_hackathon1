// Write a Dart program that performs two mathematical operations using functions.

void main() {
  // Function for multiplication
  int product(int a, int b) {
    return a*b;
  }

  // Function for Subtraction
  int difference(int a, int b) {
    return a - b;
  }

  // Numbers to perform the operations
  int num1 = 54;
  int num2 = 18;


  // Perform multiplication
  int resultMultiplication = product(num1, num2);
  print("54 * 18 = $resultMultiplication");

  // Perform Subtraction
  int resultDifference = difference(num1, num2);
  print("54 - 18 = $resultDifference");
}
