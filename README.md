# Docker и CI/CD
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
