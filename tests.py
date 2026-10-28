from app.calculator import calculate_results

def test_calculate_results_valid():
    marks = [80, 90, 70, 100]
    result = calculate_results(marks)
    assert result["total"] == 340
    assert result["average"] == 85.0

def test_calculate_results_empty():
    result = calculate_results([])
    assert result["total"] == 0
    assert result["average"] == 0.0
