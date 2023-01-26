
def get_vowels(string):
    vowels = "aeiou"
    result = [each for each in string if each.lower() in vowels]
    return result

def get_consonants(string):
    consonants = "bcdfghjklmnpqrstvwxyz"
    result = [each for each in string if each.lower() in consonants]
    return result


string = input("Enter a string: ")

operation = input(
    '''\n Enter operation number
    1. Sort the string
    2. Count the elements number
    3. Output vowels
    4. Output consonants
    5. Output the words in reverse order
    6. Output the original string
    7. Any other input will exit the program.\n ''')

match operation:
	case '1':
		print("Sorted string: " + str(sorted(string)))
	case '2':
		print("String length: " + str(len(string)))
	case '3':
		print("Vowels: " + str(get_vowels(string)))
	case '4':
		print("Consonants: " + str(get_consonants(string)))
	case '5':
		reversed = reversed(string.split (" "))
		print("String words in reverse order: ")
		print([each for each in reversed])
	case '6':
		print("Original string: " + string)