# Question ---> Given a string  , repeat the characters as given in the precending character 

def repeat_characters(input_string):
    result = []
    i = 0
    while i < len(input_string):
        
        if input_string[i].isdigit():
            repeat_count = int(input_string[i])
            i += 1
            if i < len(input_string):

                result.append(input_string[i] * repeat_count)
        else:
            result.append(input_string[i])
        i += 1
    return ''.join(result)

# Example usage
input_string = "3a2b1c4Q"
output_string = repeat_characters(input_string)
print(output_string)  # Output: "aaabbcQQQQ"
