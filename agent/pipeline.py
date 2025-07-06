import os
from .kaggle_utils import fetch_kaggle_data
from .llm_claude import suggest_eda, suggest_model, improve_code
from .notebook import create_notebook, execute_notebook

def agent_pipeline(run_id, kaggle_url, max_iterations=3, score_threshold=None):
    # Step 1: Ingest Kaggle data
    meta, data_path = fetch_kaggle_data(kaggle_url, run_id)

    # Step 2: Get EDA steps from Claude
    eda_steps = suggest_eda(meta, data_path)

    # Step 3: Get model code suggestion from Claude
    model_code = suggest_model(meta, eda_steps)

    # Step 4: Generate and execute notebook
    nb_path = create_notebook(run_id, eda_steps, model_code)
    out_nb, results = execute_notebook(nb_path)
    score = results.get("score")
    artifacts = [out_nb, results.get("submission_csv")]

    # Step 5: Iterative agent loop (improve via Claude)
    iter_count = 1
    while (
        score is not None
        and score_threshold is not None
        and score < score_threshold
        and iter_count < max_iterations
    ):
        improved_code = improve_code(model_code, score)
        nb_path = create_notebook(run_id, eda_steps, improved_code, suffix=f"_iter{iter_count}")
        out_nb, results = execute_notebook(nb_path)
        score = results.get("score")
        artifacts.extend([out_nb, results.get("submission_csv")])
        iter_count += 1

    return {
        "run_id": run_id,
        "status": "finished",
        "score": score,
        "artifacts": artifacts,
    }