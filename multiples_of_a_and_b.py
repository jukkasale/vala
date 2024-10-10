import sys
from typing import List, Tuple

def read_file(file_path: str) -> List[str]:
    """Reads the content of the file and returns it as a list of lines."""
    try:
        with open(file_path, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except IOError:
        print(f"Error: Could not read file '{file_path}'.")
        sys.exit(1)

def write_file(file_path: str, data: List[str]) -> None:
    """Writes the given data to the file."""
    try:
        with open(file_path, 'w') as file:
            file.writelines(data)
    except IOError:
        print(f"Error: Could not write to file '{file_path}'.")
        sys.exit(1)

def find_multiples(A: int, B: int, goal: int) -> List[int]:
    """Finds all multiples of A and B below the goal number."""
    multiples = []
    for i in range(1, goal):
        if i % A == 0 or i % B == 0:
            multiples.append(i)
    return multiples

def validate_input(lines: List[str]) -> bool:
    """Validates that each line contains exactly three integers."""
    errors = []
    for i, line in enumerate(lines, start=1):
        parts = line.split()
        if len(parts) != 3 or not all(part.isdigit() for part in parts):
            errors.append(f"Invalid input file format in line {i}. Each line must contain exactly three integers.")
    
    if errors:
        for error in errors:
            print(error)
        return False
    
    return True

def process_lines(lines: List[str]) -> List[Tuple[int, List[int]]]:
    """Processes each line to find multiples and returns the results."""
    results = []
    for line in lines:
        A, B, goal = map(int, line.split())
        multiples = find_multiples(A, B, goal)
        results.append((goal, multiples))
    return results

def main():
    # Check that there are exactly two command-line arguments (input and output files)
    if len(sys.argv) != 3:
        print("Usage: python my_program.py input.txt output.txt")
        return

    # Read the input and output file names from the command-line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Read the content of the input file
    lines = read_file(input_file)

    # Validate that the input file content is in the correct format
    if not validate_input(lines):
        return

    # Process the lines of the input file and find the multiples
    results = process_lines(lines)
    # Sort the results by the number of multiples in ascending order
    results.sort(key=lambda x: len(x[1]))

    # Form the output data
    output_data = []
    for goal, multiples in results:
        output_data.append(f"{goal}:{' '.join(map(str, multiples))}\n")

    # Print the output data to the console
    for line in output_data:
        print(line.strip())

    # Write the output data to the output file
    write_file(output_file, output_data)

if __name__ == "__main__":
    main()