
result = 0.0
history = []


while True:

    command = input("Enter a command:")

    if command == "add":

        operand = float(input("Please enter an operand:"))
        result = result + operand

        next_id = 1
        if history:
            next_id = max([ entry["id"] for entry in history ]) + 1

        history.append({
            "id": next_id,
            "opName": "add",
            "opValue": operand
        })

        print(result)   


    elif command == "subtract":

        operand = float(input("Please enter an operand:"))
        result = result - operand

        next_id = 1
        if history:
            next_id = max([ entry["id"] for entry in history ]) + 1

        history.append({
            "id": next_id,
            "opName": "subtract",
            "opValue": operand
        })

        print(result)   


    elif command == "multiply":

        operand = float(input("Please enter an operand:"))
        result = result * operand

        next_id = 1
        if history:
            next_id = max([ entry["id"] for entry in history ]) + 1

        history.append({
            "id": next_id,
            "opName": "multiply",
            "opValue": operand
        })

        print(result)   
      

    elif command == "divide":

        operand = float(input("Please enter an operand:"))
        result = result / operand

        next_id = 1
        if history:
            next_id = max([ entry["id"] for entry in history ]) + 1

        history.append({
            "id": next_id,
            "opName": "divide",
            "opValue": operand
        })

        print(result)   

    elif command == "exponent":

        operand = float(input("Please enter an operand:"))
        result = result ** operand

        next_id = 1
        if history:
            next_id = max([ entry["id"] for entry in history ]) + 1

        history.append({
            "id": next_id,
            "opName": "exponent",
            "opValue": operand
        })

        print(result)   


    elif command == "exit":
        break
    else:
        print("Invalid Command, Try Again")
        continue

