# friends = {"Bob", "Rolf", "Anne"}
# abroad = {"Bob", "Anne"}
#
# # # dont have to hard code this
# # local_friends = {"Rolf"}
#
# # difference takes the passed set and removes from calling set
# local_friends = friends.difference(abroad)
# print(local_friends)

# local = {"Rolf"}
# abroad = {"Bob", "Anne"}
#
# # union adds to sets together
# friends = local.union(abroad)
# print(friends)

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science)
print(both)