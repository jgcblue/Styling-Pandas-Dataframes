
# DataFrame Styler

A Python utility to style pandas DataFrames. This repository provides tools to apply various styles to DataFrames, such as adjusting font properties and coloring specific cells based on conditions.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Font Styling**: Adjust the font size, weight, and style of the DataFrame.
- **Cell Coloring**: Color specific cells of the DataFrame based on custom conditions.
- **Class-Based & Functional Approaches**: Style DataFrames using both OOP and functional paradigms.

## Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/dataframe-styler.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd dataframe-styler
   ```

## Usage

### Class-Based Approach

```python
from dataframestylerClass import DataFrameStyler

# Create an instance of the DataFrameStyler class
styler = DataFrameStyler(your_dataframe)

# Apply styles
styled_df = (styler.style_font(fontsize=15, fontweight='bold')
             .color_cells(color='red', condition=lambda x: x < 50)
             .render())
```

### Functional Approach

```python
from dataframestylerMethods import style_font, color_cells

# Apply font styling
styled_df1 = style_font(your_dataframe, fontsize=15, fontweight='bold')

# Color cells based on a condition
styled_df2 = color_cells(your_dataframe, color='red', condition=lambda x: x < 50)
```

## Examples

The repository includes examples of combining multiple styles for a more customized appearance. For instance, adjusting the font size and coloring cells based on certain conditions.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/your-username/dataframe-styler/issues) or open a new issue for feedback or suggestions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

