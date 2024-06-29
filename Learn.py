print('Aviation Career Path Finder')
print('by Okyere Gyamena Obed, Runway Aviation Ghana')

user_name = input('Can I know your name? ')
print('Hello,', user_name)

user_age = input('How old are you? ')

try:
  # Convert age input to integer and check for negative values
  user_age = int(user_age)
  if user_age < 0:
    raise ValueError("Age cannot be negative.")
except ValueError:
  print("Invalid age entered. Please enter a positive number.")
  exit()

current_year = 2024
birth_year = current_year - user_age
print('You are', user_age, 'years old.')
print('You were born in', birth_year)

print('What area of aviation are you most interested in?')

# Career paths dictionary with more options
career_paths = {
  'flying': 'Pilot',
  'communication': 'Air Traffic Controller',
  'fixing_things': 'Aircraft Maintenance Technician',
  'taking_care_of_people': 'Cabin Crew',
  'designing_or_building': 'Aerospace Engineer',
  'business_and_management': 'Aviation Management'
}

# Show available interests
print('Here are some areas you can choose from:')
for interest in career_paths:
  print(interest)

user_interest = input('What is your interest? ').lower()

career_path = career_paths.get(user_interest, 'Unknown')

if career_path == 'Unknown':
  print("I don't have information about that specific interest yet.")
else:
  print('Your potential career path could be:', career_path)

another_search = input("Do you want to perform another search (yes/no): ")

if another_search.lower() != 'yes':
  print('Thank you for using the Aviation Career Path Finder')
  print('Have a great day!')