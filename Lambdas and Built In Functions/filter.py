users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]
#extract inactive users using filter:
inactive_users = list(filter(lambda u: not u['tweets'], users))

#extract inactive users using list comprehension:
inactive_users2= [user for user in users if not user["tweets"]]

# extract usernames of inactive users w/ map and filter:
usernames = list(map(lambda user: user["username"].upper(), 
	filter(lambda u: not u['tweets'], users)))

# extract usernames of inactive users w/ list comprehension
usernames2 = [user["username"].upper() for user in users if not user["tweets"]]


def triple_and_filter(lst):
    return list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, lst)))

def extract_full_name(l):
    return list(map(lambda val: f"{val['first']} {val['last']}", l))



