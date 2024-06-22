'''
Counter is a subclass of dict that’s specially designed for counting 
hashable objects in Python. It’s a dictionary that stores objects as 
keys and counts as values. 
To count with Counter, you typically provide a sequence or iterable 
of hashable objects as an argument to the class’s constructor.

    * Counter internally iterates through the input sequence, counts 
        the number of times a given object occurs, and stores objects 
        as keys and the counts as values.
'''
from collections import Counter, deque

#Counter demo
def counter_demo() -> Counter:
    lst = [1,2,2,2,2,3,3,3,1,2,1,12,3,2,32,1,21,1,223,1]
    counter_obj = Counter(lst)
    return counter_obj

#demo of word count in a sentence
def word_count_demo(sentence : str) -> Counter:
    #initialize the list
    words = sentence.split()
    word_counter_obj = Counter(words)

    return word_counter_obj

#demo of counter as shopping cart




def test_classes():
    #Demo of counter object
    counter_obj = counter_demo()
    print(f"counter obj is : {counter_obj}")

    #Demo of word counter
    #seek string input
    sentence = input("Enter the sentence : ")
    word_counter = word_count_demo(sentence)
    print(f"word counter is {word_counter}")
    print(f"Most common word is : {word_counter.most_common(5)}")


if __name__ == "__main__":
    test_classes()