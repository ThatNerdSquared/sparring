import sys

def combine_classes(classes, greatest_value, procedures):
    stripped = list(filter(lambda x: x != greatest_value, classes))
    if len(stripped) == 0:
        print(0)
    elif len(stripped) < 2:
        procedures += 1
        print(procedures)
    else:
        for class_idx in range(len(classes)):
            if class_idx+1 < len(classes):
                if classes[class_idx] < greatest_value and classes[class_idx + 1] < greatest_value:
                    classes[class_idx] = classes[class_idx] + classes[class_idx + 1]
                    classes.pop(class_idx+1)
                    procedures +=1
        if len(classes) > 1 and len(set(classes)) != 1:
            combine_classes(classes, max(classes), procedures)
        else:
            print(procedures)



listed_input = list(sys.stdin)
TOTAL = 0
cases = {}

previous_number = ''
for idx in range(len(listed_input)):
    if idx == 0:
        TOTAL = int(listed_input[idx])
    else:
        if idx % 2:
            previous_number = listed_input[idx].rstrip()
        else:
            cases[previous_number] = [int(x.rstrip()) for x in listed_input[idx].split()]
            previous_number = ''

for item in cases:
    classes = cases[item]
    greatest_value = max(classes)
    combine_classes(classes, greatest_value, 0)
