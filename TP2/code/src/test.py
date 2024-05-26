import plotly.graph_objects as go
import pandas as pd


def draw(fig: go.Figure, data: pd.DataFrame, mode: str) -> go.Figure:
    '''
    Draws the bar chart.

    Args:
        fig: The figure comprising the bar chart.
        data: The data to be displayed.
        mode: Whether to display the count or percent data.
    Returns:
        fig: The figure comprising the drawn bar chart.
    '''
    # Validate the mode
    if mode not in ['count', 'percent']:
        raise ValueError("Mode should be either 'count' or 'percent'")

    # Determine the column to use for the y-axis based on the mode
    if mode == 'count':
        y_column = 'PlayerLine'
    elif mode == 'percent':
        y_column = 'PlayerPercent'

    # Clear existing data in the figure
    fig.data = []

    # List of unique players
    players = data['Player'].unique()

    # Add a bar trace for each player
    for player in players:
        player_data = data[data['Player'] == player]
        fig.add_trace(go.Bar(
            x=player_data['Act'],
            y=player_data[y_column],
            name=player,
            hoverinfo='x+y+name'
        ))

    # Update layout for stacked bars
    fig.update_layout(barmode='stack', title="Player Lines or Percent by Act")

    return fig


# Sample data
data = pd.DataFrame({
    'Act': [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5],
    'Player': ['Sampson', 'Juliet', 'Nurse', 'Benvolio', 'Romeo', 'Other', 'Benvolio', 'Other', 'Juliet', 'Mercutio', 'Nurse', 'Romeo', 'Capulet', 'Lady Capulet', 'Nurse', 'Romeo', 'Juliet', 'Other', 'Capulet', 'Friar Laurence', 'First Musician', 'Juliet', 'Peter', 'Other', 'Balthasar', 'Capulet', 'First Watchman', 'Friar Laurence', 'Prince', 'Other'],
    'PlayerLine': [404, 508, 542, 1900, 1935, 2033, 276, 329, 874, 964, 1634, 2222, 416, 679, 758, 766, 1032, 1578, 205, 216, 295, 308, 364, 601, 214, 214, 233, 314, 578, 748],
    'PlayerPercent': [5.517618, 6.937995, 7.402349, 25.949194, 26.427206, 27.765638, 4.381648, 5.223051, 13.875218, 15.304017, 25.940625, 35.275441, 7.955632, 12.985274, 14.496080, 14.649072, 19.736087, 30.177854, 10.306687, 10.859729, 14.831574, 15.485168, 18.300654, 30.216189, 9.300304, 9.300304, 10.126032, 13.646241, 25.119513, 32.507605]
})

# Create an empty figure
fig = go.Figure()

# Draw the bar chart with 'count' mode
fig = draw(fig, data, mode='count')

# Show the figure
fig.show()

# Draw the bar chart with 'percent' mode
fig = draw(fig, data, mode='percent')

# Show the updated figure
fig.show()
