def valid_parentheses(string):
    count = string.count('(') == string.count(')')
    if count == False: return False
    paren_list = list(filter(lambda x: x == '(' or x == ')', string))
    closing_parent_indices = [i for i, v in enumerate(paren_list) if v == ')']
    opening_parent_indices = [i for i, v in enumerate(paren_list) if v == '(']
    for n in closing_parent_indices:
        if '(' in paren_list[:n]:
            paren_list[opening_parent_indices[0]] = ''
            opening_parent_indices.pop(0)
        else:
            return False
    return True
