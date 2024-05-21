'''
    Contains some functions related to the creation of the bar chart.
    The bar chart displays the data either as counts or as percentages.
'''

import plotly.graph_objects as go
import plotly.io as pio

from hover_template import get_hover_template
from modes import MODES, MODE_TO_COLUMN
import pandas as pd


def init_figure():
    '''
        Initializes the Graph Object figure used to display the bar chart.
        Sets the template to be used to "simple_white" as a base with
        our custom template on top. Sets the title to 'Lines per act'

        Returns:
            fig: The figure which will display the bar chart
    '''
    fig = go.Figure()

    # TODO : Update the template to include our new theme and set the title

    combined_template = go.layout.Template(pio.templates['simple_white'])
    combined_template.update(pio.templates['custom_theme'])

    fig.update_layout(
        template=combined_template,
        title={
            'text': 'Lines per act',
            'xanchor': 'center',
            'yanchor': 'top'
        },
        title_pad=dict(b=10)
    )

    return fig


def draw(fig, data: pd.DataFrame, mode: str):
    '''
        Draws the bar chart.

        Arg:
            fig: The figure comprising the bar chart
            data: The data to be displayed
            mode: Whether to display the count or percent data.
        Returns:
            fig: The figure comprising the drawn bar chart
    '''

    fig = init_figure()
    y_col = []
    # TODO : Update the figure's data according to the selected mode

    if mode.lower() == 'count':
        y_col = 'PlayerLine'
    else:
        y_col = 'PlayerPercent'

    players = set(data['Player'])

    i = 0
    for player in players:
        player_data = data[data['Player'] == player]

        fig.add_trace(
            go.Bar(
                x=player_data['Act'],
                y=player_data[y_col],
                name=player,
                hovertemplate=get_hover_template(player, mode)
            )
        )

    fig.update_layout(barmode='stack')

    update_y_axis(fig, mode)

    return fig


def update_y_axis(fig: go.Figure, mode: str):
    '''
        Updates the y axis to say 'Lines (%)' or 'Lines (Count) depending on
        the current display.

        Args:
            mode: Current display mode
        Returns: 
            The updated figure
    '''
    # TODO : Update the y axis title according to the current mode

    if mode.lower() == 'count':
        y_title = 'Lines (Count)'
    elif mode.lower() == 'percent':
        y_title = 'Lines (%)'

    fig.update_yaxes(title=y_title)
