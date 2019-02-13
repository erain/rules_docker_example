load("@io_bazel_rules_docker//contrib:test.bzl", "container_test")
load(
    "@io_bazel_rules_docker//container:container.bzl",
    "container_image",
    "container_layer",
    "container_push",
)

container_image(
    name = "helloworld",
    base = "@ubuntu1604//image",
    entrypoint = "echo 'hello world!'",
)

container_image(
    name = "go-helloworld",
    base = "@go-alpine//image",
    layers = [":src"],
    entrypoint = "go run /workspace/hello.go",
)

container_layer(
    name = "src",
    files = ["//hello_world/golang:hello.go"],
    directory = "/workspace",
)

container_push(
    name = "go-helloworld-gcr",
    image = ":go-helloworld",
    format = "Docker",
    registry = "gcr.io",
    repository = "yiyu-gke-dev/go-helloworld",
    tag = "test",
)
