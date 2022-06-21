### Coalesce project

The API serves some sort of coalesce report by member id, it's feed by data providers and uses a simple service 
layer to abstract logic.

FastApi was used as the core, custom types and pydantic models were used to better structure data. Tests in this
case are some sort of integration tests given that the data providers are just a placeholder for an actual 
API client. A strategy pattern was chosen to implement the providers, given the case there is only one signature
method to implement and any provider can add query params, access tokens, throttle strategy, even prepare for 
manual auth or any behavior required to get the data. This same pattern could be implemented to
coalesce strategy(avg, sum, min).

Given that at some point we changed the data providers with real implementation we can separate integration 
and unit tests for the app, could use monkeypatching to generate needed mocks.

To test locally is recommended to use pipenv: 
- ```pipenv install --dev```
- ```uvicorn app.main:app --reload```

For quality code tooling black and flake8 were chosen.

#### Useful commands:
- ```flake8 .``` alerts on any linting issue (pep8)
- ```black . --check``` will check for errors
- ```black . --diff``` useful to see diff for actual fixes
- ```black .``` to automatically fix files (pep8)
- ```pytest --cov="."``` to run tests with coverage, remove ```--cov=-"."``` to just run tests