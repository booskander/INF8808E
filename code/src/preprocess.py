'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd
from modes import MODE_TO_COLUMN


def summarize_lines(my_df: pd.DataFrame):
    '''
        Sums each player's total of number of lines and  its
        corresponding percentage per act.

        The sum of lines per player per act is in a new
        column named 'PlayerLine'.

        The percentage of lines per player per act is
        in a new column named 'PlayerPercent'

        Args:
            my_df: The pandas dataframe containing the data from the .csv file
        Returns:
            The modified pandas dataframe containing the
            information described above.
    '''
    act_total_lines = my_df.groupby('Act')['Line'].transform('sum')

    my_df['PlayerLine'] = my_df.groupby(['Act', 'Player'])[
        'Line'].transform('sum')

    my_df['PlayerPercent'] = (my_df['PlayerLine'] / act_total_lines) * 100

    my_df = my_df.drop_duplicates(subset=['Act', 'Player'])

    my_df = my_df.drop(columns=['Scene', 'Line'])

    return my_df


def replace_others(my_df: pd.DataFrame):
    '''
        For each act, keeps the 5 players with the most lines
        throughout the play and groups the other plyaers
        together in a new line where :

        - The 'Act' column contains the act
        - The 'Player' column contains the value 'OTHER'
        - The 'LineCount' column contains the sum
            of the counts of lines in that act of
            all players who are not in the top
            5 players who have the most lines in
            the play
        - The 'PercentCount' column contains the sum
            of the percentages of lines in that
            act of all the players who are not in the
            top 5 players who have the most lines in
            the play

        Returns:
            The df with all players not in the top
            5 for the play grouped as 'OTHER'
    '''

    sorted_df = my_df.sort_values(
        ['Act', 'PlayerLine'], ascending=[True, False])

    five_firsts = sorted_df.groupby('Act').head(5)

    others = sorted_df.groupby('Act').apply(
        lambda x: x.iloc[5:]).reset_index(drop=True)

    sum1 = others.groupby('Act')['PlayerPercent'].sum()
    sum2 = others.groupby('Act')['PlayerLine'].sum()

    new_df = pd.DataFrame(
        {'Act': sum1.index, 'Player': 'OTHER', 'PlayerPercent': sum1.values, 'PlayerLine': sum2.values})

    my_df = pd.concat([five_firsts, new_df])

    my_df = my_df.sort_values(by=['Act', 'PlayerLine']).reset_index(drop=True)

    return my_df


def clean_names(my_df: pd.DataFrame):
    '''
        In the dataframe, formats the players'
        names so each word start with a capital letter.

        Returns:
            The df with formatted names
    '''
    def func(text): return ' '.join(word.capitalize() for word in text.split())

    my_df['Player'] = my_df['Player'].apply(func)

    return my_df
