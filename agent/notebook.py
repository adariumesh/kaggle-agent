import os
import nbformat

def create_notebook(run_id, eda_steps, model_code, suffix=""):
    nb_path = f"runs/{run_id}/notebook{suffix}.ipynb"
    nb = nbformat.v4.new_notebook()
    nb.cells = [
        nbformat.v4.new_markdown_cell("# Automated EDA"),
        nbformat.v4.new_code_cell(eda_steps),
        nbformat.v4.new_markdown_cell("# Baseline Model"),
        nbformat.v4.new_code_cell(model_code)
    ]
    os.makedirs(os.path.dirname(nb_path), exist_ok=True)
    with open(nb_path, "w") as f:
        nbformat.write(nb, f)
    return nb_path

def execute_notebook(nb_path):
    # Here you would use papermill or nbconvert to execute and collect results
    # This is a placeholder implementation
    results = {"submission_csv": nb_path.replace(".ipynb", ".csv"), "score": 0.85}
    with open(results["submission_csv"], "w") as f:
        f.write("id,prediction\n1,0.5\n2,0.6\n")
    return nb_path, results