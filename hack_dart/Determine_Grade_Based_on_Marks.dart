// Write a Dart program to determine the grade based on a student's marks.
void main() {
  int marks = 69;

// print out the appropriate grade
  if (marks > 85) {
    print("Excellent");
  } else if (marks >= 75 && marks <= 85) {
    print("Very Good");
  } else if (marks >= 65 && marks < 75) {
    print("Good");
  } else {
    print("Average");
  }
}
