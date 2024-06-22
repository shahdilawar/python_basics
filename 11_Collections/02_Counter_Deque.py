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

'''
* Deque was specially designed to overcome the efficiency problems of 
    .append() and .pop() in Python list.
* Append and pop operations on both ends of a deque object are stable 
    and equally efficient because deques are implemented as a 
    doubly linked list. 
* Additionally, append and pop operations on deques are also thread 
    safe and memory efficient. 
* Deques are also the way to go if you need to keep a list of 
    last-seen items because you can restrict the maximum length of 
    your deques
'''
def deque_demo():
    # Use .append methods for enqueing.
    customers = deque()

    # people arriving to restaurant    
    customers.append("Jane")
    customers.append("Raja")
    customers.append("Nayak")

    #Customers waiting in queue
    print(f"Customers waiting in queue : {customers}")
    # people getting tables
    for i in range(len(customers)):
        print(f"Customer getting table is : {customers.popleft()}")


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

    #Simple Deque demo
    deque_demo()


if __name__ == "__main__":
    test_classes()