# Project README

## Overview
This project is a Django-based web application designed to showcase the use of various technologies and skills, including Docker, GitLab CI/CD, and Kubernetes. The application is a simple educational platform that allows students to take tests, view results, and register for the platform.

## Technologies and Skills Applied

### Django
The backend of the application is built using Django 4.1.3, a high-level Python web framework. Key Django features and components used include:

- Models: Defined models for students, test results, and user registration.
- Views: Implemented views for rendering home, test, and results pages.
- Templates: Utilized Django templates for rendering HTML pages.
- Forms: Created a registration form using Django forms for user registration.
- User Authentication: Employed Django's built-in user authentication system.

### Docker
The application is containerized using Docker to ensure consistent deployment across different environments. Key Docker-related files and configurations include:

- **Dockerfile:** Specifies the base Python image, sets environment variables, copies project files, and installs dependencies.
- **docker-compose.yml:** Defines the services, including the web service, and sets up the necessary configurations.
- **entrypoint.sh:** A shell script to perform tasks like applying migrations and starting the Django development server.

### GitLab CI/CD
Continuous Integration and Continuous Deployment (CI/CD) are implemented using GitLab CI/CD pipelines. The CI/CD process involves the following steps:

1. **Build Docker Image:** The Docker image is built using the specified Dockerfile and dependencies are installed.
2. **Push to GitLab Registry:** The built Docker image is pushed to the GitLab Container Registry.
3. **Deploy to Kubernetes:** The application is deployed to a Kubernetes cluster using the Kubernetes manifest file.

The CI/CD configuration is specified in the `.gitlab-ci.yml` file, and it includes stages for building and deploying the application.

### Kubernetes
The application is deployed on a Kubernetes cluster for orchestration and scalability. Key Kubernetes-related components include:

- **Deployment:** The application is deployed as a Kubernetes Deployment to ensure high availability.
- **PodMonitor:** Implements monitoring for the application using Prometheus.
- **kubectl commands:** Various `kubectl` commands are used to apply configurations and manage the Kubernetes cluster.

## Running the Application Locally

To run the application locally, follow these steps:

1. Make sure Docker is installed and running on your machine.
2. Build and run the Docker containers using the following command:

   ```bash
   docker-compose up --build
   ```

3. Access the application at [http://localhost:8000/main/](http://localhost:8000/main/).

## Accessing Kubernetes Cluster

To deploy the application on a Kubernetes cluster, follow these steps:

1. Set up a Kubernetes cluster, for example, using Minikube or a cloud provider.
2. Apply the Kubernetes configurations using the following commands:

   ```bash
   kubectl apply -f kubernetes.yaml
   ```

3. Access the deployed application at the specified Kubernetes service endpoint.

## Conclusion
This project demonstrates the integration of Django, Docker, GitLab CI/CD, and Kubernetes to build a scalable and maintainable web application. It showcases best practices for containerization, continuous integration, and orchestration in a modern development environment.

# Docker and CI/CD
1) Create Docker files: docker-compose, Dockerfile, and entrypoint.sh.
2) Build and run locally (without CI, for now):
```bash
docker-compose up --build
```
3) Register on GitLab.
4) Add SSH key. Follow the steps [here](https://docs.gitlab.com/ee/user/ssh.html#add-an-ssh-key-to-your-gitlab-account).
5) Create a new project.
6) Update line 22 in gitlab-ci.yml with the details from the container_registry.
7) Push the project to GitLab:
```bash
git init --initial-branch=main
git remote add origin git@gitlab.com:vasiaplaton/teacher.git
git add .
git commit -m "Initial commit"
git push -u origin main
```
8) Verify that CI/CD has been triggered.
9) After successful execution, check if the container is available in the container_registry.

# Docker
10) Enable Hyper-V in Windows components.
11) Download Docker Desktop.
12) Disable WSL (Windows Subsystem for Linux).
13) Restart your machine.
14) Run locally through Docker (copy the link):
```bash
docker run -it -p 8000:8000 registry.gitlab.com/vasiaplaton/teacher/docker:main
```
15) Open [localhost:8000/main/](http://localhost:8000/main/).
16) Everything should be working fine!

# Kubernetes
17) Download VirtualBox.
18) Download Ubuntu Server.
19) Install Ubuntu Server.
20) Disable Hyper-V in Windows components.
21) Boot up the server.
22) Install Kubernetes and CRI-O.
23) Initialize Kubernetes:
```bash
kubeadm init --pod-network-cidr=10.244.0.0/16 --cri-socket=/var/run/crio/crio.sock
```
24) Apply Kubernetes configurations and expose ports:
```bash
kubectl apply -f kubernetes.yaml && kubectl expose deployment teacher-app --port=8000 --name=teacher-http && kubectl get po
```
25) Open the website running in Kubernetes at http://10.106.138.45:8000/main/.

# Kubernetes Monitoring
26) Install Prometheus using the [kube-prometheus](https://github.com/prometheus-operator/kube-prometheus) project.
27) Launch monitoring for the container:
```bash
kubectl apply -f kubernetes-monitor.yaml
```
28) Forward the Prometheus port:
```bash
kubectl --namespace monitoring port-forward svc/prometheus-k8s 9090
```
29) Open it at http://localhost:9090.

# Congratulations!
You have successfully configured CI/CD for your website, learned to run it locally in Docker, deployed it on a Kubernetes server, and set up monitoring!

# Docker и CI/CD(на русском)
1) Создаем докер файлы docker-compose Dockerfile entrypoint.sh
2) Собираем и запускаем(пока без CI, все локально):
```commandline
docker-compose up --build
```
3) Региструемся на гитлабе
4) Добавляем ssh ключ 
https://docs.gitlab.com/ee/user/ssh.html#add-an-ssh-key-to-your-gitlab-account
5) Создаем проект 
6) на 22 строчке gitlab-ci.yml меняем на данные из container_registry
7) Заливаем папку
```commandline
git init --initial-branch=main
git remote add origin git@gitlab.com:vasiaplaton/teacher.git
git add .
git commit -m "Initial commit"
git push -u origin main
```
8) провеяем что CI/CD запустился
9) Как отработал проверяем что container_registry появился container
# Docker
10) включаем hyper v в компонентах
11) Скачиваем docker desktop
12) Убираем галочку wsl
13) Перезагружаем
14) запускаем локально через докер(копируем ссылку) 
```commandline
 docker run -it -p 8000:8000 registry.gitlab.com/vasiaplaton/teacher/docker:main
```
15)  открываем localhost:8000/main/
16) Все работает!!!
# Теперь kubernetes
17) Скачиваем virtual box
18) Скачиваем ubuntu server
19) Устанвливаем  ubuntu server
20) Отключаем диск
21) Загружаем server
22) Устанавливаем kubernetes и CRI-O
23) Запускаем
```commandline
kubeadm init --pod-network-cidr=10.244.0.0/16 --cri-socket=/var/run/crio/crio.sock
```
24) Запускаем .yaml и пробрасывем порты
```commandline
cubectl apply -f kubernetes.yaml && kubectl expose deployment teacher-app --port=8000 --name=teacher-http && kubectl get po
```
25) Открываем сайт запущенный в кубере по аддресу http://10.106.138.45:8000/main/ 
# Монитрониг кубера
26) Устанавливаем prometheus https://github.com/prometheus-operator/kube-prometheus
27) Запускаем мониторинг нашего контейнера cubectl apply -f kubernetes-monitor.yaml
28) Пробрасываем порт для prometheus
```commandline
kubectl --namespace monitoring port-forward svc/prometheus-k8s 9090
```
29) Открываем его по адресу http://localhost:9090

# Поздравляю, мы настроили CI CD нашего веб сайта, научились запускать его локально в докере и на сервере в кубере и настроили мониторинг!
