pytest -v -s -m "sanity" --html=./reports/r3.html testCases --browser chrome
pytest -v -s -m "sanity" --html=./reports/r4.html testCases --browser Ie
rem pytest -v -s -m regression --html=./reports/r4.html testCases --browser Ie
