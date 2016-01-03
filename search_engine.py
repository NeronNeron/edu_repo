#that's a simple prototape of search engine

def find_index(to_search, target):
    for i, value in enumerate(to_search):
        if value == target:
            break
    else:   #non-break else
        return "no mathes"
    return i

my_list = [1, 2, 3, 7, 5, "target", 0]

index_location = find_index(my_list, "target")

print("Location of target is index: {}".format(index_location))
