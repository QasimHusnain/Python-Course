# ==============================================================================
# COURSE: Advanced Python Programming
# TOPIC: Data Structures — Part 1: Lists & Tuples
#
# LEARNING GOALS:
#   1. Understand what a List is and how to create, modify, and use it.
#   2. Understand what a Tuple is and when to pick it over a List.
#   3. Use Lists and Tuples with if/else (Day 03) and loops (Day 04).
#   4. Know the difference between mutable and immutable collections.
#   5. Build real-world mini-programs using both structures.
# WHY IT MATTERS: Every real application stores groups of data — student names,
# product prices, user IDs. Lists and Tuples are the two most basic containers
# Python gives you for holding multiple values in a single variable.
# ==============================================================================

SEPARATOR = "=" * 60

# ==============================================================================
#                         PART 1: LISTS
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. BASICS — WHAT IS A LIST?
# ------------------------------------------------------------------------------
# A List is an ordered, changeable (mutable) collection of items.
#
# Think of it like a NOTEBOOK where you write down names, one below the other.
# You can add new names, cross out old ones, and rearrange them any time.
#
# KEY RULES:
#   - Created with square brackets: []
#   - Items are separated by commas.
#   - A list can hold ANY data type — int, str, float, bool, even other lists.
#   - Items have positions called "indexes" starting from 0.
#   - Lists are MUTABLE — you CAN change them after creation.
#
# TEMPLATE:
#   my_list = [item1, item2, item3]

print(SEPARATOR)
print("  PART 1: LISTS")
print(SEPARATOR)

# --- Creating Lists ---
print("\n--- Creating Lists ---")

# Empty list — like opening a fresh notebook with no names yet
empty_list = []
print(f"Empty list: {empty_list}")
# Output: Empty list: []

print(f"Type: {type(empty_list)}")
# Output: Type: <class 'list'>

# List of student names (strings)
students = ["Ali", "Sara", "Ahmed", "Fatima"]
print(f"Students: {students}")
# Output: Students: ['Ali', 'Sara', 'Ahmed', 'Fatima']

# List of grades (integers) — reusing Day 01 variable style
grades = [85, 92, 78, 95, 88]
print(f"Grades: {grades}")
# Output: Grades: [85, 92, 78, 95, 88]

# List of prices (floats) — like a small shop inventory
prices = [19.99, 45.50, 12.00, 89.99]
print(f"Prices: {prices}")
# Output: Prices: [19.99, 45.5, 12.0, 89.99]

# Mixed list — Python lets you mix data types (but keep it clean)
user_record = ["Ali", 20, True, 3.75]
print(f"Mixed record: {user_record}")
# Output: Mixed record: ['Ali', 20, True, 3.75]

# List from range() 
numbers = list(range(1, 6))
print(f"Numbers from range: {numbers}")
# Output: Numbers from range: [1, 2, 3, 4, 5]

# --- Accessing Items (Indexing) ---
print("\n--- 1.2 Accessing Items ---")

# TOOLS:
# list[0]  : First item (index starts at 0).
# list[-1] : Last item (negative indexing counts from the end).
# list[a:b]: Slice — items from index a up to (not including) b.

students = ["Ali", "Sara", "Ahmed", "Fatima", "Zain"]

print(f"First student: {students[0]}")
# Output: First student: Ali

print(f"Last student: {students[-1]}")
# Output: Last student: Zain

print(f"Second student: {students[1]}")
# Output: Second student: Sara

print(f"Second-to-last: {students[-2]}")
# Output: Second-to-last: Fatima

# Slicing — grab a chunk of the list
print(f"First three: {students[0:3]}")
# Output: First three: ['Ali', 'Sara', 'Ahmed']

print(f"From index 2 onward: {students[2:]}")
# Output: From index 2 onward: ['Ahmed', 'Fatima', 'Zain']

print(f"Up to index 3: {students[:3]}")
# Output: Up to index 3: ['Ali', 'Sara', 'Ahmed']

# --- Connection to Previous Knowledge ---
# Remember if/else - Let's combine it with list indexing:
user_index = 2
if user_index < len(students):
    print(f"Student at index {user_index}: {students[user_index]}")
else:
    print("Index out of range!")
# Output: Student at index 2: Ahmed

# Remember loops - Let's loop through a list:
print("All students:")
for student in students:
    print(f"\n  - {student}")
# Output:
#   - Ali
#   - Sara
#   - Ahmed
#   - Fatima
#   - Zain

# ------------------------------------------------------------------------------
# 2. IN-DEPTH — LIST METHODS AND OPERATIONS
# ------------------------------------------------------------------------------
# TOOLS:
# .append(x)    : Adds x to the END of the list.
# .insert(i, x) : Inserts x at index i, pushing others to the right.
# .extend(list) : Adds ALL items from another list to the end.
# .remove(x)    : Removes the FIRST occurrence of x (raises error if not found).
# .pop(i)       : Removes and RETURNS the item at index i (default: last item).
# .clear()      : Removes ALL items — list becomes empty.
# .index(x)     : Returns the index of the FIRST occurrence of x.
# .count(x)     : Counts how many times x appears in the list.
# .sort()       : Sorts the list in ascending order (modifies the list itself).
# .reverse()    : Reverses the order of items (modifies the list itself).
# .copy()       : Creates a shallow copy of the list.
# len(list)     : Returns the total number of items.

print(SEPARATOR)
print("--- 2. List Methods (In-Depth) ---")

# ---- Adding Items ----
print("\n  [ Adding Items ]")

# .append() — Adds ONE item to the end. Most commonly used method.
students = ["Ali", "Sara"]
print(f"Before append: {students}")
# Output: Before append: ['Ali', 'Sara']

students.append("Ahmed")
print(f"After append('Ahmed'): {students}")
# Output: After append('Ahmed'): ['Ali', 'Sara', 'Ahmed']

# .insert() — Adds at a SPECIFIC position. Others shift right.
students.insert(1, "Fatima")
print(f"After insert(1, 'Fatima'): {students}")
# Output: After insert(1, 'Fatima'): ['Ali', 'Fatima', 'Sara', 'Ahmed']

# .extend() — Adds MULTIPLE items at once from another list.
new_students = ["Zain", "Hira"]
students.extend(new_students)
print(f"After extend: {students}")
# Output: After extend: ['Ali', 'Fatima', 'Sara', 'Ahmed', 'Zain', 'Hira']

# WARNING: .append() vs .extend() — A common trap!
demo = [1, 2, 3]
demo.append([4, 5])      # Adds the LIST as a single item (nested list!)
print(f"append([4,5]): {demo}")
# Output: append([4,5]): [1, 2, 3, [4, 5]]

demo2 = [1, 2, 3]
demo2.extend([4, 5])     # Adds each item INDIVIDUALLY
print(f"extend([4,5]): {demo2}")
# Output: extend([4,5]): [1, 2, 3, 4, 5]

# ---- Removing Items ----
print("\n  [ Removing Items ]")

students = ["Ali", "Sara", "Ahmed", "Fatima", "Sara"]
print(f"Before removal: {students}")
# Output: Before removal: ['Ali', 'Sara', 'Ahmed', 'Fatima', 'Sara']

# .remove() — Removes the FIRST match only.
students.remove("Sara")
print(f"After remove('Sara'): {students}")
# Output: After remove('Sara'): ['Ali', 'Ahmed', 'Fatima', 'Sara']
# Notice: Only the FIRST 'Sara' was removed, the second one is still there.

# .pop() — Removes by INDEX and gives you the removed item back.
removed = students.pop(1)
print(f"Popped index 1: '{removed}', Remaining: {students}")
# Output: Popped index 1: 'Ahmed', Remaining: ['Ali', 'Fatima', 'Sara']

# .pop() with no argument — removes the LAST item.
last = students.pop()
print(f"Popped last: '{last}', Remaining: {students}")
# Output: Popped last: 'Sara', Remaining: ['Ali', 'Fatima']

# .clear() — Wipes everything. Empty list.
temp_list = [1, 2, 3]
temp_list.clear()
print(f"After clear: {temp_list}")
# Output: After clear: []

# del keyword — Deletes by index or the entire variable
demo_del = ["a", "b", "c", "d"]
del demo_del[0]
print(f"After del [0]: {demo_del}")
# Output: After del [0]: ['b', 'c', 'd']

# ---- Searching and Counting ----
print("\n  [ Searching & Counting ]")

grades = [85, 92, 78, 95, 88, 92, 78]

# .index() — Finds the FIRST position of a value.
pos = grades.index(92)
print(f"First 92 at index: {pos}")
# Output: First 92 at index: 1

# .count() — How many times does a value appear?
count_78 = grades.count(78)
print(f"78 appears {count_78} time(s)")
# Output: 78 appears 2 time(s)

# 'in' operator — membership check!
print(f"Is 95 in grades? {95 in grades}")
# Output: Is 95 in grades? True

print(f"Is 100 in grades? {100 in grades}")
# Output: Is 100 in grades? False

# len() — Total number of items
print(f"Total grades: {len(grades)}")
# Output: Total grades: 7

# ---- Sorting and Reversing ----
print("\n  [ Sorting & Reversing ]")

scores = [78, 95, 62, 88, 71]
print(f"Original: {scores}")
# Output: Original: [78, 95, 62, 88, 71]

scores.sort()
print(f"Sorted (ascending): {scores}")
# Output: Sorted (ascending): [62, 71, 78, 88, 95]

scores.sort(reverse=True)
print(f"Sorted (descending): {scores}")
# Output: Sorted (descending): [95, 88, 78, 71, 62]

# sorted() vs .sort() — Important difference!
# .sort() changes the original list.
# sorted() creates a NEW sorted list, original stays untouched.
original = [3, 1, 4, 1, 5]
new_sorted = sorted(original)
print(f"Original after sorted(): {original}")
# Output: Original after sorted(): [3, 1, 4, 1, 5]
print(f"New sorted list: {new_sorted}")
# Output: New sorted list: [1, 1, 3, 4, 5]

# .reverse() — Flips the list in place.
names = ["Ali", "Sara", "Ahmed"]
names.reverse()
print(f"Reversed: {names}")
# Output: Reversed: ['Ahmed', 'Sara', 'Ali']

# ---- Copying ----
print("\n  [ Copying Lists ]")

# WARNING: This is a common trap for beginners!
# Assignment (=) does NOT copy — it creates a REFERENCE (both point to the same list).

original = [1, 2, 3]
reference = original       # This is NOT a copy!
reference.append(4)
print(f"Original after reference change: {original}")
# Output: Original after reference change: [1, 2, 3, 4]
# ⚠ Both variables point to the SAME list. Changing one changes the other!

# .copy() — Creates a TRUE independent copy.
original = [1, 2, 3]
real_copy = original.copy()
real_copy.append(4)
print(f"Original after copy change: {original}")
# Output: Original after copy change: [1, 2, 3]
print(f"Copy: {real_copy}")
# Output: Copy: [1, 2, 3, 4]
# ✅ Original is safe. Each list is independent now.

# ---- Useful Operations ----
print("\n  [ Useful Operations ]")

# Concatenation (+) — Joins two lists together
list_a = [1, 2, 3]
list_b = [4, 5, 6]
combined = list_a + list_b
print(f"Combined: {combined}")
# Output: Combined: [1, 2, 3, 4, 5, 6]

# Repetition (*) — Repeats the list 
repeated = [0] * 5
print(f"Repeated: {repeated}")
# Output: Repeated: [0, 0, 0, 0, 0]

# min(), max(), sum() — Quick math on number lists
grades = [85, 92, 78, 95, 88]
print(f"Highest grade: {max(grades)}")
# Output: Highest grade: 95
print(f"Lowest grade: {min(grades)}")
# Output: Lowest grade: 78
print(f"Total: {sum(grades)}")
# Output: Total: 438
print(f"Average: {sum(grades) / len(grades)}")
# Output: Average: 87.6

# ------------------------------------------------------------------------------
# 3. BUILDING ON PREVIOUS KNOWLEDGE
# ------------------------------------------------------------------------------
# This is where we connect Lists with everything you already know.
# Think of it as building with LEGO — each new block snaps onto the old ones.

print(SEPARATOR)
print("--- 3. Lists + Previous Knowledge ---")

# ---- Lists + if/else (Day 03) ----
print("\n  [ Lists + if/else ]")

students = ["Ali", "Sara", "Ahmed", "Fatima"]
target = "Sara"

if target in students:                     # 'in' from Day 01
    print(f"Found: {target} is enrolled.")
else:
    print(f"{target} not found in the list.")
# Output: Found: Sara is enrolled.

# Checking list length before accessing
grades = [85, 92]
if len(grades) >= 3:
    print(f"Third grade: {grades[2]}")
else:
    print(f"Only {len(grades)} grades recorded. Need at least 3.")
# Output: Only 2 grades recorded. Need at least 3.

# ---- Lists + for loop (Day 04) ----
print("\n  [ Lists + for loop ]")

# Loop through a list — the most natural use of for-in
students = ["Ali", "Sara", "Ahmed"]
print("Sending certificates:")
for student in students:
    print(f"  Certificate sent to {student}.")
# Output:
#   Certificate sent to Ali.
#   Certificate sent to Sara.
#   Certificate sent to Ahmed.

# enumerate() — When you need BOTH the index AND the value
#enumerate() is a built-in Python function that walks through a list and attaches numbers to each item
print("Attendance roll call:")
for index, student in enumerate(students):
    print(f"  Roll #{index + 1}: {student}")
# Output:
#   Roll #1: Ali
#   Roll #2: Sara
#   Roll #3: Ahmed

# Loop with condition (Day 03 + Day 04 combined)
grades = [85, 92, 78, 95, 60, 45, 88]
print("Grade classification:")
for grade in grades:
    if grade >= 90:
        print(f"  {grade} -> Excellent")
    elif grade >= 70:
        print(f"  {grade} -> Good")
    elif grade >= 50:
        print(f"  {grade} -> Pass")
    else:
        print(f"  {grade} -> Fail")
# Output:
#   85 -> Good
#   92 -> Excellent
#   78 -> Good
#   95 -> Excellent
#   60 -> Pass
#   45 -> Fail
#   88 -> Good

# ---- Lists + while loop (Day 04) ----
print("\n  [ Lists + while loop ]")

# Processing a task queue — remove items as you process them
tasks = ["Send email", "Update records", "Generate report"]
print("Processing tasks:")
while len(tasks) > 0:
    current_task = tasks.pop(0)    # Take the first task
    print(f"  Done: {current_task}")
print(f"  All tasks complete. Remaining: {tasks}")
# Output:
#   Done: Send email
#   Done: Update records
#   Done: Generate report
#   All tasks complete. Remaining: []

# ---- Building a list with a loop ----
print("\n  [ Building a List with a Loop ]")

# Collect even numbers from 1 to 20 — for loop + if + append
even_numbers = []
for num in range(1, 21):       # range() from Day 03/04
    if num % 2 == 0:           # % from Day 01
        even_numbers.append(num)
print(f"Even numbers: {even_numbers}")
# Output: Even numbers: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# List comprehension — a shortcut for the above (Python's special trick)
even_short = [num for num in range(1, 21) if num % 2 == 0]
print(f"Same with comprehension: {even_short}")
# Output: Same with comprehension: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# ------------------------------------------------------------------------------
# 4. PRACTICAL APPLICATION
# ------------------------------------------------------------------------------
# Real-world examples that tie everything together.

print(SEPARATOR)
print("--- 4. Practical Applications ---")

# ---- EXAMPLE A: ATTENDANCE TRACKER ----
print("\n  [ Example A: Attendance Tracker ]")

attendance = []
class_students = ["Ali", "Sara", "Ahmed", "Fatima", "Zain"]
present_today = ["Ali", "Ahmed", "Zain"]

for student in class_students:
    if student in present_today:
        attendance.append((student, "Present"))
    else:
        attendance.append((student, "Absent"))

print("Today's Attendance:")
for name, status in attendance:
    symbol = "✅" if status == "Present" else "❌"
    print(f"  {symbol} {name}: {status}")

absent_count = sum(1 for _, status in attendance if status == "Absent")
print(f"Total absent: {absent_count}")
# Output:
#   ✅ Ali: Present
#   ❌ Sara: Absent
#   ✅ Ahmed: Present
#   ❌ Fatima: Absent
#   ✅ Zain: Present
#   Total absent: 2

# ---- EXAMPLE B: GRADE TRACKER ----
print("\n  [ Example B: Grade Tracker ]")

student_grades = [85, 92, 78, 95, 60, 45, 88, 72, 55, 91]

# Using everything we know: loops, conditions, list methods
passing = []
failing = []

for grade in student_grades:
    if grade >= 50:      # Day 03 if/else
        passing.append(grade)
    else:
        failing.append(grade)

print(f"All grades: {student_grades}")
print(f"Passing ({len(passing)}): {passing}")
print(f"Failing ({len(failing)}): {failing}")
print(f"Class average: {sum(student_grades) / len(student_grades):.1f}")
print(f"Highest: {max(student_grades)}, Lowest: {min(student_grades)}")
# Output:
#   All grades: [85, 92, 78, 95, 60, 45, 88, 72, 55, 91]
#   Passing (9): [85, 92, 78, 95, 60, 88, 72, 55, 91]
#   Failing (1): [45]
#   Class average: 76.1
#   Highest: 95, Lowest: 45

# ---- EXAMPLE C: SHOPPING CART ----
print("\n  [ Example C: Shopping Cart ]")

cart = []
cart.append({"item": "Notebook", "price": 5.99})
cart.append({"item": "Pen Set", "price": 12.50})
cart.append({"item": "Backpack", "price": 45.00})

print("Your Cart:")
for i, product in enumerate(cart):
    print(f"  {i + 1}. {product['item']} — ${product['price']:.2f}")

total = sum(item["price"] for item in cart)
print(f"  Total: ${total:.2f}")
# Output:
#   Your Cart:
#   1. Notebook — $5.99
#   2. Pen Set — $12.50
#   3. Backpack — $45.00
#   Total: $63.49

# ------------------------------------------------------------------------------
# 5. COMMON PITFALLS
# ------------------------------------------------------------------------------
# These are mistakes that catch almost every beginner. Learn them now so
# you don't waste hours debugging later.

print(SEPARATOR)
print("--- 5. Common List Pitfalls ---")

# ⚠ PITFALL 1: IndexError — Accessing an index that doesn't exist
print("\n  ⚠ Pitfall 1: IndexError")
my_list = [10, 20, 30]
# ✗ WRONG:
# print(my_list[5])
# Error: IndexError: list index out of range

# ✅ CORRECT: Always check the length first
if len(my_list) > 5:
    print(my_list[5])
else:
    print(f"  List only has {len(my_list)} items. Index 5 is out of range.")
# Output: List only has 3 items. Index 5 is out of range.

# ⚠ PITFALL 2: Modifying a list while looping over it
print("\n  ⚠ Pitfall 2: Modifying while looping")
# ✗ WRONG — This gives unpredictable results:
# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     if num % 2 == 0:
#         numbers.remove(num)   # DON'T DO THIS

# ✅ CORRECT — Loop over a COPY, modify the original:
numbers = [1, 2, 3, 4, 5]
for num in numbers.copy():     # .copy() makes it safe
    if num % 2 == 0:
        numbers.remove(num)
print(f"  After removing evens: {numbers}")
# Output: After removing evens: [1, 3, 5]

# ⚠ PITFALL 3: Confusing .append() and .extend()
print("\n  ⚠ Pitfall 3: append vs extend")
# ✗ WRONG — Creates a nested list when you wanted flat:
wrong = [1, 2]
wrong.append([3, 4])
print(f"  ✗ append([3,4]): {wrong}")
# Output: ✗ append([3,4]): [1, 2, [3, 4]]

# ✅ CORRECT — Use extend for adding multiple items:
right = [1, 2]
right.extend([3, 4])
print(f"  ✅ extend([3,4]): {right}")
# Output: ✅ extend([3,4]): [1, 2, 3, 4]

# ⚠ PITFALL 4: The = trap (reference, not copy)
print("\n  ⚠ Pitfall 4: Reference vs Copy")
# ✗ WRONG:
a = [1, 2, 3]
b = a           # b is NOT a separate list — it IS a
b.append(4)
print(f"  ✗ a after b.append(4): {a}")
# Output: ✗ a after b.append(4): [1, 2, 3, 4]

# ✅ CORRECT:
a = [1, 2, 3]
b = a.copy()    # Now b is independent
b.append(4)
print(f"  ✅ a after b.copy().append(4): {a}")
# Output: ✅ a after b.copy().append(4): [1, 2, 3]

# ⚠ PITFALL 5: .sort() returns None
print("\n  ⚠ Pitfall 5: .sort() returns None")
# ✗ WRONG:
nums = [3, 1, 2]
result = nums.sort()          # .sort() modifies in place, returns None
print(f"  ✗ result = nums.sort(): {result}")
# Output: ✗ result = nums.sort(): None

# ✅ CORRECT: Use sorted() if you need a return value
nums = [3, 1, 2]
result = sorted(nums)
print(f"  ✅ result = sorted(nums): {result}")
# Output: ✅ result = sorted(nums): [1, 2, 3]


