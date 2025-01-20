import threading  # Enables multithreading for concurrent execution
from collections import Counter  # Facilitates word frequency counting
import os  # Provides functionality for file and path operations

def read_file(file_path):
    # Reads the content of the specified file and returns it as a string
    with open(file_path, 'r') as file:
        return file.read()

def segment_text(text, num_segments):
    # Splits the text into a specified number of segments for parallel processing
    words = text.split()  # Tokenize text into words
    segment_size = len(words) // num_segments  # Determine size of each segment
    segments = []
    for i in range(num_segments):
        start = i * segment_size  # Start index for the segment
        # Adjust the end index for the last segment to include any remaining words
        end = start + segment_size if i != num_segments - 1 else len(words)
        segments.append(words[start:end])  # Add the segment to the list
    return segments

def count_words(segment, results, index, lock):
    # Counts word frequencies in a segment and safely stores the result
    word_count = Counter(segment)  # Count word occurrences in the segment
    with lock:  # Acquire lock for thread-safe access to shared resources
        results[index] = word_count

def consolidate_results(results):
    # Combines word counts from all segments into a single final count
    final_count = Counter()  # Initialize an empty Counter
    for count in results:
        final_count.update(count)  # Merge individual segment counts
    return final_count

def main(file_path, num_segments):
    # Main function to orchestrate file reading, segmentation, and multithreading

    # Step 1: Read file and segment text
    text = read_file(file_path)  # Load the file's content
    segments = segment_text(text, num_segments)  # Divide text into segments

    # Step 2: Set up shared resources for thread-safe operations
    results = [None] * num_segments  # Placeholder for thread results
    lock = threading.Lock()  # Lock for synchronizing threads

    # Step 3: Create and start threads
    threads = []
    for i in range(num_segments):
        # Create a thread for counting words in a segment
        thread = threading.Thread(target=count_words, args=(segments[i], results, i, lock))
        threads.append(thread)
        thread.start()  # Start the thread

    # Step 4: Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Step 5: Consolidate results from all threads
    consolidated_count = consolidate_results(results)

    # Step 6: Output results
    print("Intermediate Word Frequencies:")
    for i, count in enumerate(results):
        print(f"Segment {i + 1}: {dict(count)}")

    print("\nFinal Consolidated Word Frequencies:")
    print(dict(consolidated_count))

if __name__ == "__main__":
    import argparse  # Facilitates command-line argument parsing

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Multithreaded Word Frequency Counter")
    parser.add_argument("file_path", type=str, help="Path to the text file")
    parser.add_argument("num_segments", type=int, help="Number of segments to divide the file into")
    args = parser.parse_args()

    # Validate file path and execute the program
    if not os.path.exists(args.file_path):
        print("Error: File not found.")
    else:
        main(args.file_path, args.num_segments)
