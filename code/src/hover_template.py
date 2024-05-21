'''
    Provides the template for the hover tooltips.
'''
from modes import MODES


def get_hover_template(name, mode):
    '''
    Sets the template for the hover tooltips.

    The template contains:
        * A title stating player name with:
            - Font family: Grenze Gotish
            - Font size: 24px
            - Font color: Black
        * The number of lines spoken by the player, formatted as:
            - The number of lines if the mode is 'Count' ("X lines").
            - The percent of lines formatted with two
                decimal points followed by a '%' symbol
                if the mode is 'Percent' ("Y% of lines").

    Args:
        name: The hovered element's player's name
        mode: The current display mode
    Returns:
        The hover template with the elements described above
    '''

    if mode.lower() == 'count':
        hover_template = (
            "<b><span style='font-family: Grenze Gotisch; font-size: 24px; color: black;'>Act: %{x}</span></b><br>" +
            f'<b>Player: {name}</b><br>' +
            "<b>Number of lines:</b> %{y} lines"
        )
    else:
        hover_template = (
            "<b><span style='font-family: Grenze Gotisch; font-size: 24px; color: black;'>Act: %{x}</span></b><br>" +
            f'<b>Player: {name}</b><br>' +
            "<b>Percentage of lines:</b> %{y:.2f}%"
        )
    return hover_template
