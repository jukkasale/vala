import sys
import os
import unittest

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from multiples_of_a_and_b import read_file, write_file, find_multiples, validate_input, process_lines

class TestMultiplesOfAAndB(unittest.TestCase):

    def test_find_multiples(self):
        # Test finding multiples
        self.assertEqual(find_multiples(3, 5, 10), [3, 5, 6, 9])
        self.assertEqual(find_multiples(2, 4, 10), [2, 4, 6, 8])
        self.assertEqual(find_multiples(7, 11, 50), [7, 11, 14, 21, 22, 28, 33, 35, 42, 44, 49])
        self.assertEqual(find_multiples(1, 1, 5), [1, 2, 3, 4])
        self.assertEqual(find_multiples(3, 5, 1), [])

    def test_validate_input(self):
        # Test valid input formats
        self.assertTrue(validate_input(["3 5 10", "2 4 20"]))
        self.assertTrue(validate_input(["5 6 50", "5 9 45", "7 8 60"]))

    def test_process_lines(self):
        # Test processing lines to find multiples
        lines = ["3 5 10", "2 4 20"]
        expected = [(10, [3, 5, 6, 9]), (20, [2, 4, 6, 8, 10, 12, 14, 16, 18])]
        self.assertEqual(process_lines(lines), expected)

    def test_read_file(self):
        # Test reading file content
        with open('test_input1.txt', 'w') as f:
            f.write("3 5 10\n2 4 20\n")
        self.assertEqual(read_file('test_input1.txt'), ["3 5 10\n", "2 4 20\n"])

    def test_write_file(self):
        # Test writing data to file
        data = ["10:3 5 6 9\n", "20:2 4 6 8 10 12 14 16 18\n"]
        write_file('test_output2.txt', data)
        with open('test_output2.txt', 'r') as f:
            self.assertEqual(f.readlines(), data)

    def test_integration(self):
        # Test the integration of reading, processing, and writing data
        input_data = [
            "3 5 50\n",
            "2 7 30\n",
            "4 6 40\n",
            "5 9 45\n",
            "7 8 60\n",
            "3 4 25\n",
            "6 10 55\n",
            "2 3 20\n",
            "5 7 35\n",
            "4 9 50\n",
            "3 6 30\n",
            "2 5 40\n",
            "7 10 70\n",
            "4 8 45\n",
            "5 6 50\n",
            "3 9 60\n",
            "2 4 35\n",
            "6 8 55\n",
            "5 10 65\n",
            "3 7 40\n"
        ]
        expected_output = [
            "30:3 6 9 12 15 18 21 24 27\n",
            "35:5 7 10 14 15 20 21 25 28 30\n",
            "45:4 8 12 16 20 24 28 32 36 40 44\n",
            "40:4 6 8 12 16 18 20 24 28 30 32 36\n",
            "45:5 9 10 15 18 20 25 27 30 35 36 40\n",
            "25:3 4 6 8 9 12 15 16 18 20 21 24\n",
            "20:2 3 4 6 8 9 10 12 14 15 16 18\n",
            "65:5 10 15 20 25 30 35 40 45 50 55 60\n",
            "55:6 10 12 18 20 24 30 36 40 42 48 50 54\n",
            "55:6 8 12 16 18 24 30 32 36 40 42 48 54\n",
            "60:7 8 14 16 21 24 28 32 35 40 42 48 49 56\n",
            "70:7 10 14 20 21 28 30 35 40 42 49 50 56 60 63\n",
            "30:2 4 6 7 8 10 12 14 16 18 20 21 22 24 26 28\n",
            "50:4 8 9 12 16 18 20 24 27 28 32 36 40 44 45 48\n",
            "50:5 6 10 12 15 18 20 24 25 30 35 36 40 42 45 48\n",
            "35:2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34\n",
            "40:3 6 7 9 12 14 15 18 21 24 27 28 30 33 35 36 39\n",
            "60:3 6 9 12 15 18 21 24 27 30 33 36 39 42 45 48 51 54 57\n",
            "50:3 5 6 9 10 12 15 18 20 21 24 25 27 30 33 35 36 39 40 42 45 48\n",
            "40:2 4 5 6 8 10 12 14 15 16 18 20 22 24 25 26 28 30 32 34 35 36 38\n"
        ]

        with open('test_input.txt', 'w') as f:
            f.writelines(input_data)

        lines = read_file('test_input.txt')
        results = process_lines(lines)
        results.sort(key=lambda x: len(x[1]))

        output_data = []
        for goal, multiples in results:
            output_data.append(f"{goal}:{' '.join(map(str, multiples))}\n")

        write_file('test_output.txt', output_data)

        with open('test_output.txt', 'r') as f:
            self.assertEqual(f.readlines(), expected_output)

if __name__ == '__main__':
    unittest.main()