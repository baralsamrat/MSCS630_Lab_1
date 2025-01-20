
# Multithreading Word Frequency Lab Report

## Design and Structure
The program is designed to split a given text file into multiple segments based on the user-specified number of segments. Each segment is processed by a separate thread to compute the frequency of words. Intermediate results are stored in a thread-safe manner and consolidated by the main thread.

### Key Components:
1. **File Segmentation**: The file is split into nearly equal-sized segments.
2. **Thread-based Processing**: Each thread computes word frequencies for its assigned segment.
3. **Consolidation**: The main thread aggregates results into the final word frequency count.

## Logic Behind Segmentation and Word Counting
The text is split into words, and segments are created based on the total word count divided by the number of segments. Uneven word distribution is handled by including the remainder in the last segment.

## Multithreading Implementation
Python's `threading` module is used to create and manage threads. A `Lock` ensures thread-safe operations on shared resources. The use of `Counter` from the `collections` module simplifies frequency counting.

## Challenges Encountered
1. **Thread Synchronization**: Ensuring correct handling of shared data required careful use of locks.
2. **Uneven Segmentation**: Adjustments were needed to handle files with a word count not divisible by the number of segments.

## Sample
Multithreading is a concept that allows a program to run multiple threads concurrently.
Each thread is a smaller unit of process, enabling parallelism and improving performance.
This text is used to test the multithreading word frequency counting program.
Feel free to customize or expand this text to test additional cases.

## Sample Output
### Intermediate Word Frequencies:
- Segment 1: {'Multithreading': 1, 'is': 2, 'a': 2, 'concept': 1, 'that': 1, 'allows': 1, 'program': 1, 'to': 1, 'run': 1, 'multiple': 1, 'threads': 1, 'concurrently.': 1, 'Each': 1, 'thread': 1}
- Segment 2: {'a': 1, 'smaller': 1, 'unit': 1, 'of': 1, 'process,': 1, 'enabling': 1, 'parallelism': 1, 'and': 1, 'improving': 1, 'performance.': 1, 'This': 1, 'text': 1, 'is': 1, 'used': 1, 'to': 1, 'test': 1}
- Segment 3: {'the': 1, 'multithreading': 1, 'word': 1, 'frequency': 1, 'counting': 1, 'program.': 1, 'Feel': 1, 'free': 1, 'to': 2, 'customize': 1, 'or': 1, 'expand': 1, 'this': 1, 'text': 1, 'test': 1, 'additional': 1, 'cases.': 1}

### Final Consolidated Word Frequencies:
{'Multithreading': 1, 'is': 3, 'a': 3, 'concept': 1, 'that': 1, 'allows': 1, 'program': 1, 'to': 4, 'run': 1, 'multiple': 1, 'threads': 1, 'concurrently.': 1, 'Each': 1, 'thread': 1, 'smaller': 1, 'unit': 1, 'of': 1, 'process,': 1, 'enabling': 1, 'parallelism': 1, 'and': 1, 'improving': 1, 'performance.': 1, 'This': 1, 'text': 2, 'used': 1, 'test': 2, 'the': 1, 'multithreading': 1, 'word': 1, 'frequency': 1, 'counting': 1, 'program.': 1, 'Feel': 1, 'free': 1, 'customize': 1, 'or': 1, 'expand': 1, 'this': 1, 'additional': 1, 'cases.': 1}

## Instructions to Compile and Run
1. Place the script `multithreading_word_frequency.py` and the text file in the same directory.
2. Run the script using the command: `python3 multithreading_word_frequency.py <file_path> <num_segments>`.
3. Replace `<file_path>` with the path to your text file and `<num_segments>` with the desired number of segments.

## Notes
Ensure that Python 3 and necessary permissions are available for execution.
