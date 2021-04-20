DOCKER_REPO="$DOCKER_USERNAME/todo-app"
docker build --target prod -t "$DOCKER_REPO:$TRAVIS_COMMIT" -t "$DOCKER_REPO:latest" .
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker push "$DOCKER_REPO"
docker tag "$DOCKER_REPO" registry.heroku.com/tidi-ipp/web
heroku container:login
docker push registry.heroku.com/tidi-ipp/web
heroku container:release web -a tidi-ipp
