from agent.pipeline import agent_pipeline

def test_agent_pipeline_runs():
    run_id = "test123"
    kaggle_url = "https://www.kaggle.com/c/sample-competition"
    result = agent_pipeline(run_id, kaggle_url, max_iterations=1, score_threshold=0.9)
    assert result["run_id"] == run_id
    assert result["status"] == "finished"
    assert "artifacts" in result