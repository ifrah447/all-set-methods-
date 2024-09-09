# day 31
# sets are unordered collection of data items. they store multiple items in a single variable. sets are seperated by commas and enclosed within curly brackets. sets are unchangeable, meaning you cannot change items of the set once created.
# sets do not contain duplicate items.
sets = {2, 4, 2, 6}
# for accesiing the items in sets we use a for loop
print(sets)
for s in sets:
  print(s)

# it does'nt maintains the order of the items.
# making an empty set
set1 = set()
print(type(set1))
len = int(input("enter the lenght of the set: "))
for i in range(len):
  item = input(f"enter {i+1} item: ")
  set1.add(item)

print(set1)
# day 32 set methods/operations on sets
s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}
#union of two sets means adding two sets together and removing the duplicate values
print("union of s1 and s2 is \n", s1.union(s2))
print("old sets", s1, s2)  #this will not change the existing set
s1.update(s2)
print("updated s1 set with s2 values", s1,
      s2)  #this will update the existing set s1
s2.update(s1)
print("updated s2 set with s1 values", s1, s2)
# intersection of two sets means common values in both the sets
employee1 = {"harry", "rohan", "sohan", "mohan"}
student1 = {"harry", "sohan", "mohan", "sachin"}
print("intersection of sets employee and student is \n",
      employee1.intersection(student1))
# symmetric difference means values which are not common in both the sets

print("symetric differeces of employees and students sets are \n ",
      employee1.symmetric_difference(student1))
# difference of two sets means values which are only present in the original set and not in the other set
print("differeces of employees and students sets are \n ",
      employee1.difference(student1))
# disjiont of two sets means values which are not common in both the sets
print("the given two sets of employee and students has common elements? ",
      employee1.isdisjoint(student1))
# superset means all the values of the original set are present in the other set
print("the employee's set is a super set of student set?",
      employee1.issuperset(student1))
schoolfrnd = {"wajeeha", "savera", "roumaisa", "sheree", "laiba"}
collegefrnd = {"wajeeha", "savera", "roumaisa", "laiba"}
print("school frnds set is super set of clg frnd set?",
      schoolfrnd.issuperset(collegefrnd))
print(collegefrnd.issubset(schoolfrnd))
collegefrnd.add("rukhsar")
# remove method is used to remove the element from the set if the element is present in the set if not it does throw an error
collegefrnd.remove("laiba")
# discard method is used to remove the element from the set if the element is present in the set if not it does'nt throw an error
collegefrnd.discard("laiba2")
print(collegefrnd)
h1 = collegefrnd.pop()
print(h1)
print(collegefrnd)
# clear method is used to clear the items of the set
collegefrnd.clear()
print(collegefrnd)
# del method is use to delete the entire set
del collegefrnd
if "wajeeha" in schoolfrnd:
      print("yes")
