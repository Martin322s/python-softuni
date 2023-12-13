number_messages = int(input())
message_88 = "Hello"
message_86 = "How are you?"
message_over_88 = ""
message_diff_86_88 = ""

for _ in range(number_messages):
    message = int(input())

    if message > 88:
        message_over_88 = "Bye."

    if (message != 88 and message != 86) and message <= 88:
        message_diff_86_88 = "GREAT!"

    if message == 88:
        print(message_88)
    elif message == 86:
        print(message_86)
    elif (message != 88 and message != 86) and message <= 88:
        print(message_diff_86_88)
    else:
        print(message_over_88)
