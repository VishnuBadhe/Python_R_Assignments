#  2. Given a dictionary of students and their favourite colours:
#     people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'}
#     A. Find out how many students are in the list
#     B. Change Lisa’s favourite colour
#     C. Remove 'Jenny' and her favourite colour
#     D. Sort and print students and their favourite colours alphabetically by name


def function():
    # A. Find out how many students are in the list
    sliced_list = []
    people = {'Arham': 'Blue', 'Lisa': 'Yellow', 'Vinod':'Purple', 'Jenny': 'Pink'}
    print(f"No of students in the list: {len(people)}")


    # B.Change Lisa’s favourite colour
    print(f"Lisa's favourite colour: {people['Lisa']}")
    people['Lisa'] = 'White'
    print(f"Lisa's changed favourite colour: {people['Lisa']}")


    # C. Remove 'Jenny' and her favourite colour
    print(f"Dictionary before removing: {people}")
    for key in people:
        if key == 'Jenny':
            sliced_List = {key: people[key]}
    people.pop('Jenny')
    print(f"Dictionary after removing: {people}")


    # Sort and print students and their favourite colours alphabetically by name
    people.update(sliced_list)
    sorted_list = dict(sorted(people.items()))
    print(f"After sorting alphabetically: {sorted_list}")

function()





