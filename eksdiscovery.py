import boto3

def discover_eks_clusters():
   
    eks_client = boto3.client('eks')

   
    response = eks_client.list_clusters()

    
    cluster_names = response['clusters']

   
    for cluster_name in cluster_names:
        cluster_details = eks_client.describe_cluster(name=cluster_name)
        print(f"Cluster Name: {cluster_details['cluster']['name']}")
        print(f"Cluster ARN: {cluster_details['cluster']['arn']}")
        print(f"Cluster Status: {cluster_details['cluster']['status']}")
        print("---")


discover_eks_clusters()
