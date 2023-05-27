import boto3

def discover_eks_components():
    
    eks_client = boto3.client('eks')
    
   
    clusters = eks_client.list_clusters()['clusters']
    
   
    for cluster_name in clusters:
        print(f"Cluster: {cluster_name}")
        
       
        cluster_info = eks_client.describe_cluster(name=cluster_name)
        
       
        node_groups = cluster_info['cluster']['nodeGroups']
        
        
        for node_group in node_groups:
            print(f"  Node Group: {node_group['nodegroupName']}")
            print(f"    Status: {node_group['status']}")
            print(f"    Min Size: {node_group['scalingConfig']['minSize']}")
            print(f"    Max Size: {node_group['scalingConfig']['maxSize']}")
            print()
            
       
        fargate_profiles = cluster_info['cluster']['fargateProfiles']
        
       
        for fargate_profile in fargate_profiles:
            print(f"  Fargate Profile: {fargate_profile['fargateProfileName']}")
            print(f"    Status: {fargate_profile['status']}")
            print(f"    Pod Execution Role: {fargate_profile['podExecutionRoleArn']}")
            print()
            
        print("--------------------------------------")


discover_eks_components()
