# trigger-ado-pipeline-python
This techhub contains the Python script helps you trigger a azure devops pipeline using azure devops api.

In this tech hub, the python code will trigger the azure devops pipeline using azure devops api, the pipeline ca be called for any branch specified by the use in input and without any other parameters.

## Steps for Execution

- clone the repository
- python trigger-ado-pipeline-python.py
- export the azure devops personal access token for the azure devops organization having permission to trigger the pipeline using the following command:
  - export ADO_PAT='<azure devops personal-access-token>'
- Enter the values when the program prompot for input
  - pipeline_id
  - organization_name
  - project_name
  - branch_name
