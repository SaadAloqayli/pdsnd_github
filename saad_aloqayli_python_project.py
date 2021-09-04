import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june','all']
days_of_week = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','All']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # user input for city (chicago, new york city, washington).
    citylist = list(CITY_DATA.keys())
    print("would you like to see data for",citylist)
    while True:
        city = input().lower()
        if city not in CITY_DATA:
            print("please try again")
            continue
        else:
            break

    # user input for month (all, january, february, ... , june)
    print("which month?",months)
    while True:
        month = input().lower()
        if month not in months:
            print("please try again")
            continue
        else:
            break

    # user input for day of week (all, monday, tuesday, ... sunday)
    print("which day?",days_of_week)
    while True:
        day = input().title()
        if day not in days_of_week:
            print("please try again")
            continue
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #  the most common month
    popular_month = df['month'].mode()[0]

    # the most common day of week
    popular_day = df['day_of_week'].mode()[0]

    # the most common start hour

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print("Most Popular month:",popular_month)
    print("Most Popular day:", popular_day)
    print("Most Popular Start Hour:", popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #  display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]

    #  display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    #  display most frequent combination of start station and end station trip
    popular_combination = df.groupby(['Start Station','End Station']).size().idxmax()
    print("Most Popular Start Station:",popular_start_station)
    print("Most Popular End Station:",popular_end_station)
    print("Most Popular trip:",popular_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #  display total travel time
    total_travel_time = df['Trip Duration'].sum()

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print("total travel time:",total_travel_time)
    print("the avreage travel time:",mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    user_types = df['User Type'].value_counts()
    # Display counts of gender
    if 'Gender' in df:
        gender_types = df['Gender'].value_counts()
        print('count of males and females is :' , gender_types)
    else:
        print('there is no gender data for this city')
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        popular = int(df['Birth Year'].mode()[0])
        print("the earlies birth was in",earliest ,"and the most recent birth was in",recent,"the most common birth was in",popular)
    else:
        print('there is no Birth Year data for this city')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def data(df):
    raw_input = 0

    while True:
        # to ask the user if he wants to see the raw data or not
        choice = input('do you want to see five rows of raw data ? please type yes if you want to and no If you don\'t: ').lower()
        if choice == 'no':
            break
        elif choice == 'yes':
            raw_input += 5
            print(df.iloc[raw_input : raw_input + 5])
            print(choice)

        else:
            print('Wrong input')

def main():
    city = ()
    month = ()
    day = ()
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
