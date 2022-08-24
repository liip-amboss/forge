# Review Apps
A review app is a dynamic environment that is generated for each merge request. 
Forge deploys merge requests using a Gitlab CI/CD job to a kubernetes cluster using the [forge helm chart](https://gitlab.liip.ch/amboss/ambops/forge-helm-chart)

## Setup
Forge will automatically deploy to a k8s cluster if the following two ci/cd variables are available.

- K8S_NAMESPACE   
  The name of the k8s namespace to deploy the review app to. The given kube config file must have access to this
- KUBE_CONFIG_FILE
  A variable of type file containing the kube config for this cluster. Must have access to the given namespace.

::: warning
Review apps generate many docker images. Setup an expiration policy in the Gitlab container registry
:::