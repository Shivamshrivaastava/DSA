# def calculate_rectangle_area(length, width):
#     """
#     Function to calculate the area of a rectangle.
    
#     Parameters:
#     length (float): The length of the rectangle.
#     width (float): The width of the rectangle.
    
#     Returns:
#     float: The area of the rectangle.
#     """
#     area = length * width
#     return area

# def main():
#     print("Welcome to the Rectangle Area Calculator!")
#     length = float(input("Enter the length of the rectangle: "))
#     width = float(input("Enter the width of the rectangle: "))
    
#     # Calculate area
#     area = calculate_rectangle_area(length, width)
    
#     print("The area of the rectangle is:", area)

# if __name__ == "__main__":
#     main()







# import hashlib

# class URLShortener:
#     def __init__(self):
#         self.url_mapping = {}

#     def shorten_url(self, long_url):
#         hash_object = hashlib.md5(long_url.encode())
#         short_url = hash_object.hexdigest()[:6]
#         self.url_mapping[short_url] = long_url
#         return short_url

#     def get_long_url(self, short_url):
#         return self.url_mapping.get(short_url, None)

# def main():
#     shortener = URLShortener()

#     while True:
#         print("\n1. Shorten URL\n2. Get Long URL\n3. Exit")
#         choice = input("Enter your choice: ")

#         if choice == '1':
#             long_url = input("Enter the long URL: ")
#             short_url = shortener.shorten_url(long_url)
#             print("Shortened URL:", short_url)
#         elif choice == '2':
#             short_url = input("Enter the shortened URL: ")
#             long_url = shortener.get_long_url(short_url)
#             if long_url:
#                 print("Long URL:", long_url)
#             else:
#                 print("Shortened URL not found.")
#         elif choice == '3':
#             print("Exiting...")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()

import urllib.parse
import urllib.error
import urllib.request
import json

def find_github_repos(username):
    base_url = "https://api.github.com/users/{}/repos".format(username)

    try:
        # Making the HTTP request
        with urllib.request.urlopen(base_url) as response:
            data = json.load(response)
            return data
    except urllib.error.HTTPError as e:
        print("HTTP Error:", e.code)
    except urllib.error.URLError as e:
        print("URL Error:", e.reason)

def main():
    username = input("Enter a GitHub username: ")
    repos = find_github_repos(username)

    if repos:
        print("Repositories for user '{}':".format(username))
        for repo in repos:
            print(repo['name'])
    else:
        print("No repositories found for user '{}'.".format(username))

if __name__ == "__main__":
    main()



































