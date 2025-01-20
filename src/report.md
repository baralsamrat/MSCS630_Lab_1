
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

## 1. Program Design and Structure

The program is designed with modularity and clarity in mind, enabling efficient text processing and multithreading. The key components of the program are:

- **`read_file`**: Reads the contents of the specified text file into memory as a single string.
- **`segment_text`**: Divides the input text into a specified number of segments to allow parallel processing by multiple threads.
- **`count_words`**: Uses Python's `Counter` from the `collections` module to calculate word frequencies for a given text segment.
- **`consolidate_results`**: Merges the word frequency counts from all threads into a single `Counter` object.
- **`main`**: Orchestrates the overall workflow, including reading the file, segmenting the text, initializing threads, and consolidating results.

The use of modular functions enhances the maintainability and readability of the code. Each function focuses on a specific task, ensuring separation of concerns.

## 2. Logic for File Segmentation and Word Counting

The input file is divided into segments to enable concurrent processing. The segmentation logic ensures that:

- The words are evenly distributed across segments, calculated based on the total number of words and the desired number of segments.
- Any remaining words (when the total word count is not perfectly divisible by the number of segments) are included in the last segment.

This approach minimizes imbalance in workload across threads, ensuring efficient use of computational resources. Each thread processes its assigned segment independently, computing word frequencies.

## 3. Multithreading Implementation and Key Challenges

Multithreading was implemented using Python's `threading` module. The implementation details include:

- **Thread Creation**: A separate thread is created for processing each text segment. The threads execute the `count_words` function concurrently.
- **Shared Resources**: A shared list, `results`, stores the word frequencies computed by each thread. A threading lock (`threading.Lock`) ensures that updates to the shared list are thread-safe.

### Challenges Encountered

1. **Thread Synchronization**: Ensuring thread-safe access to shared resources required careful use of locks to avoid data races.
2. **Overhead**: While multithreading improved performance for large inputs, the overhead associated with thread management slightly impacted performance for smaller inputs.
3. **Error Handling**: Validating input parameters (e.g., file existence and number of segments) and handling exceptions was critical to avoid runtime errors.
 
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
1. Place the script `main_multithreading_word_frequency.py` and the text file in the same directory.
2. Run the script using the command: `python3 main_multithreading_word_frequency.py <file_path> <num_segments>`.
3. Replace `<file_path>` with the path to your text file and `<num_segments>` with the desired number of segments.

## Notes
Ensure that Python 3 and necessary permissions are available for execution.
