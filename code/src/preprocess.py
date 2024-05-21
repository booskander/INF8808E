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

    players_occurrences = my_df.groupby(
        ['Act', 'Player']).size().reset_index(name='PlayerLine')

    lines_per_act = my_df.groupby('Act').size().reset_index(name='TotalLines')

    merged_df = pd.merge(players_occurrences, lines_per_act, on='Act')

    merged_df['PlayerPercent'] = (
        merged_df['PlayerLine'] / merged_df['TotalLines']) * 100

    return merged_df


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

    player_lines = my_df.groupby('Player')['PlayerLine'].sum()

    top_players = player_lines.sort_values(ascending=False).head(5)

    top_players_data = my_df[my_df['Player'].isin(top_players.index)]

    other_players_data = my_df[~my_df.index.isin(top_players_data.index)]

    aggregated_other_players = other_players_data.groupby('Act').agg({
        'PlayerLine': 'sum',
        'PlayerPercent': 'sum'
    }).reset_index()

    aggregated_other_players['Player'] = 'OTHER'

    my_df = pd.concat(
        [top_players_data, aggregated_other_players], ignore_index=True)

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
