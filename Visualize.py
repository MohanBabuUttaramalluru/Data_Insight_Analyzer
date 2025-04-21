import matplotlib.pyplot as plt
import seaborn as sns
import Query_Processing as QP

# Selection of visualization types
def select_chart_type(tokens, df):
    if 'scatter' in tokens:
        return scatter_plot(tokens, df)
    elif 'bar' in tokens:
        return bar_chart(tokens, df)
    elif 'line' in tokens:
        return line_chart(tokens, df)
    elif 'box' in tokens:
        return box_plot(tokens, df)
    elif 'heatmap' in tokens:
        return heatmap(tokens, df)
    else:
        return "Please specify a valid chart type (scatter, bar, line, box, heatmap)."

# Scatter Plot
def scatter_plot(tokens, df):
    columns = QP.extract_column_names(tokens, df)
    if len(columns) < 2:
        return "Scatter plot requires at least two numerical columns."
    sns.scatterplot(x=df[columns[0]], y=df[columns[1]])
    plt.title(f'Scatter Plot: {columns[0]} vs {columns[1]}')
    plt.xlabel(columns[0])
    plt.ylabel(columns[1])
    plt.show()
    return f"Displaying scatter plot for {columns[0]} vs {columns[1]}."

# Bar Chart
def bar_chart(tokens, df):
    categorical_cols = QP.extract_column_names(tokens, df)
    if len(categorical_cols) == 0:
        return "No categorical columns found for bar chart."
    columns = categorical_cols[0]
    sns.countplot(x=df[columns])
    plt.title(f'Bar Chart for {columns}')
    plt.xlabel(columns)
    plt.ylabel('Frequency')
    plt.show()
    return f"Displaying bar chart for {columns}."

# Line Chart
def line_chart(tokens, df):
    numerical_cols = QP.extract_column_names(tokens, df)
    if len(numerical_cols) < 2:
        return "Line chart requires at least two numerical columns."
    sns.lineplot(x=df[numerical_cols[0]], y=df[numerical_cols[1]])
    plt.title(f'Line Chart: {numerical_cols[0]} vs {numerical_cols[1]}')
    plt.xlabel(numerical_cols[0])
    plt.ylabel(numerical_cols[1])
    plt.show()
    return f"Displaying line chart for {numerical_cols[0]} vs {numerical_cols[1]}."

# Box Plot
def box_plot(tokens, df):
    numerical_cols = df.select_dtypes(include=[float, int]).columns
    if len(numerical_cols) == 0:
        return "No numerical columns found for box plot."
    sns.boxplot(data=df[numerical_cols])
    plt.title('Box Plot for Numerical Columns')
    plt.show()
    return "Displaying box plot for numerical columns."

# Heatmap
def heatmap(tokens, df):
    numerical_cols = df.select_dtypes(include=[float, int]).columns
    if len(numerical_cols) < 2:
        return "Heatmap requires at least two numerical columns."
    corr_matrix = df[numerical_cols].corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    plt.title('Heatmap of Correlations')
    plt.show()
    return "Displaying heatmap of correlations."


# In[ ]:




