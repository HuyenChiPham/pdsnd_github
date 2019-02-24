import time
import pandas as pd
import numpy as np
# delete import os
from collections import Counter


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    '''
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    '''
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Would you like to see data for chicago, new york city or washington? \n')
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month = int(input('\nWhich month? January, February, March, April, May, or June? Please type your response as an integer (e.g., 1=January) \n'))
    '''return df[df['Start Time'].dt.month == datetime.strptime(month, '%B').month]'''
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = int(input('Which day? Please type your response as an integer (e.g., 1=Sunday)\n'))
    '''return df[df['Start Time'].dt.day == day_input]'''

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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is: ',common_month)

    # TO DO: display the most common day of week
    '''df['day_of_week'] = df['Start Time'].dt.dayofweek'''
    common_dayofweek = df['day_of_week'].mode()[0]
    print('The most common day of week is: ',common_dayofweek)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_starthour = df['hour'].mode()[0]
    print('The most common hour is: ',common_starthour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    #count = df['Start Station'].count   
    most_start,num_most_start = Counter(df['Start Station']).most_common(1)[0]
    print('The most common start station is: ',most_start, num_most_start)

    # TO DO: display most commonly used end station
    most_end,num_most_end = Counter(df['End Station']).most_common(1)[0]
    print('The most common end station is: ',most_end,num_most_end)

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'].map(str) + ' - ' + df['End Station']
    most_trip,num_most_trip = Counter(df['Trip']).most_common(1)[0]
    print('The most common combination start-end station is: ',most_trip,num_most_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['travel_time'] = df['End Time'] - df['Start Time'] 
    #total_travel_time = df['travel_time'].sum()
    print('The total travel time is: ',df['travel_time'].sum())
    
    # TO DO: display mean travel time
    mean_travel_time = df['travel_time'].mean()
    print('The mean travel time is: ',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    # TO DO: Display earliest, most recent, and most common year of birth
    if (city == 'washington'):
        print('washington data does not have Gender and  Birth Year field')
    else:
        gender = df['Gender'].value_counts()
        print(gender)
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common = Counter(df['Birth Year']).most_common(1)[0]
        print('The earliest year of birth is: ',earliest)
        print('The most recent year of birth is: ',most_recent)
        print('The most common year of birth is: ',most_common)
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    # limited 5 displayed rows
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()