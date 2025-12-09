users = {
"Alice": ["Coding", "Music", "Hiking", "Pizza"],
"Bob": ["Movies", "Hiking", "Tacos"],
"Charlie": ["Coding", "Pizza", "Gaming", "Music"],
"David": ["Cooking", "Travel"]
}
target = "Alice"
target_interest=users.get(target)
best_match=0
best_inter_name=''
for name, interests in users.items():
   if name!=target:
        shared_hobbies=0
        for interest in interests:
            if interest in target_interest:
                shared_hobbies+=1
        print(f"Comparing {target} with {name}... {shared_hobbies} shared interests.")
        if best_match<shared_hobbies:
          best_inter_name=name
          best_match=shared_hobbies
print(f'Best match for {target} is {best_inter_name} with {best_match} shared interests.')