# This Marimo notebook was created for interactive data analysis
# Email (for verification): 22f1001941@ds.study.iitm.ac.in

import marimo

app = marimo.App()


# --- Cell 1: Imports and synthetic dataset generation ---
# This cell does not depend on any other cell.
# Other cells will *depend* on the DataFrame produced here.
@app.cell
def _(pd=__import__("pandas"), np=__import__("numpy")):
    # Generate a simple synthetic dataset
    np.random.seed(42)
    x = np.linspace(0, 10, 100)
    y = 3 * x + np.random.normal(0, 3, size=100)

    import pandas as pd
    df = pd.DataFrame({"x": x, "y": y})
    df
    return df
    


# --- Cell 2: Widget (Slider) ---
# This slider will control the slope used in the dynamic explanation.
@app.cell
def _(mo=marimo,):
    slope_slider = mo.ui.slider(1, 10, value=3, label="Adjust Model Slope")
    slope_slider
    return slope_slider


# --- Cell 3: Compute model prediction based on slider ---
# This cell depends on df (from Cell 1) and slope_slider (from Cell 2)
@app.cell
def _(df, slope_slider, np=__import__("numpy")):
    slope = slope_slider.value
    df["pred"] = slope * df["x"]
    df
    return slope
    


# --- Cell 4: Dynamic Markdown Output ---
# This cell depends on the `slope` value from Cell 3.
@app.cell
def _(slope, mo=marimo):
    mo.md(
        f"""
        ### 🔍 Model Interpretation

        The current slope selected is **{slope}**.

        - A higher slope means a steeper relationship between x and y  
        - A lower slope means a gentler trend  
        - Try adjusting the slider to see how the prediction changes dynamically  

        This markdown updates **automatically** whenever you move the slider.
        """
    )
    return
    


# --- Cell 5: Visualization ---
# This depends on df and slope
@app.cell
def _(df, slope, plt=__import__("matplotlib.pyplot").pyplot):
    plt.figure(figsize=(6, 4))
    plt.scatter(df["x"], df["y"], label="Observed Data")
    plt.plot(df["x"], df["pred"], color="red", label=f"Predicted Line (slope={slope})")
    plt.title("Interactive Regression Model")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.tight_layout()
    plt.show()
    return


app.run()
