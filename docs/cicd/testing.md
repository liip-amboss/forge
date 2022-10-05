# Testing
Test run in the test-build stage include;

## PyTest
```pytest --cov-fail-under=$MIN_COVERAGE_BACKEND -c pytest-ci.ini ```
$MIN_COVERAGE_BACKEND is a gitlab ci variable. If the pytest threshold falls below this the pipeline will fail

## Test Frontend
```npm run test -- --coverageThreshold='{"global":{"statements":"$MIN_COVERAGE_FRONTEND"}}' ```
$MIN_COVERAGE_FRONTEND is a gitlab ci variable. If the pytest threshold falls below this the pipeline will fail

## black
```black backend/ -S```
black runs python linting on the backend

## Code Quality
The Gitlab provided code quality test is used to measure changes in code quality. 
Changes in code quality will appear in the Merge Request.
