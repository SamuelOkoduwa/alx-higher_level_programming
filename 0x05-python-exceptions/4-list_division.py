#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            # Check if lists are too short
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            
            # Perform division
            quotient = my_list_1[i] / my_list_2[i]
        
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        
        except IndexError as e:
            print(e)
            result.append(0)
        
        except TypeError:
            print("wrong type")
            result.append(0)
        
        else:
            result.append(quotient)
        
        finally:
            pass
    
    return result

'''
# Sample test based on the example given
my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)
'''