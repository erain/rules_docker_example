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
    name = "go_helloworld",
    base = "@go_alpine//image",
    entrypoint = "go run /workspace/hello.go",
    layers = [":src"],
)

container_layer(
    name = "src",
    directory = "/workspace",
    files = ["//lang_images/golang:hello.go"],
)

container_push(
    name = "go_helloworld_gcr",
    format = "Docker",
    image = ":go_helloworld",
    registry = "gcr.io",
    repository = "yiyu-gke-dev/go-helloworld",
    tag = "test",
)
