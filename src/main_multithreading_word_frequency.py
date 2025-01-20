
import threading
from collections import Counter
import os

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def segment_text(text, num_segments):
    words = text.split()
    segment_size = len(words) // num_segments
    segments = []
    for i in range(num_segments):
        start = i * segment_size
        # Include remainder words in the last segment
        end = start + segment_size if i != num_segments - 1 else len(words)
        segments.append(words[start:end])
    return segments

def count_words(segment, results, index, lock):
    word_count = Counter(segment)
    with lock:
        results[index] = word_count

def consolidate_results(results):
    final_count = Counter()
    for count in results:
        final_count.update(count)
    return final_count

def main(file_path, num_segments):
    # Read file and segment text
    text = read_file(file_path)
    segments = segment_text(text, num_segments)

    # Shared resources for thread-safe communication
    results = [None] * num_segments
    lock = threading.Lock()

    # Create and start threads
    threads = []
    for i in range(num_segments):
        thread = threading.Thread(target=count_words, args=(segments[i], results, i, lock))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Consolidate results
    consolidated_count = consolidate_results(results)

    # Output results
    print("Intermediate Word Frequencies:")
    for i, count in enumerate(results):
        print(f"Segment {i + 1}: {dict(count)}")

    print("\nFinal Consolidated Word Frequencies:")
    print(dict(consolidated_count))

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Multithreaded Word Frequency Counter")
    parser.add_argument("file_path", type=str, help="Path to the text file")
    parser.add_argument("num_segments", type=int, help="Number of segments to divide the file into")
    args = parser.parse_args()

    if not os.path.exists(args.file_path):
        print("Error: File not found.")
    else:
        main(args.file_path, args.num_segments)
