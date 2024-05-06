import csv
import hashlib
import random
import string

# Function to generate random string of given length
def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

# Function to hash password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# Generate CSV data
data = []
num_records = 10  # Change this to the number of records you want

for i in range(num_records):
    first_name = generate_random_string(6)
    last_name = generate_random_string(6)
    email = f"{first_name}.{last_name}@example.com"
    password = "123"
    hashed_password = hash_password(password)
    data.append([i+1, first_name, last_name, email, hashed_password])

# Write data to CSV file
csv_file = "user_data.csv"
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['ID', 'FirstName', 'LastName', 'Email', 'Password'])
    writer.writerows(data)

print(f"CSV data generated and saved to '{csv_file}'")
