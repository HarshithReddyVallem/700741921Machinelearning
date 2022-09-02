it_companies = {'Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon' }
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#finding  the Length of it_companies
print("Length of it_companies  :",len(it_companies))

#adding Twitter to it_companies
it_companies.add("Twitter")
print(it_companies)

#inserting multiple it_companies to list
new_it_companies={"TCS","Cognizant","Capgemini"}
it_companies.update(new_it_companies)
print("after addition of  new companies\n",it_companies)

#removing one of the companies from  set
it_companies.remove("Amazon")
print("after removing a company  \n",it_companies)

### remove() method  raises an error if the specified element doesn't exist iin the given set, and the discard() method doesn't raise any error if the specified element is not present in the setand the set  remains unchanged

#joining of A and B
A_B = A.union(B)
print("\nJoining A and B ",A_B)

#intersection of A and B
A_intersection_B = A.intersection(B)
print("\nIntersection of A and B ",A_intersection_B)

#Is A subset of B
print("\nA is subset of B :", A.issubset(B))

#Is A  disjoint set of B
print("\n A is disjoin set of B:",A.isdisjoint(B))

#joining  A with B and B with A
print("\n Joining A with B :",A.union(B))
print("\n Joining B with A :",B.union(A))

#symmetric difference between A and B
print("\nSymmetric difference between A and B :",A.symmetric_difference(B))

#removing the sets 
A.clear()
B.clear()
print(A)
print(B)

#converting ages to set 
set_age = set(age)
print("\n ages = ",set_age)
#comparing the length of list and set
print("Length of  list age = ",len(age))
print("Length of set_age = ",len(set_age))