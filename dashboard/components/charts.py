import plotly.express as px


def line_chart(
    data,
    x,
    y,
    title
):

    fig = px.line(
        data,
        x=x,
        y=y,
        title=title,
        markers=True
    )

    fig.update_layout(
        template="plotly_white",
        font_family="Vazirmatn"
    )

    return fig