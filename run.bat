pytest -s -v -m "sanity" --html=./reports/report.html testCases/ --browser Edge 
rem pytest -s -v -m "sanity or regression" --html=./reports/report.html testCases/ --browser Edge
rem pytest -s -v -m "sanity and regression" --html=./reports/report.html testCases/ --browser Edge
rem pytest -s -v -m "regression" --html=./reports/report.html testCases/ --browser Edge   