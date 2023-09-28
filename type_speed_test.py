import time

def speed_typing_test():
    sentence = "cat or dog, what do you prefer?"
    print("Type the following sentence as fast as you can:")
    print(sentence)
    
    input("Press Enter when you are ready to start...")
    start_time = time.time()

    user_input = input("\nStart typing here: ")

    end_time = time.time()
    time_taken = end_time - start_time

    if user_input == sentence:
        print(f"\nCorrect! You took {time_taken:.2f} seconds.")
    else:
        print("\nThe sentence you typed does not match the given sentence. Please try again.")

if __name__ == "__main__":
    speed_typing_test()
