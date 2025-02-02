from Vector import Vector as vec

vectors = []
user_input = ''
while True:
    print(f"Amount of created vectors: {len(vectors)}")
    for v in range(len(vectors)):
        print(f"{v+1}. {vectors[v]}")
    print("Choose a command:\n"
          "Create a vector: create [Ax] [Ay] [Bx] [By]\n"
          "Summarize vectors: sum [v1] [v2] ... \n"
          "Scalar multiplication for vectors: mult [v1] [v2]\n"
          "Multiply vector by number: multn [v] [num]\n"
          "Subtract vectors: sub [v1] [v2]\n"
          "Remove vectors: rm [v1] [v2] ...\n"
          "Display vector length: len [v]\n"
          "Clear all: clear\n"
          "Exit: exit\n")
    user_input = input()
    command = user_input.split()[0]
    args = user_input.split()[1:]

    match command:
        case 'create':
            if len(args) != 4:
                raise ValueError(f"Expected 4 arguments, got {len(args)}")

            coordinates = []
            for i in range(4):
                coordinates.append(float(args[i]))

            p1 = (coordinates[0], coordinates[1])
            p2 = (coordinates[2], coordinates[3])
            vector = vec(p1, p2)
            vectors.append(vector)

        case 'sum':
            for i in args:
                if int(i)<1 or int(i)>len(vectors):
                    raise ValueError(f"Vector {i} doesn't exist")

            result = vectors[int(args[0])-1]
            for i in range(1, len(args)):
                result+=vectors[int(args[i])-1]
            print("result:", result)
            user_input = input("Add result to vectors list? y/N:")
            if user_input == "y" or user_input == "Y":
                vectors.append(result)

        case 'mult':
            if len(args) != 2:
                raise ValueError(f"Expected 2 arguments, got {len(args)}")
            for i in args:
                if int(i) < 1 or int(i) > len(vectors):
                    raise ValueError(f"Vector {i} doesn't exist")

            result = vectors[int(args[0])-1]*vectors[int(args[1])-1]
            print("result:", result)

        case 'multn':
            if len(args) != 2:
                raise ValueError(f"Expected 2 arguments, got {len(args)}")
            if int(args[0]) < 1 or int(args[0]) > len(vectors):
                raise ValueError(f"Vector {args[0]} doesn't exist")
            result = vectors[int(args[0])-1].multiply_by_number(float(args[1]))
            print("result:", result)
            user_input = input("Add result to vectors list? y/N:")
            if user_input == "y" or user_input == "Y":
                vectors.append(result)

        case 'sub':
            if len(args) != 2:
                raise ValueError(f"Expected 2 arguments, got {len(args)}")
            for i in range(2):
                if int(args[i]) < 1 or int(args[i]) > len(vectors):
                    raise ValueError(f"Vector {args[i]} doesn't exist")

            result = vectors[int(args[0])-1] - vectors[int(args[1])-1]
            print("result:", result)
            user_input = input("Add result to vectors list? y/N:")
            if user_input == "y" or user_input == "Y":
                vectors.append(result)

        case 'rm':
            for i in args:
                if int(i) < 1 or int(i) > len(vectors):
                    raise ValueError(f"Vector {i} doesn't exist")
            new_vectors=[]
            for i in range(len(vectors)):
                if str(i+1) not in args:
                    new_vectors.append(vectors[i])
            vectors=new_vectors

        case 'len':
            if len(args) != 1:
                raise ValueError(f"Expected 1 arguments, got {len(args)}")
            if int(args[0]) < 1 or int(args[0]) > len(vectors):
                raise ValueError(f"Vector {args[0]} doesn't exist")
            print(f"Length of vector {args[0]}: {vectors[int(args[0])-1].get_length()}")

        case 'clear':
            vectors=[]

        case 'exit':
            break

        case _:
            print("Unknown command!")