def oxford_comma(items):
    # Check if the input list is empty
    if not items:
        return ""
    
    # If there is only one item, return it as a string
    if len(items) == 1:
        return items[0]

    # If there are two items, join them with "and"
    elif len(items) == 2:
        return f"{items[0]} and {items[1]}"

    # If there are three or more items, use commas and add "and" before the last item
    else:
        oxford_string = ", ".join(items[:-1])  # Join all but the last item with commas
        oxford_string += f", and {items[-1]}"  # Add "and" before the last item
        return oxford_string

# Test cases
result1 = oxford_comma(["KIWI"])
print(result1)

result2 = oxford_comma(["kiwi", "durian"])
print(result2)

result3 = oxford_comma(["kiwi", "durian", "starfruit"])
print(result3)
