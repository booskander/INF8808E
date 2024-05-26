'''
    Contains some functions related to the creation of the heatmap.
'''
import plotly.express as px
import hover_template
import pandas as pd

import plotly.io as pio


def get_figure(data: pd.DataFrame):
    '''
        Generates the heatmap from the given dataset.

        Make sure to set the title of the color bar to 'Trees'
        and to display each year as an x-tick. The x and y axes should
        be titled "Year" and "Neighborhood". 

        Args:
            data: The data to display
        Returns:
            The figure to be displayed.
    '''

    # TODO : Create the heatmap. Make sure to set dragmode=False in
    # the layout. Also don't forget to include the hover template.
    fig = px.imshow(data, template=pio.templates['default'])
    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="Neighborhood",
        coloraxis_colorbar=dict(
            title="Trees"
        ),
    )

    return fig
