load("@io_bazel_rules_docker//contrib:test.bzl", "container_test")
load(
    "@io_bazel_rules_docker//container:container.bzl",
    "container_image",
    "container_layer",
    "container_push",
)

container_image(
    name = "helloworld",
    base = "@ubuntu16_04//image",
    entrypoint = "echo 'hello world!'",
)

container_image(
    name = "go-ubuntu",
    base = ":helloworld",
    layers = [":go-toolchain", ":go-src"],
    entrypoint = "/bin/bash",
)

container_layer(
    name = "go-toolchain",
    env = {
        "GOPATH": "/go",
        "PATH": "$PATH:/usr/local/go/bin",
    },
    tars = ["//third_party/golang:tar"],
)

container_layer(
    name = "go-src",
    files = ["//hello_world/golang:hello.go"],
    directory = "/workspace",
)

container_push(
    name = "go-ubuntu-gcr",
    image = ":go-ubuntu",
    format = "Docker",
    registry = "gcr.io",
    repository = "yiyu-testing/go-ubuntu",
    tag = "test",
)
