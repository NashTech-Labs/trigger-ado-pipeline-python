import os
import requests
import base64

# build headers for pipeline api call
def build_headers_for_ado_with_authorization(
    ado_pat_token: str, content_type: str = "application/json"
) -> dict:
    headers = {
        "Authorization": "Basic "
        + base64.b64encode(f":{ado_pat_token}".encode("ascii")).decode("ascii"),
        "Content-Type": content_type,
    }
    return headers

# trigger pipeline
def trigger_pipeline(
    pipeline_id: str,
    organization_name: str,
    project_name: str,
    token: str,
    branch_name: str = None,
) -> int:
    """
    trigger ado pipeline

    Args:
        pipeline_id (str): pipeline id of the ado pipeline
        organization_name (str): organization name of the ado
        project_name (str): project name of the ado
        token (str): pat of the ado
        branch_name (str, optional): _description_. Defaults to None.
        component_dict (dict, optional): _description_. Defaults to None.

    Returns:
        int: returns the status code of the request to the azure devops
    """
    api_url = f"https://dev.azure.com/{organization_name}/{project_name}/_apis/pipelines/{pipeline_id}/runs?api-version=7.0"
    ado_pat = token

    body_json = {"definition": {"id": pipeline_id}}

    if branch_name is not None:
        resources_body_json = {
            "repositories": {"self": {"refName": f"refs/heads/{branch_name}"}}
        }

        body_json["resources"] = resources_body_json

        print("body json")
        print(body_json)
        print("")

    response = requests.post(
        api_url,
        headers=build_headers_for_ado_with_authorization(ado_pat_token=ado_pat),
        json=body_json,
    )

    if response.status_code == 200:
        print("triggered successfully!")
        return 0
    else:
        print(f"failed{response.status_code}")
        return response.status_code
    
    
def main():
    pipeline_id=input("Enter a pipeline id: ")
    print(f"PipelineId: {pipeline_id}")
    
    organization_name=input("Enter a organization name: ")
    print(f"PipelineId: {organization_name}")
    
    project_name=input("Enter a project name: ")
    print(f"PipelineId: {project_name}")
    
    if not "ADO_PAT" in os.environ:  # ADO_PAT is not available
        print(f"ADO_PAT not found. Enter the Azure DevOps PAT as an environment variable")
        exit(1)
    else:  # ADO_PAT is available
        token = os.environ.get("ADO_PAT")
    print("ADO_PAT found")
    
    branch_name=input("Enter a branch name: ")
    print(f"PipelineId: {branch_name}")

    
    trigger_pipeline(pipeline_id=pipeline_id, organization_name=organization_name, project_name=project_name,token=token,branch_name=branch_name)
    
    
#########################
# calling main function #
#########################
if __name__ == "__main__":
    main()
