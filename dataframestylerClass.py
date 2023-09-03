import pandas as pd

class DataFrameStyler:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.styled = df.style

    def style_font(self, fontsize: int = 12, fontweight: str = 'normal', fontstyle: str = 'normal') -> 'DataFrameStyler':
        """
        Adjust the font size, weight, and style of the DataFrame.
        """
        styles = {
            'font-size': f'{fontsize}px',
            'font-weight': fontweight,
            'font-style': fontstyle
        }
        self.styled = self.styled.set_properties(**styles)
        return self

    def color_cells(self, color: str = 'yellow', condition=None) -> 'DataFrameStyler':
        """
        Color specific cells of the DataFrame based on a condition.
        """
        if condition:
            cell_colors = self.df.applymap(lambda x: color if condition(x) else '')
            self.styled = self.styled.apply(lambda x: cell_colors, axis=None)
        else:
            cell_colors = pd.DataFrame(color, index=self.df.index, columns=self.df.columns)
            self.styled = self.styled.apply(lambda x: cell_colors, axis=None)
        return self

    def render(self) -> None:
        """
        Render the styled DataFrame.
        """
        return self.styled

