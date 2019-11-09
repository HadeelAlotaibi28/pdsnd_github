import time
import statistics
from statistics import mode
import pandas as pd
import numpy as np
# update for the branch documentation




CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    while True:
        city = input("Would you like to see data for Chicago, New York, or Washington?").lower()
        if city in (CITY_DATA.keys()):
            break
        else:
            print("invalid option. choose from the cities above")

    while True:
        month = input("Which month - January, February, March, April, May, or June? choose all for all").lower()
        if month in ('january', 'february', 'march', 'april', 'june', 'all'):
            break
    else:
        print("invalid option. choose from the months above")

    while True:
        day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? choose all for all ").lower()
        if day in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
            break
    else:
        print("invalid option. choose from the days above")

    print('-'*40)
    return city, month, day

def load_data(city, month, day):

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()
    print("Most Common Start Station: ", start_station)

    # display most commonly used end station
    end_station = df['End Station'].mode()
    print("Most Common End Station: ", end_station)


    # display most frequent combination of start station and end station trip
    df['frequent station'] = df['Start Station'] + df['End Station']
    frequency_stat = df['frequent station'].mode()[0]
    print('frequent combination of start station and end station trip:', frequency_stat)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total = df['Trip Duration'].sum()
    print ("Total Travel time", total)

    # display mean travel time
    mean = df['Trip Duration'].mean()
    print ("Mean Travel time", mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def time_stats(df):


    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['months'] = df['Start Time'].dt.month
    popular_month = df['months'].mode()[0]
    print('Most Popular Month:', popular_month)
    # display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day'] = df['Start Time'].dt.day
    popular_day = df['day'].mode()[0]
    print('Most Popular Day:', popular_day)
    # display the most common start hour
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)


    # Display counts of gender
    user_gender = df['Gender'].value_counts()
    print(user_gender)

    # Display earliest, most recent, and most common year of birth
    min_year = df['Birth Year'].min()
    max_year = df['Birth Year'].max()
    common_year = df['Birth Year'].mode()
    print("Earliest Birth Year is: ", min_year)
    print("Recent Birth Year is: ", max_year)
    print("Common Birth Year is: ", common_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        trip_duration_stats(df)
        station_stats(df)
        if city != 'washington':
            user_stats(df)
        else:
            print("Note: washington Doesn't have user stats")


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
    counter = 0
    while True:
        rawss = input("Would you like to see more data?").lower()
        if rawss == ("yes"):
            print(df.iloc[counter:counter+5])
            counter= counter+5
        else:
            break



if __name__ == "__main__":
	main()
