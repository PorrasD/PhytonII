import requests
import matplotlib.pyplot as plt
import pandas as pd


url = "https://restcountries.com/v2/all"


def most_populated_countries():
    response_most_populated = requests.get(url)
    countries_data = response_most_populated.json()

# Extract the population and country name for each country
    population_data = [(country['population'], country['name']) for country in countries_data]

# Sort the population data in descending order and select the top 10
    population_data.sort(reverse=True)
    top_10_countries = population_data[:10]

# Extract the country names and respective populations from the top 10 list
    countries = [country[1] for country in top_10_countries]
    populations = [country[0] for country in top_10_countries]

# Create a bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(countries, populations)
    plt.title("Top 10 Countries with Highest Population")
    plt.xlabel("Country")
    plt.ylabel("Population")
    plt.xticks(rotation=45)
    plt.show()


def least_populated_countries():
    response_least_populated = requests.get(url)
    data = response_least_populated.json()
    countries_population = {}
    for country in data:
           name = country['name']['common']
           population = country['population'] if 'population' in country else 0
           countries_population[name] = population
    #Sort the population information in ascending order:
    sorted_populations = sorted(countries_population.items(), key=lambda x: x[1])[:10]

    #Separate the country names and populations into two lists:
    countries = [name for name, _ in sorted_populations]
    populations = [population for _, population in sorted_populations]
    #Create the chart using Matplotlib:
    fig, ax = plt.subplots()
    ax.bar(countries, populations)
    ax.set_xlabel("Countries")
    ax.set_ylabel("Population")
    ax.set_title("Top 10 Countries with the Least Population")

    plt.xticks(rotation=45)
    plt.show()


def most_used_languages():
    # Make the API request to REST Countries
    response_mostUsed_languages = requests.get(url)
    countries = response_mostUsed_languages.json()

    # Create a dictionary to store language counts
    language_counts = {
        'Spanish': 0,
        'English': 0,
        'French': 0,
        'Portuguese': 0,
        'German': 0
    }

    # Loop through each country to count the languages
    for country in countries:
        languages = country['languages']
        for language in languages:
            if language['name'] in language_counts:
                language_counts[language['name']] += 1

    # Prepare the data for the pie chart
    labels = []
    sizes = []
    for language, count in language_counts.items():
        if count > 0:
            labels.append(language)
            sizes.append(count)

    # Create the pie chart
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')

    # Set chart title
    ax1.set_title("Languages Usage around the world")

    # Display the chart
    plt.show()

def least_used_languages():
    # Fetch data from REST Countries API

    # Make a GET request to fetch the data
    response = requests.get("https://restcountries.com/v2/all")
    data = response.json()

    # Create a DataFrame using pandas
    df = pd.DataFrame(data)

    # Explode the 'languages' column to have multiple rows with one language each
    df = df.explode('languages')

    # Count the occurrences of each language
    language_counts = df['languages'].value_counts().reset_index()

    # Select languages with fewer than 10 occurrences
    less_used_languages = language_counts[language_counts['languages'] < 20]

    # Plot the less used languages chart
    plt.figure(figsize=(10, 6))
    plt.bar(less_used_languages['index'], less_used_languages['languages'])
    plt.title('Less Used Languages')
    plt.xlabel('Language')
    plt.ylabel('Occurrences')
    plt.xticks(rotation=45)
    plt.show()

def show_menu():
    print("Menu options:")
    print("1. Get most populated countries")
    print("2. Get less populated countries")
    print("3. Get the most used languages percentage")
    print("4. Get the less used languages percentage")
    print("5. Exit")

if __name__ == "__main__":
    while True:
        show_menu()
        option = input("pick a number: ")
        if option == '1':
            most_populated_countries()
        elif option == '2':
            least_populated_countries()
        elif option == '3':
            most_used_languages()
        elif option == '4':
            least_used_languages()
        elif option == '5':
            print("¡See you later for more population information, Good bye!")
            break