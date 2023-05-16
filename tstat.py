import json
from terraformlib import TerraformState

def extract_main_tf(terraform_tfstate_file):
    with open(terraform_tfstate_file, 'r') as f:
        tfstate_data = json.load(f)

    tfstate = TerraformState(tfstate_data)
    resources = tfstate.resources

    main_tf_content = ""

    for resource in resources:
        if resource['type'] == 'terraform_remote_state':
            # Skip remote state resources
            continue
        
        # Retrieve the resource configuration
        config = resource['instances'][0]['attributes']['config']
        
        # Check if 'main.tf' exists in the resource configuration
        if 'main.tf' in config:
            main_tf_content += config['main.tf']

    return main_tf_content

# Example usage
terraform_tfstate_file = 'path/to/terraform.tfstate'
main_tf_content = extract_main_tf(terraform_tfstate_file)
print(main_tf_content)
