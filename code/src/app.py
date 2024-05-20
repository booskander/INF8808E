import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import pandas as pd
import preprocess
import bar_chart
from template import create_template
from modes import MODES, MODE_TO_COLUMN

app = dash.Dash(__name__)
app.title = 'TP2 | INF8808'


def prep_data():
    dataframe = pd.read_csv('./assets/data/romeo_and_juliet.csv')
    proc_data = preprocess.summarize_lines(dataframe)
    proc_data = preprocess.replace_others(proc_data)
    proc_data = preprocess.clean_names(proc_data)
    return proc_data


def init_app_layout(figure):
    return html.Div(className='content', children=[
        html.Header(children=[
            html.H1('Who\'s Speaking?'),
            html.H2('An analysis of Shakespeare\'s Romeo and Juliet')
        ]),
        html.Main(children=[
            html.Div(className='viz-container', children=[
                dcc.Graph(
                    figure=figure,
                    config=dict(
                        scrollZoom=False,
                        showTips=False,
                        showAxisDragHandles=False,
                        doubleClick=False,
                        displayModeBar=False
                    ),
                    className='graph',
                    id='line-chart'
                )
            ])
        ]),
        html.Footer(children=[
            html.Div(className='panel', children=[
                html.Div(id='info', children=[
                    html.P('Use the radio buttons to change the display.'),
                    html.P(children=[
                        html.Span('The current mode is : '),
                        html.Span(MODES['count'], id='mode')
                    ])
                ]),
                html.Div(children=[
                    dcc.RadioItems(
                        id='radio-items',
                        options=[
                            dict(
                                label=MODES['count'],
                                value='count'),
                            dict(
                                label=MODES['percent'],
                                value='percent'),
                        ],
                        value='count'
                    )
                ])
            ])
        ])
    ])


@app.callback(
    [Output('line-chart', 'figure'), Output('mode', 'children')],
    [Input('radio-items', 'value')],
    [State('line-chart', 'figure')]
)
def radio_updated(mode, figure):
    new_fig = bar_chart.draw(figure, data, mode)
    new_fig = bar_chart.update_y_axis(new_fig, mode)
    mode_text = mode.capitalize()
    return new_fig, mode_text


data = prep_data()

create_template()

fig = bar_chart.init_figure()

app.layout = init_app_layout(fig)
