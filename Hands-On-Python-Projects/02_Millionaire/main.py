questions = [["1. What is the capital of France?","Berlin","Paris","London","Rome",1], 
             ["2. Which planet is known as the 'Red Planet'?","Earth","Mars","Jupiter","Saturn",1], 
             ["3. Who is the author of the book 'To Kill a Mockingbird'?","F. Scott Fitzgerald","Harper Lee","Jane Austen","J.K. Rowling",1], 
             ["4. What is the chemical symbol for gold?","Ag","Au","Hg","Pb",1], 
             ["5. Which Indian state is known as the 'Land of Five Rivers'?","Punjab","Haryana","Uttar Pradesh","Bihar",0], 
             ["6. Who is the founder of Microsoft?","Bill Gates","Steve Jobs","Mark Zuckerberg","Larry Page",0], 
             ["7. What is the largest mammal on Earth?","Elephant","Blue whale","Lion","Giraffe",1], 
             ["8. Which river is the longest in South America?","Amazon River","Paraná River","São Francisco River","Magdalena River",0], 
             ["9. Who painted the famous artwork 'The Starry Night'?","Leonardo da Vinci","Vincent van Gogh","Pablo Picasso","Claude Monet",1], 
             ["10. What is the smallest country in the world, both in terms of population and land area?","Vatican City","Monaco","Nauru","Tuvalu",0]]

score = 0

for question in questions:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    # check whether the answer is correct or not.
    a = int(input("Enter your answer. 0 for a, 1 for b, 2 for c, 3 for d: "))
    if (question[5] == a):
        print("Correct Answer\n")
        score += 1
    else:
        print(f"Incorrect, the correct answer was {['a', 'b', 'c', 'd'][question[5]]}\n")

print(f"Quiz finished. Your final score is {score} out of {len(questions)}")