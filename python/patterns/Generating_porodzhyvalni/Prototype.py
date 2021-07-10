import copy


class Data:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent


class Action:

    def __init__(self, some_int, some_list_of_objects, some_circular_ref):
        self.some_int = some_int
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref

    def __copy__(self):
        # First, let's create copies of the nested objects.
        some_list_of_objects = copy.copy(self.some_list_of_objects)
        some_circular_ref = copy.copy(self.some_circular_ref)

        # Then, let's clone the object itself, using the prepared clones of the
        # nested objects.
        new = self.__class__(self.some_int, some_list_of_objects, some_circular_ref)
        new.__dict__.update(self.__dict__)
        return new

    def __deepcopy__(self, memo={}):
        # First, let's create copies of the nested objects.
        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memo)

        # Then, let's clone the object itself, using the prepared clones of the
        # nested objects.
        new = self.__class__(self.some_int, some_list_of_objects, some_circular_ref)
        new.__dict__ = copy.deepcopy(self.__dict__, memo)
        return new


if __name__ == "__main__":

    list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
    circular_ref = Data()
    component = Action(23, list_of_objects, circular_ref)
    circular_ref.set_parent(component)

    shallow_copied_component = copy.copy(component)
    # Let's change the list in shallow_copied_component and see if it changes in component.
    shallow_copied_component.some_list_of_objects.append("another object")
    print("Done") if component.some_list_of_objects[-1] == "another object" else print("Isn't Done")

    # Let's change the set in the list of objects.
    component.some_list_of_objects[1].add(4)
    print("Done") if 4 in shallow_copied_component.some_list_of_objects[1] else print("Isn't Done")

    deep_copied_component = copy.deepcopy(component)

    # Let's change the list in deep_copied_component and see if it changes in
    # component.
    deep_copied_component.some_list_of_objects.append("one more object")
    print("Done") if component.some_list_of_objects[-1] == "one more object" else print("Isn't Done")

    # Let's change the set in the list of objects.
    component.some_list_of_objects[1].add(10)
    print("Done") if 10 in deep_copied_component.some_list_of_objects[1] else print("Isn't Done")
