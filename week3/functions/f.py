def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
#arbitrary kwargs <-> **kwargs
# if the number of kwargs is unknown 