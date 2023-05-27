from kubernetes import client, config

def discover_eks_workloads():
   
    config.load_kube_config()
    
   
    api_client = client.ApiClient()
    
    
    namespaces = client.CoreV1Api(api_client).list_namespace().items
    
 
    for namespace in namespaces:
        namespace_name = namespace.metadata.name
        print(f"Namespace: {namespace_name}")
        
       
        pods = client.CoreV1Api(api_client).list_namespaced_pod(namespace_name).items
        
        
        for pod in pods:
            pod_name = pod.metadata.name
            pod_status = pod.status.phase
            pod_labels = pod.metadata.labels
            print(f"  Pod: {pod_name}")
            print(f"    Status: {pod_status}")
            print(f"    Labels: {pod_labels}")
            print()
        
        print("--------------------------------------")


discover_eks_workloads()
