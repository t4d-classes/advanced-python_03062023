person = { "fn": "Bob", "ln": "Smith" }
person_secure = { "ssn": "333-33-3333" }

full_person = { **person, **person_secure }

# print(full_person)

# print(list(full_person))
# print(*full_person)

# does not work
# print(**full_person)
