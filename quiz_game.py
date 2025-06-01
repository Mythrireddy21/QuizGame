import random
import time
import threading
import sys

quiz_data = {
    "C": {
        "Easy": [
            {"question": "Who is the father of C language?", "options": ["Dennis Ritchie", "Bjarne Stroustrup", "James Gosling", "Guido van Rossum"], "answer": "Dennis Ritchie"},
            {"question": "Which of the following is a valid C variable name?", "options": ["int", "float", "my_var", "main"], "answer": "my_var"},
            {"question": "Which operator is used to assign a value to a variable?", "options": ["=", "==", ":", "->"], "answer": "="},
            {"question": "What is the correct file extension for C programs?", "options": [".c", ".cpp", ".java", ".py"], "answer": ".c"},
        ],
        "Medium": [
            {"question": "Which of the following is not a loop structure in C?", "options": ["for", "while", "do-while", "repeat-until"], "answer": "repeat-until"},
            {"question": "What is the size of an int data type in C (on a 32-bit system)?", "options": ["2 bytes", "4 bytes", "8 bytes", "Depends on the system"], "answer": "4 bytes"},
            {"question": "Which function is used to read a formatted input in C?", "options": ["scanf()", "printf()", "gets()", "puts()"], "answer": "scanf()"},
            {"question": "What is the output of: printf(\"%d\", (5 + 2 * 3));", "options": ["11", "21", "16", "13"], "answer": "11"},
            {"question": "Which header file is required for using printf() function?", "options": ["stdio.h", "conio.h", "stdlib.h", "string.h"], "answer": "stdio.h"},
            {"question": "Which keyword is used to prevent modification of a variable?", "options": ["const", "volatile", "static", "register"], "answer": "const"},
        ],
        "Hard": [
            {"question": "What is a dangling pointer in C?", "options": ["Pointer pointing to NULL", "Pointer pointing to freed memory", "Pointer not initialized", "None"], "answer": "Pointer pointing to freed memory"},
            {"question": "What is the scope of a static variable inside a function?", "options": ["Global", "Local to block", "Local to function", "Shared"], "answer": "Local to function"},
            {"question": "What is a function pointer in C?", "options": ["A pointer to int", "A pointer to float", "A pointer to a function", "None"], "answer": "A pointer to a function"},
            {"question": "What is sizeof('A') in C?", "options": ["1", "2", "4", "8"], "answer": "1"},
            {"question": "What is the output of printf(\"%c\", 65);", "options": ["65", "A", "a", "error"], "answer": "A"},
            {"question": "What is the default return type of main() in C?", "options": ["int", "void", "char", "float"], "answer": "int"},
            {"question": "Which is valid syntax to declare a variable in C?", "options": ["int num(10);", "int num = 10;", "int num : 10;", "int num <- 10;"], "answer": "int num = 10;"},
            {"question": "What is a segmentation fault?", "options": ["Memory leak", "Divide by zero", "Accessing restricted memory", "Overwriting data"], "answer": "Accessing restricted memory"},
            {"question": "What will sizeof(int*) return?", "options": ["4", "2", "Size of pointer", "Size of int"], "answer": "Size of pointer"},
            {"question": "Which of these is a preprocessor directive in C?", "options": ["#include", "#define", "#ifdef", "All of these"], "answer": "All of these"},
        ],
    },
    "C++": {
        "Easy": [
            {"question": "Who developed C++?", "options": ["Dennis Ritchie", "Bjarne Stroustrup", "James Gosling", "Guido van Rossum"], "answer": "Bjarne Stroustrup"},
            {"question": "Which of the following is a valid C++ variable name?", "options": ["int", "float", "myVar", "main"], "answer": "myVar"},
            {"question": "Which operator is used to assign a value to a variable in C++?", "options": ["=", "==", ":", "->"], "answer": "="},
            {"question": "What is the correct file extension for C++ programs?", "options": [".c", ".cpp", ".java", ".py"], "answer": ".cpp"},
        ],
        "Medium": [
            {"question": "Which of the following is not a loop structure in C++?", "options": ["for", "while", "do-while", "repeat-until"], "answer": "repeat-until"},
            {"question": "What is the size of an int data type in C++ (on a 32-bit system)?", "options": ["2 bytes", "4 bytes", "8 bytes", "Depends on the system"], "answer": "4 bytes"},
            {"question": "Which function is used to read input in C++?", "options": ["cin", "scanf", "gets", "input"], "answer": "cin"},
            {"question": "What is the output of: cout << (5 + 2 * 3);", "options": ["11", "21", "16", "13"], "answer": "11"},
            {"question": "Which header file is required for using cout in C++?", "options": ["iostream", "stdio.h", "stdlib.h", "string.h"], "answer": "iostream"},
            {"question": "Which keyword is used to prevent modification of a variable in C++?", "options": ["const", "volatile", "static", "register"], "answer": "const"},
        ],
        "Hard": [
            {"question": "What is a dangling pointer in C++?", "options": ["Pointer pointing to NULL", "Pointer pointing to freed memory", "Pointer not initialized", "None"], "answer": "Pointer pointing to freed memory"},
            {"question": "What is the scope of a static variable inside a function in C++?", "options": ["Global", "Local to block", "Local to function", "Shared"], "answer": "Local to function"},
            {"question": "What is a function pointer in C++?", "options": ["A pointer to int", "A pointer to float", "A pointer to a function", "None"], "answer": "A pointer to a function"},
            {"question": "What is sizeof('A') in C++?", "options": ["1", "2", "4", "8"], "answer": "1"},
            {"question": "What is the output of cout << char(65);", "options": ["65", "A", "a", "error"], "answer": "A"},
            {"question": "What is the default return type of main() in C++?", "options": ["int", "void", "char", "float"], "answer": "int"},
            {"question": "Which is valid syntax to declare a variable in C++?", "options": ["int num(10);", "int num = 10;", "int num : 10;", "int num <- 10;"], "answer": "int num = 10;"},
            {"question": "What is a segmentation fault in C++?", "options": ["Memory leak", "Divide by zero", "Accessing restricted memory", "Overwriting data"], "answer": "Accessing restricted memory"},
            {"question": "What will sizeof(int*) return in C++?", "options": ["4", "2", "Size of pointer", "Size of int"], "answer": "Size of pointer"},
            {"question": "Which of these is a preprocessor directive in C++?", "options": ["#include", "#define", "#ifdef", "All of these"], "answer": "All of these"},
        ],
    },
    "Python": {
        "Easy": [
            {"question": "What keyword is used to define a function in Python?", "options": ["fun", "define", "def", "func"], "answer": "def"},
            {"question": "What symbol is used to comment a line in Python?", "options": ["//", "#", "/*", "<!--"], "answer": "#"},
            {"question": "What is the correct file extension for Python files?", "options": [".pyth", ".pt", ".py", ".pyt"], "answer": ".py"},
            {"question": "Which operator is used for exponentiation in Python?", "options": ["^", "**", "%", "//"], "answer": "**"},
        ],
        "Medium": [
            {"question": "Which of the following is used to create a list in Python?", "options": ["{}", "()", "[]", "<>"], "answer": "[]"},
            {"question": "What does the 'len()' function do in Python?", "options": ["Returns length", "Returns type", "Returns value", "Returns max"], "answer": "Returns length"},
            {"question": "Which keyword is used for exception handling in Python?", "options": ["catch", "try", "except", "handle"], "answer": "try"},
            {"question": "What is the output of: print(type(3.14))?", "options": ["int", "float", "double", "string"], "answer": "float"},
            {"question": "Which function converts a string to an integer in Python?", "options": ["int()", "str()", "float()", "convert()"], "answer": "int()"},
            {"question": "What is the output of: print(3 // 2)?", "options": ["1", "1.5", "2", "0"], "answer": "1"},
        ],
        "Hard": [
            {"question": "What is a lambda function in Python?", "options": ["Anonymous function", "Recursive function", "Decorator", "Class"], "answer": "Anonymous function"},
            {"question": "What does the 'map()' function do?", "options": ["Applies a function to all items", "Maps one list to another", "Creates a dictionary", "Filters a list"], "answer": "Applies a function to all items"},
            {"question": "What will be the output of: print(list(range(1, 10, 3)))?", "options": ["[1,4,7]", "[1,3,6,9]", "[1,4,7,10]", "[3,6,9]"], "answer": "[1,4,7]"},
            {"question": "What does the 'yield' keyword do in Python?", "options": ["Returns a generator", "Returns a value", "Stops function", "Raises exception"], "answer": "Returns a generator"},
            {"question": "Which module in Python supports regular expressions?", "options": ["regex", "re", "pyregex", "expression"], "answer": "re"},
            {"question": "What is a Python decorator?", "options": ["Function that modifies another function", "A type of loop", "A variable type", "A keyword"], "answer": "Function that modifies another function"},
            {"question": "What will be the output of: print([i*i for i in range(3)])?", "options": ["[1,4,9]", "[0,1,4]", "[0,1,4,9]", "[0,1,2]"], "answer": "[0,1,4]"},
            {"question": "What does 'PEP' stand for in Python?", "options": ["Python Enhancement Proposal", "Programming Environment Python", "Python Encrypted Protocol", "Program Execution Plan"], "answer": "Python Enhancement Proposal"},
            {"question": "Which of these is not a Python data structure?", "options": ["List", "Tuple", "Set", "Tree"], "answer": "Tree"},
            {"question": "Which statement is used to handle exceptions?", "options": ["try-except", "catch", "handle", "throw"], "answer": "try-except"},
        ],
    },
    "Java": {
        "Easy": [
            {"question": "Who developed Java?", "options": ["James Gosling", "Bjarne Stroustrup", "Dennis Ritchie", "Guido van Rossum"], "answer": "James Gosling"},
            {"question": "What is the file extension for Java files?", "options": [".java", ".class", ".jar", ".jv"], "answer": ".java"},
            {"question": "Which keyword is used to define a class in Java?", "options": ["class", "def", "function", "struct"], "answer": "class"},
            {"question": "What is the main method signature in Java?", "options": ["public static void main(String[] args)", "void main()", "main()", "public void main()"], "answer": "public static void main(String[] args)"},
        ],
        "Medium": [
            {"question": "Which of the following is not a Java keyword?", "options": ["static", "Boolean", "void", "private"], "answer": "Boolean"},
            {"question": "What does JVM stand for?", "options": ["Java Virtual Machine", "Java Variable Method", "Java Visual Model", "Java Verified Module"], "answer": "Java Virtual Machine"},
            {"question": "What is inheritance in Java?", "options": ["Using parent class properties", "Data hiding", "Polymorphism", "Encapsulation"], "answer": "Using parent class properties"},
            {"question": "Which method is used to start a thread in Java?", "options": ["start()", "run()", "init()", "execute()"], "answer": "start()"},
            {"question": "What is the size of an int data type in Java?", "options": ["2 bytes", "4 bytes", "8 bytes", "Depends on JVM"], "answer": "4 bytes"},
            {"question": "Which keyword is used to prevent modification of a variable in Java?", "options": ["final", "const", "static", "volatile"], "answer": "final"},
        ],
        "Hard": [
            {"question": "What is the difference between an interface and an abstract class?", "options": ["Interface has no implementation", "Abstract class can have implemented methods", "A and B", "None"], "answer": "A and B"},
            {"question": "What is a Java package?", "options": ["Namespace", "Class", "Object", "Method"], "answer": "Namespace"},
            {"question": "What does the 'volatile' keyword do in Java?", "options": ["Ensures visibility across threads", "Declares constants", "Declares variables", "None"], "answer": "Ensures visibility across threads"},
            {"question": "What is a singleton class in Java?", "options": ["Class with single instance", "Class with multiple instances", "Class with static methods", "None"], "answer": "Class with single instance"},
            {"question": "What is method overloading?", "options": ["Multiple methods with same name but different parameters", "Multiple methods with same name and parameters", "Overriding methods", "None"], "answer": "Multiple methods with same name but different parameters"},
            {"question": "What is the default value of a boolean variable in Java?", "options": ["true", "false", "null", "0"], "answer": "false"},
            {"question": "What is the use of the 'super' keyword?", "options": ["Access parent class members", "Access child class members", "Declare variables", "None"], "answer": "Access parent class members"},
            {"question": "What is the use of 'try-catch' block in Java?", "options": ["Handle exceptions", "Define methods", "Declare variables", "None"], "answer": "Handle exceptions"},
            {"question": "What is the output of 'System.out.println(10 + 20 + \"30\")'?", "options": ["3030", "102030", "30", "None"], "answer": "3030"},
            {"question": "Which of the following is a checked exception in Java?", "options": ["IOException", "NullPointerException", "ArithmeticException", "ArrayIndexOutOfBoundsException"], "answer": "IOException"},
        ],
    },
}


timeout_flag = False
input_received = False


def countdown(seconds):
    global timeout_flag, input_received
    for remaining in range(seconds, 0, -1):
        if timeout_flag or input_received:
            break
        # Update timer in-place
        sys.stdout.write(f"\r⏳ Time left: {remaining:2}s  ")
        sys.stdout.flush()
        time.sleep(1)
    else:
        if not input_received:
            timeout_flag = True
            sys.stdout.write("\r⏰ Time's up! No answer recorded.      \n")
            sys.stdout.flush()

def combined_quiz(subject):
    global timeout_flag, input_received
    all_questions = []

    for difficulty, questions in quiz_data[subject].items():
        for q in questions:
            q_copy = q.copy()
            q_copy['difficulty'] = difficulty
            all_questions.append(q_copy)

    random.shuffle(all_questions)
    print(f"\n🎯 Starting quiz on '{subject}' with {len(all_questions)} questions.\n")

    correct = 0
    user_answers = []

    for idx, q in enumerate(all_questions, 1):
        print(f"\nQ{idx} [{q['difficulty']}]: {q['question']}")
        for i, opt in enumerate(q['options'], 1):
            print(f"  {i}. {opt}")

        timeout_flag = False
        input_received = False
        answer = None

        timer_thread = threading.Thread(target=countdown, args=(15,))
        timer_thread.daemon = True
        timer_thread.start()

        while not timeout_flag:
            try:
                # Print input prompt on a new line (timer is on previous line)
                user_input = input("\nYour answer (enter option number): ").strip()
                if user_input.isdigit() and 1 <= int(user_input) <= len(q['options']):
                    answer = q['options'][int(user_input) - 1]
                    input_received = True
                    timeout_flag = True
                    break
                else:
                    print("⚠️ Invalid input. Please enter a valid option number.")
            except EOFError:
                # In case of input interruption
                timeout_flag = True
                break

        timer_thread.join()

        if not answer:
            selected = "No Answer"
            is_correct = False
            print(f"❌ Wrong! Correct answer: {q['answer']}\n")
        else:
            selected = answer
            is_correct = (selected == q['answer'])
            print("✅ Correct!\n" if is_correct else f"❌ Wrong! Correct answer: {q['answer']}\n")

        if is_correct:
            correct += 1

        user_answers.append({
            'question': q['question'],
            'difficulty': q['difficulty'],
            'your_answer': selected,
            'correct_answer': q['answer'],
            'correct': is_correct
        })

    total = len(all_questions)
    incorrect = total - correct
    percent = (correct / total) * 100
    emoji = "🎉" if percent >= 80 else "🙂" if percent >= 50 else "😢"

    print(f"\n🎉 Quiz Complete! You scored {correct} out of {total}.")
    print("\n📊 Quiz Summary:")
    print(f"  ✅ Correct: {correct}")
    print(f"  ❌ Incorrect: {incorrect}")
    print(f"  📈 Score: {percent:.2f}% {emoji}")

    while True:
        view = input("\n🔍 Do you want to see all answers? (y/n): ").strip().lower()
        if view == 'y':
            for i, ans in enumerate(user_answers, 1):
                print(f"\nQ{i} [{ans['difficulty']}]: {ans['question']}")
                print(f"  Your answer: {ans['your_answer']}")
                print(f"  Correct answer: {ans['correct_answer']}")
                print(f"  {'✅ Correct' if ans['correct'] else '❌ Wrong'}")
            break
        elif view == 'n':
            break
        else:
            print("Please enter y or n.")

    while True:
        replay = input("\n🔁 Play again (p) or change subject (c) or exit (e)? ").strip().lower()
        if replay == 'p':
            return combined_quiz(subject)
        elif replay == 'c':
            return main_menu()
        elif replay == 'e':
            print("👋 Thank you for playing!")
            exit()
        else:
            print("Please enter p, c, or e.")

def main_menu():
    print("\n📚 Available Subjects:")
    for idx, subj in enumerate(quiz_data.keys(), 1):
        print(f"  {idx}. {subj}")
    while True:
        choice = input("\nChoose subject number to start quiz: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(quiz_data):
            subject = list(quiz_data.keys())[int(choice) - 1]
            combined_quiz(subject)
            break
        else:
            print("Invalid input. Try again.")

if __name__ == "__main__":
    main_menu()
