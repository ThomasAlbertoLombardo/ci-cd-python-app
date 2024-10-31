## Flujo de Trabajo (Git Flow)

Este proyecto utiliza Git Flow para la gestión de ramas. Aquí está el flujo básico:

1. Las nuevas características se desarrollan en ramas `feature/*`.
2. El desarrollo se integra en la rama `develop`.
3. Las releases se preparan en ramas `release/*`.
4. Los hotfixes se manejan en ramas `hotfix/*`.
5. La rama `main` contiene el código de producción.

Para más detalles sobre cómo usar Git Flow, consulta [esta guía](https://danielkummer.github.io/git-flow-cheatsheet/).

## Despliegue en Kubernetes

Este proyecto incluye manifiestos de Kubernetes para su despliegue:

- `kubernetes/deployment.yaml`: Define el Deployment de la aplicación.
- `kubernetes/service.yaml`: Define el Service para exponer la aplicación.

Para desplegar la aplicación en un cluster de Kubernetes:

1. Asegúrate de tener `kubectl` configurado y conectado a tu cluster.
2. Aplica los manifiestos:
kubectl apply -f kubernetes/

3. Verifica el despliegue:
kubectl get pods
kubectl get services



## Construcción y Publicación de la Imagen Docker

Para construir y publicar la imagen Docker:

1. Construye la imagen:
docker build -t thomasalberto/python-app:latest .
2. Publica la imagen en Docker Hub:
docker push thomasalberto/python-app:latest
