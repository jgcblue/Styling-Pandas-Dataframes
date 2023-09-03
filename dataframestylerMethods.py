import pandas as pd
'''
Pandas provides a comprehensive set of functionalities to style DataFrames, especially when displaying them in Jupyter notebooks. Beyond basic styling, there are numerous ways to customize the appearance of DataFrames to make them more informative and visually appealing.
'''

def color_cells(df: pd.DataFrame, color: str = 'yellow', condition=None) -> pd.DataFrame:
    """
    Color specific cells of a DataFrame based on a condition.
    
    Parameters:
    - df (pd.DataFrame): The input DataFrame.
    - color (str): Desired cell color. Default is 'yellow'.
    - condition (function): A function that takes a cell value and returns True/False.
    
    Returns:
    - pd.DataFrame: DataFrame with colored cells.
    """
    if condition:
        cell_colors = df.applymap(lambda x: color if condition(x) else '')
    else:
        cell_colors = pd.DataFrame(color, index=df.index, columns=df.columns)
    return df.style.apply(lambda x: cell_colors, axis=None)

def style_font(df: pd.DataFrame, fontsize: int = 12, fontweight: str = 'normal', fontstyle: str = 'normal') -> pd.DataFrame:
    """
    Adjust the font size, weight, and style of a DataFrame.
    
    Parameters:
    - df (pd.DataFrame): The input DataFrame.
    - fontsize (int): Desired font size. Default is 12.
    - fontweight (str): Desired font weight ('bold', 'normal'). Default is 'normal'.
    - fontstyle (str): Desired font style ('italic', 'normal'). Default is 'normal'.
    
    Returns:
    - pd.DataFrame: DataFrame with adjusted font styling.
    """
    styles = {
        'font-size': f'{fontsize}px',
        'font-weight': fontweight,
        'font-style': fontstyle
    }
    return df.style.set_properties(**styles)

'''
You can combine multiple styles for a more customized appearance. For instance, you might want to adjust the font size and color cells based on certain conditions.

'''

styled_df = (df.style
             .applymap(lambda x: 'color: red' if x < 50 else 'color: green')  # Coloring cells based on condition
             .set_properties(**{'font-size': '15px', 'font-weight': 'bold'})  # Adjusting font size and weight
            )

